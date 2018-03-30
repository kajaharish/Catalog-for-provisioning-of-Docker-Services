#!/usr/bin/python

import Cookie as coo
import Cookie, datetime, uuid

def genCookie(sessionId):
    cookie = coo.SimpleCookie()
    cookie["docker_session"] = sessionId
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=10*365) # expires in 30 days
    cookie['docker_session']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")

    print cookie

genCookie("gaurav")
