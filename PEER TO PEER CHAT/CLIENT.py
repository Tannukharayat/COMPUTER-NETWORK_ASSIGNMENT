import socket
s=socket.socket()
host='127.0.0.2'
port=9999
s.connect((host,port))

msg=s.recv(1024)
print(msg.decode("utf-8"))

while 1:
  rec=s.recv(1024)
  
  if str(rec.decode("utf-8"))=='bye':
     print(rec.decode("utf-8"))  
     break  
  else:
     print("Friend:>>",rec.decode("utf-8"))
     sent=input("You:>>")
     if sent=='bye':
           s.send(bytes(sent,"utf-8"))
           break
     else:
           s.send(bytes(sent,"utf-8"))

s.close()
