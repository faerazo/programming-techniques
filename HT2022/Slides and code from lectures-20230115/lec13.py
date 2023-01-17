#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# LECTURE 13

# What did we do in this course?

# - Output (print) / Input (input)

print("hello world")

# - Expressions
#   "Formulas" that we can write in Python that return something
#   (sometimes None), and can be built out of different operators
#   - arithmetic: +, *, / , .... applied to ints and other types

4 + (5 * 3) + 2
"hi" * 3

class Dog:
    def __init__(self,value):
        self.value = value
        
    def __add__(self, other):
        return Dog(self.value * other.value)
    
    def __str__(self):
        return str(self.value)
    
    def __int__(self):
        return self.value

#   - boolean expressions:
    
True or False and not True

#   - function applications

print("hello world")

#   - variables, where we store things

x = 5
x + 3

#   - lists
#     - mutability

l = [1,2,3,4]
l.append(5)
l[3:5]
l[::-1]

l2 = [x ** 2 for x in range(5)]
4 in l2 # boolean expression


#    - dictionaries
#      instead of storing things in a line,
#      have things indexed by keys

d = {4: "hi", 2: "bye"}
for k,v in d.items(): # or d or d.values()
    print(k,v)
    
len(d) # get the number of key-value pairs
# __len__ method

# - Types (actually classes)
#   - sometimes we need to convert things, sometimes happens automatically

#my_str = input("What's your age? ")
# age = int(my_str)

# print("your age is " + str(age))

# - Statements
#   - Variable assignments

x = 5

#   - Function definitions
#     - global and local variables, scoping

def f(x): # parameters
    # body
    return x + 4

def g(y):
    x = 6
    return x + y

def h():
    return x

#   - If statements
#     control flow

def j(x):
    return x == 5

if j(x): # expression returns a boolean
    print("hi")
elif x == 4:
    print("bye")
else:
    print("no!!!")

#   - For and while loops

l = [0,1,2,3,4]
for x in l: # variable + list expression
    print(x) # body

while 2 in l: # boolean expression
    l.pop()

l = [[3,2], [5,3], [8,4]]
def my_fun(lst):
    """
    Takes in a list of lists,
    checks if any element of any list is 5
    """
    for inner_list in lst:
        for x in inner_list:
            if x == 5:
                return True     
    return False

for c in "hello there":
    print(c)
    
#   - Try, except, raise, and exceptions

try:
    try:
        for x in [1,2,3,4,5,6]:
            print(x)
            raise ZeroDivisionError
    except ValueError:
        print("there was a value error!")
except ZeroDivisionError:
    print("there was a zero division error!")
    
def find_or_cry(l,x):
    try:
        return l.index(x)
    except ValueError:
        return "boohoo i'm so sad"
    
# File handling
# works with "handles"

handle = open("moby-dick.txt", "r") # or "w"
handle.close()

# more convenient
with open("moby-dick.txt","r") as handle:
   # handle.read() handle.readline(), handle.readlines()
   for line in handle:
       pass#print(line.upper()) 

# Functional programming
# - recursion
# - higher-order functions

def factorial(n):
    if n == 0: # base case
        return "1"
    else: # recursive call to a smaller argument
        return str(n) + " * " + factorial(n-1) # recursive call

# think of non-negative ints as made by adding one
# think of lists as made by appending one item at a time

def double(x):
    return x * 2

def apply_twice(f,x):
    return f(f(x))

apply_twice(double,5)

def my_map(f,l):
    return [f(x) for x in l]

# anonymous function
f = lambda x: x * 2

# Generators

def those_greater_than_5(l):
    for x in l:
        if x > 5:
            yield x

for x in those_greater_than_5([3,8,5,7,2,4]):
    print(x)

# Modules and importing
# Organization of programs:
    # - functions
    # - modules to separate your code into files and use others' code
    # - import with import

import math as M
M.sqrt(5)
from math import sqrt
sqrt(5)

# Object-orientation

class A: # superclass
    class_attr = 6
    
    def __init__(self):
        self.instance_attr = 5
        pass
    
    def method(self,x):
        return self.instance_attr
    
class B(A): # subclass that inherits from A
    def new_method(self):
        return self.method(6)
    
assert 0 == 0 # defensive programming
# testing and unit testing

class Triangle:
    def __init__(self, h, w):
        self.height = h
        self.width = w

    def area(self):
        return 0.5 * self.height * self.width
    
    def shrink(self):
        self.height /= 2
        self.width /= 2

t = Triangle(4,4)
u = Triangle(3,2)
v = Triangle(1,2)

for tri in [t,u,v]:
    print(tri.area())
    
# 5 min = 14:35