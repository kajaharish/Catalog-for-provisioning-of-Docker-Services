import random

def randomKey():
    key = ""
    i=0
    while i<15:
        n = random.randint(97,122)
        key = key + chr(n)
        i+=1
    return key

