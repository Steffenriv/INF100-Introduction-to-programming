a = []
b = "True"
c = 42 
d = -1.5 

#print(type(a*b))           error
print(type(b*c))           #string
#print(type('b'+ c))       error
print(type(c*a))            #list
print(type(c == 10.3))      #bool
print(type(a+a))            #list
#print(type(len(c)))        error
print(type(f"{int(d)+c}")) #string
print(type([b]))            #list
#print(type(a+b))           error

# Få rekkefølga A B C

a = 450

if a > 100:
    print('A')
if a > 400:
    print('B')
if a % 10 == 0:
    print('C')
elif a <  1000:
    print('D')

xs {
    'a' : 5,
    '5' : hello,
    'z' : 3.1415,
    '5' : 7
}

sum = 0

for x in xs[:3]:
    if x > 5:
        sum += x
        