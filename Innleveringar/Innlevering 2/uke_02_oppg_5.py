navn = input("Hva er ditt navn? ")
adresse = input("Hva er din adresse? ")
post = input("Hva er ditt postnummer og poststed? ")

str1 = len(navn)
str2 = len(adresse)
str3 = len(post)

print(max(str1, str2, str3))
