# open ("", "")
# open takes 3 parameters. filename, mode, buffering
# read()
# readline()
# readlines()

f1 = open("dummy.txt", 'r')
print(f1.read())

f1.seek(0)

print(f1.readline())

print(f1.readlines())
# print(f1.read())
f1.close()
