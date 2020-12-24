import pygame

from settings import *
from img.images import *
from sound.sounds import *

from sprites.bullet import Bullet

class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = doodle_right_img
    
    self.rect = self.image.get_rect()
    self.size = self.image.get_size()
    
    self.width = self.size[0] 
    self.height = self.size[1] 
    
    self.rect.centerx = WIDTH / 2
    self.rect.bottom = HEIGHT
    
    self.speed_x = 0;
    self.is_right = True
    self.acceleration_x = 0.3
    self.is_accelerating_x = False
    
    self.default_speed_y = 10
    self.speed_y = 10
    self.gravity = ((3*self.height - self.default_speed_y*FPS/3*2)*2)/((FPS/3*2)**2)
    self.is_squezing = False
    self.is_falling = False
    self.is_stop = False
    
    self.is_loose = False
    self.is_scrolling_up = False
    
    self.is_shoot = False
    self.anim_shoot_count = 0
    self.bullets = []
  
  def update(self):
    self.move_x()
    
    if not self.is_stop and not self.is_loose:
      self.jump()
    
    if self.is_shoot:
      self.shoot_anim()
    
    for bullet in self.bullets:
      bullet.update()
    
    if self.rect.bottom > HEIGHT and not self.is_loose:
      self.end_game()
    
    if self.is_loose:
      if self.is_scrolling_up:
        self.scroll_up()
      else: 
        self.fall()
    
    self.kill_bullets()
  
  def kill_bullets(self):
    for bullet in self.bullets:
      if bullet.rect.bottom <= 0:
        bullet.rect.left = -500
        bullet.kill()
  
  def draw(self, screen):
    screen.blit(self.image, self.rect)
    for bullet in self.bullets:
      bullet.draw(screen)
  
  def start_accelerating_x(self, is_right):
    self.is_accelerating_x = True
    
    if self.is_squezing:
      if is_right:
        if not self.is_shoot:
          self.image = doodle_squeeze_right_img
        self.is_right = True
      else:
        if not self.is_shoot:
          self.image = doodle_squeeze_left_img
        self.is_right = False
    else:
      if not is_right:
        if not self.is_shoot:
          self.image = doodle_left_img
        self.is_right = False
      else:
        if not self.is_shoot:
          self.image = doodle_right_img
        self.is_right = True
  
  def stop_accelerating_x(self):
    self.is_accelerating_x = False
  
  def move_x(self):
    self.rect.x += self.speed_x
    
    if self.is_right and self.is_accelerating_x:
      self.speed_x += self.acceleration_x
    elif not self.is_right and self.is_accelerating_x:
      self.speed_x -= self.acceleration_x
    
    if self.rect.left > (WIDTH - self.width/4):
      self.rect.left = -self.width*3/4
    
    if self.rect.left < (-self.width*3/4) :
      self.rect.left = WIDTH - self.width/4

  def start_jump(self):
    self.speed_y = self.default_speed_y
    
    jump_sound.play()
    
    self.is_squezing = True
    self.is_falling = False
    
    if not self.is_shoot:
      if self.is_right:
        self.image = doodle_squeeze_right_img
      else:
        self.image = doodle_squeeze_left_img
    
    pygame.time.set_timer(JUMPEVENT, 200, True)
  
  def un_squeeze(self):
    self.is_squezing = False
    
    if not self.is_shoot:
      if self.is_right:
        self.image = doodle_right_img
      else:
        self.image = doodle_left_img
  
  def jump(self): 
    self.rect.bottom -= self.speed_y
    self.speed_y = self.speed_y + self.gravity

    if self.speed_y <= 0:
      self.is_falling = True
  
  def scroll_up(self):
    if self.rect.top > HEIGHT/2:
      self.rect.bottom -= self.speed_y
      self.speed_y = self.speed_y + abs(self.gravity)/5
    else:
      self.is_scrolling_up = False
      self.speed_y = -5
  
  def fall(self):
    self.rect.bottom -= self.speed_y
    self.speed_y = self.speed_y + self.gravity
  
  def shoot(self):
    center = self.rect.center
    self.image = doodle_shoot_img
    self.rect = self.image.get_rect()
    self.rect.center = center
    
    self.anim_shoot_count = 0
    self.is_shoot = True
    
    shoot_sound.play()
    
    new_bullet = Bullet(self.rect.centerx, self.rect.top)
    self.bullets.append(new_bullet)
  
  def shoot_anim(self):
    self.anim_shoot_count += 1
    if self.anim_shoot_count >= 20:
      self.is_shoot = False
      self.anim_shoot_count = 0
      
      center = self.rect.center
      if self.is_right:
        self.image = doodle_right_img
      else:
        self.image = doodle_left_img
      self.rect = self.image.get_rect()
      self.rect.center = center
  
  def end_game(self):
    self.is_loose = True
    self.is_scrolling_up = True
    self.speed_y = abs(self.speed_y)/2
    loose_sound.play()
  
  def play_again(self):
    self.rect.centerx = WIDTH / 2
    self.rect.bottom = HEIGHT
    
    self.speed_x = 0;
    self.is_right = True
    
    self.speed_y = 10
    self.is_squezing = False
    self.is_falling = False
    self.is_stop = False
    self.is_scrolling_up = False
    
    self.is_loose = False
    
    self.is_shoot = False
    self.anim_shoot_count = 0
  