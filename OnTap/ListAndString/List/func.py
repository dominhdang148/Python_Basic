def InterchangeFirst_Last(a: list):
    a[0], a[-1] = a[-1], a[0]
    return a


def SwapElements(a: list, pos1: int, pos2: int):
    a[pos1], a[pos2] = a[pos2], a[pos1]
    return a


def GetLength(a: list):
    s = 0
    for item in enumerate(a):
        s += 1
    return s


def CheckExist(a: list, item):
    return item in a


def CleanList(a: list):
    a = []
    return a


def Reversing(a: list):
    result = []
    for item in a:
        result.insert(0, item)
    return result