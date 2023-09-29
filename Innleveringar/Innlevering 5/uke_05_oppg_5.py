def egen_abs(a):
    if a < 0:
        a = -1*a
    return a

def egen_max(a, b):
    if a < 0 and b < 0:
        x = (a+b + (b-a))/2
    else:
        x = ((a+b + (a - b))/2)
    return x

print(egen_max(-12, -4))

def egen_min(a, b):
    if a < 0 and b <0:
        x = (a +b -(b-a))/2
    else: 
        x = ((a+b - (a - b))/2)
    return x

print(egen_min(-12, -4))


def egen_len(navn):
    n = 1
    count = 0
    for n in navn:
        count += 1 
    return count
    
print(egen_len("hello"))
    
