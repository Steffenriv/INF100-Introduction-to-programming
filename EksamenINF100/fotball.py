from numpy import e, gcd
import pandas

def make_stats(matches):
    teams = {} # dict of dicts: name -> {GF, GA, GD, PT}
    ########## vvvvvv edit this part vvvvvvv ##############
    teamnames = []
    for i in range(len(matches)):
        if matches[i][0] not in teamnames:
            teamnames.append(matches[i[0]])
        elif matches[i][1] not in teamnames:
    teaminfo = {
        'GF':0,
        'GA':0, 
        'GD':0, 
        'PT':0
    }
    teams.setdefault(teamnames, {})             # Setting default standard for teams dictionarien

    for name in teamnames:                      # Looper gjennom kvart lag i teamnames lista vår
        for i in range(len(matches)):           # Looper gjennom kvar match i matches lista
            if name == matches[i][0]:           
                teaminfo['GF'] += matches[i][2]
                teaminfo['GA'] += matches[i][3]
                teaminfo['GD'] += matches[i][2] - matches[i][3]
                
                if matches[i][2] >= matches[i][3]:
                    teaminfo['PT'] += 3
                elif matches[i][2] == matches[i][3]:
                    teaminfo['PT'] += 1

            elif name == matches[i][1]:
                teaminfo['GF'] += matches[i][3]
                teaminfo['GA'] += matches[i][2]
                teaminfo['GD'] += matches[i][3] - matches[i][2]
                
                if matches[i][3] >= matches[i][2]:
                    teaminfo['PT'] += 3
                elif matches[i][3] == matches[i][2]:
                    teaminfo['PT'] += 1
        teams[name] = teaminfo

            

            # lage ein liste med alle laga
            # vist lagnavn fra lista = lagnavn fra matches[i][1]
            # så skal teams[laget] oppdaterast med 
    

    # real team names should be taken from the "matches" list
    # and the following filled in
    # GF: goals for the team
    # GA: goals agains the team
    # GD: goal difference, always the same as GF-GA
    # PT: points: 3 for win, 1 for draw
    teams['teamname1'] = {'GF':0, 'GA':0, 'GD':0, 'PT':0}
    teams['teamname2'] = {'GF':0, 'GA':0, 'GD':0, 'PT':0}
    teams['teamname3'] = {'GF':0, 'GA':0, 'GD':0, 'PT':0}
    teams['teamname4'] = {'GF':0, 'GA':0, 'GD':0, 'PT':0}
    ########## ^^^^^^ edit this part ^^^^^^^ ##############
    return teams


# an example for the "matches" datastructure
FIFA_1998_A = [
    ("Brazil", "Scotland", 2, 1),
    ("Morocco", "Norway", 2, 2),
    ("Scotland", "Norway", 1, 1),
    ("Brazil", "Morocco", 3, 0),
    ("Brazil", "Norway", 1, 2),
    ("Scotland", "Morocco", 0, 3),
]

# make_stats(FIFA_1998_A) takes this ^^^^ 
# and the return value should be 

FIFA_1998_A_data = { 
    'Brazil': {'GF': 6, 'GA': 3, 'GD': 3, 'PT': 6}, 
    'Scotland': {'GF': 2, 'GA': 6, 'GD': -4, 'PT': 1},
    'Morocco': {'GF': 5, 'GA': 5, 'GD': 0, 'PT': 4},
    'Norway': {'GF': 5, 'GA': 4, 'GD': 1, 'PT': 5}
}

# checking the return value matches what we expect
if make_stats(FIFA_1998_A) == FIFA_1998_A_data:
    print("make_stats looks good, you can remove the exit() line now!\n\n\n")
else:
    print("Something is wrong in make_stats")

exit()

from collections import OrderedDict

def compare(matches, data, a, b):
    """
    Compare two team _names_ a and b. 
    matches is a list of match results.
    data is the result of make_stats(matches).
    
    If a is ranked higher, return 1
    If b is ranked higher, return -1
    If a and b are undecided, print f"LOTTERY {a} {b}" and return 0
    
    Sequence for ranking (go to the next rule if the two teams are equal)
    (1) The higher points score PT wins
    (2) The higher goal difference GD wins
    (3) The higher "goals for" GF wins
    (4) The winner of the direct match between the two teams
        (we will ignore the situation where 3 teams are equal)
    (5) Lottery draw
    """
    ########## vvvvvv edit this part vvvvvvv ##############
    # right now, the team names get ranked based on alphabet
    # need to fix this
 

    sortedbyPoints = OrderedDict(sorted(data.items(), key=lambda x: x[1]['PT'], reverse=True))          # Kilde: https://stackoverflow.com/questions/16412563/python-sorting-dictionary-of-dictionaries, tatt fra svar fra Ashwini chaudhary
    sortedbyGD = OrderedDict(sorted(data.items(), key=lambda x: x[1]['GD'], reverse=True)) 
    sortedbyGF = OrderedDict(sorted(data.items(), key=lambda x: x[1]['GF'], reverse=True)) 
    # Mellom dei ulike ville eg ha satt if data[lag1] == data[lag2] så vil først gd ha noke å seie så gf, deretter ville satt if match where name = team1 and name =team2 så er vinner lik gf - ga og viss - vinne bortlaget viss + vinne heimelaget


    if a > b:
        return 1
    elif b > a:
        return -1
    else:
        print(f"LOTTERY {a} {b}")
        return 0
    ########## ^^^^^^ edit this part ^^^^^^^ ##############
    

