import socket
s=socket.socket()
host=socket.gethostname()
port=1234
s.bind((host,port))
s.listen(5)
while True:
    conn,addr=s.accept()
    print("Got connection from:",addr)
    conn.send(b'Thank you for connecting')
    conn.close() 




















f