#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# DA2005 HT22 Lecture 2

# Lab 1 is due on Monday @ 20:00
# Lab 2 is also up on the site, due the following Monday @ 20:00

# Grade 3 labs from the other students
# We give you a simple questionnaire
# Questions like: does the solution to Task 2 correctly solve it

# ==============================

# Code written in the Python language

def function0():
    print("hi there")

# Type "expressions" and Python will "evaluate" them

# print((4 + 5) ** 2)

def function1():
    x = (4 + 5) ** 2
    # 4 + 5 = 9
    # 9 ** 2 = 81
    print(x + x)
    
    my_word = input("Give me your name: ")
    print("Hi,",my_word + "!")

# =================================
# PYTHON's TYPE SYSTEM

# types of things:
    # - strings like "hello" (str)
    # - integers like 4, 5 (int)
    # - floating-point numbers like 5.6 3.0 (float)
    # - complex numbers 1+2j (complex)
    # - boolean True, False (bool)
    # - NoneType None

def function2():
    your_age = input("Give me your age: ")
    print("Here's your age in dog years:", int(your_age) * 7)

# conversion functions to change between types

def function3():
    x = int("17")
    y = float("16.5")
    print(x + y)

# SYNTAX: the "grammer" of code, gets checked first

def function4():
    print('hi')
    # f dosi d

# SEMANTICS: with "meaning" of code

def function5():
    # a semantic error
    print("hi")
    4 + "hi"
    print("dog")
    
# =======================================
# FUNCTIONS

# functions: operations that we can do to things
def function6():
    print("hi") # print is the function, "hi" is the argument
    int("7") # int is the function, "7" is the argument
    5 + 3 # + is the function, 5 and 3 are arguments

y = 6

# A function is declared using the "def" keyword
# HEAD(ER): name of the function (the parameters / arguments 
# that it takes)
def square(x):
    # the BODY of the function is just some code,
    # indented to show it's inside
    print("hi")
    # a new y for the inside of this function
    # y is in scope only below here inside the function
    y = x ** 2
    # we can RETURN a result of a function
    # using the return keyword
    return y

# VARIABLE SCOPE

def outer_function():
    def inner_function():
        z = 5
    return z

# Let's write some useful functions

def from_centimeters(x):
    return x / 100

def area(length, width):
    """
        Computes the area of a rectangle from its length
        and width.
        Parameters: length and width
        Returns: the area
    """
    return length * width

def volume(length, width, height):
    """
        Computes the area of a rectangular solid
        length, width and height
        Parameters: length, width, and height
    """
    return length * width * height

def surface_area(length, width, height):
    """
        Computes the surface area of a rectangular solid
        Parameters: length, width, and height
    """
    # return 2 * (length * width) + 2 * (width * height) + 2 * (length * height) 
    top = area(length,width)
    front = area(width,height)
    left = area(length,height)
    return 2 * top + 2 * front + 2 * left

def surface_to_volume(length,width,height):
    """
        Computes the ratio of surface area to volume
        of a rectangular solid
    """
    return surface_area(length,width,height) / volume(length,width,height)

# 15 MINUTE BREAK
# return 14:20

def happy_birthday(name):
    return "Happy birthday, "  + name + '!'

def print_happy_birthday(name):
    print("Happy birthday, "  + name + '!')

# happy_birthday("Horse")
# print_happy_birthday("Horse")
# happy_birthday(happy_birthday("Horse"))
# print_happy_birthday(print_happy_birthday("Horse"))

# ===========================
# CONDITIONALS or IF-STATEMENTS

def happy_birthday(name,age):
    if 0 <= age and age <= 30:
        age_string = str(age)
        return "Happy birthday, "  + name + \
               '! You are ' + age_string + ' years old!'
    else:
        return "No you aren't!"

# COMPARISON OPERATORS
# LESS THAN <
# GREATER THAN >
# LESS THAN OR EQUAL <=
# GREATER THAN OR EQUAL >=
# EQUAL ==

# BOOLEAN OPERATORS
# and
# or
# not

# example with while True and break
def function40():
    x = 0
    while True:
        x = x + 1
        print(x)
        if x >= 20:
            break

# ====================================

def bank():
    account = 0
    while True:
        my_input = input("What do you want to do? ")
        if my_input == "deposit":
            amount = int(input("How much to deposit? "))
            account += amount
        elif my_input == "withdraw":
            amount = int(input("How much to withdraw? "))
            account -= amount
        elif my_input == "i'm leaving":
            break
        else:
            print("I don't understand")
        print("Your account has", account, "money")
    print("goodbye!")