import csv


def lesdata(file):
    fylker = {}
    kommuner = {}
    with open(f'{file}', newline='', encoding='iso-8859-1') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        admincode_fylke = 0
        name_fylke = ""
        for row in csvreader:
            try:
                if row[5] == "ADM1":
                    name_fylke = str(row[1])
                    admincode_fylke = int(row[7])
                if row[5] == "ADM2":
                    name_kommune = str(row[1])
                    admincode_kommune = int(row[7])
                elif ValueError:
                    continue
            except ValueError:
                continue
            
            fylker[f"{name_fylke}"] = admincode_fylke
            kommuner[f"{name_kommune}"] = admincode_kommune
    return fylker,kommuner

#print(lesdata("NO_ADM12.csv"))

def largest_and_smallest(file):
    with open(f'{file}', newline='', encoding='iso-8859-1') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        sizetup= []
        nametup = []
        for row in csvreader:
            sizetup.append(row[9])
            nametup.append(row[1])
        
        zip_tup = zip(sizetup, nametup)
        list_tup = list(zip_tup)
        sorted_list = list_tup.sort()
 

print(largest_and_smallest("NO_ADM12.csv"))
