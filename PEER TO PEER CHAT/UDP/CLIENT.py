import socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host='192.168.144.59'
port=9999
b=(host,port)

s.sendto(bytes("I am here","utf-8"),b)

while 1:
  msg,addr=s.recvfrom(1024)
  if msg.decode("utf-8")=='bye':
    print("UR FRIEND IS OFFLINE")
    s.close()
    break
 
  else:
     print("Friend:>>",msg.decode("utf-8"))
     sent=input("You:>>")
     if sent=="bye":
      s.sendto(bytes(sent,"utf-8"),b)
      s.close()
      break
     else:
      s.sendto(bytes(sent,"utf-8"),b)
     
s.close() 
