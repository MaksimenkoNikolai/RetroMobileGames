import pygame

from settings import *
from img.images import *

gap = 0.12*HEIGHT

class Menu(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    
    self.doodle_btn = doodle_btn
    self.doodle_rect = self.doodle_btn.get_rect()
    self.doodle_rect.center = (WIDTH/2, 0.3*HEIGHT + gap)
    
    self.flappy_btn = flappy_btn
    self.flappy_rect = self.flappy_btn.get_rect()
    self.flappy_rect.center = (WIDTH/2, 0.3*HEIGHT + 2*gap)
    
    self.snake_btn = snake_btn
    self.snake_rect = self.snake_btn.get_rect()
    self.snake_rect.center = (WIDTH/2, 0.3*HEIGHT + 3*gap)
    
    self.tetris_btn = tetris_btn
    self.tetris_rect = self.tetris_btn.get_rect()
    self.tetris_rect.center = (WIDTH/2, 0.3*HEIGHT + 4*gap)
  
  def draw(self, screen):
    screen.blit(self.doodle_btn, self.doodle_rect)
    screen.blit(self.flappy_btn, self.flappy_rect)
    screen.blit(self.snake_btn, self.snake_rect)
    screen.blit(self.tetris_btn, self.tetris_rect)
    
    font = pygame.font.SysFont('roboto', 50)
    text = font.render("Ok, boomer", True, (255, 255, 255))
    screen.blit(text, (0.27*WIDTH, 0.2*HEIGHT))
  
  def is_doodle_clicked(self, mouse_pos):
    x, y = mouse_pos
    return y < self.doodle_rect.bottom and y > self.doodle_rect.top and x < self.doodle_rect.right and x > self.doodle_rect.left
  
  def is_flappy_clicked(self, mouse_pos):
    x, y = mouse_pos
    return y < self.flappy_rect.bottom and y > self.flappy_rect.top and x < self.flappy_rect.right and x > self.flappy_rect.left
  
  def is_snake_clicked(self, mouse_pos):
    x, y = mouse_pos
    return y < self.snake_rect.bottom and y > self.snake_rect.top and x < self.snake_rect.right and x > self.snake_rect.left
  
  def is_tetris_clicked(self, mouse_pos):
    x, y = mouse_pos
    return y < self.tetris_rect.bottom and y > self.tetris_rect.top and x < self.tetris_rect.right and x > self.tetris_rect.left