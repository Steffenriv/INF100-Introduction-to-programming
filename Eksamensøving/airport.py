import matplotlib.pyplot as plt
import csv
import pandas as pd

large_airport = {}
medium_airport = {}
coords = []

data = pd.read_csv(
    'airport-codes.csv',
    sep=',',
    header=0,
    encoding='utf8'
)
print(data.columns)

iata_code = data['iata_code']
coordinates = data['coordinates']
airport_type = data['type']

print(airport_type)

data[['x_coords','y_coords']] = data.coordinates.str.split(", ",expand=True,)

xs = data['x_coords']
ys = data['y_coords']

data.plot.scatter(x='x_coords', y='y_coords', alpha=0.2)
plt.show()
    #for line in data:
    #    airporttype = line[1]
    #    iata_code = line[9]
    #    coordinates = line[11]
    #    coords.append(coordinates.split(', '))
    #    print(coords)
    #    if  airporttype == 'large_airport':
    #        large_airport.setdefault(iata_code, [])
    #        large_airport[iata_code].append()
    #    elif airporttype == 'medium_airport':
    #        medium_airport.setdefault(iata_code, [])
    #        large_airport[iata_code].append()