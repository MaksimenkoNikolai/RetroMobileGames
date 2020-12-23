import pygame
import random

from settings import *
from img.images import *
from sound.sounds import *

class Monster(pygame.sprite.Sprite):
  def __init__(self, x, y, player):
    pygame.sprite.Sprite.__init__(self)
    