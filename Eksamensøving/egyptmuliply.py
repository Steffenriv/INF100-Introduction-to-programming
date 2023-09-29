import itertools

a = int(input("Faktor A: "))
b = int(input("Faktor B: "))


if a > b:
    temp = a
    a = b
    b = temp


kolonne0 = []
kolonne1 = []
kolonne2 = []

################## Kolonne 1
n = 1
while n < a:
    kolonne1.append(n)
    n = n*2
################### Kolonne0
kolonne1.reverse()
target = 0

for i in range(len(kolonne1)):
    target += kolonne1[i]
    if target <= a:
        kolonne0.append("X")
    else:
        kolonne0.append(" ")
        target -= kolonne1[i]

kolonne1.reverse()
kolonne0.reverse()
##################### Kolonne2

i = b
while i < a*b:
    kolonne2.append(i)
    i = i*2
#################### Printa ut:

layout = ("{:<8} {:<13} {:<0}".format(kolonne0[0], kolonne1[0], kolonne2[0])+"\n")
length = len(layout)
skillevegg = "="*length + "\n".strip()
layout = ""
for rad in range(len(kolonne1)):
    layout += ("{:<8} {:<13} {:<0}".format(kolonne0[rad], kolonne1[rad], kolonne2[rad])+"\n")
layout = layout[:-1]
print(skillevegg)
print(layout)
print(skillevegg)

utrekning1 = ""
utrekning2 = ""
for i in range(len(kolonne0)):
    if kolonne0{i} == "X":
        utrekning1 += f"{kolonne1[i]}"
        

