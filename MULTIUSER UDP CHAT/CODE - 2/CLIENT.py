from socket import *
import _thread
port=12345
broad =''

s= socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) 
s.bind((broad,port))
LIST= []

def send(s,data,adr):
	for i in LIST:
		if(i!=adr):
		    s.sendto(data,i)

def rec(s):
	while True:
		m,adr=s.recvfrom(1024)
		global LIST
		if not(adr in LIST):
			LIST.append(adr)
		send(s,m,adr)

rec(s)

/* true everywhere, s in patameter  globa;l list sent.encode(),str .input*/
