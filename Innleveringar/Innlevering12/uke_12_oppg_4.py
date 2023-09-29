import csv

def read_first_col(file):
    with open(f'{file}', newline='') as csvfile:
        akvareader = csv.reader(csvfile, delimiter=' ')
        firstcolumn = []
        for row in akvareader:
            values= str(row[0])
            firstcolumn.append(values)
        csvfile.close()
    return "\n".join(firstcolumn)

print(read_first_col("2019-06-01_Oslo.csv"))