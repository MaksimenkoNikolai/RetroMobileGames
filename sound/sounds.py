import pygame
import os

from settings import *

pygame.mixer.init()

if pygame.mixer.get_init():
  jump_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'jump.wav'))
  loose_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'loose.wav'))
  break_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'break.wav'))
  shoot_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'shoot.wav'))