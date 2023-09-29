tup1 = (
  ("mandag", 16.0),
  ("tirsdag", 13.0),
  ("onsdag", 14.0),
  ("torsdag", 13.0),
  ("fredag", 15.0),
  ("lørdag", 13.0),
)

def data_reorganize(x):
  a,b = zip(*x)
  return a,b

print(data_reorganize(tup1))