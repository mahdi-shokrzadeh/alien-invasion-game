# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:25:07 2020

@author: MAhdi
"""


import pygame
import sys
#from tkinter import *
from time import sleep
from Settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlineInvasion():
    
    
    def __init__(self) :
        
        pygame.init()
        self.set = Settings()
        
        self.screen = pygame.display.set_mode((0 , 0) , pygame.FULLSCREEN)
        self.set.width = self.screen.get_rect().width
        self.set.height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.a_ship = Ship(self)
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.bullet_number = 0
        self.btn_play = Button(self , "play")
        
        
    
    def run_game(self):
        
        while True :
         self._check_enents()
         
         if self.stats.game_active :
             self.a_ship.update()
             self.bullets.update()
             self._update_aliens()
             for bullet in self.bullets.copy() :
                 if bullet.rect.bottom < 0 :
                     self.bullets.remove(bullet)
             collisions = pygame.sprite.groupcollide(self.bullets , self.aliens , False , True) 
             
             if collisions :
                 for aliens in collisions.values() :
                     self.stats.game_score += (self.set.alien_points * len(aliens))
                 self.sb.render_score()
                 self.sb.check_high_score()
                 
             if not self.aliens :
                 self.set.speed_up()
                 self._create_fleet()
                 self.bullets.empty()
                 self.bullet_number = 0 
                 self.stats.game_level += 1
                 self.sb.render_level()
             
         self._update_screen()
          
         
            
    def _check_enents(self) :
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                
            elif event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_RIGHT :
                    self.a_ship.moving_right = True
                elif event.key == pygame.K_LEFT :
                    self.a_ship.moving_left = True
                elif event.key == pygame.K_SPACE :
                    self._fire_bullet()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #print(mouse_pos)
                if self.btn_play.rect.collidepoint(mouse_pos) and not self.stats.game_active :
                    
                    self.set.initialize_dynamic_settings()
                    self.stats.game_active = True
                    self.stats.reset_stats()
                    self.sb.render_score()
                    self.sb.render_level()
                    self.sb.render_ship()
                    self.aliens.empty()
                    self.bullets.empty()
                    self.bullet_number = 0
                    self._create_fleet()
                    self.a_ship.reset_ship()
                    pygame.mouse.set_visible(False)
                    
            elif event.type == pygame.KEYUP :
                if event.key == pygame.K_RIGHT :
                    self.a_ship.moving_right = False
                elif event.key == pygame.K_LEFT :
                    self.a_ship.moving_left = False  
                elif event.key == pygame.K_q :
                    #sys.exit()
                    pygame.quit()
                    
    
    
    def _fire_bullet(self) :
        if self.bullet_number < self.set.bullet_allowed :
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.bullet_number +=1 
    
    
    
    def _update_aliens(self) :
        self._check_direction()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.a_ship , self.aliens) :
            #print("ship hits!")
            self._ship_hits()
        self._check_alien_bottom()
        
        
        
    def _ship_hits(self) :
        
        if self.stats.ship_left > 0 :
            self.a_ship.reset_ship()
            self.stats.ship_left -= 1
            self.sb.render_ship()
            self.bullets.empty()
            self.bullet_number = 0
            self.aliens.empty ()
            self._create_fleet()
            sleep(2)
        else :
            
            self.stats.game_active = False
            self.btn_play = Button(self , "play again!")
            pygame.mouse.set_visible(True)
            
        
        
    def _check_alien_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites() :
            if alien.rect.bottom >= screen_rect.bottom :
                self._ship_hits()
                break
        
        
        
    def _check_direction(self) :
        for alien in self.aliens.sprites() :
            if alien.rect.right >= self.screen.get_rect().right or alien.rect.left <= 0 :
                self.set.fleet_direction *= -1
                for alien in self.aliens.sprites() :
                    
                    alien.rect.y += self.set.fleet_drop_speed
                break
    
    
    
    def _create_fleet(self) :
        
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        ship_height = self.a_ship.rect.height
        
        
        available_space_x = self.set.width - (2*alien_width)
        number_alien_x = available_space_x // (2*alien_width)
        
        available_space_y = self.set.height - (2 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)
        
        
        for row_number in range(number_rows) :
            for alien_number in range(number_alien_x) :
                self._create_aliens(alien_number , row_number)
            
    
    
    def _create_aliens(self , alien_number , row_number) :
        
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height 
        alien.x = alien_width + 2 * (alien_width) * (alien_number)
        alien.rect.x = alien.x
        self.aliens.add(alien)
        alien.rect.y = (1 * alien_height) + 2 * alien_height * row_number
        #alien_height
    
    
    def _update_screen(self) :
               
        self.screen.fill(self.set.bg_color)
        self.a_ship.blitme()
        for bullet in self.bullets.sprites() :
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.draw_score()
        if not self.stats.game_active :
            self.btn_play.draw_button()
            
        pygame.display.flip()
            
    
if __name__ == "__main__" :
    ai = AlineInvasion()
    ai.run_game()
          