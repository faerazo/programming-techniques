#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# DA2005 HT22 Lecture 5

# TODAY:
# ERROR HANDLING
# LIST COMPREHENSIONS

# - lab 3 is out
# - peer-grading due tomorrow!
# - some feedback from the labs is on peergrade

# ERROR HANDLING
# EXCEPTIONS
# try-except blocks
# raise statements

def function1():
    # IndexError
    my_list = [1,2,3]
    x = my_list[5]
    print("My favorite number is", x)

# NameError
# print(y)

# ZeroDivisionError
# 5 / 0

# ValueError
# int("str")

# SyntaxError
# fios doif jaio

# These are called EXCEPTIONS

def ask_for_birth_year():
    year = int(input("What year were you born?"))
    print("You are probably", 2023-year, "years old")
    

def ask_for_birth_year2():
    try:
        year = int(input("What year were you born?"))
        print("You are probably", 2023-year, "years old")
    except ValueError:
        print("You did not enter a number")
    except EOFError:
        print("You did something weird")
    print("Goodbye")

# One exception:
#   try:
#       dfiso dfjioj
#   except SyntaxError:
#       print("hi")

def ask_for_file():
    filename = input("Please enter a filename: ")
    try:
        with open(filename, "r") as handle:
            lst = handle.readlines()
            print(lst[0])
    except FileNotFoundError:
        print("that file does not exist")

# Raising our own exceptions

def perfect_sqrt(x):
    """
    Take an integer x as a parameter.
    If x is a perfect square, return its square root.
    Otherwise, raise a ValueError.
    """
    y = 0
    while y * y <= x:
        if y * y == x:
            return y
        y += 1
    raise ValueError(str(x) + " is not a perfect square")

def ask_for_perfect_square():
    while True:
        try:
            square = int(input("Give me a perfect square:"))
        except ValueError:
            print("That's not an integer!")
            continue
        try:
            sqrt = perfect_sqrt(square)
            print("The square root is", sqrt)
            break
        except ValueError:
            print(square, "is not a perfect square")
            continue

# LIST COMPREHENSIONS
# Syntactic sugar: some easier way of writing some common
# kind of code which is shorter and easier to read

def list_of_squares(lst:
    """
    Takes in a lst of numbers and returns a new list
    with the square of each number in the original list.
    """
    result = []
    for i in lst: # [5,4,3]
        result.append(i ** 2)
    return result

def list_of_squares2(lst):
    # using list comprehension
    return [i ** 2 for i in lst]

def function40():
    numbers = [2,5,6]
    strings = ["a","b","c"]
    
    [str(n) + s for n in numbers for s in strings if n > 4]
    # vs
    l = []
    for n in numbers:
        for s in strings:
            if n > 4:
                l.append(str(n) + s)
    return l

l = [2,3,4,5]
d = {i : i*200 for i in l}
l2 = [j - 1 for j in d.values()]
l3 = ["a" + s for s in "hello there"]



