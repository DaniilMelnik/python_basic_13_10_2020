"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""
def my_max(arg1, arg2, *args):
    if(len(args) == 0):
        if arg1 > arg2:
            return arg1
        else:
            return arg2
    else:
        if arg1 > arg2:
            for arg in args:
                if arg > arg1:
                    arg1 = arg
            return arg1
        else:
            for arg in args:
                if arg > arg2:
                    arg2 = arg
            return arg2


def my_func(a, b, c):
    return my_max(a + b, a + c, b + c)


print(my_func(3,5,7))
