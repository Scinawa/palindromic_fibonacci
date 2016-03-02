#!/usr/bin/python3
__author__ = 'user'

from tests import *
from itertools import *
import functools
from pprint import pprint
import sys

""" Decorators """


def decorator(d):
    "Make function d a decorator: d wraps a function fn."

    def _d(fn):
        return functools.update_wrapper(d(fn), fn)

    return _d


decorator = decorator(decorator)


@decorator
def trace(f):
    indent = '   '

    def _f(*args):
        signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        print('%s--> %s' % (trace.level * indent, signature))
        trace.level += 1
        try:
            result = f(*args)
            print('%s<-- %s == %s' % ((trace.level - 1) * indent,
                                      signature, result))
        finally:
            trace.level -= 1
        return result

    trace.level = 0
    return _f


"""" Algorithms for finding fibonacci sequences """


def find_all_fibonacci1(seq):
    """
    This function is a wrapper of find_all_finbonacci1_ which actually does
    all the recursive work. This function unwrap the results of the real
    function, and add all the single elements (x,1) to the set of results,
    and the double elements (x,2).

    :param seq: a sequence of unsigned int.
    :return: the set of all (index, len) of sub-sequences that satisfy the
    fibonacci condition
    """

    # @trace
    def find_all_fibonacci1_(seq, pos=0, start=0, results=None, is_rec=0):
        """
        Find all the Fibonacci sequences of length > 2 in a recurisve flavour.
        It specifically needs python3 because of iterable unpacking.

        :param seq: the sequence
        :param pos: position in the sequence
        :param start: the last position where a sequence started
        :param results: a set of (index, length) of valid Fibonacci sequences.
        :param is_rec: keep track if in recursion branch
        :return: the complete set of (index, length) of valid Fibonacci
        sequences.
        """
        if results is None: results = set()
        if len(seq) == 0 and pos == 0:  return seq, {(0, 0)}

        try:
            a, b, c, *d = seq[pos:]
        except ValueError:  # better ask forgiveness than permission: if len > 3
            if len(seq[pos:]) == 1: results.add((pos, 1))
            if len(seq[pos:]) == 2:
                results |= {(pos, 1), (pos, 2), (pos+1, 1)}
            return pos, results

        if (a == c) or (a + b == c) or (a == b + c):
            elm = {(i, pos + 3 - i) for i in range(start, pos + 3)}
            results |= elm
            pos, results = find_all_fibonacci1_(seq, pos + 1, start, results, 1)
        else:
            if is_rec:
                return pos, results
        start = pos
        if d:
            return find_all_fibonacci1_(seq, pos + 1, pos + 1, results)
        else:
            return pos, results

    pos, results = find_all_fibonacci1_(seq)
    results |= {(i, 1) for i in range(0, len(seq))} | \
               {(i, 2) for i in range(0, len(seq) - 1)}

    return results


def find_all_fibonacci2(seq):
    """
    Return all the possible pair (index, length) satisfying the "fibonacci
    condition".

    parm: seq: list of unsigned int
    return: (i, len) where i is the position in the seq. and len in the length.
    """
    if not seq:
        return {(0, 0)}

    results = set()

    # take the position of the sequence that matter.
    condition = lambda a, b, c: (a == c) or (a + b == c) or (a == b + c)
    triplets = [pos for pos, item in enumerate(zip(seq, seq[1:], seq[2:]),
                                               0) if condition(*item)]

    # group contiguous sequences of valid triplets
    neighbours = []
    for k, g in groupby(enumerate(triplets),
                        key=lambda enum: enum[1] - enum[0]):
        neighbours.append([i[1] for i in g])

    for g in neighbours:
        for i in product(g, g + [max(g) + 1, max(g)+2, max(g) + 3], repeat=1):
            if sorted(i) == list(i) and i[1] - i[0] > 0 and i[0] <= max(g):
                results.add((i[0], i[1] - i[0]))

    results |= {(i, 1) for i in range(0, len(seq))} | \
               {(i, 2) for i in range(0, len(seq) - 1)}

    return results


""" All in one approach """


