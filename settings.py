import pygame
import os

WIDTH = 414
HEIGHT = 736
FPS = 60

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

JUMPEVENT = pygame.USEREVENT + 1