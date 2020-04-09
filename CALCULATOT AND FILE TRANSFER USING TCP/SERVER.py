import socket 
import sys

host="127.0.0.1"           #ip of the local host
port=9999
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)           
b=(host,port)                  #bind function accepts tuple
s.bind(b)           #bind function binds our ip and port for the working of the server
s.listen(5)                    #listens to the connection requests
print("Waiting for the client")
conn,address=s.accept()              #accepts the coonection request stored in object conn with address addr
print("CONNECTION ESTABLISHED.......")
conn.send(bytes("Hello","utf-8"))
msg=conn.recv(1024)
print(msg.decode("utf-8"))
choice=conn.recv(1024)
	#print(choice.decode("utf-8"))
	
if int(choice.decode("utf-8"))==2:
		a=conn.recv(1024)
		#print(a.decode("utf-8"))
		b=conn.recv(1024)
		#print(b.decode("utf-8"))
		c=conn.recv(1024)
		#print(c.decode("utf-8"))
		
		if str(c.decode("utf-8"))=='+':
			res=int(a.decode("utf-8"))+int(b.decode("utf-8"))
			res=str(res)
			conn.send(bytes(res,"utf-8"))

		if str(c.decode("utf-8"))=='-':
			res=int(a.decode("utf-8"))-int(b.decode("utf-8"))
			res=str(res)
			conn.send(bytes(res,"utf-8"))

		if str(c.decode("utf-8"))=='*':
			res=int(a.decode("utf-8"))*int(b.decode("utf-8"))
			res=str(res)
			conn.send(bytes(res,"utf-8"))

		if str(c.decode("utf-8"))=='/':
			res=int(a.decode("utf-8"))/int(b.decode("utf-8"))
			res=str(res)
			conn.send(bytes(res,"utf-8"))

if int(choice.decode("utf-8"))==1:
		name=conn.recv(1024)
		name=name.decode("utf-8")
		file = open(name,'rb')
		file_data=file.read(1024)
		print(file_data)	
		conn.send(file_data)
		file.close()

conn.close()
