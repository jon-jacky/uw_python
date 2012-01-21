"""
hello_www.py - minimal web server + web application
"""

import socket 
import sys


page = """
HTTP/1.0 200 OK
Content-Type text/html

<html>
<body>
Hello, world!
</body>
</html>
"""

host = '' 
port = 8081 # different default port than thirty_minute_webserver

# optional command line argument: port 
if len(sys.argv) > 1:
    port = int(sys.argv[1])

backlog = 5 
size = 1024 

# server's listener socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Release listener socket immediately when program exits, 
# avoid socket.error: [Errno 48] Address already in use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host,port)) 

print 'hello_www listening on port', port
s.listen(backlog) 

while True: # just keep serving page to any client that connects
    client, address = s.accept() # create client socket
    client.recv(size) # HTTP request - not too big!  Just ignore contents
    client.send(page) # HTTP response - same for any request
    client.close()
