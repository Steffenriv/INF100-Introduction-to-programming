import pandas as pd
import collections

N_seats = 169

def mandatfordeling(filnavn, antall_mandater):

    data = pd.read_csv(f"{filnavn}", 
    delimiter=',',
    encoding='utf-8',
    header=0
    )
    distrikt = [valgdistrikt for valgdistrikt in data['Valgdistrikt']]
    innbyggere = [antall for antall in data['Innbyggere']]
    areal = [size for size in data['Areal (km2)']]
    fordelingstall = []
    mandater = {}

    for n in range(len(innbyggere)): # ingenting å seie om vi velger innbyggere eller areal som lengde, like lange begge 
       fordelingstall.append(innbyggere[n] + areal[n]*1.8)

    vote_data = tuple(zip(distrikt, fordelingstall))     # lager tuple for å samle data
    
    divisor = [1] 
    for n in range(1, antall_mandater):             # kalkulerer divisor etter kor mange mandata det er å dele
        next = 2 * n + 1
        divisor.append(next)

    ranking = []
    for party, count in vote_data:                  # lister kor mange ganger dei ulike distrikta vil komme opp på lista utifra kor mange mandatar vi har
        for i, f in enumerate(divisor, 1):
            ranking.append((count / f, f"{party}"))  

    ranking.sort(reverse=True) 
    assigned_seats = ranking[:antall_mandater]

    for name in distrikt:                       # Finner ut nøyaktig kor mange gangar dei ulike distrikta dukka opp og kor mange stemmer dei får.
        num_seats = 0
        for _, seat_name in assigned_seats:
            if name == seat_name:
                num_seats += 1
        if num_seats > 0:
            mandater[name] = num_seats
    return mandater

print(mandatfordeling("valgdistrikt_2020-01-01.csv", N_seats))
mandatdict = mandatfordeling("valgdistrikt_2020-01-01.csv", N_seats)
mandatsorted = {k: v for k, v in sorted(mandatdict.items(), key=lambda item: item[1], reverse=True)} #Kilde: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value Brukte kode fra første kommentar som kom opp, med tittel Python 3.7+ or CPython 3.6, sist redigert av wjandrea og svart av Devin Jeanpierre. Henta 06.12.2021

result = ["Parti            Mandater"]
width = len(result[0])
result.append(width * "=")
for name, seats in mandatsorted.items():                
    result.append(f"{name:18} {seats:6d}")                  # Formaterer det på ein fin måte.
print("\n".join(result))

#Kilde: Brukte uke_08_oppg_5.py sitt løsningsforslag som grunnlag for løsninga mi og modifiserte koden
    