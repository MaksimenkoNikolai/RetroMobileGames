import pygame

import snake.main as snake
import flappy.main as flappy
import doodle.main as doodle

from settings import *

from menu import Menu

# init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nostalgic games")
clock = pygame.time.Clock()
running = True

menu = Menu()

def handle_events():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
      if menu.is_doodle_clicked(event.pos):
        doodle.init()
      if menu.is_flappy_clicked(event.pos):
        flappy.init()
      if menu.is_snake_clicked(event.pos):
        snake.init()
      # if menu.is_doodle_clicked(event.pos):
      #   doodle.init()


def draw():
  surf = pygame.Surface((WIDTH, HEIGHT))
  surf.fill((42, 62, 81))
  screen.blit(surf, (0, 0))
  
  menu.draw(screen)
  
  pygame.display.flip()


# def update():
#   if screen_manager.is_game_start:
  # pass

while running:
  clock.tick(FPS)
  handle_events()
  # update()
  draw()

pygame.quit()
