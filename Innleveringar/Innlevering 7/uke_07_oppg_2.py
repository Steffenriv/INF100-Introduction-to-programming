def update_weather(y):
    stringtiltuple = tuple(map(float, y.split(' ')))  # Geeksforgeeks https://www.geeksforgeeks.org/python-convert-string-to-tuple/; 06.10.2021
    return stringtiltuple

x = update_weather("16.1 14.1 13.3 15.0 13.0 13.2 12.9")

def tuesday_weather(y):
    x = list(y)
    return x[1]

print(tuesday_weather(x))
print(update_weather("16.1 14.1 13.3 15.0 13.0 13.2 12.9"))