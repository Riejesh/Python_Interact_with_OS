#!/usr/bin/env python3
import requests
import socket

def check_localhost():
        #print ("first line ")
        localhost = socket.gethostbyname('localhost')
        print (localhost)
        if localhost == str("""127.0.0.1"""):
                #print ('True')
                return True
        #print ("firstst line Inside loop")

def check_connectivity():
        #print ("Entering connectivity test")
        request = requests.get("http://www.google.com")
        #print (request)
        #print (type(request))
        response = request.status_code
        print (response)
        if response == 200:
                return True
