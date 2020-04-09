import socket

host="127.0.0.1"
port=9999   #if port of client and server if different then connection refused error will occur

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b=(host,port);

print("Enter the file name:")
name=input()
s.sendto(bytes(name,"utf-8"),b)
file=open('myfile','wb')
file_data,addr=s.recvfrom(1024)
print(file_data)
while(file_data):
    if str(file_data)=="b'ENDSHERE'":
       break
    else:
       file.write(file_data)
       file_data,addr=s.recvfrom(1024)
       

file.close()
s.close()

