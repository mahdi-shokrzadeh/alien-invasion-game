# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 19:24:33 2020

@author: MAhdi
"""


import pygame.font
from pygame.sprite import Group
from ship import Ship
class Scoreboard :
    
    def __init__(self , ai_game) :
        
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = ai_game.stats
        self.settings = ai_game.set
        self.text_color = (0 , 0 , 255)
        self.font = pygame.font.SysFont(None , 45)
        self.render_score()
        self.render_high_score()
        self.render_level()
        self.render_ship()
    def render_score(self):
        
        #score_str = str(self.stats.game_score)
        rounded_score = round(self.stats.game_score , -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str , True , self.text_color , self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10
        self.render_ship()
        
   
    def render_ship(self):
        
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + (ship_number * ship.rect.width)
            ship.rect.y = 10 
            self.ships.add(ship)
            
            
    def render_high_score(self):
        
        #score_str = str(self.stats.game_score)
        rounded_score = round(self.stats.high_score , -1)
        score_str = "{:,}".format(rounded_score)
        self.high_score_image = self.font.render(score_str , True , self.text_color , self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 10
        
        
    
    def render_level(self):
        
        level_str =str(self.stats.game_level)
        #str(self.stats.game_level)
        self.level_image = self.font.render(level_str , True , self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right 
        self.level_rect.top = self.score_rect.bottom - 5 


    
    def draw_score (self) :
        self.screen.blit(self.score_image , self.score_rect )
        self.screen.blit(self.high_score_image , self.high_score_rect)
        self.screen.blit(self.level_image , self.level_rect)
        self.ships.draw(self.screen)
    
    
    def check_high_score(self) :
        if self.stats.game_score > self.stats.high_score :
            self.stats.high_score = self.stats.game_score
            self.render_high_score()