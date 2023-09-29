a = "Hello"
b = 1.3
c = 7
d = True

print(type(a+'b'))          # string        - correct
#print(type(a*b))            # error     - correct
print(type(b*c))            # float     - correct
print(type(f"{d}"))         # string        - correct
#print(type(a+b))            # error        - fekk feil skreiv string
print(type([d]))            # list      - correct
print(type(len(a)))         # int       - correct 
print(type(c*a))            # string        - correct
print(type(c==10.3))        # bool     - sjekker viss den er false eller true og den gir jo svar false så korrekte er bool ikkje error
print(type(a+a))            # string        - correct