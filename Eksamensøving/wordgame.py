import random
wordlist = ["dishwasher, soap, curtain, chair, roof"]

def dice(wordlist):
    choice = random.choice(wordlist)
    return choice

def main(wordlist):
    word = dice(wordlist)
    N_tries = 6
    count = 0
    riktig = False
    guess = ""
    hidden_word = ""
    for i in range(N_tries):
        for letter in word:
            if guess == letter:
                hidden_word += letter
            elif guess == word:
                riktig = True
            else: 
                hidden_word += "*"
        count += 1
        if riktig == True:
            print("Riktig!")
            break
        else:
            print(f"Ordet er {hidden_word}")
        if count > N_tries:
            print("du klarte dessverre ikkje gjette ordet lykke til neste gang")
        guess = input(f"Bokstav eller løsning ({count}/{N_tries}):")
            
main(wordlist)