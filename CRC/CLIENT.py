import socket			 

def xor(a, b): 
	result = [] 
	for i in range(1, len(b)): 
		if a[i] == b[i]: 
			result.append('0') 
		else: 
			result.append('1') 

	return ''.join(result) 

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

def encodeData(data, key): 
	l_key = len(key)  
	appended_data = data + '0'*(l_key-1) 
	remainder = mod2div(appended_data, key)  
	codeword = data + remainder 
	return codeword	 
 
	 
host='127.0.0.2' 
port = 9999
s = socket.socket()			
s.connect((host, port)) 

key = "1001"
input_string = input("Enter data you want to send->") 

data =(''.join(format(ord(x), 'b') for x in input_string))
print ("The binary format of our data is:  ",data) 

ans = encodeData(data,key) 
print("The data to be send as codeword is:",ans) 
s.send(bytes(ans,"utf-8")) 
status=s.recv(1024)
print(status.decode("utf-8")) 
s.close() 


