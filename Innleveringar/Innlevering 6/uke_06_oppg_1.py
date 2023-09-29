def remove_sevens(a):
    ny = []
    for i in a:
        if i == 7:
            continue
        else:
            ny.append(i)
    return ny

def every_other(a):
    length = len(a)
    x = slice(0, 7, 2)
    return (a[x])

def reverse(a):
    ny = a
    length = len(a)
    ny.reverse()
    return ny

def double_values(a):
    ny = []
    for i in a:
        i *= 2
        ny.append(i)
    return ny

def unique_values(a):
    ny = []
    for i in a:
        if i not in ny:
            ny.append(i)
    return ny
    

numberlist = ["a", 1, "b", "c", 2, 6, "g", 4, "p"]


print(every_other(numberlist))
print("----------------------------")
print(remove_sevens(numberlist))
print("----------------------------")
print(reverse(numberlist))
print("----------------------------")
print(double_values(numberlist))
print("----------------------------")
print(unique_values(numberlist))

