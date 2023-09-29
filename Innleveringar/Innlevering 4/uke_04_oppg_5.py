n = int(input("Tall: "))
fakulteten = int(1)
if n > 0:
    while n != 0:
      fakulteten *= n
      n -= 1
elif n < 0:
    while n != 0:
        fakulteten *= n
        n += 1
    
print(round(fakulteten))

