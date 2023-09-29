factorA = int(input("Factor A :"))
factorB = int(input("Factor B :"))

if factorB > factorA:
    tmp = factorB
    factorB = factorA
    factorA = tmp
