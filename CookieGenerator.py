import Cookie as coo

def genCookie(sessionId):
    cookie = coo.SimpleCookie()
    cookie["docker_session"] = sessionId
    print cookie

