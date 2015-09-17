import pytest


def check_if_binary_palindrome(number):
    number = (bin(number)).split('0b')[1]
    reverse = number[::-1]
    if number == reverse:
        return True
    return False


def give_kth_binary_palindrome(k):
    is_palindrome = False
    counter = 1
    value_to_check = 1
    if k != 1:
        while (counter <= k):
            is_palindrome = check_if_binary_palindrome(value_to_check)
            if is_palindrome is True:
                if counter != k:
                    counter += 1
                    value_to_check += 1
                elif counter == k:
                    return value_to_check
            else:
                value_to_check += 1
    return value_to_check


def test_is_palindrome_true():
    assert check_if_binary_palindrome(1) is True
    assert check_if_binary_palindrome(3) is True
    assert check_if_binary_palindrome(5) is True
    assert check_if_binary_palindrome(7) is True


def test_is_palindrome_false():
    assert check_if_binary_palindrome(2) is False
    assert check_if_binary_palindrome(4) is False


def test_first_palindrome():
    assert give_kth_binary_palindrome(1) == 1


def test_fourth_palindrome():
    assert give_kth_binary_palindrome(4) == 7


def test_tenth_palindrome():
    assert give_kth_binary_palindrome(10) == 31
