def stones_to_pounds(stones):
    pounds = float(stones) * 14
    return pounds

print(stones_to_pounds(10))

def stones_to_kg(stones):
    kg = float(stones) / 0.15747
    return kg

print(stones_to_kg(10))

def pounds_to_kg(pounds):
    kg = float(pounds) / 2.20462
    return kg

print(pounds_to_kg(10))

def imperial_to_metric(stones, pounds):
    kg = round((float(pounds) / 2.20462) + (float(stones)/ 0.15747), 2)
    
    return kg

print(imperial_to_metric(12, 4))    