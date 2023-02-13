def sayhello(name):
    print(f" Hi, {name}")


def _sum_(a, b):
    return a+b


def _sub_(a, b):
    return a-b


def _mul_(a, b):
    return a*b


def _div_(a, b):
    return a/b


def module(a, b):
    if a > b:
        return a-b
    else:
        return b-a


a, b = 40, 5
# print(_sum_(a, b))
# print(_sub_(a, b))
# print(_mul_(a, b))
print(module(a, b))
# sayhello('Rupam')
