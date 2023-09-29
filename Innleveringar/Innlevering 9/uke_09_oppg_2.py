def collatz_sequence(n):        #Tok collatz funksjonen fra oppgava på folk uib
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def first_ten_collatz():
    first10dict = {}
    for i in range(1,11):
        collatz = collatz_sequence(i)
        first10dict[i] = collatz
    return first10dict

print(first_ten_collatz())
