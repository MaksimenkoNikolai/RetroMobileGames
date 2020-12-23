import pygame
import os
from PIL import Image

from settings import *

doodle_right_size = Image.open(os.path.join(img_folder, 'doodle_right.png')).size

doodle_right_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'doodle_right.png')
    ), 
  (int(WIDTH/7), int(WIDTH/7/doodle_right_size[0]*doodle_right_size[1]))
  )


doodle_left_size = Image.open(os.path.join(img_folder, 'doodle_left.png')).size

doodle_left_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'doodle_left.png')
    ), 
  (int(WIDTH/7), int(WIDTH/7/doodle_left_size[0]*doodle_left_size[1]))
  )


doodle_squeeze_right_size = Image.open(os.path.join(img_folder, 'doodle_squeeze_right.png')).size

doodle_squeeze_right_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'doodle_squeeze_right.png')
    ), 
  (int(WIDTH/7), int(WIDTH/7/doodle_squeeze_right_size[0]*doodle_squeeze_right_size[1]))
  )


doodle_squeeze_left_size = Image.open(os.path.join(img_folder, 'doodle_squeeze_left.png')).size

doodle_squeeze_left_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'doodle_squeeze_left.png')
    ), 
  (int(WIDTH/7), int(WIDTH/7/doodle_squeeze_left_size[0]*doodle_squeeze_left_size[1]))
  )

doodle_shoot_size = Image.open(os.path.join(img_folder, 'doodle_shoot.png')).size

doodle_shoot_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'doodle_shoot.png')
    ), 
  (int(int(WIDTH/7)*0.65), int(int(int(WIDTH/7)*0.65)/doodle_shoot_size[0]*doodle_shoot_size[1]))
  )


(width, height) = Image.open(os.path.join(img_folder, 'background.png')).size
bg_size = (int(int(1.5*HEIGHT)/height*width), int(1.5*HEIGHT))

bg = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'background.png')
    ),
  (bg_size[0], bg_size[1])
  )


ragged_bottom_size = Image.open(os.path.join(img_folder, 'ragged_bottom.png')).size

ragged_bottom_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'ragged_bottom.png')
    ), 
  (bg_size[0], int(bg_size[0]/ragged_bottom_size[0]*ragged_bottom_size[1]))
)


top_score_size = Image.open(os.path.join(img_folder, 'top_score.png')).size

top_score_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'top_score.png')
  ),
  (int(WIDTH), int(int(WIDTH)/top_score_size[0]*top_score_size[1]))
)


platform_size = Image.open(os.path.join(img_folder, 'platform_green.png')).size

platform_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'platform_green.png')
    ), 
  (int(WIDTH/5), int(int(WIDTH/5)/platform_size[0]*platform_size[1]) + 3)
)

platform_blue_size = Image.open(os.path.join(img_folder, 'platform_blue.png')).size

platform_blue_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'platform_blue.png')
    ), 
  (int(WIDTH/5), int(int(WIDTH/5)/platform_blue_size[0]*platform_blue_size[1]))
)

platform_break1_size = Image.open(os.path.join(img_folder, 'platform_break1.png')).size

platform_break1_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'platform_break1.png')
    ), 
  (int(WIDTH/5), int(int(WIDTH/5)/platform_break1_size[0]*platform_break1_size[1]))
)

platform_break2_size = Image.open(os.path.join(img_folder, 'platform_break2.png')).size

platform_break2_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'platform_break2.png')
    ), 
  (int(WIDTH/5), int(int(WIDTH/5)/platform_break2_size[0]*platform_break2_size[1]))
)

platform_break3_size = Image.open(os.path.join(img_folder, 'platform_break3.png')).size

platform_break3_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'platform_break3.png')
    ), 
  (int(WIDTH/5), int(int(WIDTH/5)/platform_break3_size[0]*platform_break3_size[1]))
)


platform_break4_size = Image.open(os.path.join(img_folder, 'platform_break4.png')).size

platform_break4_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'platform_break4.png')
    ), 
  (int(WIDTH/5), int(int(WIDTH/5)/platform_break4_size[0]*platform_break4_size[1]))
)


play_again_size = Image.open(os.path.join(img_folder, 'play_again.png')).size

play_again_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'play_again.png')
    ), 
  (int(WIDTH/3), int(int(WIDTH/3)/play_again_size[0]*play_again_size[1]))
)

play_again_on_size = Image.open(os.path.join(img_folder, 'play_again_on.png')).size

play_again_on_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'play_again_on.png')
    ), 
  (int(WIDTH/3), int(int(WIDTH/3)/play_again_on_size[0]*play_again_on_size[1]))
)

doodle_logo_size = Image.open(os.path.join(img_folder, 'doodle_logo.png')).size

doodle_logo_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'doodle_logo.png')
    ), 
  (int(WIDTH/3*2), int(int(WIDTH/3*2)/doodle_logo_size[0]*doodle_logo_size[1]))
)

game_over_size = Image.open(os.path.join(img_folder, 'game_over.png')).size

game_over_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'game_over.png')
    ), 
  (int(WIDTH/4*3), int(int(WIDTH/4*3)/game_over_size[0]*game_over_size[1]))
)

play_size = Image.open(os.path.join(img_folder, 'play.png')).size

play_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'play.png')
    ), 
  (int(WIDTH/3), int(int(WIDTH/3)/play_size[0]*play_size[1]))
)

play_on_size = Image.open(os.path.join(img_folder, 'play_on.png')).size

play_on_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'play_on.png')
    ), 
  (int(WIDTH/3), int(int(WIDTH/3)/play_on_size[0]*play_on_size[1]))
)

menu_size = Image.open(os.path.join(img_folder, 'menu.png')).size

menu_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'menu.png')
    ), 
  (int(WIDTH/3), int(int(WIDTH/3)/menu_size[0]*menu_size[1]))
)

menu_on_size = Image.open(os.path.join(img_folder, 'menu_on.png')).size

menu_on_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'menu_on.png')
    ), 
  (int(WIDTH/3), int(int(WIDTH/3)/menu_on_size[0]*menu_on_size[1]))
)

bullet_size = Image.open(os.path.join(img_folder, 'bullet.png')).size

bullet_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'bullet.png')
    ), 
  (int(WIDTH/22), int(int(WIDTH/22)/bullet_size[0]*bullet_size[1]))
)

monster1_size = Image.open(os.path.join(img_folder, 'monster1.png')).size

monster1_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'monster1.png')
    ), 
  (int(WIDTH/3), int(int(WIDTH/3)/monster1_size[0]*monster1_size[1]))
)

ufo_size = Image.open(os.path.join(img_folder, 'ufo.png')).size

ufo_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'ufo.png')
    ), 
  (int(WIDTH/4), int(int(WIDTH/4)/ufo_size[0]*ufo_size[1]))
)

bugs_size = Image.open(os.path.join(img_folder, 'bugs.png')).size

bugs_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'bugs.png')
    ), 
  (int(WIDTH/3*2), int(int(WIDTH/3*2)/bugs_size[0]*bugs_size[1]))
)

hole_size = Image.open(os.path.join(img_folder, 'hole.png')).size

hole_img = pygame.transform.scale(
  pygame.image.load(
    os.path.join(img_folder, 'hole.png')
    ), 
  (int(WIDTH/4), int(int(WIDTH/4)/hole_size[0]*hole_size[1]))
)