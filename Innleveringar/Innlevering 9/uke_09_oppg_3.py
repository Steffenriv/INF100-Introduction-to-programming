my_dict = {
  0 : 0,
  1 : "vafler",
  "two" : 2,
  5 : 4
}

my_list = [0, 1, "boller", 4]

print("Dictionary Keys:")
for keys in my_dict.keys():
    print(keys)
print("")

print("Dictionary Values:")
for values in my_dict.values():
    print(values)
print("")

print("Dictionary keys/value:")
for k,v in my_dict.items():
    print(k,v)
print("")

print("List values:")
for i in range(len(my_list)):
    print(my_list[i])
print("")

print("List indices/value:")
for i in range(len(my_list)):
    print(i, my_list[i])