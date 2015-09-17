import pytest


def check(text):
    results = []
    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i+1]
            if chunk == chunk[::-1]:
                results.append(chunk)
    if results:
        value = max(results, key=len)
        return text.index(max(results, key=len)), len(value)
    else:
        return 'No palindrome here.'


def test_simple_string():
    assert check('panama') == (1, 3)


def test_not_palindrome():
    assert check('not') == 'No palindrome here.'


def test_given_example():
    assert check('12111122221212121') == (9, 7)
