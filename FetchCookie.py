import os

def getCookieValue():
    handler = {}
    if 'HTTP_COOKIE' in os.environ:
        cookies = os.environ['HTTP_COOKIE']
        cookies = cookies.split('; ')
        for cookie in cookies:
            cookie = cookie.split('=')
            handler[cookie[0]] = cookie[1]
    try :
        return handler["docker_session"]
    except KeyError:
        return ""

