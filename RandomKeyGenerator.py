import random

def randomKey():
    key = ""
    i=0
    while i<35:
        n = random.randint(48,122)
        key = key + chr(n)
        i+=1
    print key
    return key

