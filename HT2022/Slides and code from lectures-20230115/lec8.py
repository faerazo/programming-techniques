#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# LECTURE 8

# FUNCTIONAL PROGRAMMING
# RECURSION and HIGHER-ORDER FUNCTIONS

# What is it?
# A lot of things, which don't necessarily have to go together
# - Programming that involves manipulating functions as
#   objects like any other (just like integers, strings, etc)
# - Programming that makes MORE use of functions than
#   other kinds (as opposed to say loops)
# - Avoiding mutation
# - Strong type system

# We've been doing "imperative programming"
# - programming that involves a lot of loops and mutation

# FUNCTIONAL PROGRAMMING LANGUAGES
# - languages that are especially designed for functional programming
# - Lisp (1958) and descendents (Scheme, Racket)
# - ML (1973) and descendents (OCaml, Standard ML)
# - Haskell (1990)

# RECURSION
# Getting "iteration" without using loops

def f(n):
    if n > 100:
        return "I'm done"
    else:
        print("Calling f with", n+1)
        return f(n+1) # Recursive call
    
# Idea for writing useful recursive functions:
# Write our function to work on larger inputs by
# using the function on smaller inputs
    
# Think of multiplication as repeated addition
# 2 * 3 = 2 + 2 + 2

# "Imperative" way of writing multiplication
def imperative_multiply(m,n):
    """
    Multiplies two integers m,n >= 0
    """
    result = 0
    for i in range(n):
        result += m
    return result

# Think of multiplication as repeated addition
# 2 * 0 = 0
# 2 * 1 = (2 * 0) + 2
# 2 * 2 = (2 * 1) + 2
# 2 * 3 = (2 * 2) + 2

# "Recursive" way of writing multiplication
def multiply(m,n):
    """
    Multiplies two integers m,n >= 0
    """
    print("I want to multiply", m, "by", n)
    if n == 0:
        return 0
    else:
        result = multiply(m,n - 1) # recursive call to multiply
        print("I multiplied", m, "by", n-1, "and got", result)
        return result + m

# multiply(2,3)
# multiply(2,3) | multiply(2,2)
# multiply(2,3) | multiply(2,2) | multiply(2,1)
# multiply(2,3) | multiply(2,2) | multiply(2,1) | multiply(2,0)
#                                                 returns 0
#                                 result gets assigned 0
#                                 returns 2
#                 result gets assigned 2
#                 returns 4
# result gets assigned 4
# returns 6

# if we want to avoid having all these call stack info pile up:
# "tail recursion" "tail call optimization"

# Example to try on your own: exponentiation
# 2 ** 3 = 2 * 2 * 2

# A smarter way to do recursive multiplication
# 2 * 6 = (2 * 3) + (2 * 3)
# 2 * 8 = (2 * 4) + (2 * 4)

def smarter_multiply(m,n):
    """
    Multiplies two integers m,n >= 0
    """
    print("I want to multiply", m, "by", n)
    if m >= n:
        if n == 0:
            return 0
        elif n % 2 == 0:
            result = smarter_multiply(m, n // 2)
            print("I multiplied", m, "by", n // 2, "and got", result)
            return result + result
        else:
            result = smarter_multiply(m,n - 1) # recursive call to multiply
            print("I multiplied", m, "by", n-1, "and got", result)
            return result + m
    else:
        smarter_multiply(n,m)
        
# Very classic example of a recursive function
# Fibonacci sequence:
# 0  1  2  3  4  5
# 1, 1, 2, 3, 5, 8, ...

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        # two recursive calls
        # repeating a lot of work!
        return fib(n-2) + fib(n-1)

# fib(4) --> fib(3) + fib(2)
# fib(3) --> fib(2) + fib(1)
# fib(2) --> fib(0) + fib(1)

# Suggestions for thinking about recursion:
# some sorting algorithms, like quicksort or mergesort
# "Divide and conquer"

# HIGHER-ORDER FUNCTIONS

def times_two(n):
    return n * 2

def print_hello():
    print("hello!")
    
# higher order function
def call_twice0(f):
    f()
    f()

def call_twice1(f,x):
    f(x)
    f(x)
    
def call_repeatedly(f,n):
    for i in range(n):
        f(i)
        

# iterate(f, 0, 5) = f(f(f(f(f(0)))))
def iterate(f,initial,number_of_times):
    result = initial
    for _ in range(number_of_times):
        result = f(result)
    return result

# def add_one(x):
#     return x + 1

def add_three(x):
    return x + 3

# ANONYMOUS FUNCTIONS
# Write a function definition as an expression or inside an
# expression
# Uses "lambda-notation"

add_one = lambda x: x + 1

def multiply_with_lambda(m,n):
    return iterate((lambda x: x + m), 0, n)

def exponential_with_lambda(m,n):
    return iterate((lambda x: x * m), 1, n)

# lambda is named after the lambda-calculus
# very simple "programming language" invented by Alonzo Church
# in the 1930s

print(list(map(lambda x: x + x,[4,5,6,7])))
print([x + x for x in [4,5,6,7]])

# Example to try: sorting function that takes a comparison function

# Python's built-in sorted takes a key argument

def first(p):
    return p[1]

print(sorted([(1,2),(5,3),(9,1),(7,4)],key=first))

# look further: functools library
import functools
