from socket import *
import _thread
port=12345
host='127.0.0.1'


s= socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) 

def rec(s):
	while True:
		m=s.recvfrom(1024)
		print('[' + m[1][0] + ':' + str(m[1][1]) + '] :: ' + m[0].decode())

_thread.start_new_thread(rec,(s,))
while True:
	data=str(input())
	s.sendto(data.encode(),(host,port))
	
