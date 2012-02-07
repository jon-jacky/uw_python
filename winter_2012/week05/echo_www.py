"""
echo_www.py - echo the path part of the URL to the browser
              based on hello_www.py, minimal web server + web application
"""

import socket 
import sys


# page includes uw-student for identification and %s placeholder for URL path
page = """
HTTP/1.0 200 OK
Content-Type: text/html

<html>
<body>
uw-student: %s
</body>
</html>
"""

host = '' 
port = 8082 # different default port than thirty_minute_webserver or hello_www

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

print 'echo_www listening on port', port
s.listen(backlog) 

while True: # just keep serving page to any client that connects
    client, address = s.accept() # create client socket
    request = client.recv(size) # HTTP request
    words = request.split()  # break request into words
    path = words[1] # url path including initial '/'
    client.send(page % path) # HTTP response
    client.close()
