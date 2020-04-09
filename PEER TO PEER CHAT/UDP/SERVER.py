import socket

host='127.0.0.2'
port=9999
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b=(host,port)   
s.bind(b)

while 1:
 
   msg,address=s.recvfrom(1024)
   if msg.decode("utf-8")=='bye':
     print("UR FRIEND IS OFFLINE")
     s.close()
     break
   else:
    print("Friend:>>",msg.decode("utf-8"))
    sent=input("You:>>")
    if sent=="bye":
      s.sendto(bytes(sent,"utf-8"),address)
      s.close()
      break
    else:
      s.sendto(bytes(sent,"utf-8"),address)

s.close()
 
