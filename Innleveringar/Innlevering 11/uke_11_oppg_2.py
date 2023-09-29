from datetime import date

date_1901 = date(1901,1,1)
date_2000 = date(2000,12,31)
wednesdays = 0
for n in range(1901, 2001):
    for i in range(1,12):
        if date(n,i,1).weekday() == 2:
            wednesdays += 1
            
print(wednesdays)
