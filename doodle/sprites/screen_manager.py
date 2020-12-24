import pygame

from doodle.settings import *
from doodle.img.images import *
from doodle.sound.sounds import *

class ScreenManager(pygame.sprite.Sprite):
  def __init__(self, platforms, player, score, loose_screen):
    pygame.sprite.Sprite.__init__(self)
    
    self.is_game_start = False
    
    self.platforms = platforms
    self.player = player
    self.score = score
    self.loose_screen = loose_screen
  
  def start_game(self):
    self.is_game_start = True
    self.platforms.play_again()
    self.player.play_again()
    self.score.play_again()
    self.loose_screen.play_again()
  
  def end_game(self):
    self.is_game_start = False