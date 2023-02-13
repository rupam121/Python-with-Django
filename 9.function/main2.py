

def findlength(n):
    count = 0
    while n > 0:
        count += 1
        n = int(n/10)
    return count


def findsum(n, length):
    ssum = 0
    while n > 0:
        rem = n % 10
        ssum += (rem**length)
        n = int(n/10)
    return ssum


def findanstrom(n, ssum):
    if n == ssum:
        return True
    else:
        return False


def isAnstrom(n, ssum):
    if n == ssum:
        return True
    else:
        return False
    # print()


def arestronginfindlength(_range):
    _sum_ = 0
    for i in range(_range):
        n = i
        lenght = findlength(n)
        _sum_ = findsum(n, lenght)
        if isAnstrom(n, _sum_):
            print(i)


# _range = int(input())
# arestronginfindlength(_range)
