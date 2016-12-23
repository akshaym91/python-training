import os
import sys

if len(sys.argv) == 2:
    path_of = sys.argv[1]
    if os.path.isfile(path_of):
        f1 = open(path_of)
        print(f1.read())
        f1.close()
    else:
        print("File does not exist.")
else:
    print("Too many or too few arguments.")
