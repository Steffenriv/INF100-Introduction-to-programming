

def hvem_eldst(navn1, alder1, navn2, alder2):
    eldst = max(alder1,alder2)
    if eldst == alder1:
        return f"{navn1} er {alder1} år og eldst."
    elif eldst == alder2:
        return f"{navn2} er {alder2} år og eldst."

print(hvem_eldst("Ola", 43, "Katrine", 23))
