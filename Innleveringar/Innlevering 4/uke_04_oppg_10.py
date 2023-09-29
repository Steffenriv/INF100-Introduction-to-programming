n = float(25)
count = float(0)

while n >= 25 and n <= 100:
    x = str(round(n, 1))
    y = str(round(count))
    grader = (y + "s = " + x + "°C")
    print(grader)
    n+= 0.625
    count += 1

print ("100°C i " + y + " sekunder")
