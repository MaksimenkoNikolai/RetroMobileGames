import pygame

from settings import *
from img.images import *
from sound.sounds import *

class Menu(pygame.sprite.Sprite):
  def __init__(self, screen_manager):
    pygame.sprite.Sprite.__init__(self)
    self.image = doodle_logo_img
    self.rect = self.image.get_rect()
    self.rect.topleft = (WIDTH/20, HEIGHT/10)
    
    self.play_img = play_img
    self.rect_play = self.play_img.get_rect()
    self.rect_play.bottomleft = (WIDTH*0.28, HEIGHT*0.42)
    
    self.ufo_img = ufo_img
    self.rect_ufo = self.ufo_img.get_rect()
    self.rect_ufo.topright = (WIDTH/20*19, HEIGHT/25)
    
    self.bugs_img = bugs_img
    self.rect_bugs = self.bugs_img.get_rect()
    self.rect_bugs.topleft = (WIDTH/10, HEIGHT/3)
    
    self.hole_img = hole_img
    self.rect_hole = self.hole_img.get_rect()
    self.rect_hole.topleft = (WIDTH*0.7, HEIGHT*0.5)
    
    self.platform_img = platform_img
    self.rect_platform = self.platform_img.get_rect()
    self.rect_platform.topleft = (WIDTH*0.1, HEIGHT*0.8)
    
    self.ragged_img = ragged_bottom_img
    self.rect_ragged = self.ragged_img.get_rect()
    self.rect_ragged.bottomleft = (0, HEIGHT*1.05)

    self.screen_manager = screen_manager
  
  def draw(self, screen):
    screen.blit(self.image, self.rect)
    screen.blit(self.play_img, self.rect_play)
    screen.blit(self.ufo_img, self.rect_ufo)
    screen.blit(self.bugs_img, self.rect_bugs)
    screen.blit(self.hole_img, self.rect_hole)
    screen.blit(self.platform_img, self.rect_platform)
    
    # draw black rectangle
    black_surface = pygame.Surface((ragged_bottom_size[0], 2*ragged_bottom_size[1]))
    black_surface.fill((0,0,0))
    screen.blit(black_surface, self.rect_ragged)
    
    screen.blit(self.ragged_img, self.rect_ragged)
  
  def on_click(self, mouse_pos):
    x, y = mouse_pos
    if y < self.rect_play.bottom and y > self.rect_play.top and x < self.rect_play.right and x > self.rect_play.left:
      self.play_img = play_on_img
  
  def on_click_up(self, mouse_pos):
    x, y = mouse_pos
    if y < self.rect_play.bottom and y > self.rect_play.top and x < self.rect_play.right and x > self.rect_play.left:
      self.play_img = play_img
      self.screen_manager.start_game()