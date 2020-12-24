import pygame
import os

from doodle.settings import *

pygame.mixer.init()

if pygame.mixer.get_init():
  jump_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'jump.wav'))
  loose_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'loose.wav'))
  break_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'break.wav'))
  shoot_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'shoot.wav'))
  hit_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'hit.wav'))
  monster_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'monster.wav'))