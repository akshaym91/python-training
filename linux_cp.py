import os
import sys

if len(sys.argv) == 3:
    path_of_source = sys.argv[1]
    path_of_destination = sys.argv[2]
    if os.path.isfile(path_of_source):
        f1 = open(path_of_source)
        f2 = open(path_of_destination, 'w+')
        text = f1.read()
        f2.write(text)
        f1.close()
        f2.close()
    else:
        print("Source File does not exist.")
else:
    print("Too many or too few arguments.")
