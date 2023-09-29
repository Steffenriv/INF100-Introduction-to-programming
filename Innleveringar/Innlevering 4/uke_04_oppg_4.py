n = 12
while(n >= 12 and n <= 27):
    if(n % 2 == 0):
        tal = str(n)
        print((tal + " er et partall!"))
    elif(n % 2 == 1):
        tal = str(n)
        print((tal + " er et oddetall!"))
    n += 1