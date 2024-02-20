import math


def greet(name):
    """
    Simple greet function, prints hello
    :param name: string
    :return: None
    """
    print("Hello")


# greet('Homer')
# greet('Tom')
# greet('Max')

def special_op(x=10, y=10, z=10):
    """

    :param x: int or float
    :param y: int or float
    :param z: int or float
    :return: the result of the operation
    """
    return x * y + z


result = special_op(2, 3, 4)
print(result)
print(special_op(2, 3))
print(special_op())

print(special_op(z=2, x=3, y=4))

greet(special_op(2, 3, 4))


def factorial(n):
    """
    Factorial of a number
    :param n: int number
    :return: the value of n!
    """

    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(10))

H = ['1', '5', '10', '12', '34', '2', '3', '2000']
H.append(math.log(2))
print(H)

A = ['a', 'b', 'c']
x = A.pop(0)
print(x)


