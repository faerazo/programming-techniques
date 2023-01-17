#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# LECTURE 12

# "DEFENSIVE PROGRAMMING"
# planning for code going wrong
# things like testing

def fib(n):
    # Defensive programming by raising errors
    # in the case of bad inputs
    if type(n) != int:
        raise TypeError("Called fib with non-integer")
    elif n < 0:
        raise ValueError("Called fib with negative number")
    elif n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Exceptions
# - For situations that are expected but unusual
# - For situations that we might want to handle (or recover from)

try: 
    l = [1,2,3,4]
    l.index(6) # not in the list
except ValueError:
    pass

# Assertions
# - For situations that are really fatal

assert 1 == 1

# Example: binary search
# Binary search is an efficient way to find an element
# in a sorted list

# reference implementation
def linear_search(l, x):
    for i in range(len(l)):
        if l[i] == x:
            return i
    raise ValueError

def linear_is_in(l, x):
    try:
        linear_search(l,x)
        return True
    except ValueError:
        return False

# thing to test
def binary_search(l, x):
    """
    l: a sorted list
    x: an element to look for
    Returns the index of an occurrence of x in l if there
    is one, raises a ValueError otherwise
    """
    # pre-conditions
    # obligation of the user
    assert isinstance(l, list) # l is an instance of a subclass of list
    assert sorted(l) == l, "Input list is not sorted"
    if l == []:
        raise ValueError
    lower = 0
    upper = len(l)
    if l[lower] > x or l[upper-1] < x:
        assert not linear_is_in(l,x) # post-condition
        raise ValueError   
    while lower < upper + 1:
        # checking that some things remain true as we go
        # through a loop == "loop invariants"
        assert l[lower] <= x, f'Value {l[lower]} at {lower} is greater than {x}'
        assert l[upper-1] >= x, f'Value {l[upper-1]} at {upper-1} is less than {x}'
        # looking for the element in l[lower:upper]
        mid = lower + (upper - lower) // 2
        if l[mid] == x: # found what we want
            return mid
        elif l[mid] > x: # element we want is smaller
            upper = mid
        elif l[mid] < x: # element we want is larger
            lower = mid + 1
    if l[lower] == x:
        return lower
    else:
        # element is not in the list---our guarantee to the user
        assert not linear_is_in(l,x) # post-condition
        raise ValueError

# pre-condition: something the user guarantees
# post-condition: something that we guarantee
# loop invariant: something we expect to remain true,
#  every time we go through a loop

# ensured by the end of our function/program/etc

# UNIT TESTING

# general idea:
# - design your code so that you can test "units" of it
#   that is, pieces in isolation

