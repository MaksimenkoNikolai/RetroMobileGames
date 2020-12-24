import pygame

import snake.main as snake
import flappy.main as flappy
import doodle.main as doodle

FPS = 60

# init
pygame.init()
screen = pygame.display.set_mode((414, 736))
pygame.display.set_caption("Nostalgic games")
clock = pygame.time.Clock()
running = True

def handle_events():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        doodle.init()
      if event.key == pygame.K_RIGHT:
        flappy.init()
      if event.key == pygame.K_SPACE:
        snake.init()


def draw():
  surf = pygame.Surface((200, 200))
  surf.fill((0,0,0))
  screen.blit(surf, (50, 50))
  pygame.display.flip()
  # screen.blit(bg, (0, 0)) 



# def update():
#   if screen_manager.is_game_start:
  # pass

while running:
  clock.tick(FPS)
  handle_events()
  # update()
  draw()

pygame.quit()
