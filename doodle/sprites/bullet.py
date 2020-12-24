import pygame

from doodle.settings import *
from doodle.img.images import *
from doodle.sound.sounds import *

class Bullet(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = bullet_img
    self.rect = self.image.get_rect()
    self.rect.bottom = y
    self.rect.centerx = x
    
  def update(self):
    self.rect.bottom -= 15
  
  def draw(self, screen):
    screen.blit(self.image, self.rect)