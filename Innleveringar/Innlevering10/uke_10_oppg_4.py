
def  first_letter_last_word(filename):
    file = open(f"{filename}", "r")
    output = ""
    wordcount = 0
    word = []
    for line in file:
        for words in line.split():
            wordcount += 1
            word.append(words)

        lastword = word[wordcount-1]
        output += lastword[0]

    file.close()
    return output
