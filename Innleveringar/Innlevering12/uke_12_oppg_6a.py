import csv

with open("Akvakulturregisteret.csv", newline="", encoding="iso-8859-1") as csvfile:
    akvareader = csv.reader(csvfile, delimiter=";")
    counter = {}
    for row in akvareader:
        if row[12] in counter:
            counter[row[12]] += 1
        else: 
            counter[row[12]] = 1
    csvfile.close()
sortedvalues = sorted(counter.items())
sortedvalues.remove(sortedvalues[0])
sortedvalues.remove(sortedvalues[0]) # bruker dei for å få vekk dei to første linjene som er urelevante
length = len(sortedvalues)
for i in range(length):
    print(f"{sortedvalues[i][0]}: {sortedvalues[i][1]}")