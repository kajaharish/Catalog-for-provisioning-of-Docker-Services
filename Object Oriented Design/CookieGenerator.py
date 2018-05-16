#!/usr/bin/python

import Cookie as coo
import Cookie, datetime, uuid

class CookieGenerator:

    def __init__(self):
        pass
    
    #Takes the session Id and creates cookie with it.
    def genCookie(sessionId):

        #Initiate cookie
        cookie = coo.SimpleCookie()

        #Assign sessionId to the docker_session key in dictionary.
        cookie["docker_session"] = sessionId

        #Create expiration time for cookie.
        expires = datetime.datetime.utcnow() + datetime.timedelta(days=10*365) # expires in 30 days
        
        #Assign expiration time to the cookie.
        cookie['docker_session']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")

        #Print the cookie value as the header.
        print cookie

