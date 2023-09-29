import csv

latssalt = []
lonssalt = []
lonsfersk = []
latsfersk = []
latS = 0
lonS = 0
latF = 0
lonF = 0

with open('Akvakulturregisteret.csv', newline='', encoding='iso-8859-1') as csvfile:
    akvareader = csv.reader(csvfile, delimiter=';')
    for row in akvareader:
        try:
            if row[20] == "FERSKVANN":
                latS = float(row[-2]) # latitude is second last
                lonS = float(row[-1]) # longitude is last
            if row[20] == "SALTVANN":
                latF = float(row[-2]) #latitude is second last
                lonF = float(row[-1]) # longitude is last
            elif ValueError:
                continue
        except ValueError:
            continue
        
        latssalt.append(latS)
        lonssalt.append(lonS)
        latsfersk.append(latF)
        lonsfersk.append(lonF)
try:
    import matplotlib.pyplot as plt

    plt.plot(lonsfersk,latsfersk,'+b')
    plt.plot(lonssalt,latssalt, '+g')
    plt.savefig("uke_12_oppg_6c.png")
    plt.show()
except (ImportError, ModuleNotFoundError) as e:
    print(f'Import of matplotlib failed: {e}')
    print(f'We have {len(lats)} latitudes and {len(lons)} longitudes')