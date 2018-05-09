#!/usr/bin/python

from time import sleep
'''
def foo(bar):
    print ('INSIDE FOO..')
    return bar + 1

print('foo is',foo)
print('foo(2) is',foo(2))
print('type(foo)...',type(foo))


def call_foo_with_arg(foo, arg):
    print ('INSIDE CALL_FOO_WITH_ARG. ARG..',arg)
    return foo(arg)

print(call_foo_with_arg(foo, 3))
'''



def sleep_decorator(function):

    """
    Limits how fast the function is
    called.
    """

    def wrapper(*args, **kwargs):
        sleep(2)
        print ('INSIDE WRAPPER OF SLEEP_DECORATOR..',function(*args, **kwargs))
        return function(*args, **kwargs)
    return wrapper

# @sleep_decorator is same as following
# print_number = sleep_decorator(print_number)
# print_number(arg)

# any function following @decorator will be passed as an argument to def decorator(f)
# the contents of that function will be printed as part of wrapper func inside def deco...

@sleep_decorator
def hello():
    print ('hello world')

hello()

@sleep_decorator
def print_number(num):
    return num

print(print_number(222))

for num in range(1, 6):
    print(print_number(num))
