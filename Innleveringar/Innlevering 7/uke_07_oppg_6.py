vokal = "aeiou"
konsonant = "bcdfghjklmnpqrstvwxyz"

def pigify(y):

    letter1 = y[0]
    count = 0
    length = len(y)
    word = []

    if letter1 in vokal:
        word.append(f"{y}way")
    else:
        for i in y:
            if i in vokal:
                break
            count += 1
        if count == length:
            word.append(f"{y}ay")
        else:
            word.append(y[count:] + y[:count] + "ay") 
    y = word[0] 
    return y


print(pigify("string"))

def pigify_sentence(sentence):
    splitsentence = tuple(map(str, sentence.split(" ")))
    sentencelength = len(splitsentence)
    words = []
    done = ""
    for i in range(sentencelength):
        words.append(pigify(splitsentence[i]))
        done += words[i] + " "
    return done


print(pigify_sentence("alice was beginning to get very tired"))