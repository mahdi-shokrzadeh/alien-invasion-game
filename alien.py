# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 21:47:49 2020

@author: MAhdi
"""


import pygame
from pygame.sprite import Sprite


class Alien(Sprite) :
    
    def __init__(self , ai_game) :
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.set
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 
        self.x = float(self.rect.x)
        
        
    def update(self) :
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
        