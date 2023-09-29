import csv

### part a) ###

fylker = {}
kommuner = {}

all_kommuner = [] # for part b)

with open('NO_ADM12.csv', newline='', encoding='utf8') as f:
    data = csv.reader(f, delimiter=';')
    for line in data:
        #print(line[5])
        _,name,_,_,_,feature,_,adm1code,_,pop,_ = line # setter opp kva dei ulike kolonnene på linjene er for noke, setter det urelevante til _ og gir navn på resten.
        if feature == 'ADM1':
            fylker[adm1code] = name
        elif feature == 'ADM2':
            kommuner.setdefault(adm1code, [])# setter default oppsettet på dict, til adm1code, som er den vi finnere i lista, og som er koden som kobler fylke og kommune, som keyen i dictionaryen og setter value til ein liste av navn og populasjon av kommunane.
            kommuner[adm1code].append((name,pop)) #legger til navn og populasjon i lista til kommunane.
            all_kommuner.append((int(pop),name)) # for part b) lager ny liste med navn og populasjon for å lettare hente ut.

### part b) ###
print(fylker)
print("")
print(kommuner)
print("")
print(all_kommuner)
pop_sorted = sorted(all_kommuner)

print('The 5 smallest kommuner')
for pop, name in pop_sorted[:5]:
    print(f'{name:20}{pop:6d}')

print('The 5 largest kommuner')
for pop, name in pop_sorted[-5:]:
    print(f'{name:20}{pop:6d}')

### part c) ###

def print_fylke(num):
    koms = kommuner[num]
    print('='*26)
    print(num, fylker[num])
    print('='*26)
    for name, pop in sorted(koms):
        pop = int(pop)
        print(f'{name:20}{pop:6d}')


### part d) ###

while True:
    wanted = input("Search word (q to quit)? ")
    if wanted == 'q':
        break

    code = None
    for adm1code, fylke in fylker.items():
        if wanted.lower() in fylke.lower():
            code = adm1code
            break
    
    if code is None:
        print("Not found. Try again")
        # print("Possible options:")
        # for fylke in sorted(fylker.values()):
        #     print(fylke)
        continue

    print_fylke(code)
    
