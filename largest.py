import pytest


def merge_sort(alist):
    if len(alist) > 1:
        middle = len(alist) // 2
        left = alist[:middle]
        right = alist[middle:]

        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1
    return alist


def nth_largest(alist, number):
    if number != 0 and number < len(alist):
        return alist[-number]
    if number == 0:
        raise Exception("The nth_largest parameter can't be 0.")
    if number >= len(alist):
        raise Exception("The nth_largest parameter excedees list length.")

alist = [100, 98, 200, 30000, -1, 12, 0]
alist = merge_sort(alist)

def test_exception_zero():
    with pytest.raises(Exception):
        nth_largest(alist, 0)

def test_exception_to_large():
    with pytest.raises(Exception):
        nth_largest(alist, len(alist) + 1)

def test_the_same_numbers():
    alist = [1] * 100
    assert nth_largest(alist, 3) ==  1

def test_large_sorted_input():
    alist = [x for x in range(500000)]
    assert nth_largest(alist, 50) == 499950
