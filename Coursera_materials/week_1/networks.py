#!/usr/bin/env python3
import requests   #allows you to send HTTP/1.1 requests and a primary tool for interacting with web services, fetching content from websites, and sending data to APIs.
import socket # This Library is a fundamental way to perform network communication. Allows to create and manage network connections.

def check_localhost(): # Localhost typically means this machine.
        #print ("first line ")
        localhost = socket.gethostbyname('localhost') 
        print (localhost)
        if localhost == str("""127.0.0.1"""):    # 127.0.0.1 is the standard IPv4 loopback address. The 127.0.0.0/8 IP address block (from 127.0.0.0 to 127.255.255.255) is reserved for loopback purposes.
                #print ('True')                # Services like web servers, databases, or local proxies can listen on localhost and only accept connections from processes on the same machine, enhancing security.
                return True
        #print ("firstst line Inside loop")

def check_connectivity():
        #print ("Entering connectivity test")
        request = requests.get("http://www.google.com", timeout=5) #Added a timeout to requests.get() to prevent the function from hanging indefinitely if the server doesn't respond.
        #print (request)
        #print (type(request))
        response = request.status_code
        print (response)
        if response == 200:
                return True

# Other Http status codes 
# 404 Not Found, 403 Forbidden, 500 Internal Server Error, 301 Moved Permanently (Browsers typically automatically redirect in this case.) , 400 Bad Request

#The socket module operates closer to the Transport Layer (e.g., TCP or UDP) and interacts with the Network Layer (IP). Socket provides the fundamental building blocks for network communication.
#The requests library operates at the Application Layer (HTTP/HTTPS). It builds on top of lower-level network capabilities (which internally might use sockets).

