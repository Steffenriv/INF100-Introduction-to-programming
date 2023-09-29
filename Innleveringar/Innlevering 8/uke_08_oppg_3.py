my_fridge = ["tomato sauce", "mustard", "potatoes", "carrots", "chicken", "frozen fish"]

meals = [
    ("fish_sticks", ["frozen fish", "potatoes", "mustard"]),
    ("chicken_curry", ["chicken", "curry paste", "carrots", "potatoes", "rice"]),
    ("chicken_veg", ["chicken", "potatoes", "carrots"]),
    ("pasta", ["spaghetti", "tomato sauce"]),
]

def meal_list(fridge, ingredient_list):
    length = len(ingredient_list)
    count = 0
    for i in range(length):
        if ingredient_list[i] in fridge:
            count += 1
    if length == count:
        trueorfalse = True
    else: 
        trueorfalse = False
    return trueorfalse

def meal_options(fridge, meals):
    listlength = len(meals)
    meal_options_ls = []
    for i in range(listlength):
        if meal_list(my_fridge, meals[i][1]) == True:
            meal_options_ls.append(meals[i][0])
    return meal_options_ls
    
print(meal_list(my_fridge, meals[0][1]))

print(meal_options(my_fridge, meals))