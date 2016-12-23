import unittest
import doctest


def myavg(a, b):
    """
    tests this problem
    >>> myavg(10,20)
    15
    >>> myavg(2,4)
    3
    >>> myavg(1,1)
    1
    """
    return (a + b) / 2

doctest.testmod()


def multiply(x, y):
    return x * y


class TestStringMethods(unittest.TestCase):
    """docstring for TestStringMethods"""

    def test_mulitply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(2, 4), 8)

if __name__ == '__main__':
    unittest.main()
