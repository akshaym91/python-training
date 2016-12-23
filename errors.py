# Errors:
# 1. Command/file not found
# 2. Bad Intepreter
# 3. Syntax error
# 4. Exception (run time error)
# 5. Logical bug a. Code review
#                b. print messages
#                c. Use debugger
#                d. Trial and error
# PDB is the Python Debugger used for debugging. Set the pdb.set_trace()
# pdb> help
# pdb> print(p) breakpoint(b) next(n)
#
import pdb

a = 2+3
# pdb.set_trace()
b = a+5
c = b+a
d = 25

try:
    a = 10/0
    print b
    raise
except ZeroDivisionError, detail:
    print "Divided by Zero, Unacceptable", detail
except NameError, detail:
    print detail
else:
    sys.exit()
finally:
    pass