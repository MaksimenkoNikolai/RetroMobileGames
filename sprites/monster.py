import pygame
import random

from settings import *
from img.images import *
from sound.sounds import *

class Monster(pygame.sprite.Sprite):
  def __init__(self, x, y, player):
    pygame.sprite.Sprite.__init__(self)
    
    self.image = monster1_img
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.bottom = y
    
    self.player = player
    
    self.speed_y = 0
    self.is_scrolling_down = False
    self.is_scrolling_up = False
  
  def update(self):
    if self.player.rect.top < HEIGHT/2 and not self.is_scrolling_down and not self.player.is_falling:
      self.start_scroll_down()
    
    if self.is_scrolling_down:
      self.scroll_down()
    
    if self.is_scrolling_up:
      self.scroll_up()
  
  def is_collide_with_player(self):
    return len(pygame.sprite.spritecollide(self.player, [self], False)) > 0

  def start_scroll_down(self):
    self.player.is_stop = True
    self.is_scrolling_down = True
    self.speed_y = self.player.speed_y

  def scroll_down(self):
    if self.is_scrolling_down:
      if self.speed_y <= 0:
        self.is_scrolling_down = False
        
        self.player.speed_y = 0
        self.player.is_stop = False
        return
      
      self.rect.bottom += self.speed_y
      self.speed_y = self.speed_y + self.player.gravity
  
  def start_scroll_up(self):
    self.is_scrolling_up = True
    self.speed_y = abs(self.player.speed_y)
  
  def scroll_up(self):
    if self.is_scrolling_up:
      self.rect.bottom -= self.speed_y
      self.speed_y = self.speed_y + abs(self.player.gravity)
  
  def end_game(self):
    self.start_scroll_up()