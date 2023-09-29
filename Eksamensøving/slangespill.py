import random

BOARDSIZE = 16

board = {i:i for i in range(BOARDSIZE)}
board[3] = 8
board[9] = 13
board[10] = 2 

def terningkast():
    terningkast = random.randint(1,6)
    return terningkast

def simulate(rounds):
    players = 100000
    endposition = {i:i for i in range(BOARDSIZE)} 
    for i in range(players):                     # antall spillere, tar 1 spiller om gangen
        position = 0

        for n in range(rounds):                                      
            new_position = position + terningkast()         
            if position >= BOARDSIZE:
                new_position = new_position % BOARDSIZE
            position = board[new_position]

        endposition[position] += 1

    for position in endposition.values():
        percent = 100 * position / players
    print(f"{percent:2.0f}", end="  ")
print()
    
simulate(20)
        
        