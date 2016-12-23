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
# During the inheritance only the constructor of the derived class is called.
# Constructor of the super class has to be explicitly involed like so:
# SuperClass.__init__(self, x, x)
# Multilevel Inheritance
# Multiple Ineritance
#   Precedence class C(A, B): The variables of A will overwrite B.
#


class Shape(object):
    """docstring for Shape"""

    def __init__(self, x, y):
        super(Shape, self).__init__()
        self.x = x
        self.y = y

    def area():
        return self.x * self.y

    def perimeter():
        return 2*(self.x + self.y)


class Square(Shape):
    """docstring for Square"""

    def __init__(self, arg):
        super(Square, self).__init__(arg, arg)
        self.arg = arg

# Multilevel inheritance


class DoubleSquare(Square):
    """docstring for DoubleSquare"""

    def __init__(self, arg):
        super(DoubleSquare, self).__init__()
        self.arg = arg

    def area():
        return 2*super(DoubleSquare, self).__init__(arg, arg)


# Multiple inheritance


class Pyramid(Square, DoubleSquare):
    """docstring for Pyramid"""

    def __init__(self, arg):
        super(Pyramid, self).__init__()
        self.arg = arg

    def area():
        pass

    def perimeter():
        pass

# Static memebers:
# Just before the memeber.
# Accessed using the class name
# Single instance for the class, any number of the object.
#