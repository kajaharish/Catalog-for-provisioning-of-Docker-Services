import random


class RandomKeyGenerator:

    def __init__(self):

        #randomKey is used to store the value of the key generated.
        self.randomKey = ""

    #Function to generate the value of Random Key.
    def getRandomKey(self):
        i=0
        while i<15:
            n = random.randint(97,122)
            self.randomKey = self.randomKey + chr(n)
            i+=1
