year = int(input("Angi år: "))

if(year % 4 == 0):
    if(year % 400 == 0):
        print("Dette er et skuddår.")
    elif(year % 100 == 0):
        print("Dette er ikke et skuddår.")
    else:
        print("Dette er et skuddår.")
else:
    print("Dette er ikke et skuddår.")