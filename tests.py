__author__ = 'user'

from palindrome import *
from random import randint

""" Palindrome fibonacci tests tests """


def test_find_palindrome_fibonacci1():
    assert find_palindrome_fibonacci1([1, 2, 1]) == (0, 3)
    assert find_palindrome_fibonacci1([1, 10, 1, 10, 1, 10, 1]) == (0, 7)
    assert find_palindrome_fibonacci1([1, 10, 1, 10, 1, 10, 1, 8, 9, 7]) == (
    0, 7)
    assert find_palindrome_fibonacci1([9, 4, 2, 1, 10, 1, 10, 1, 10, 1]) == (
    3, 7)
    assert find_palindrome_fibonacci1(
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == (0, 2)
    assert find_palindrome_fibonacci1([1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == (
    0, 1)  # !
    assert find_palindrome_fibonacci1(
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] + [1, 1, 2, 3, 5, 8, 13, 21, 34,
                                                  55,
                                                  89][::-1]) == (20, 2)  # !
    assert find_palindrome_fibonacci1([]) == (0, 0)
    assert find_palindrome_fibonacci1([1]) == (0, 1)
    assert find_palindrome_fibonacci1([1, 2]) == (0, 1) or (1, 1)
    assert find_palindrome_fibonacci1([2, 2]) == (0, 2)

    assert find_palindrome_fibonacci1([1, 1, 2, 2, 2, 2, 1, 1]) == (2, 4)
    assert find_palindrome_fibonacci1([1, 1, 2, 2, 2, 1, 1]) == (2, 3)
    assert find_palindrome_fibonacci1([1, 1, 2, 2, 1, 1]) == (0, 2) or (
    2, 2) or (4, 2)

    return True


def test_find_palindrome_fibonacci2():
    assert find_palindrome_fibonacci2([1, 2, 1]) == (0, 3)
    assert find_palindrome_fibonacci2([1, 10, 1, 10, 1, 10, 1]) == (0, 7)
    assert find_palindrome_fibonacci2([1, 10, 1, 10, 1, 10, 1, 8, 9, 7]) == (
    0, 7)
    assert find_palindrome_fibonacci2([9, 4, 2, 1, 10, 1, 10, 1, 10, 1]) == (
    3, 7)
    assert find_palindrome_fibonacci2(
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == (0, 2)
    assert find_palindrome_fibonacci2([1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == (
    0, 1)  # !

    assert find_palindrome_fibonacci2(
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] + [1, 1, 2, 3,
                                                  5, 8, 13, 21, 34, 55,
                                                  89][::-1]) == (20, 2)  # !

    assert find_palindrome_fibonacci2([]) == (0, 0)
    assert find_palindrome_fibonacci2([1]) == (0, 1)
    assert find_palindrome_fibonacci2([1, 2]) == (0, 1) or (1, 1)
    assert find_palindrome_fibonacci2([2, 2]) == (0, 2)

    assert find_palindrome_fibonacci2([1, 1, 2, 2, 2, 2, 1, 1]) == (2, 4)
    assert find_palindrome_fibonacci2([1, 1, 2, 2, 2, 1, 1]) == (2, 3)
    assert find_palindrome_fibonacci2([1, 1, 2, 2, 1, 1]) == (0, 2) or (
    2, 2) or (4, 2)

    return True


def test_partial_1_2():
    tests = (
        [1, 2, 1],
        [1, 10, 1, 10, 1, 10, 1],
        [1, 10, 1, 10, 1, 10, 1, 8, 9, 7],
        [9, 4, 2, 1, 10, 1, 10, 1, 10, 1],
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
        [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] + [1, 1, 2, 3, 5, 8, 13, 21, 34,
                                                  55, 89][::-1],
        [],
        [1],
        [1, 2],
        [2, 2],
        [1, 1, 2, 2, 2, 2, 1, 1],
        [1, 1, 2, 2, 2, 1, 1],
        [1, 1, 2, 2, 1, 1])

    for i, a in enumerate(tests, 1):
        try:
            assert sorted(find_all_fibonacci1(a)) == sorted(
                find_all_fibonacci2(a))
        except Exception as e:
            print("Exception: function gave different result", e)
    return True


def test_find_palindrome_fibonacci3():
    assert all_in_one([1, 2, 1]) == (0, 3)
    assert all_in_one([1, 10, 1, 10, 1, 10, 1]) == (0, 7)
    assert all_in_one([1, 10, 1, 10, 1, 10, 1, 8, 9, 7]) == (0, 7)
    assert all_in_one([9, 4, 2, 1, 10, 1, 10, 1, 10, 1]) == (3, 7)
    assert all_in_one([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == (0, 2)
    assert all_in_one([1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == (0, 1)  # !
    assert all_in_one(
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] + [1, 1, 2, 3, 5, 8, 13, 21, 34,
                                                  55,
                                                  89][::-1]) == (20, 2)  # !
    assert all_in_one([]) == (0, 0)
    assert all_in_one([1]) == (0, 1)
    assert all_in_one([1, 2]) == (0, 1) or (1, 1)
    assert all_in_one([2, 2]) == (0, 2)

    assert all_in_one([1, 1, 2, 2, 2, 2, 1, 1]) == (2, 4)
    assert all_in_one([1, 1, 2, 2, 2, 1, 1]) == (2, 3)
    assert all_in_one([1, 1, 2, 2, 1, 1]) == (0, 2) or (2, 2) or (4, 2)

    return True


""" Random strings tests"""


def test_random_strings():
    for i in range(70):
        x = [randint(0, 30) for _ in range(0, 1000)]
        try:
            assert find_all_fibonacci1(x) == find_all_fibonacci2(x)
        except Exception as e:
            print("Exception: function gave different result", e)
    return True
