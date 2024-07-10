import socket

s = socket.socket()
host = str(input("addr"))
port = int(input("port"))
s.connect((host,port))

print("Connected")

filename = 'recv.txt'
fw = open(filename,'wb')
filedata = s.recv(1024)
fw.write(filedata)
print('received',filedata)

