# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:51:15 2020

@author: MAhdi
"""


import pygame 
from pygame.sprite import Sprite
class Ship(Sprite) :
    
    
    def __init__(self , ai_game) :
        
        super().__init__()
        
        
        self.game_screen = ai_game.screen
        self.game_screen_rect= ai_game.screen.get_rect()
        
        self.settings = ai_game.set
        
        self.image = pygame.image.load(self.settings.ship_image)
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.game_screen_rect.midbottom
        
        
        self.moving_right = False
        self.moving_left = False
    
    def update(self) :
        if self.moving_right and self.rect.right < self.game_screen_rect.right  :
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0 :
            self.rect.x -= self.settings.ship_speed
        
    def blitme(self) :
        
        self.game_screen.blit(self.image , self.rect)
        
        
        
    def reset_ship(self) :
        self.rect.midbottom = self.game_screen_rect.midbottom