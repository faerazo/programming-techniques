#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# snake

import pygame
import time
import random

black = pygame.Color(0,0,0)
green = pygame.Color(0,255,0)
gray = pygame.Color(200,200,200)

class Snake:
    def __init__(self,pos):
        self.pos = pos
        self.dir = (1,0)
    
    def move(self, diff_x, diff_y):
        x, y = self.pos[-1]
        self.pos = self.pos[1:]
        self.pos.append((x + diff_x, y + diff_y))
        
    def move_in_current_direction(self):
        self.move(self.dir[0], self.dir[1])
        
    def set_direction(self, direction):
        self.dir = direction
    
class Game:
    def __init__(self,height, width):
        self.height = height
        self.width = width 
        self.set_mouse()
        
    def set_mouse(self):
        self.mouse = (random.randrange(0, self.height), random.randrange(0, self.width))

def main():
    game = Game(20, 20)
    snake = Snake([(x,10) for x in range(5,10)])
    unit = 10
    
    pygame.init() # initialize pygame
    pygame.display.set_caption("snake") # setting up window
    win = pygame.display.set_mode((game.height * unit, game.width * unit)) # setting up window
    
    t = 0
    while t < 50:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.set_direction((1,0))
                elif event.key == pygame.K_LEFT:
                    snake.set_direction((-1,0))
                elif event.key == pygame.K_UP:
                    snake.set_direction((0,-1))
                elif event.key == pygame.K_DOWN:
                    snake.set_direction((0,1))
        
        snake.move_in_current_direction()
        
        
        # doing something on a screen we're getting ready to show
        win.fill(black)
        
        for x, y in snake.pos:
            pygame.draw.rect(win, green, pygame.Rect(x * unit, y * unit, unit, unit))
            
        mouse_x, mouse_y = game.mouse
        pygame.draw.rect(win, gray, pygame.Rect(mouse_x * unit, mouse_y * unit, unit, unit))
        
        # show the screen
        pygame.display.update()
        time.sleep(0.3)
        
        t += 1
        
    pygame.quit()
    
main()
