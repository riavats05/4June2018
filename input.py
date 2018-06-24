#!/usr/bin/python

import cgi

print "Content-type:text/html\n\n" #for python prgrm to read both text and html 
data=cgi.FieldStorage() #fiels storage fun is in cgi 3
print "pyhton file"
value=data.getvalue('submit')
print value
