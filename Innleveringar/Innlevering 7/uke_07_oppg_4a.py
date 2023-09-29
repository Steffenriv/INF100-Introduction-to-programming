def tuple_repack(x,y):
    zip_tup = zip(x,y)
    list_tup = list(zip_tup)
    personlighet_tuple = list_tup[1]
    personlighet_liste = list(personlighet_tuple)
    return personlighet_liste

print(tuple_repack(("Princess Sparkle", "aloof", "tuna"), ("Mr Cat", "energetic", "cream")))

