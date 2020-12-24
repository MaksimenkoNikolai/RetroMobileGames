import pygame

from doodle.settings import *
from doodle.img.images import *

from doodle.sprites.player import Player
from doodle.sprites.platforms import Platforms
from doodle.sprites.score import Score
from doodle.sprites.loose_screen import LooseScreen
from doodle.sprites.screen_manager import ScreenManager
from doodle.sprites.menu_screen import Menu

def init():
  # init
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Doodle Jump")
  clock = pygame.time.Clock()
  running = True


  # init sprites
  all_sprites = pygame.sprite.Group()

  player = Player()
  platforms = Platforms(player)
  score = Score(player, platforms.platforms[0])
  loose_screen = LooseScreen(player, score)

  for platform in platforms.platforms:
    all_sprites.add(platform)

  screen_manager = ScreenManager(platforms, player, score, loose_screen) 
  menu = Menu(screen_manager)

  def handle_events(screen_manager, player, loose_screen, menu):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      
      if screen_manager.is_game_start:
        
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            player.stop_accelerating_x()

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            player.start_accelerating_x(False)
          if event.key == pygame.K_RIGHT:
            player.start_accelerating_x(True)
          if event.key == pygame.K_SPACE:
            player.shoot()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          loose_screen.on_click(event.pos)
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
          is_go_to_menu = loose_screen.on_click_up(event.pos)
          if is_go_to_menu:
            screen_manager.end_game()

        if event.type == JUMPEVENT:
          player.un_squeeze()
        
      else:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          menu.on_click(event.pos)
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
          menu.on_click_up(event.pos)
        


  def draw(screen_manager, all_sprites, platforms, loose_screen, player, score, screen, menu):
    screen.blit(bg, (0, 0)) 
    
    if screen_manager.is_game_start:
      loose_screen.draw(screen)
      all_sprites.draw(screen)
      player.draw(screen)
      score.draw(screen)
    else:
      menu.draw(screen)

    pygame.display.flip()


  def update(screen_manager, all_sprites, platforms, loose_screen, player, score):
    if screen_manager.is_game_start:
      all_sprites.update()
      platforms.update()
      loose_screen.update()
      player.update()
      score.update()

      all_sprites = platforms.append_new_platforms(all_sprites)

  while running:
    clock.tick(FPS)
    handle_events(screen_manager, player, loose_screen, menu)
    update(screen_manager, all_sprites, platforms, loose_screen, player, score)
    draw(screen_manager, all_sprites, platforms, loose_screen, player, score, screen, menu)

  pygame.quit()
