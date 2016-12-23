import math


def add(operand1, operand2):
    "Takes two integer or float and returns the sum of the two numbers."
    return operand1 + operand2


def subtract(operand1, operand2):
    "Takes two integer or float and returns the difference of first from the second."
    return operand1 - operand2


def multiply(operand1, operand2):
    "Takes two integer or float and returns the product of the two numbers."
    return operand1 * operand2


def divide(operand1, operand2):
    "Takes two integer or float and returns the division result of first by second."
    return operand1 / operand2


def sine(operand1):
    "Takes one argument in radians and returns the sine of that operand."
    return math.sin(operand1)


def cosine(operand1):
    "Takes one argument in radians and returns the cosine of that operand."
    return math.cos(operand1)


def power(operand1, operand2):
    "Takes two integer or float and returns the division result first / raised to the power of second."
    return operand1 ** operand2


def squareroot(operand1):
    "Takes one argument and returns its squareroot"
    return math.sqrt(operand1)
