# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 00:38:16 2020

@author: MAhdi
"""


class GameStats :
    
    def __init__ (self , ai_game) :
        
        self.settings = ai_game.set
        self.game_active = False
        self.reset_stats()
        self.high_score = 0
       
    def reset_stats(self):
        self.ship_left = self.settings.ship_allowed
        self.game_score = 0
        self.game_level = 1