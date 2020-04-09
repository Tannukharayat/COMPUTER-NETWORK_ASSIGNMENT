import socket
#import sys

host="127.0.0.1"
port=9999

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b=(host,port)
s.bind(b)

name,address=s.recvfrom(1024)
print(name,address)
file = open(name,'rb')
file_data=file.read(1024)
while(file_data):
   print(file_data)
   s.sendto(file_data,address)
   file_data=file.read(1024)

st="ENDSHERE"
s.sendto(st.encode(),address)
file.close()
s.close()
