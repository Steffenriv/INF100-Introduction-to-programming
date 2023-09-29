enhet = input("Angi enhet: ")
verdi = float(input("Angi verdi: "))

if(enhet == "nm"):
    if(verdi >= (1e9)):
        print("Dette er radiobølger.")
    elif(verdi >= (1e6)):
        print("Dette er mikrobølger.")
    elif(verdi >= 740):
        print("Dette er infrarød stråling.")
    elif(verdi >= 380):
        print("Dette er synlig lys.")
    elif(verdi >= 10):
        print("Dette er ultraviolet stråling.")
    elif(verdi >= 0.01):
        print("Dette er røntgen stråling.")
    elif(verdi < 0.01):
        print("Dette er gamma stråling.")
elif(enhet == "THz"):
    if(verdi <= (3e-4)):
        print("Dette er radiobølger.")
    elif(verdi <= 0.3):
        print("Dette er mikrobølger.")
    elif(verdi <= 405):
        print("Dette er infrarød stråling.")
    elif(verdi <= 790):
        print("Dette er synlig lys.")
    elif(verdi <= (3e4)):
        print("Dette er ultraviolet stråling.")
    elif(verdi <= (3e7)):
        print("Dette er røntgen stråling.")
    elif(verdi > (3e7)):
        print("Dette er gamma stråling.")
