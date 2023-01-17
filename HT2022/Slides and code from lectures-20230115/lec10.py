#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# LECTURE 10

# OO PART II: INHERITANCE

# Lab 5 due on TUESDAY 20:00
# peer-grading due on THURSDAY 20:00

# Project info should be out later today
# Due dates:
    # TUESDAY DEC 20
    # Peer-grading: THURSDAY DEC 22
    
# Review of tuesday: classes, methods, attributes, etc

# Example: heroes and fighting
# Objects that represent heroes, which carry around information
# such as HP, level, shield ability, experience. (in attributes)
# and a function for having heroes fight each other

class Character:
    # class attribute
    starting_experience = 0
    
    def __init__(self, name, hit_points, level):
        # setting instance attributes
        self.name = name
        self.hp = hit_points
        self.level = level
        self.exp = self.starting_experience
             
    def inc_hp(self, amt):
        self.hp += amt   

    def inc_lvl(self):
        self.level += 1
        
    def take_damage(self,amt):
        self.inc_hp(-amt)

class Hero(Character):
    starting_experience = 10
    
    def __init__(self, name, hit_points, shield, level):
        # Apply the superclass's constructor with these arguments
        super().__init__(name + " the Great", hit_points, level)
        self.shield = shield

    def take_damage(self, amt):
        damage = amt - self.shield
        if damage >= 0:
            self.inc_hp(-damage)
            
    def shout(self):
        print("I am ", self.name, "!!!!!")

class Wizard(Character):
    starting_experience = 15
    # Every method from the Character class is automatically
    # carried over to the Wizard class;
    # we can also _redefine_ methods by giving them a new definition
    # in Wizard,
    # and can add new methods
    
    def __init__(self, name, hit_points, forcefield, level):
        super().__init__(name + " the Wizard", hit_points, level)
        self.forcefield = forcefield
        
    def take_damage(self, amt):
        # Wizards take all the damage if we break through their
        # forcefield
        if amt > self.forcefield:
            self.inc_hp(-amt)
            
    def heal(self, hero):
        hero.inc_hp(10)    

def fight(hero1, hero2):
    """
    Takes two instances the class Character and has them
    fight each other.
    - Whichever hero has the highest level wins.
    - The winner levels up.
    - The loser takes 20 damage.
    If the heroes have the same level, nothing happens.
    """
    if hero1.level > hero2.level:
        hero1.inc_lvl()
        hero2.take_damage(20)
        print(hero1.name, "wins!")
        return hero1
    elif hero1.level < hero2.level:
        hero2.inc_lvl()
        hero1.take_damage(20)
        print(hero2.name, "wins!")
        return hero2
    else:
        print("No one wins!")
        return None

super_mario = Hero("Mario", 100, 5, 2)
rudolf = Hero("Hulk Rudolf the Reindeer", 300, 1, 0)

blue_wizard = Wizard("Blue Wizard", 50, 15, 10)
red_wizard = Wizard("Red Wizard", 30, 13, 20)

random_peasant = Character("George", 10, 0)

# multiple inheritance
# diamond problem: avoid!

class A:
    def a(self):
        print("hi")
        
class B(A):
    def b(self):
        print("it's b!")
        
    def cool(self):
        print("wow!")
        
class C(A):
    def c(self):
        print("it's c!")
        
    def cool(self):
        print("Neat!")
        
class D(C,B):
    def d(self):
        print("it's d!")

#     A
#    / \
#   B   C
#    \ /
#     D

my_b = B()
my_c = C()
my_d = D()
