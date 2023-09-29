in_storage = {
    "Ancillary Justice": 1_046, # vi kan bruke _ i tall, den blir ignorert
    "The Use of Weapons": 372,
    "1984": 5_332,
    "The Three-Body Problem": 523,
    "A Fisherman of the Inland Sea": 728,
}
while True:
    tittel = input("Tittel: ")
    if tittel in in_storage:
        print(f'Vi har {in_storage.get(tittel)} av "{tittel}"\n')
    elif tittel == "":
        print("Ha det!")
        break
    else:
        print(f'Vi har 0 av "{tittel}"\n')