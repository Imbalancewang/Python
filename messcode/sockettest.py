import socket
s=socket.socket()
host=socket.gethostbyname()
port=1234
s.bind((host,port))
s.listen(5)
while True:
    c.addr=s.accept()
    print 'got connection from' ,addr
    c.send('thank you')
    c.close