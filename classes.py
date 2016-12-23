# __<name>__ : Builtin name(Standard name) in classes
# __init__(): Constructor
# __del__(): Destructor


class A(object):
    """docstring for A"""

    def __init__(self, arg):
        super(A, self).__init__()
        self.arg = arg
        self.x = 10
        self._y = "Semi private"
        self.__z = "Fully private"
        print "inside the constructor"

    def fn1(self):
        print "fn(1)"

    def _fn2(self):
        print "Semiprivate fn(2)"

    def __fn3(self):
        print "Fully private fn(2)"

    def __del__(self):
        print "inside the destructor"

#
# Conventionally 'self' is used for referring to 'this'
# Private: __something
# Semiprivate: _something
# Public: something
# Fully private also can be accessed indirectly by using
# object._classname__fullyprivatevariable
# object._classname__fullyprivatefunction
#
# Inheritance and Custom Exceptions:


class SpecialException(Exception):
    pass
    try:
        raise SpecialException
    except SpecialException:
        print "SpecialException is Working"

"""
In [10]: str = "Akshay"

In [11]: str
Out[11]: 'Akshay'

In [12]: str(12)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-12-f8aff8fbe7bf> in <module>()
----> 1 str(12)

TypeError: 'str' object is not callable

In [13]: del str

In [14]: str(12)
Out[14]: '12'
"""
