__author__ = "Shobhit Kundu"
__copyright__ = "Copyright (C) 2020 Shobhit Kundu"
__license__ = "Public Demo"
__version__ = "1.0"

import math

def add(nm1, nm2):
    return nm1+nm2


def sub(nm1, nm2):
    return nm2-nm1


def mul(nm1, nm2):
    return nm1*nm2


def div(nm1, nm2, md='q'):
    """
    md:q, r, fd
    q = 3/2 = 1.5
    r = 3/2 = 1
    fd = 7/4 = 1 insted of 1.75
    """
    if md=='r':
        return nm1%nm2
    elif md=='fd':
        return nm1//nm2
    else:
        return nm1/nm2

def log(a,b=None):
    return math.log(a,b)


def sqr(a,b=2):
    return a**b


def rt(a,b=2):
    return a**(1/b)