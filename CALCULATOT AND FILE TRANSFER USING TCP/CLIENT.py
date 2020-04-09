import socket 
s=socket.socket()
host="127.0.0.1" #ip of the server
port=9999
s.connect((host,port))
#receiving 'hello' from the server
msg=s.recv(1024)
print(msg.decode("utf-8"))               #utf-8

#sending hello to the server
s.send(bytes("Hello","utf-8"))

print("What do you want to do?")
print("1.File Transfer")
print("2.Calculator")
choice=input("Enter your choice::")
s.send(bytes(choice,"utf-8"))

if choice=='2':
  a=input("Enter first number:")
  s.send(bytes(a,"utf-8"))
  b=input("Enter second number:")
  s.send(bytes(b,"utf-8"))
  c=input("Enter operation - '+','-','*','/' :")
  s.send(bytes(c,"utf-8"))
  
  print("The result is:",end=" ")
  res=s.recv(1024)
  print(res.decode("utf-8"))
  s.close()

if choice=='1':
  name=input("Enter the file name:")
  s.send(bytes(name,"utf-8"))
  file=open('myfile.txt','a')
  file_data=s.recv(1024)
  file_data=str(file_data.decode("utf-8"))
  
  file.write(file_data)
  file.close()
  s.close()
