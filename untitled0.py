#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 23:43:40 2020

@author: kasutav
"""
import pygame, sys
from pygame.locals import *
#noinspection PyUnresolvedReference

catx=10
caty=10
screen=0

def myquit():
    pygame.quit()
    sys.exit()
    


red=[255,0,0]

pygame.init()
display_surf=pygame.display.set_mode((400,300))

pygame.display.set_caption('The Snake')

screen=pygame.display.get_surface()
screen.fill(red)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    