import copy

parties = ["H", "Ap", "FrP", "SP", "SV", "KrF", "R", "V", "MdG"]
votes = [74282, 68945, 38352, 29981, 26901, 14724, 14150, 13163, 11940]
N_seats = 15

def valgresultat(parties,votes,N_seats):
    length = len(votes)
    mandat_fordeling = [1.4, 3, 5, 7, 9]      #Lager ein tuple til dei ulike mandat fordelingane for å lettare loope igjennom.
    lengde_fordeling = len(mandat_fordeling)    # trenger da sjølvsagt lengda av mandat fordelingane for å bruke den i loopen.
    new_voting = []
    new_parties = []
    for i in range(length):
        for n in range(lengde_fordeling):
            new_voting.append(votes[i] / mandat_fordeling[n])          # Looper igjennom dei ulike stemmene og deler på mandat fordelinga
            new_parties.append(parties[i])                             
    zip_seats = zip(new_voting, new_parties)
    seats = list(zip_seats)
    seats.sort(reverse=True)
    
    return seats[:N_seats]
            

def parti_mandater(party_list,votes,N_seats):
    mandater = []  
    new_votes, new_parties = zip(*valgresultat(party_list, votes, N_seats))  
    for i in party_list:
        mandatcount = new_parties.count(i)
        mandater.append(mandatcount)
    ny = []
    for i in mandater:
        if i == 0:
            continue
        else:
            ny.append(i)
    length = len(ny)
    parties = party_list[:length]
    voteamount = votes[:length]
    zip_info = zip(parties, voteamount, ny)
    valginfo = list(zip_info)
    return valginfo

def pretty(mandater):
    layout = ("{:<6} {:<8} {:<0}".format('Parti','Stemmer','Mandater',"\n"))                # Brukte format funksjonen som eg lærte på:
    length = len(layout)                                                                    # delftstack https://www.delftstack.com/howto/python/data-in-table-format-python/ 17.10.21
    layout += "\n" +"="*(length) +"\n"                                                      # Legger til = tegna som skiller navna til kolonnene og infoen i kolonnene
    for i in mandater:                                                                      # {:<number} er det som vil bestemme avstanden, så vi endre den til den ser nokelunde lik ut den som står i oppgava
        parti, stemmer, mandat = i 
        layout += ("{:<8} {:<13} {:<0}".format(parti, stemmer, mandat)+"\n")
    layout = layout[:-1]
    return layout




print(parti_mandater(parties, votes, N_seats))
print(valgresultat(parties, votes, N_seats))
print(pretty(parti_mandater(parties,votes,N_seats)))