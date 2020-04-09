import socket 
import random

#function for devision by xor-ing
def xor(a, b): 
	result = [] 
	for i in range(1, len(b)): 
		if a[i] == b[i]: 
			result.append('0') 
		else: 
			result.append('1') 
	return ''.join(result) 

#function to send divident and divisor for xor-ing
def mod2div(divident, divisor): 
	pick = len(divisor) 
	tmp = divident[0 : pick] 

	while pick < len(divident): 

		if tmp[0] == '1': 
			tmp = xor(divisor, tmp) + divident[pick] 
		else:
			tmp = xor('0'*pick, tmp) + divident[pick] 

		pick += 1

	if tmp[0] == '1': 
		tmp = xor(divisor, tmp) 
	else: 
		tmp = xor('0'*pick, tmp) 

	checkword = tmp 
	return checkword 

#function to append the data with 0's as per length of key
def decodeData(data, key): 

	l_key = len(key) 
	appended_data = data #+ '0'*(l_key-1) 
	remainder = mod2div(appended_data, key) 

	return remainder 
#_____________________________________________________________________________________________________

s = socket.socket() 
port = 9999
s.bind(('127.0.0.1', port)) 
s.listen(5) 
c,addr=s.accept()
key='1001'
data=c.recv(1024)
data= data.decode("utf-8")

temp='0'*(len(key)-1)
ans=decodeData(data,key)
if(ans==temp):
	c.send(bytes("SUCCESS","utf-8"))
	print("The data is received without error:",data) 
	print("Remainder after  decoding is:",ans)
  
	r=random.randint(0,1000)
	r=r%(len(data)-1)
	l=list(data)
	if l[r]=='0':
		l[r]='1'
	else:
		l[r]='0'
	
	data=str(l)
	ans=decodeData(data,key)
	print("The data received has an error at location ",r)
	print("Remainder after  decoding is:",ans)
		
else:
	c.send(bytes("RESEND THE DATA","utf-8"))
	ans=decodeData(data,key)
	print("The data received has an error at location ",r)
	print("Remainder after  decoding is:",ans)

c.close() 
