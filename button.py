# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 17:14:56 2020

@author: MAhdi
"""

import pygame.font

class Button :
    
    def __init__(self , ai_game , msg) :
        
        self.screen = ai_game.screen 
        self.screen_rect = self.screen.get_rect() 
        
        self.width , self.height = 300 , 80
        self.button_color = (0 , 240 , 0)
        self.text_color = (0 , 0 , 0)
        self.font = pygame.font.SysFont(None , 50)
        
        self.rect = pygame.Rect(0 , 0 , self.width , self.height)
        self.rect.center = self.screen_rect.center
        self.bg_color = (150, 150 , 150 ,20)
        
        self._set_msg(msg) 
        
            
            
    def _set_msg(self , msg) :
        
        self.image_msg = self.font.render(msg , True , self.text_color , self.button_color)
        self.image_msg_rect = self.image_msg.get_rect()
        self.image_msg_rect.center = self.rect.center
        
        
    def draw_button(self):
        self.screen.fill(self.bg_color)
        self.screen.fill(self.button_color , self.rect)
        self.screen.blit(self.image_msg , self.image_msg_rect)