######################################################
############# nothing to edit below here #############
############ some more examples for testing ##########
######################################################

FIFA_1994_D = [
    ("Argentina", "Greece", 4, 0),
    ("Nigeria", "Bulgaria", 3, 0),
    ("Argentina", "Nigeria", 2, 1),
    ("Bulgaria", "Greece", 4, 0),
    ("Argentina", "Bulgaria", 0, 2),
    ("Greece", "Nigeria", 0, 2),
]

FIFA_1994_D_data = {
    'Argentina': {'GF': 6, 'GA': 3, 'GD': 3, 'PT': 6}, 
    'Greece': {'GF': 0, 'GA': 10, 'GD': -10, 'PT': 0}, 
    'Nigeria': {'GF': 6, 'GA': 2, 'GD': 4, 'PT': 6}, 
    'Bulgaria': {'GF': 6, 'GA': 3, 'GD': 3, 'PT': 6},
}

FIFA_1994_E = [
    ("Italy", "Ireland", 0, 1),
    ("Norway", "Mexico", 1, 0),
    ("Italy", "Norway", 1, 0),
    ("Mexico", "Ireland", 2, 1),
    ("Italy", "Mexico", 1, 1),
    ("Ireland", "Norway", 0, 0),
]

FIFA_1994_E_data = {
    'Italy': {'GF': 2, 'GA': 2, 'GD': 0, 'PT': 4}, 
    'Ireland': {'GF': 2, 'GA': 2, 'GD': 0, 'PT': 4}, 
    'Norway': {'GF': 1, 'GA': 1, 'GD': 0, 'PT': 4}, 
    'Mexico': {'GF': 3, 'GA': 3, 'GD': 0, 'PT': 4},
}


FIFA_1990_F = [
    ("England", "Ireland", 1, 1),
    ("Netherlands", "Egypt", 1, 1),
    ("England", "Netherlands", 0, 0),
    ("Ireland", "Egypt", 0, 0),
    ("England", "Egypt", 1, 0),
    ("Ireland", "Netherlands", 1, 1),
]

FIFA_1990_F_data = {
    'England': {'GF': 2, 'GA': 1, 'GD': 1, 'PT': 5}, 
    'Ireland': {'GF': 2, 'GA': 2, 'GD': 0, 'PT': 3}, 
    'Netherlands': {'GF': 2, 'GA': 2, 'GD': 0, 'PT': 3}, 
    'Egypt': {'GF': 1, 'GA': 2, 'GD': -1, 'PT': 2},
}

from functools import cmp_to_key, partial

def pretty(order, data):
    print(f"{' ':14} {'GF':>3} {'GA':>3} {'GD':>3}   {'PT':>3}")
    for team in order:
        k = team
        v = data[team]    
        print(f"{k:14} {v['GF']:3d} {v['GA']:3d} {v['GD']:3d}   {v['PT']:3d}")
    print("-"*20)

all_groups = [FIFA_1998_A, FIFA_1994_D, FIFA_1994_E, FIFA_1990_F]
all_data = [FIFA_1998_A_data, FIFA_1994_D_data, FIFA_1994_E_data, FIFA_1990_F_data]

expected = [
    ['Brazil', 'Norway', 'Morocco', 'Scotland'],
    ['Nigeria', 'Bulgaria', 'Argentina', 'Greece'],
    ['Mexico', 'Ireland', 'Italy', 'Norway'],
    ['England', 'Ireland', 'Netherlands', 'Egypt'],
]

for matches,data,ex in zip(all_groups,all_data,expected):
    order = sorted(data, key=cmp_to_key(partial(compare,matches,data)), reverse=True)
    pretty(order, data)
    if order == ex:
        print("This looks good!\n\n\n")
    else:
        print(f"!!! expected {ex}, but got {order}")
        
    
