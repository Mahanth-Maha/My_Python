import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
print(host)
s.listen(1)

print("waiting")
conn,addr = s.accept()

print(addr,'connected')

filename = "sent.txt"
fp = open(filename,'rb')
conn.send(fp.read(1024))
print("datasent")

