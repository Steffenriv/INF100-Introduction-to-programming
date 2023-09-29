import random

def randomchoice():
    randomnum = random.randint(1,3)
    if randomnum == 1:
        choice = "rock"
    elif randomnum == 2:
        choice = "paper"
    elif randomnum == 3:
        choice = "scissors"
    return choice


count = 1
playerscore = 0
aiscore = 0
while True:
    print(f"Let's play round {count}")
    playerchoice = input("Your choice (Rock/Paper/Scissors)? ")
    aichoice = randomchoice()
    if playerchoice == aichoice:
        print(f"My choice was {aichoice}. It's a tie")
    else:
        if playerchoice == "rock":
            if aichoice == "scissor":
                print(f"My choice was {aichoice}. You win.")
                playerscore += 1
                print(f"Score: me {aiscore}, you {playerscore}")
            elif aichoice == "paper":
                print(f"My choice was {aichoice}. I win.")
                aiscore += 1
                print(f"Score: me {aiscore}, you {playerscore}")
        elif playerchoice == "paper":
            if aichoice == "rock":
                print(f"My choice was {aichoice}. You win.")
                playerscore += 1
                print(f"Score: me {aiscore}, you {playerscore}")
            elif aichoice == "scissor":
                print(f"My choice was {aichoice}. I win.")
                aiscore += 1
                print(f"Score: me {aiscore}, you {playerscore}")
        elif playerchoice == "scissor":
            if aichoice == "paper":
                print(f"My choice was {aichoice}. You win.")
                playerscore += 1
                print(f"Score: me {aiscore}, you {playerscore}")
            elif aichoice == "rock":
                print(f"My choice was {aichoice}. I win.")
                aiscore += 1
                print(f"Score: me {aiscore}, you {playerscore}")
        else: 
            print(f"I don't understand {playerchoice}. Try again")
    keepgoing = input("continue y/n?")
    if keepgoing == "n":
        break
    elif keepgoing == "y":
        continue