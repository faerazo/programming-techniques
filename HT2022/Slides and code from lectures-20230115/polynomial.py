#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    A library for working with polynomials.
    Polynomials are represented as dictionaries from degrees to coefficients
"""

# {0:2,3:1}
# 2x^0 + 1x^3

def polynomial_from_list(lst):
    """
    Creates a polynomial from a list of coefficients.

    Parameters
    ----------
    lst : list

    Returns
    -------
    d : polynomial
    """
    d = {}
    for degree,coeff in enumerate(lst):
        d[degree] = coeff
    return d

def eval_at(p,x):
    """
    Evaluate the polynomial p at the value x

    Parameters
    ----------
    p : polynomial
    x : int, float, or complex
        A value at which to evaluate the polynomial

    Returns
    -------
    result : int, float, or complex
    """
    result = 0
    for degree, coeff in p.items():
        result += coeff * x ** degree
    return result

def add(p,q):
    """
    Return a new polynomial obtained by adding polynomials p and q.

    Parameters
    ----------
    p : polynomial
    q : polynomial
    Returns
    -------
    result : polynomial
    """
    result = p.copy()
    for degree, coeff in q.items():
        current = result.get(degree,0)
        result[degree] = current + coeff
    return result

def mult(p,q):
    """
    Return a new polynomial obtained by multiplying polynomials p and q.

    Parameters
    ----------
    p : polynomial
    q : polynomial
    Returns
    -------
    result : polynomial
    """
    result = {}
    for degree1, coeff1 in p.items():
        for degree2, coeff2 in q.items():
            sum_degree = degree1 + degree2
            current = result.get(sum_degree, 0)
            result[sum_degree] = current + coeff1*coeff2
    return result

if __name__ == '__main__':
    print("Welcome to the polynomial module. Running tests:")
    if eval_at({0:0},0) == 0:
        print("All tests passed!")
    else:
        print("Oh no!")
