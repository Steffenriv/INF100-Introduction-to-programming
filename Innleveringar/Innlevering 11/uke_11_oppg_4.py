import random
from collections import Counter

def kast_n_2(n):
    sumterninger = []
    for i in range(n):
        terning1 = (random.randint(1,6))
        terning2 = (random.randint(1,6))
        sumterninger.append(terning1 + terning2) 
    return sumterninger

def print_histo(xs):
    listen = Counter(xs)
    histogram = ""
    for i in range(2, 13):
        histogram += f"{i:} {int(listen.get(i) * '*')}\n"
    return histogram



print(print_histo(kast_n_2(100)))