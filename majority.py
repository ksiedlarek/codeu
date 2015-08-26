import pytest


def has_majority(alist):
    majority_point = 0.5 * len(alist)
    occurences = [[item, alist.count(item)] for item in alist]
    for item in occurences:
        if item[1] > majority_point:
            return item[0]
    return None


def test_has_majority():
    alist = [5, 3, 9, 4, 3, 3, 8, 3, 3]
    assert has_majority(alist) == 3


def test_without_majority():
    alist = [5, 3, 9, 4, 3, 3, 8, 3]
    assert has_majority(alist) is None
