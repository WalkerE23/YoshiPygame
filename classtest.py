
import random





lissy = []
loopCount = 0

class Enemy(object):

    def __init__(self, name, pword):

        self.name = name
        self.pword = pword
        lissy.append(self)

    def __str__(self):

        print'''

XXXXXXXXXXXXXXXXXXX
XXXX   BADGUY  XXXX
XXXXXXXXXXXXXXXXXXX

'''

def addE():
    ba = Enemy("enemy", "676")

    return ba


def removeE():

    lissy.pop()
    

def main():
    while True:
        rad = raw_input("INPUT HERE ")

        if rad == "remove":
            removeE()
            
        elif rad == "break":
            break

        elif rad == "print":
            print lissy

        else:
            print "continuing"
            if (not (len(lissy) >= 3)):
                addE()

        for item in lissy:
            item.__str__()



def rand():

    x = random.randint(0,1)
    print x


            
        
