#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 12:54:13 2022

@author: ecavallo
"""

# LECTURE 7
# MODULES AND "GOOD CODE"

# MODULES

# Modules that we wrote ourselves:

import polynomial as poly # module/library
# import polynomial
# from polynomial import add, eval_at

p = poly.polynomial_from_list([2,0,0,1]) # {0:2,3:1}
q = poly.add(p,p)
poly.eval_at(q,5)
r = poly.mult(p,q)
print(r)

# Python comes with STANDARD LIBRARY
# A bunch of modules that are built in to Python

import math
math.sqrt(45)
dir(math)

# functions for dealing with the operating system
import os

# numerical stuff
import numpy
import scipy

# importing modules within package
# outside the standard library of python
import matplotlib.pyplot

# Currently, to use the polynomial module,
# I would write down some polynomial as a dictionary.

# It would best to have more "ABSTRACTION"
# That is, as a user, I shouldn't have to know how polynomials
# are implemented.

# Abstraction means writing your code in such a way that the user
# doesn't need to know how things are working "internally",
# they only need to know the "interface"

# GOOD CODE

# STYLE
# - avoid long lines
# - document your code (docstrings and comments)
# - follow language conventions

# PEP-8 "Python Enhancement Proposal"
# pep8.org
# https://www.youtube.com/watch?v=hgI0p1zf31k

# CONCEPTUAL
# - abstraction:
#   - think about what a user of your code needs to know,
#     make this an "interface"
#   - make it easy to modify the internals of your code without
#     having to change that interface
#   - applies to both modules and functions
#   - try to write modules and functions so that they
#     group together functionality naturally
#   - avoid code duplication
#
# - avoid global state:
#   - keep information in LOCAL variables and pass it around via
#     via function parameters
#   - the one situation where global variables are GOOD style is
#     for constants---as opposed to using "magic numbers"
#
# - avoid using strings for non-string-like purposes

# hard to write a function like
# add_poly("1x + 5x^2 + 4x^5","4x^2 + 3x^6") == "1x + 9x^2 + 3x^6"

# ways to improve conceptual organization of code
# - functional programming
# - object-oriented programming (classes and so on)

