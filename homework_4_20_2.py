"""Python提供的sum()函数可以接受一个list并求和，
请编写一个prod函数，可以接受一个list并利用reduce求积"""
from functools import reduce


def mul(x, y):
    return x * y


def prod(l):
    return reduce(mul, l)


input_list = [1, 2, 3, 4, 5, 6]
print(prod(input_list))
