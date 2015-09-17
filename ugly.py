import pytest


def check(number):
    if number == 1:
        return True
    return any([not number % i for i in [2, 3, 5]])


def kth_ugly(k):
    number = 1
    while k > 0:
        if check(number) is True:
            yield number
            k -= 1
        number += 1


def print_kth_ugly(k):
    alist = list(kth_ugly(k))
    element = alist[len(alist)-1]
    print(element)
    return element


def test_first():
    assert print_kth_ugly(1) == 1


def test_tenth():
    assert print_kth_ugly(10) == 12
