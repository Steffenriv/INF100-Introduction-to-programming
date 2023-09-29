from copy import copy

a = (
  ("mandag", 16.0),
  ("tirsdag", 13.0),
  ("onsdag", 14.0),
  ("torsdag", 13.0),
  ("fredag", 15.0),
  ("lørdag", 13.0),
)

b = copy(a)

def adjust_daily_temps(y):
    x = list(y)
    x[3] = ("torsdag", 12) 
    y = tuple(x)
    return y
    


print(adjust_daily_temps(b))