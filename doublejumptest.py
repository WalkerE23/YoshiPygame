
jumpsLeft = 2


while (jumpsLeft > 0):
    nput = raw_input("JUMP: (y/n)")
    if (nput == "y"):
        jumpsLeft -= 1
        print "Jumped!!!"
    if (nput =="g"):
        jumpsLeft = 2
