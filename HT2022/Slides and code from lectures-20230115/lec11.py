#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# LECTURE 11

# OO III: Using classes and inheritance for recursive data structures

class Character: # superclass
    # general functionality
    pass

class Human:
    pass

class Wizard(Character): # subclass
    # modify the generic Character functionality,
    # and add more methods/attributes/we that are wizard-specific
    pass

class Hero(Character,Human):
    pass

class Necromancer(Wizard,Hero): #dangerous!
    pass

# Hierarchical inheritance:
# one superclass has multiple subclasses
# Character -> Wizard, Hero

# Multilevel inheritance:
# a superclass has a subclass that has another subclass

# Multiple inheritance:
# a single class inherits from multiple superclasses
# this is a little dangerous if those superclasses have overlapping behavior

# Going back to RECURSION

# n! == n * ... * 1
# 0! == 1
# 2! == 2 * 1 = 2
# 3! == 3 * 2 * 1 = 6

# 1! == 1 * 0!
# 4! == 4 * 3!
# (n+1)! == (n + 1) * n!

def factorial(n):
    """
        Takes a non-negative integer n, returns its factorial.
    """
    if n == 0: # base case
        return 1
    else: # recursive case
        return n * factorial(n-1)

# [1,3,4]
# is built up by putting 1 in front of [3,4]
# which is built up by putting 3 in front of [4]
# which is built up by putting 4 in front of []

def total(lst):
    """
        Returns the sum of all integers in a list of integers
    """
    if lst == []:
        return 0
    else:
        return lst[0] + total(lst[1:])
              # 4 + total([3,2,1])
              # 4 + 3 + total([2,1])
              # 4 + 3 + 2 + total([1])
              # 4 + 3 + 2 + 1 + total([])
              # 4 + 3 + 2 + 1 + 0
              
def is_in(lst,x):
    """
        Tests if x occurs in the list lst
    """
    if lst == []:
        return False
    else:
        return lst[0] == x or is_in(lst[1:],x)
        
# Implementing lists as a recursive data structure using classes
# This is going to be more like "linked lists" than Python's
# way of storing lists in memory (arrays)

class List:
    def __init__(self):
        raise ValueError("List should be Empty or Cons")
    
    def not_in(self,x):
        return not self.is_in(x)
    
    def __str__(self):
        return "[" + self.to_string() + "]"

class Empty(List):
    def __init__(self):
        pass
    
    def total(self):
        return 0 # base case
    
    def is_in(self, x):
        return False # base case
    
    def to_string(self):
        return ""
    
    def __len__(self):
        return 0
    
    def __getitem__(self, i):
        raise IndexError("Index out of bounds")
    
class Cons(List):
    def __init__(self, head, tail):
        self._head = head
        self._tail = tail
        
    def total(self):
        return self._head + self._tail.total() # recursive case
    
    def is_in(self,x):
        return x == self._head or self._tail.is_in(x) # recursive case
    
    def to_string(self):
        # exercise: get rid of annoying comma at the end
        return str(self._head) + ", " + self._tail.to_string()
    
    def __len__(self):
        return 1 + len(self._tail)

    def __getitem__(self, i):
        if i == 0:
            return self._head
        else:
            return self._tail.__getitem__(i - 1)

# exercise: write an in-place map for lists

# get element at index 1 in [3,4,2]
# == get element at index 0 [4,2]

# [3,4,2]
lst1 = Empty()
lst2 = Cons(3, Cons(4, Cons(2, Empty())))

# teaser: representing algebraic expressions using classes
#
# ((4 + x) * 3) + x

# =======================================
