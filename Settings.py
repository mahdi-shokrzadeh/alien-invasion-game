# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:25:32 2020

@author: MAhdi
"""



class Settings :
    
    def __init__(self) :
        
        self.width = 800
        self.height = 600
        self.bg_color = (255 , 255 , 255)
        
        
        
        
        #Image URLs
        self.ship_image = 'image/ship.bmp'
        self.alien_image = 'image/alien.bmp'
        
        
        
        #Bullet
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (50 , 50 , 50)
        self.bullet_allowed = 30
        
        
        
        #Alien settings 
        self.fleet_drop_speed = 10
           
        
        #speed level
        self.game_speed_scale = 1.1
        self.score_scale = 1.5
        
        #ship settings 
        self.ship_allowed = 3
        self.initialize_dynamic_settings()
        
        
    def initialize_dynamic_settings(self) :
        
        self.alien_speed = 1.5
        self.bullet_speed = 1
        self.ship_speed = 2
        self.alien_points = 20
        
        # 1 is right ; -1 is left
        self.fleet_direction = 1
    
    def speed_up(self) :
        
        self.alien_points = int(self.alien_points * self.score_scale)
        self.alien_speed *= self.game_speed_scale
        self.bullet_speed *= self.game_speed_scale
        self.ship_speed *= self.game_speed_scale
        