
n = 0
spaces = 0

while n != 5:
    print(spaces * "  " + "*")
    spaces += 1
    n += 1

spaces -= 2
n -= 1

while n != 0:
    print(spaces * "  " + "*")
    spaces -= 1
    n -= 1