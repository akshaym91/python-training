# Scope resolution follows:
# L: Local
# E: Enclosure
# G: Global
# B: Builtin
# In python there is only one scope in a block(Enclosure).
# Recursion is allowed only 900 times
# Parameter is passed by object: if the type of the object is mutable,
# then the object is new. Else is it overwritten. Integer is immutable.
# Mutability is the ability to edit in bits and pieces.

x = 100
print x


def scoping():
    x = 300
    global x
    print x
    x = 200
    print x

scoping()

print x


def fn():
    print "Outside"

    def fn():
        print"Inside"
    fn()
fn()

dct1 = {10: 20, "sachin": 99}


def passing(*pos, **kwd):
    print "Positional:", pos
    print "Keywords:", kwd

passing(24, 30, 32, a=24, b=32, c=64)
