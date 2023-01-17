#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# DA2005 HT22 Lecture 4

# TODAY: Dictionaries and file handling

# FOLLOW UP ON LISTS: slice notation

animals = ["dog","cat","horse","magpie"]

# index from the beginning of the list
animals[1]

# index from the end of the list using a negative index
animals[-1]
animals[-2]

# access a "slice" of a list, which is some segment, or chunk
# starting at one index and ending at another
animals[1:3]
animals[-3:-1]
animals[0:4:2]

animals[::2]
animals[1:]

# INTERLUDE: the lab

# from the chat:
# please address elementwise addition with different size lists

#0 1 2 3 
[1,2,3,4]
[3,7,8]
# --------
[4,9,11,4]

# build up the "sum" list by iterating over indices
# start from index 0, and we end at the length of the longer list

# if i < len(list1) or i < len(list2):
    
# x⁴ = 0x⁰ + 0x¹ + 0x² + 0x³ + 1x⁴
# [0,0,0,0,1]
# [0,0,0,0,1,0]
# [0,0,0,0,1,0,0]

# 1x⁰
# [1]

# 3 + 4x + 2x⁵
# 3x⁰ + 4x¹ + 0x² + 0x³ + 0x⁴ + 2x⁵
# [3,4,0,0,0,2]
# [3,4,0,0,0,2,0,0,0,0]

p = [3,4,0,0,0,2]

def poly_to_string(p_list):
    '''
    Return a string with a nice readable version of the polynomial given in p_list.
    '''
    terms = []
    degree = 0

    # Collect a list of terms
    for coeff in p_list:
        if p_list[degree] == coeff:
            print("things are as they should be",degree,coeff)
        if degree == 0:
            terms.append(str(coeff))
        elif degree == 1:
            terms.append(str(coeff) + 'x')
        else:
            term = str(coeff) + 'x^' + str(degree)
            terms.append(term)
        degree += 1

    final_string = ' + '.join(terms) # The string ' + ' is used as "glue" between the elements in the string
    return final_string

# DICTIONARIES

# Another way of organizing some arbitrary amount of data
# Similar to lists

# Shaped like a real-life dictionary
# In a real-life dictionary we have WORDS,
# and we can look up a word to see its DEFINITION
# In a Python dictionary, we have KEYS,
# and you can look up a key to see its VALUE

translations = {
    "dog" : "hund",
    "cat" : "katt",
    "horse" : "häst",
    "magpie" : "skata"
    }

translations["horse"]
translations["dog"]
# translations["hund"]

translations.get("horse","not found")
translations.get("hund","not found")

important_events = {
    1443 : "King Sejong invents the Korean alphabet",
    1935 : "Birth of Elvis Presley",
    2022 : "We all learned about dictionaries"
    }

one_weird_dict = {
    "cat" : True,
    "dog" : True,
    34.2 : [None,5]
    }

# Python also has "sets", which are like dictionaries
# but only have keys, no values

# Can't have mutable keys
# Dictionaries are mutable

important_events[1523] = "Gustav Vasa becomes King of Sweden"
del important_events[1443]

# could use "association list", but inconvenient and inefficient
important_events_list = [
    [1443, "King Sejong invents the Korean alphabet"],
    [1935, "Birth of Elvis Presley"],
    [2022, "We all learned about dictionaries"]
    ]

# Some other dictionary operations

def function0():
    for k in important_events: # keys by default
        print(k, important_events[k])
        
    for v in important_events.values():
        print(v)
        
    for k, v in important_events.items():
        print(k,v)
  
def function1():
    for k in important_events:
        if k % 2 == 0:
            print(k,important_events[k])
        else:
            print("Something happened in a boring year")
            
# EXAMPLE: "sparse" polynomials

# x⁶⁷⁹
# [0,0,0,0,...,0,1]

# Representing polynomials as a dictionary from degrees to non-zero
# coefficents

# 5x² + 3x⁵ + 2x⁶⁷⁹
p = {2: 5, 679: 2, 5 : 3}

# 10x² + 3x⁸
q = {2: 10, 8: 3}

# p + q == 15x² + 3x⁵ + 3x⁸ + 2x⁶⁷⁹
# start with zero
# go through p, and add each piece of p into this
# go through q, and add each piece of q into this

def poly_to_string(p):
    terms = []
    for coeff, degree in p.items():
        terms.append(str(coeff) + "x^" + str(degree))
    return " + ".join(terms)

def eval_poly(p,x):
    result = 0
    # go through each term and evaluate at x
    for degree, coeff in p.items():
        result += coeff * x ** degree
    return result

def add_poly(p,q):
    result = {}
    for degree, coeff in p.items():
        result[degree] = coeff
    for degree, coeff in q.items():
        current = result.get(degree,0)
        result[degree] = current + coeff
    return result

# alternative definition
def add_poly_2(p,q):
    result = p.copy() # make a copy so we don't change p
    for degree, coeff in q.items():
        current = result.get(degree,0)
        result[degree] = current + coeff
    return result

# FILE HANDLING
# Reading and writing from and to text files

# In order to interact with the file system,
# Python has to ask it for a HANDLE
# A HANDLE is permission to do something with a file,
# such as read from it or write to it, and some information
# about where Python is looking in the file

# there are different modes
# "r" - read
# "w" - write
# "a"- append

# reading from a file
def function2():
    input_handle = open("moby-dick.txt","r")
    
    # read() gives me all the contents of the file
    # file_contents = input_handle.read()
    
    # read one line at a time
    line1 = input_handle.readline()
    line2 = input_handle.readline()
    
    rest = input_handle.readlines()
    
    # when I'm finished with a handle, I should close it
    input_handle.close()
    
# writing to a file
def function3():
    output_handle = open("info.txt","w")
    
    output_handle.write("hello there\n")
    output_handle.write("it's me")
    
    output_handle.close()
    
# more "idiomatic" way of opening a file, the with block
def function4():
    with open("moby-dick.txt","r") as input_handle:  
        # read() gives me all the contents of the file
        # file_contents = input_handle.read()
        
        # read one line at a time
        line1 = input_handle.readline()
        line2 = input_handle.readline()
        
        rest = input_handle.readlines()
        # at the end of the block, the handle is automatically closed
    return rest

def get_word_list(filename):
    with open(filename,"r") as handle:
        words = []
        for word in handle:
            words.append(word[:-1])
    return words

def spell_check(words_file,text_file):
    words = get_word_list(words_file)
    with open(text_file,"r") as handle:
        for line in handle:
            for word in line.split():
                if word not in words:
                    print("Spelling error!", word, "is not a word!")

