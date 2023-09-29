
def render_histogram(values):
    histogram = ""
    length = len(values)
    height = max(values)

    for x in range(height):  # Lager for loop for høgda sånn at vi gjer det nedafor for antall rader = height
        for y in range(length):  # Lager for loop for lengda så loopen slutter når vi er ferdig med lengda av histogrammet
            if (height - x == values[y]): # Gjer sånn at vi printa ut * når verdien på den rada vi er på stemmer med verdien til values.
                histogram += "*"
                values[y] = values[y] - 1 # setter minus - 1 for verdien i histogrammet slik at om vi har funnet startpunktet ved at den er lik høgda
            else:                         # så vil den fortsette å printe ut nedover, hadde vi ikkje hatt det ville rada under blitt ulikt valuen vår.
                histogram += " "
        if x == height-1:
            break
        else:
            histogram += ("\n")               
    return histogram
                
print(render_histogram([5, 4, 2, 7, 0, 3, 10]))