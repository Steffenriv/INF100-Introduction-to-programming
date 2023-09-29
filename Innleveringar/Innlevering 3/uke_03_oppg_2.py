navn = input("Hva er ditt navn? ")
adresse = input("Hva er din adresse? ")
post = input("Hva er ditt postnummer og poststed? ")
str1 = len(navn)
str2 = len(adresse)
str3 = len(post)
lengde = max(str1, str2, str3)
print("")
if(lengde == str1):
    print(navn)
if(lengde == str2):
    print(adresse)
if(lengde == str3):
    print(post)
