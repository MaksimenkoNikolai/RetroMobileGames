import pygame

from settings import *
from img.images import *

gap_btw_img_and_play_again = HEIGHT*0.07

gap_btw_play_again_and_game_over = HEIGHT*0.25
gap_btw_play_again_and_score = HEIGHT*0.15

class LooseScreen(pygame.sprite.Sprite):
  def __init__(self, player, score):
    pygame.sprite.Sprite.__init__(self)
    self.image = ragged_bottom_img
    self.rect = self.image.get_rect()
    self.rect.top = HEIGHT + gap_btw_img_and_play_again + play_again_size[1] + gap_btw_play_again_and_game_over + game_over_size[1]
    
    self.image_play_again = play_again_img
    self.rect_play_again = self.image_play_again.get_rect()
    self.rect_play_again.top = HEIGHT + gap_btw_play_again_and_game_over + game_over_size[1]
    self.rect_play_again.centerx = WIDTH/4
    
    self.image_menu = menu_img
    self.rect_menu = self.image_menu.get_rect()
    self.rect_menu.top = HEIGHT + gap_btw_play_again_and_game_over + game_over_size[1]
    self.rect_menu.centerx = WIDTH/4*3
    
    self.image_game_over = game_over_img
    self.rect_game_over = self.image_game_over.get_rect()
    self.rect_game_over.top = HEIGHT
    self.rect_game_over.centerx = WIDTH/2
    
    self.player = player
    self.score = score
    
    self.is_loose = False
    self.speed_y = 0
  
  def update(self):
    if self.player.is_loose and not self.player.is_scrolling_up and not self.is_loose:
      self.end_game()
    
    if self.is_loose:
      self.scroll_up()
    
    if self.is_loose and not self.player.is_loose:
      self.play_again()
    
    self.rect_play_again.bottom = self.rect.top - gap_btw_img_and_play_again
    self.rect_menu.bottom = self.rect.top - gap_btw_img_and_play_again
    self.rect_game_over.bottom = self.rect_menu.top - gap_btw_play_again_and_game_over
  
  def draw(self, screen):
    # draw black rectangle
    black_surface = pygame.Surface((ragged_bottom_size[0], 2*ragged_bottom_size[1]))
    black_surface.fill((0,0,0))
    screen.blit(black_surface, self.rect)
    
    # draw ragged paper
    screen.blit(self.image, self.rect)
    
    # draw play again button
    screen.blit(self.image_play_again, self.rect_play_again)
    
    # draw menu button
    screen.blit(self.image_menu, self.rect_menu)
    
    screen.blit(self.image_game_over, self.rect_game_over)
    
    font = pygame.font.Font(font_name, 40)
    text_surface = font.render(f'Your score: {str(self.score.score)}', True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.center = (WIDTH/2, self.rect_menu.top - gap_btw_play_again_and_score)
    screen.blit(text_surface, text_rect)
  
  def scroll_up(self):
    if not self.rect.bottom <= HEIGHT*1.05:
      if self.rect.bottom - self.speed_y < HEIGHT:
        self.rect.bottom = HEIGHT
      else:
        self.rect.bottom -= self.speed_y
        self.speed_y += abs(self.player.gravity)

  def on_click_up(self, mouse_pos):
    self.image_play_again = play_again_img
    self.image_menu = menu_img
    
    x, y = mouse_pos
    if self.is_clicked(x, y, self.rect_play_again):
      self.player.play_again()
    
    if self.is_clicked(x, y, self.rect_menu):
      return True
    return False
  
  def on_click(self, mouse_pos):
    x, y = mouse_pos
    if self.is_clicked(x, y, self.rect_play_again):
      self.image_play_again = play_again_on_img
    
    if self.is_clicked(x, y, self.rect_menu):
      self.image_menu = menu_on_img
  
  def end_game(self):
    self.is_loose = True
  
  def play_again(self):
    self.rect.top = HEIGHT + gap_btw_img_and_play_again + play_again_size[1] + gap_btw_play_again_and_game_over + game_over_size[1]
    self.is_loose = False
    self.speed_y = 0
  
  def is_clicked(self, x, y, rect):
    return y < rect.bottom and y > rect.top and x < rect.right and x > rect.left