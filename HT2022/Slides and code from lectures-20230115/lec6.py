#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# LECTURE 6
# SEQUENCES, GENERATORS, DEBUGGING

# SEQUENCES
# A sequence is one of a few different things in Python
# examples:
    # - list
    # - string
# today we'll talk about some more
    # - tuples
    # - range
    
# Both lists and strings are "collections" of
# smaller things
# - string is a collection of characters
#   ("a", "b", "c")
# - list is a collection of anything
# The smaller things are collected in a linear order

list1 = [1,2,3,4,5]
list2 = [6,8,100]

str1 = "hello"
str2 = "world"

# indexing / lookup

list1[3]
str1[3]

list1[1:4]
str1[1:4]

# test what's inside or not inside a sequence

100 in list1
100 in list2
"e" in str1
"ell" in str1

# iterate over sequences

def function0():
    for i in list1:
        print(i)
        
    for c in str1:
        print(c)
        
# - lists are mutable,
# - strings are immutable

list1[4] = 101 # mutating a list
list1.append(-4)

# mutating "in-place" is good for SPACE EFFICIENCY
# but mutation can also be dangerous!
# sometimes, we mutate things without meaning to
# and it can be hard to find these mistakes

# multiply_lists([1,2,3],[4,5,6]) == [1*4, 2*5, 3*6]

def multiply_lists(list1,list2):
           # range(3)
           # 0,1,2
    for i in range(len(list1)):
        list1[i] = list1[i] * list2[i]
    return list1 # changing list1

# response to a question
def print_list(list1):
    for i, u in enumerate(list1):
        print(i,u)
        
# strings in Python are immutable

def function1():
    try:
        str1[1] = "t"
    except TypeError:
        print("oh no!")

# TUPLES
# tuples are like strings but "for anything"
# tuples are like lists but immutable

tup1 = ("a","b",101)
tup2 = (1,2)
tup3 = (4,)

tup1[2]
# tup1[2] = 4
tup1 + tup2

# confident that this doesn't change tuple inputs
def multiply_tuples(tup1,tup2):
    result = ()
    for i in range(len(tup1)):
        result = result + (tup1[i] * tup2[i],)
    return result

# RANGES
# another immutable sequence type
# which is also LAZY

range(0,10)

# lists are EAGER

# GENERATORS
# "your own ranges"

# example of a generator
# to mimic range(n)
def range_generator(n):
    """
    Generates the numbers from 0 to n (exclusive)
    """
    i = 0
    while i < n:
        yield i
        i += 1       
      
# how about range for pairs?
# (1,3)
# stop at (4,6)
# (1,3), (2,4), (3,5), (4,6)

def pair_generator(x1,y1,x2,y2):
    x = x1
    y = y1
    while (x,y) != (x2,y2):
        yield (x,y)
        x += 1
        y += 1

# DEBUGGING

def collides(x1,y1,x2,y2):
    """
        Tests if adding (1,1) to (x1,y1)
        repeatedly will get us to (x2,y2)
    """
    x = x1
    y = y1
    while not (x == x2 and y == y2):
        x += 1
        y += 1
        if x > x2 or y > y2:
            return False
        print(x,y)
        print(x != x2)
        print(y != y2)
    return True

# example from an earlier lecture

def eval_poly(p,x):
    result = 0
    for degree, coeff in p.items():
        result += coeff * x ** degree
    return result

def add_poly(p,q):
    result = p.copy()
    for degree, coeff in q.items():
        current = result.get(degree,0)
        result[degree] = current + coeff
    return result

# testing with ax⁰ + bx¹ (a + bx)
for a in range(100):
    for b in range(100):
        poly = {0: a, 1: b}
        poly2 = add_poly(poly,poly)
        if eval_poly(poly2,4) != 2 * eval_poly(poly,4):
            print(a,b)
            
# try and find a minimal test that causes a bug

    