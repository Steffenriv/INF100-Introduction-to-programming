menneske = int(input("Angi menneskeår: "))

if(menneske <= 2):
    hund = str(menneske * 10.5)
    print("Dette tilsvarer " + hund + " hundeår.")
else:
    hund = str(menneske * 4 + 13)
    print("Dette tilsvarer " + hund + " hundeår.")