def all_in_one(seq):
    """
    It is the core of Solution 3. It does everything in a C-style algorithm.
    Al the necessary check for symmetry are embedded in this function.

    :param seq: a sequence of unsigned integers
    :return: (index, offset) such as sequence[index:index+offset] is the
    longest palindrome sub-sequence that satisfy the fibonacci condition.

    """

    def create_combinations(start, y):
        combi = set()
        for a in range(start, y + 2):
            for b in range(start + 1, y + 3):
                if a < b:
                    combi.add((a, b - a))
        return combi

    def keep_matching(start, results):
        y = start
        while (y < len(seq) - 2):
            a, b, c = seq[y:y + 3]
            if (a == c) or (a + b == c) or (a == b + c):
                y += 1
            else:
                break
        results |= {(a, b) for a, b in create_combinations(start, y)
                    if seq[a:a + b] == seq[a:a + b][::-1]}
        return y, results

    if len(seq) == 0: return ((0, 0))
    # if len(seq) == 1: return ((0, 1))

    results = set()
    i = 0

    while (i < len(seq) - 2):
        a, b, c = seq[i:i + 3]
        if (a == c) or (a + b == c) or (a == b + c):
            i, results = keep_matching(i, results)
            i += 1
        else:
            i += 1

    # add manually all elements of length 2 (if symmetric) and 1.
    results |= {(i, 1) for i in range(0, len(seq))} | \
               {(i, 2) for i in range(0, len(seq) - 1)
                if seq[i:i + 2] == seq[i:i + 2][::-1]}

    return max(results, key=lambda x: x[1])


""" Algorithm for symmetry """

def symmetry(sequence, positions):
    """
    Return those (start, len) elements of the sequence that points to a
    symmetric sequence of element.

    :param sequence: list or tuple.
    :param positions: iterable of (start, offset)
    :return: a set of (start, offset) such as
    sequence[start:start+offset] == sequence[start:start+offset].reverse()

    Note:
    [a:b:-1] wont work, because of how list slicing is made in python (b
    should be None to reach the first element of the string)
    I could have used .reverse() as well.
    """
    return {(start, offset) for start, offset in positions if
            sequence[start:start + offset] ==
            sequence[start:start + offset][::-1]}


"""" Putting everything together """

def find_palindrome_fibonacci1(sequence):
    """
    First algorithm for solving the problem.

    :param sequence: a sequence of unsigned integers
    :return: (startIndex, length). such as sequence[
    startIndex:startIndex+length] satisfy the condition of the problem.
    """

    return max(symmetry(sequence, find_all_fibonacci1(sequence)),
               key=lambda x: x[1])


def find_palindrome_fibonacci2(sequence):
    """
    Second algorithm for solving the problem

    :param sequence: a sequence of unsigned integers
    :return: (startIndex, length). such as sequence[
    startIndex:startIndex+length] satisfy the condition of the problem.
    """

    return max(symmetry(sequence, find_all_fibonacci2(sequence)),
               key=lambda x: x[1])


def find_palindrome_fibonacci3(sequence):
    """
    Third algorithm for solving the problem

    :param sequence: a sequence of unsigned integers
    :return: (startIndex, length). such as sequence[
    startIndex:startIndex+length] satisfy the condition of the problem.
    """

    return all_in_one(sequence)


def FindFibonacciPalindrome(sequence):
    """
    More detail in this implementation are in the Documentation and the
    docstrings of the functions.

    :param sequence: a sequence of unsigned integers
    :return: (startIndex, length). such as sequence[
    startIndex:startIndex+length] satisfy the condition of the problem.
    """
    return find_palindrome_fibonacci1(sequence)  # change 1 to 2 or 3


if __name__ == "__main__":

    if test_find_palindrome_fibonacci1():
        print("1] Passed tests for Solution 1")

    if test_find_palindrome_fibonacci2():
        print("2] Passed tests for Solution 2")

    if test_find_palindrome_fibonacci3():
        print("3] Passed tests for Solution 3")

    if test_partial_1_2():
        print("4] Passed tests for (partial) Solution 1 and Solution 2")

    if test_random_strings():
        print("5] Passed tests on 1000 random sequences (just check for "
              "exceptions)")

    print("\nExample: [1,2,1]:")
    print(FindFibonacciPalindrome([1, 2, 1]))
