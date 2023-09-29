from itertools import combinations

def card_combinations(k, n):
    tuples = {}
    for i in range(n):
        tuples[i] = combinations(range(2,11), k)
    return tuples

print(card_combinations(3, 21))