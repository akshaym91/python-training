# Containers
# List is a mutable container.
LIST = [10, 20, "hi", 40.8]
# Tuple is an immutable container.
TUPLE = (10, "hi", "20")
# Dictionary is a key-value pairs container. Key and value can take any values.
# Keys must always be unique. Is mutable.
DICTIONARY = {10: 20, 30: 40}
DICT_IN_DICT = {10: {10: 20, 20: 30}, 50: 70, 80: 90}
# Sequences are a list of tuples.
SEQUENCE = [10, 20, 30, (40, 50)]
# Negative Indexes
# Slicing [start:end:step]
print("1----------------------------------List")
print(LIST)
print("2: While-------------------------------")
i = 0
while(i < len(LIST)):
    print(LIST[i])
    i = i + 1
print("2: For---------------------------------")
for a in LIST:
    print(a)
print("3--------------------------------------")
LIST.insert(0, 30)
print(LIST)
print("4--------------------------------------")
LIST.insert(1, 40)
print(LIST)
print("5--------------------------------------")
LIST.append(50)
print(LIST)
print("6--------------------------------------")
del LIST[1]
print(LIST)
print("7--------------------------------------")
print(LIST.pop())
print("8--------------------------------------")
LIST.remove(30)
print(LIST)
print("9--------------------------------------")
print(len(LIST))

print("1----------------------------------Tuple")
print(TUPLE)

print("1----------------------------------Dictionary")
print(DICTIONARY)

print("1----------------------------------Dictionary")
print(DICTIONARY.keys())

print("1----------------------------------Dictionary")
print(DICTIONARY.values())

print("1----------------------------------Dictionary")
print(DICTIONARY.has_key(20))

print("1-----------------------------DICT in Dictionary")
print(DICTIONARY.has_key(20))
