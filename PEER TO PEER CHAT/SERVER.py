import socket
host='127.0.0.2'
port=9999
s=socket.socket()
b=(host,port)   
s.bind(b)
s.listen()
conn,addr=s.accept()
print("Ur friend is online")
conn.send(bytes("Ur friend is online","utf-8"))

while 1:
  sent=input("You:>>")
  if sent=='bye':
    conn.send(bytes(sent,"utf-8"))
    conn.close()
    break
 
  else:
   conn.send(bytes(sent,"utf-8"))
   rec=conn.recv(1024)

   if str(rec.decode("utf-8"))=='bye':
           print("Friend:>>",rec.decode("utf-8"))
           conn.close()
           break
   else:
           print("Friend:>>",rec.decode("utf-8"))
