n = 0
spaces = 0

for n in range(0,5):
    print(spaces * "  " + "*")
    spaces += 1
    n += 1

spaces -= 2
n = 0

for n in range(1,5):
    print(spaces * "  " + "*")
    spaces -= 1
    n += 1