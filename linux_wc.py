import os
import sys

if len(sys.argv) == 2:
    path_of_source = sys.argv[1]
    if os.path.isfile(path_of_source):
        f1 = open(path_of_source)

        text = f1.read()
        characters = len(text)
        words = len(text.split())
        f1.seek(0)
        lines = len(f1.readlines())
        print "Words:", words, "Characters:", characters, "Lines:", lines
        f1.close()

    else:
        print("Source File does not exist.")
else:
    print("Too many or too few arguments.")
