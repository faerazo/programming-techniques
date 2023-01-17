#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# DA2005 HT22 Lecture 3

# TODAY: Lists and iteration
# Doing things repeatedly, or having a bunch of data together

# Peergrading due Wed @ 20:00
# Lab 2 is out and due Mon @ 20:00

# While loops, then lists, and then for loops

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

# while: we want to do some code over and over
# "while" some condition holds

def function0():
    # never run
    while False:
        print("hello")
    
    # can write more complicated conditions with and or not
    i = 0
    while i < 10 and i * i < 81:
        i += 1
        print(i)
    print('hi')
    
# example: integer division

# 10 // 2
# 10 - 2 = 8   # 1
# 8 - 2 = 6    # 2
# 6 - 2 = 4    # 3
# 4 - 2 = 2    # 4
# 2 - 2 = 0    # 5

def intdiv(a,b):
    """
        Return the integer division of a by b, rounding down
        Parameters: a,b positive integers
        Return an int
    """
    remaining = a # initial conditions
    count = 0
    while remaining >= b:
        remaining -= b
        count += 1
    return count

# example: square root of perfect squares

# 49 is the square of 7 (7 * 7 == 49)
# 7 is the square root of 49

def perfect_sqrt(x):
    """
        Return the square root of x if it is an integer,
        otherwise return None
    """
    # want to find i such that i * i == x
    i = 0
    while i * i <= x:
        if i * i == x:
            return i
        i += 1
    return None # this is not necessary

# say x is 48
# start with i = 0 ---> i ** 2 == 0
#            i = 1 ---> i ** 2 == 1
#  ....
#            i = 7 ---> i ** 2 == 49
# we went too far, there isn't an integer square root

def ask_for_perfect_square():
    while True:
        x = int(input("Give me a perfect square!: "))
        y = perfect_sqrt(x)
        # if y: has similar but not the same behavior (0)
        if y == None:
            print("No! That's not a perfect square")
        else:
            print("Thank you the square root is", y)
            break
        
def function1():
    i = 0
    while i < 3:
        j = 0
        while True:
            print(i,j)
            j += 1
            if j >= 3:
                # break exits from innermost loop
                break
        # something
        i += 1

# ======= LISTS =======

# new type of data

# list literals
l = [1,2,3,4]
favorite_words = ['dog','cat','soup']
favorite_numbers = [5175]
empty = [] # THE EMPTY LIST
stuff_i_found = [35, "wow", 1.5, [1,3], favorite_words]

def function1():
    # list indexing
    
    print(favorite_words[0])
    print(favorite_words[2])
    print(stuff_i_found[4][1])
    
    # modifying lists
    # lists are the first thing we've seen we can modify
    # lists are MUTABLE
    # other things like numbers, strings, booleans are IMMUTABLE
    
    print(favorite_words)
    # this is a METHOD, which is sort of like a function,
    # but I think of it as happening to the thing before the .
    favorite_words.append("dirt") # add at the end
    print(favorite_words)
    favorite_words.insert(2, "carrot") # add anywhere
    print(favorite_words)
    # a special keyword
    del favorite_words[3] # remove anywhere
    print(favorite_words)

# tests / boolean expressions involving lists

if 'dirt' in favorite_words:
    print("I love dirt!")
    
# simple example: list of numbers up to n
def list_up_to(n):
    """
        Takes a positive integer n,
        returns the list of numbers from 1 to n
    """
    result_list = []
    i = 1
    while i <= n:
        result_list.append(i)
        i += 1
    return result_list
 
# simple example: take a list of numbers 
# and double all the numbers in it

def double_list(lst):
    i = 0
    while i < len(lst):
        lst[i] = lst[i] * 2
        i += 1
    return lst

# try calling me with a list or string in a variable
def doubler(x):
    x *= 2
    return x

# lists are mutable, strings are not

# when I call a function:
# immutable things (ints, strs) are passed "by value"
#   n = 5
#   doubler(n) # the doubler function gets 5
# mutable things (lists) are passesd "by reference"
#   l = [1,2,3]
#   doubler(l) # the doubler function gets l / a reference to l

# for LOOPS ==============

# doing something "for" every element in some sequence
# types of sequences: lists, strings, "range"s, others...

def function2():
    l = [1,2,3,4]
    for i in l + favorite_words:
        print(i)
        
    for c in "hello there":
        print(c)
        
    for x in range(5,15):
        print(x)

# rewriting an example we did with while loops
def double_list_for(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] * 2
    return lst

# simple example: taking the product of a list of numbers
# [1,2,3,4] ---> return 1 * 2 * 3 * 4 == 24
def product(lst):
    prod = 1
    for n in lst:
        prod *= n
    return prod

# doesn't work as you might expect
def double_list_for_weird(l):
    for x in l:
        x *= 2
    return l

# x + x^2 + 24x^3
# POLYNOMIAL:
# arithmetic expression in one variable x
# which is a sum of things of the form n * (x ** k)

# n0 + n1 * x + n2 * x^2 + n3 * x^3 + ..... + nk * x^k
# m0 + m1 * x + m2 * x^2 + m3 * x^3 + ..... + mk * x^k
# ====================================================
# (n0 + m0) + (n1 + m1) * x + ....

def f(x):
    return x + x ** 2 + 24 * (x ** 3)

# n0 + n1 * x + n2 * x^2 + n3 * x^3 + ..... + nk * x^k
# represented as
# [n0,n1,n2,n3,...,nk]

# x + x^2 + 24x^3
# represented
# [0,1,1,24]

# 2 + x^4
# [2,0,0,0,1]

# poly_to_string([0,1,1,24])
# returns "0 + 1x + 1x^2 + 24x^3"

# add_poly([1,2],[0,3,4])

# we could also represent things differently
# 2 + x^4
# [[2,0],[1,4]]

# in 24x^3, 24 is the coefficent, 3 is the degree,
# and the whole thing is a term of the polynomial


