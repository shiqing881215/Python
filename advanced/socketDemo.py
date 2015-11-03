import socket

# open socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))

# This is exactly as what we did while using telnet. Based on the HTTP protocal request format 
# Like hitting enter twice at the end to send the request
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True :
    # Each time read up to 512 char
    # For some reason, it stucks here, TODO  Debug more
    data = mysock.recv(512)
    if (len(data) < 1) :
        break
    print data;

print 'close'
mysock.close()
