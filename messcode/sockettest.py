import socket
s=socket.socket()
host=socket.gethostname()
port=2847
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print 'got connection from' ,addr
    c.send('thank you')
    c.close