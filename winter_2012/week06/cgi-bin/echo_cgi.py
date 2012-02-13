#!/usr/bin/python

"""
Minimal CGI + forms demo

Send HTML page that echoes message from HTTP request 
Intended to be invoked via action attribute in form tag in echo_cgi.html
"""

import cgi
import cgitb

cgitb.enable()  # so tracebacks in the web page, not the console

form = cgi.FieldStorage() # invoke only once
message = form.getfirst('message')

print """Content-type: text/html

<html>
<head>
<title>Echo response</title>
</head>
<body>
Message: %s
</form>
</body>
</html>
""" % message
