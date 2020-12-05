__author__ = "Shobhit Kundu"
__copyright__ = "Copyright (C) 2020 Shobhit Kundu"
__license__ = "Public Demo"
__version__ = "1.0"

import math


def add(nm1, nm2):
    """
    :param nm1: int or float
    :param nm2: int or float
    :return: int or float
    """
    return nm1+nm2


def sub(nm1, nm2):
    """
    :param nm1: int or float
    :param nm2: int or float
    :return: int or float
    """
    return nm2-nm1


def mul(nm1, nm2):
    """
    :param nm1: int or float
    :param nm2: int or float
    :return: int or float
    """
    return nm1*nm2


def div(nm1, nm2, md='q'):
    """
    :param nm1: int or float
    :param nm2: int or float
    :param md: str 'q', 'r', 'fd'
    q = 3/2 = 1.5
    r = 3/2 = 1
    fd = 7/4 = 1 instead of 1.75
    :return: int or float
    """
    if md == 'r':
        return nm1 % nm2
    elif md == 'fd':
        return nm1//nm2
    else:
        return nm1/nm2


def log(a, b=None):
    """
    :param a: log of a int
    :param b: base int
    :return: int or float
    """
    return math.log(a, b)


def sqr(a, b=2):
    """
    :param a: int or float
    :param b: int only
    :return: int or float
    """
    return a**b


def rt(a, b=2):
    """
    :param a: int or float to find root of
    :param b: int only
    :return: int or float
    """
    return a**(1/b)
