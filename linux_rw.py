import os
import sys

if len(sys.argv) == 1:
        f1 = open("newdummy.txt", 'w+')
        f1.write("This is new file text. This will be re-read once again.")
        f1.seek(0)
        print("We wrote the following:")
        print(f1.read())
        f1.close()
else:
    print("Too many or too few arguments.")
