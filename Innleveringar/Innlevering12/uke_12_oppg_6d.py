import csv

lats = []
lons = []
matlons = []
matlats = []
matlon = 0
matlat = 0
lat = 0
lon = 0

with open('Akvakulturregisteret.csv', newline='', encoding='iso-8859-1') as csvfile:
    akvareader = csv.reader(csvfile, delimiter=';')
    for row in akvareader:
        try:
            if row[11] == "MATFISK":        #Sjekker hvor produksjonen av fisk til mat er 
                matlat = float(row[-2])
                matlon = float(row[-1])
            if row[11] == "SETTEFISK":      #Sjekker hvor produksjonen av fisk til sette er
                lat = float(row[-2]) # latitude is second last
                lon = float(row[-1]) # longitude is last
            elif ValueError:
                continue
        except ValueError:
            continue

        lats.append(lat)
        lons.append(lon)
        matlons.append(matlon)
        matlats.append(matlat)

try:
    import matplotlib.pyplot as plt
    plt.plot(lons,lats,'+b')
    plt.plot(matlon,matlat, '+r')
    plt.savefig("uke_12_oppg_6d.png")
    plt.show()
except (ImportError, ModuleNotFoundError) as e:
    print(f'Import of matplotlib failed: {e}')
    print(f'We have {len(lats)} latitudes and {len(lons)} longitudes')