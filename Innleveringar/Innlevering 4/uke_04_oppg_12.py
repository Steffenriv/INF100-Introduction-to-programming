
binary = input("Binært tall: ")
length = len(binary)
tall = 0
n = 0
eksponent = int(length-1)

for n in binary:
    
    tall += int(n)*2**eksponent
    eksponent -= 1

print(tall)



