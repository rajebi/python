
print ("hello world")

#=============================================
#                Sockets
#
#     Socket client example in python
#=============================================
 
import socket   #for sockets
import sys  	#for exit

#-------------------------------------
#create an AF_INET, STREAM socket (TCP)
#-------------------------------------
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print ("Failed to create socket. Error code: " + str(msg[0]) + " , Error message : " + msg[1])
    sys.exit();
 
print (" Client Socket is Created")
#-------------------------------------------------------------
# Now get IP address of remote host and connect to its server 
#-------------------------------------------------------------
host = 'localhost'
port = 8888
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print ("Hostname could not be resolved. Exiting")
    sys.exit()
     
print ("Ip address of " + host + " is " + remote_ip)

# Connect to remote server 
s.connect((remote_ip , port))
print ("Socket Connected to " + host + " on ip " + remote_ip)

while 1:

	# input message
	message = input("Enter your name: ") 
    # Send the whole string
	# The first argument (message) needs to be bytes, but you're passing a string. 
	# You should encode it before sending e.g. message.encode('utf-8'). If you 
	# don't do this step, you will get ERROR: a bytes-like object is required, not 'str'
	s.sendall(message.encode('utf-8'))
	print ("Message sent successfully")

	#-------------------------------- 
	# receive response
	#--------------------------------
	reply = s.recv(4096)
	
	print (reply)




