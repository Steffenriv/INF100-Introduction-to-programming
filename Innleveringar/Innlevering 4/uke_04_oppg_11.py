
height = float(input("Stenen droppes fra høyde: "))
time = float(0)
result = height

while result >= 0:
    result = height -(1/2*9.8*time**2)
    if result > 0:
        print(str(round(result,1)) + " m")
    elif result <= 0:
        print("0 m")
        print("Stenen lander mellom " + str(round(time)-1) + " og " + str(round(time)) + " sekunder etter at den droppes.")
        break
    time += 1