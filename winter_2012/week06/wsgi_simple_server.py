"""
Simple WSGI application runner, including its own WSGI server

Usage: python simple_wsgi_server.py <application> <port>

Example: python simple_wsgi_server.py test.wsgi 8080

Default application is wsgi_test, default port is 8000

The application module can be named anything, but the 
application callable it provides MUST be named 'application'
"""

import sys
from wsgiref.simple_server import make_server

appname = 'wsgi_test'
port = 8000


nargs = len(sys.argv)
if nargs > 1:
    appname = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

app = __import__(appname)
httpd = make_server('', port, app.application)
print "Running %s on port %s ..." % (appname, port)

# Respond to requests until process is killed
httpd.serve_forever()
