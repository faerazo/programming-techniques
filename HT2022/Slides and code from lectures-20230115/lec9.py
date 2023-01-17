#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# LECTURE 9

lines = [
        "Here's a line",
        "here's another line",
        "here's the last line"
        ]

def function0():
    
    i = 0
    while i < len(lines):
        print(i, lines[i])
        i += 1
          
    for i, line in enumerate(lines):
        print(i, line)
        
    def my_enumerate(lst):
        i = 0
        while i < len(lst):
            yield (i, lst[i])
            i += 1
            
    for i, line in my_enumerate(lines):
        print(i, line)
        
# lab 5

# AAACCC has an overlap of length 3 with CCCCGATT
# CCCCGATT has an overlap of length 0 with AAACCC
  
# overlaps(seq1, seq2) != overlaps(seq2, seq1)

def print_lines_with_numbers(lines):
    if type(lines) == []:
        raise ValueError
    else:
        for i, line in enumerate(lines):
            print(i, line)

try:
    print_lines_with_numbers([])
except ValueError:
    print("there was a problem")
    
# TTAAACCC
#      CCCCGATT
# overlap 3

# CCCAAT
#       CCTTAC
# overlap 0

# CCTTAC
#      CCCAAT
# overlap 1

# OBJECT-ORIENTED PROGRAMMING

# Another "programming paradigm",
# another way to organize your code

# OO: organized around classes, objects, attributes, and methods

l = [1,2,3]
l.append(5)

# l is an object of the class list
# append is a method of the class list

class EmailAccount:
    """
        Stores a username and a domain
        eg "evan.cavallo" and "math.su.se"
    """

    def __init__(self, username, domain):
        """
           Creates an email account for username@domain
           with an empty inbox and outbox
        """
        # constructor (or initializer) for this class
        # takes any arguments we want it to 
        # + a first "self" argument that refers to the object we're
        #   constructing
        if type(username) != str or type(domain) != str:
            raise TypeError
        self.username = username
        self.domain = domain
        self.inbox = [] # list of (sender, text) tuples
        self.outbox = [] # list of (destination, text) tuples
        
    def address(self):
        """
            Return the account's email address as a string
        """
        return self.username + "@" + self.domain
    
    def add_to_inbox(self, sender, text):
        """
            Adds an email from sender containing text
            to the account's inbox
        """
        self.inbox.append((sender, text))
        
    def add_to_outbox(self, destination, text):
        """
            Adds an email to destination containing text
            to the account's outbox
        """
        self.outbox.append((destination, text))
        
    def send(self):
        """
            Sends all email in the account's outbox
        """
        for destination, text in self.outbox:
            destination.add_to_inbox(self, text)
        self.outbox = []
        
    def __str__(self):
        """
            Convert an email account to a human-readable string
        """
        return self.address()
    
    def __repr__(self):
        return str(self) + str(self.inbox) + str(self.outbox)
    
    def __len__(self):
        return len(self.inbox) + len(self.outbox)

# Write the class name with arguments to construct an object
# of the classs
# The arguments get passed to the __init__ definition in the class
evan = EmailAccount("evan.cavallo", "math.su.se")
anders = EmailAccount("anders.mortberg","math.su.se")
dog = EmailAccount("dog","doghouse.com")

evan.username # an object can have attributes

evan.address()

evan.add_to_outbox(anders, "what are we doing for the projects?")
evan.add_to_outbox(dog, "Woof!")

evan.send()


class EmailAccount2:
    def __init__(self, username, domain):
        """
           Creates an email account for username@domain
           with an empty inbox and outbox
        """
        # constructor (or initializer) for this class
        # takes any arguments we want it to 
        # + a first "self" argument that refers to the object we're
        #   constructing
        self._username = username
        self._domain = domain
        self._inbox = [] # list of (sender, text) tuples
        self._outbox = [] # list of (destination, text) tuples
        
    def get_address(self):
        return self._username + "@" + self._domain

    def set_address(self, address):
        parts = address.split("@")
        if len(parts) == 2:
            self._username = parts[0]
            self._domain = parts[1]
        else:
            raise ValueError("Bad email address")

    def add_to_inbox(self, sender, text):
        """
            Adds an email from sender containing text
            to the account's inbox
        """
        self._inbox.append((sender, text))
        
    def add_to_outbox(self, destination, text):
        """
            Adds an email to destination containing text
            to the account's outbox
        """
        self._outbox.append((destination, text))
        
    def _clear_outbox(self):
        self._outbox = []
        
    def send(self):
        """
            Sends all email in the account's outbox
        """
        for destination, text in self._outbox:
            destination.add_to_inbox(self, text)
        self._clear_outbox()
        
    def __str__(self):
        """
            Convert an email account to a human-readable string
        """
        return self.get_address()
    
    def __repr__(self):
        return str(self) + str(self._inbox) + str(self._outbox)
    
    def __len__(self):
        return len(self.inbox) + len(self.outbox)
    
evan2 = EmailAccount2("evan.cavallo","math.su.se")
evan2.get_address()
evan2.set_address("evancavallo@gmail.com")

# exercise: replace the tuple representation of emails
# with objects from an email class

class Horse:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed # store speed in the object
        
    def __str__(self):
        return self.name
        
    def race(self, other_horse):
        if self.speed > other_horse.speed:
            return str(self) + " wins!"
        else:
            return str(other_horse) + " wins!"
        
    # exercise, write special method __lt__
    # which determines what < does on horses
        
shadowfax = Horse("Shadowfax", 300)
rocinante = Horse("Rocinante", 50)
evan = Horse("Evan", 100)

def race(horse1,horse2):
    if horse1.speed > horse2.speed:
        return "First horse wins!"
    else:
        return "Second horse wins!"
    
# exercise: give horses an energy stat
# and a "eat" method so that a horse will consume
# energy by racing and will lose if they run out

def hello():
    t = 5
    pass
    return t

hello()

