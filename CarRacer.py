#import pygame----------------------------------------------------------------------------------------------------------
import pygame, sys, random
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()

TITLE_FONT = pygame.font.SysFont("perpetua", 40)

highscore = []

#----set colours---------------------------------------------

white = (255, 255, 255)
grey = (128, 128, 128)
green = (49, 99, 0)
grassgreen = (0, 255, 0)
skyblue = (0, 191, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

#----set game background-------------------------------------

sky = []
grass = []
grassdots = []

for i in range(0, 200):
 sky += [i]

for i in range(205, 950, 1):
 grass += [i]

#crash menu function----------------------------------------------------------------------------------------------------

def crash_menu():

   global highscore
   highscore.append(score)

   global TITLE_FONT
   score_display = TITLE_FONT.render("You Had A Score Of: " + score_string, True, (255, 255, 255))
   highscore_display = TITLE_FONT.render("The High Score is:" + str(max(highscore)), True, (255, 255, 255))

   crash_background = pygame.image.load("crashbackground.jpg")

   #----import images--------------------------------------------

   mainmenu_button = pygame.image.load("main menu button.png")
   playagain_button = pygame.image.load("play again button.png")
   youdied_image = pygame.image.load("You died.png")
   main_menu_blue = pygame.image.load("main menu button (1).png")
   playagain_button_blue = pygame.image.load("play again button blue.png")

   #----set Rects--------------------------------------------

   playagain_rect = pygame.Rect(350, 300, 300, 75)
   mainmenu_rect = pygame.Rect(350, 400, 300, 75)

   #----set selection variables--------------------------------------------

   mainmenu_selection = 0
   playagain_selection = 0

   #----event handling--------------------------------------------

   while True:
       clock.tick(60)

       for event in pygame.event.get():
           if event.type == QUIT:
               pygame.quit()
               sys.exit()
           elif event.type == MOUSEBUTTONDOWN:
               if playagain_rect.collidepoint(event.pos):
                   music = "car chase music.wav"
                   pygame.mixer.music.load(music)
                   pygame.mixer.music.play(-1, 0.0)
                   pygame.mixer.music.set_volume(0.5)
                   play_game()
               if mainmenu_rect.collidepoint(event.pos):
                   main_menu()
           elif event.type == MOUSEMOTION:
               if playagain_rect.collidepoint(event.pos):
                   playagain_selection = 1
               else:
                   playagain_selection = 0
               if mainmenu_rect.collidepoint(event.pos):
                   mainmenu_selection = 1
               else:
                   mainmenu_selection = 0

   #----words display--------------------------------------------

       screen.fill((0,0,0))
       screen.blit(pygame.transform.scale(crash_background, (1000, 700)), (0, 0))
       screen.blit(pygame.transform.scale(youdied_image, (500, 200)), (250, 70))
       screen.blit(pygame.transform.scale(playagain_button, (300, 75)), (350, 300))
       screen.blit(pygame.transform.scale(mainmenu_button, (300, 75)), (350, 400))
       screen.blit(score_display, (350, 550))
       screen.blit(highscore_display, (350, 600))

   #----button mechanics--------------------------------------------

       if mainmenu_selection == 1:
           screen.blit(pygame.transform.scale(main_menu_blue, (300, 75)), (350, 400))
       else:
           screen.blit(pygame.transform.scale(mainmenu_button, (300, 75)), (350, 400))

       if playagain_selection == 1:
           screen.blit(pygame.transform.scale(playagain_button_blue, (300, 75)), (350, 300))
       else:
           screen.blit(pygame.transform.scale(playagain_button, (300, 75)), (350, 300))

       pygame.display.update()

#instructions menu functioin--------------------------------------------------------------------------------------------

def show_instructions():

   #----import images--------------------------------------------

   instructions_titleimage = pygame.image.load("instructions.png")
   rightkey_image = pygame.image.load("computer_key_Arrow_Right.png")
   leftkey_image = pygame.image.load("computer_key_Arrow_Left.png")
   coin_image = pygame.image.load('gold-coin-icon.png')
   green_car = pygame.image.load('CAR 2.png')
   rock_image = pygame.image.load('ROCK.png')
   barrier_image = pygame.image.load('obstacle.gif')
   mushroom_image = pygame.image.load('mushroom.png')
   leftarrow_image = pygame.image.load('Arrow_left.png')
   rightarrow_image = pygame.image.load('right arrow.png')
   leftarrow_image_red = pygame.image.load('Arrow_left.svg.png')
   rightarrow_image_red = pygame.image.load('arrow.png')
   escape_button = pygame.image.load('escape key.jpg')

   background = pygame.image.load("background.jpg")

   #----instructions page 2--------------------------------------------

   def instructions_page2():

       #----set word instructions page 2--------------------------------------------

       global TITLE_FONT
       title2 = TITLE_FONT.render("Objects", True, (255, 255, 255))
       car_instructions = TITLE_FONT.render("Player Car: ", True, (255, 255, 255))
       point_instructions = TITLE_FONT.render("Point Objects", True, (255, 255, 255))
       coin_instructions = TITLE_FONT.render("1 Point", True, (255, 255, 255))
       mushroom_instructions = TITLE_FONT.render("5 Points", True, (255, 255, 255))
       controls_instructions = TITLE_FONT.render("     Controls", True, (255, 255, 255))

       obstacles_instructions = TITLE_FONT.render('Obstacles (Avoid These):', True, (255, 255, 255))
       rock_instructions = TITLE_FONT.render('Rock:', True, (255, 255, 255))
       barrier_instruction = TITLE_FONT.render('Barrier:', True, (255, 255, 255))

       #----set Rects--------------------------------------------

       leftarrow_rect = pygame.Rect(0, 660, 50, 25)

       #----set MOUSEMOTION variables--------------------------------------------

       leftarrow_mousemotion = 0

       #----event handling--------------------------------------------

       while True:
           clock.tick(60)

           for event in pygame.event.get():
               if event.type == QUIT:
                   pygame.quit()
                   sys.exit()
               elif event.type == KEYDOWN:
                   if event.key == K_ESCAPE or event.key == K_LEFT:
                       return
               elif event.type == MOUSEBUTTONDOWN:
                   if leftarrow_rect.collidepoint(event.pos):
                       return
               elif event.type == MOUSEMOTION:
                   if leftarrow_rect.collidepoint(event.pos):
                       leftarrow_mousemotion = 1
                   else:
                       leftarrow_mousemotion = 0

           #----draw instructions page 2--------------------------------------------
           #----draw car & coin instructions--------------------------------------------

           screen.fill((0,0,0))
           screen.blit(pygame.transform.scale(background, (1000, 700)), (0,0))
           screen.blit(pygame.transform.scale(instructions_titleimage, (400, 200)), (15, 20))
           screen.blit(title2, (50, 150))
           screen.blit(car_instructions, (100, 200))
           screen.blit(pygame.transform.scale(green_car, (50, 50)), (275, 200))
           screen.blit(point_instructions, (100, 300))
           screen.blit(coin_instructions, (150, 350))
           screen.blit(pygame.transform.scale(coin_image, (60, 50)), (260, 350))
           screen.blit(mushroom_instructions, (150, 400))
           screen.blit(pygame.transform.scale(mushroom_image, (50, 50)), (270, 400))

           #----draw obstacles instructions--------------------------------------------

           screen.blit(obstacles_instructions, (450, 150))
           screen.blit(rock_instructions,(500, 200))
           screen.blit(pygame.transform.scale(rock_image, (50, 50)), (600, 200))
           screen.blit(barrier_instruction, (500, 250))
           screen.blit(pygame.transform.scale(barrier_image, (60, 50)), (625, 250))

           screen.blit(controls_instructions, (10, 650))

           #----arrow mechanics--------------------------------------------

           if leftarrow_mousemotion == 1:
               screen.blit(pygame.transform.scale(leftarrow_image_red, (50, 25)), (0, 660))
           else:
               screen.blit(pygame.transform.scale(leftarrow_image, (50, 25)), (0, 660))

           pygame.display.update()

   #----set words instructions--------------------------------------------

   global TITLE_FONT
   title2 = TITLE_FONT.render("Controls:", True, (255, 255, 255))
   instructions = TITLE_FONT.render("Press the          key to go Left", True, (255, 255, 255))
   instructions2 = TITLE_FONT.render("Press the          key to go Right", True, (255, 255, 255))
   instructions3 = TITLE_FONT.render("Press         to go back", True, (255, 255, 255))
   objects_instructions = TITLE_FONT.render("Objects: ", True, (255, 255, 255))

   #----event Rect--------------------------------------------

   rightarrow_rect = pygame.Rect(925, 662, 50, 25)

   #----set MOUSEMOTION variables--------------------------------------------

   rightarrow_mousemotion = 0

   #----event handling--------------------------------------------

   while True:
       clock.tick(60)

       for event in pygame.event.get():
           if event.type == QUIT:
               pygame.quit()
               sys.exit()
           elif event.type == KEYDOWN:
               if event.key == K_RIGHT:
                   instructions_page2()
               if event.key == K_ESCAPE:
                   return
           elif event.type == MOUSEBUTTONDOWN:
               if rightarrow_rect.collidepoint(event.pos):
                   instructions_page2()
           elif event.type == MOUSEMOTION:
               if rightarrow_rect.collidepoint(event.pos):
                   rightarrow_mousemotion = 1
               else:
                   rightarrow_mousemotion = 0

       #----draw instructions--------------------------------------------

       screen.fill((0,0,0))
       screen.blit(pygame.transform.scale(background, (1000, 700)), (0,0))
       screen.blit(pygame.transform.scale(instructions_titleimage, (400, 200)), (15, 20))
       screen.blit(title2, (50, 100))
       screen.blit(instructions, (100, 200))
       screen.blit(pygame.transform.scale(leftkey_image,(50, 50)), (250, 190))
       screen.blit(instructions2, (100, 250))
       screen.blit(pygame.transform.scale(rightkey_image, (50, 50)), (250, 240))
       screen.blit(instructions3, (100, 500))
       screen.blit(pygame.transform.scale(escape_button,(50, 50)), (190, 500))
       screen.blit(objects_instructions, (800, 650))

       #----arrow mechanics--------------------------------------------

       if rightarrow_mousemotion == 1:
           screen.blit(pygame.transform.scale(rightarrow_image_red, (50, 25)), (925, 662))
       else:
           screen.blit(pygame.transform.scale(rightarrow_image, (50, 25)), (925, 662))

       pygame.display.update()

#----play game function-------------------------------------------------------------------------------------------------

def play_game():

   global score
   score = 0
   counter = 0

   global TITLE_FONT

   #----import game images-----------------------------------------------

   coin_image = pygame.image.load('gold-coin-icon.png')
   rock_image = pygame.image.load('ROCK.png')
   barrier_image = pygame.image.load('obstacle.gif')
   tree_image = pygame.image.load('tree.png')
   mushroom_image = pygame.image.load('mushroom.png')
   cloud_image = pygame.image.load('clouds.png')

   green_car = pygame.image.load('CAR 2.png')
   blue_car = pygame.image.load("blue car.png")
   red_car = pygame.image.load("red car.png")
   purple_car = pygame.image.load("purple car.png")
   black_car = pygame.image.load("black car.png")

   #----set game lists and variables--------------------------------------------

   player_xposition = 200

   rock_rect = []
   barrier_rect = []
   trees = []
   trees_xposition = [250, 625]
   coins_rect = []
   clouds = []

   player_xchange = 0

   rock_y = 175
   barrier_y = 175
   trees_y = 80
   coins_y = 175

   #----car selection menu---------------------------------------------------------------------------------------------

   def car_selection():
       global TITLE_FONT

       instructions = TITLE_FONT.render("Choose A Car", True, (255, 255, 255))

       car_selection_background = pygame.image.load("garage background.jpg")

       #----create Rects--------------------------------------------

       player_greencar = pygame.Rect(300, 200, 100, 100)
       player_bluecar = pygame.Rect(600, 200, 100, 100)
       player_redcar = pygame.Rect(300, 400, 100, 100)
       player_purplecar = pygame.Rect(600, 400, 100, 100)

       #----set variables--------------------------------------------

       global car_list
       car_list = [green_car, blue_car, red_car, purple_car]

       screen.fill((0, 0, 0))
       screen.blit(pygame.transform.scale(car_selection_background, (1000, 700)), (0, 0))
       screen.blit(instructions, (400, 50))

       green_car_selection = 0
       blue_car_selection = 0
       red_car_selection = 0
       purple_car_selection = 0

       #----event handling--------------------------------------------

       while True:
           clock.tick(60)

           for event in pygame.event.get():
               if event.type == QUIT:
                   pygame.quit()
                   sys.exit()
               if event.type == MOUSEBUTTONDOWN:
                   if player_greencar.collidepoint(event.pos):
                       car_list.append(0)
                       return
                   if player_bluecar.collidepoint(event.pos):
                       car_list.append(1)
                       return
                   if player_redcar.collidepoint(event.pos):
                       car_list.append(2)
                       return
                   if player_purplecar.collidepoint(event.pos):
                       car_list.append(3)
                       return
               if event.type == MOUSEMOTION:
                   if player_greencar.collidepoint(event.pos):
                       green_car_selection = 1
                   else:
                       green_car_selection = 0
                   if player_bluecar.collidepoint(event.pos):
                       blue_car_selection = 1
                   else:
                       blue_car_selection = 0
                   if player_redcar.collidepoint(event.pos):
                       red_car_selection = 1
                   else:
                       red_car_selection = 0
                   if player_purplecar.collidepoint(event.pos):
                       purple_car_selection = 1
                   else:
                       purple_car_selection = 0

           #----draw images--------------------------------------------

           screen.blit(pygame.transform.scale(green_car, (100, 100)), (300, 200))
           screen.blit(pygame.transform.scale(blue_car, (100, 100)), (600, 200))
           screen.blit(pygame.transform.scale(red_car, (100, 100)), (300, 400))
           screen.blit(pygame.transform.scale(purple_car, (100, 100)), (600, 400))

           #----car selection MOUSEMOTION mechanics--------------------------------------------

           if green_car_selection == 1:
               screen.blit(pygame.transform.scale(black_car, (100, 100)), (300, 200))
           else:
               screen.blit(pygame.transform.scale(green_car, (100, 100)), (300, 200))
           if blue_car_selection == 1:
               screen.blit(pygame.transform.scale(black_car, (100, 100)), (600, 200))
           else:
               screen.blit(pygame.transform.scale(blue_car, (100, 100)), (600, 200))
           if red_car_selection == 1:
               screen.blit(pygame.transform.scale(black_car, (100, 100)), (300, 400))
           else:
               screen.blit(pygame.transform.scale(red_car, (100, 100)), (300, 400))
           if purple_car_selection == 1:
               screen.blit(pygame.transform.scale(black_car, (100, 100)), (600, 400))
           else:
               screen.blit(pygame.transform.scale(purple_car, (100, 100)), (600, 400))

           pygame.display.update()

   car_selection()

   #----stop music from playing------

   pygame.mixer.music.stop()

   #----set beginning positions of objects--------------------------------------------

   for i in range(1):
       position = random.randrange(0,3)
       positions = [425, 475, 525]
       rock_xposition = positions[position]
       rock_yvelocity = 1
       rock_type = random.randint(0, 1)
       rock_rect.append([pygame.Rect(rock_xposition, rock_y, 50, 20), rock_yvelocity, rock_xposition, rock_type])

   for i in range(1):
       position = random.randrange(0,3)
       positions = [425, 475, 525]
       barrier_xposition = positions[position]
       barrier_yvelocity = 1
       barrier_type = random.randint(0, 1)
       barrier_rect.append([pygame.Rect(barrier_xposition, barrier_y, 50, 20), barrier_yvelocity, barrier_xposition, barrier_type])

   for i in range(2):
       tree_position = trees_xposition[random.randint(0 ,1)]
       trees_yvelocity = 1
       trees.append([pygame.Rect(tree_position, trees_y, 20, 20), trees_yvelocity, tree_position])

   for i in range(1):
       coins_xposition = random.randrange(450, 550)
       coin_spawnposition = coins_xposition
       coins_yvelocity = 1
       coins_rect.append([pygame.Rect(coins_xposition, coins_y, 20, 20), coins_yvelocity, coin_spawnposition])

   for i in range(1):
       cloud_startposition = -200
       cloud_yposition = random.randrange(0, 100)
       clouds.append([cloud_startposition, cloud_yposition])

   #----game loop--------------------------------------------

   while True:
       clock.tick(60) # restricts the refresh rate, means 60 times per second
       global score_string
       score_string = str(score)
       score_display = TITLE_FONT.render("Score:" + score_string, True, (0, 0, 0))

       player_rect = pygame.Rect(player_xposition, 500, 125, 125)

       player_xposition += player_xchange

       if player_xposition >= 950 or player_xposition <= 0:
           pygame.mixer.music.load('Car-crash-sound-effect.mp3')
           pygame.mixer.music.play(1, 0.0)
           pygame.mixer.music.set_volume(0.5)
           crash_menu()

       #----event handling--------------------------------------------

       for event in pygame.event.get():
           if event.type == QUIT:
               pygame.quit()
               sys.exit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_RIGHT and player_xposition <= 950:
                   player_xchange += 10
               elif event.key == pygame.K_LEFT and player_xposition >= 0:
                   player_xchange += -10
               elif event.key == K_ESCAPE:
                   return
           if event.type == KEYUP:
               if event.key == 275 or event.key == 276:
                   player_xchange = 0

       #----draw background--------------------------------------------

       screen.fill(white)

       for i in range(len(sky)):
           pygame.draw.line(screen, (int(100+i*0.5), int(100+i*0.5), int(255-i*0.5)), (0, sky[i]),(1150,sky[i]), 10)

       for i in range(len(grass)):
           pygame.draw.line(screen, (int(0+0.1*i), int(170-0.2*i), int(50+0.1*i)), (0, grass[i]), (1150, grass[i]), 10)

       pygame.draw.polygon(screen, grey, ((400, 200), (600, 200), (1180, 700), (-180, 700)))

       pygame.draw.line(screen, white, (410, 200), (-104, 700), 5)
       pygame.draw.line(screen, white, (590, 200), (1104, 700), 5)
       pygame.draw.polygon(screen, white, ((499, 200), (501, 200), (510, 700), (490, 700)))

       #----import car selection--------------------------------------------

       global car_list
       car_choice = car_list[4]
       screen.blit(pygame.transform.scale(car_list[car_choice], (150, 150)), (player_xposition, 500))

       #----rock obstacle movement mechanics--------------------------------------------

       for rock in rock_rect:
           if rock[0].y > 800:
               rock_yvelocity = 1
               rock_rect.remove(rock)
               position = random.randrange(0,3)
               positions = [425, 475, 525]
               rock_xposition = positions[position]
               rock_xsize = 1 + int(0.1*rock[0].y)
               rock_ysize = 1 + int(0.1*rock[0].y)
               rock_rect.append([pygame.Rect(rock_xposition, rock_y, rock_xsize, rock_ysize), rock_yvelocity, rock_xposition])

       for rock in rock_rect:
           rock[1] += 0.03
           speed_increase = int((score / 10))
           rock[1] += speed_increase/50
           x_movement = rock[2] - 475
           if x_movement >= 20:
               rock[0].move_ip(rock[1]*0.75, rock[1])
           elif x_movement <= -20:
               rock[0].move_ip(-rock[1]*0.75, rock[1])
           else:
               rock[0].move_ip(0, rock[1])

       for rock in rock_rect:
           if player_rect.colliderect(rock[0]):
               pygame.mixer.music.load('Car-crash-sound-effect.mp3')
               pygame.mixer.music.play(1, 0.0)
               pygame.mixer.music.set_volume(0.5)
               crash_menu()

       for rock in rock_rect:
           rock_yposition = rock[0].y
           rock_xposition = rock[0].x
           rock_xsize = 1 + int(0.2*rock[0].y)
           rock_ysize = 1 + int(0.2*rock[0].y)
           screen.blit(pygame.transform.scale(rock_image, (rock_xsize, rock_ysize)), (rock_xposition, rock_yposition))

       #----barrier obstacle movement mechanics--------------------------------------------

       for barrier in barrier_rect:
           if barrier[0].y > 900:
               barrier_rect.remove(barrier)
               barrier_yvelocity = 1
               position = random.randrange(0,3)
               positions = [425, 475, 525]
               barrier_xposition = positions[position]
               barrier_xsize = 1 + int(0.1*barrier[0].y)
               barrier_ysize = 1 + int(0.1*barrier[0].y)
               barrier_rect.append([pygame.Rect(barrier_xposition, barrier_y, barrier_xsize, barrier_ysize), barrier_yvelocity, barrier_xposition])

       for barrier in barrier_rect:
           barrier[1] += 0.03
           speed_increase = int((score / 10))
           barrier[1] += speed_increase/50
           x_movement = barrier[2] - 475
           if x_movement >= 20:
               barrier[0].move_ip(barrier[1]*0.75, barrier[1])
           elif x_movement <= -20:
               barrier[0].move_ip(-barrier[1]*0.75, barrier[1])
           else:
               barrier[0].move_ip(0, barrier[1])

       for barrier in barrier_rect:
           if player_rect.colliderect(barrier[0]):
               pygame.mixer.music.load('Car-crash-sound-effect.mp3')
               pygame.mixer.music.play(1, 0.0)
               pygame.mixer.music.set_volume(0.5)
               crash_menu()

       for barrier in barrier_rect:
           barrier_yposition = barrier[0].y
           barrier_xposition = barrier[0].x
           barrier_xsize = 1 + int(0.25*barrier[0].y)
           barrier_ysize = 1 + int(0.2*barrier[0].y)
           screen.blit(pygame.transform.scale(barrier_image, (barrier_xsize, barrier_ysize)), (barrier_xposition, barrier_yposition))

       #----coin and mushroom movement mechanics--------------------------------------------

       for coin in coins_rect:
           if coin[0].y > 800:
               counter += 1
               coins_rect.remove(coin)
               coins_xposition = random.randrange(450, 550)
               coin_spawnposition = coins_xposition
               coins_yvelocity = 1
               coin_xsize = 1 + int(0.05*coin[0].y)
               coin_ysize = 1 + int(0.05*coin[0].y)
               coins_rect.append([pygame.Rect(coins_xposition, coins_y, coin_xsize, coin_ysize), coins_yvelocity, coin_spawnposition])

       for coin in coins_rect:
           coin[1] += 0.03
           speed_increase = int((score / 10))
           coin[1] += speed_increase/50
           coin_xmovement = coin[2] - 490
           if coin_xmovement >= 25:
               coin[0].move_ip(coin[1]*0.75, coin[1])
           elif coin_xmovement <= -25:
               coin[0].move_ip(-coin[1]*0.75, coin[1])
           else:
               coin[0].move_ip(0, coin[1])

       for coin in coins_rect:
           if player_rect.colliderect(coin[0]):

               #----set coin sound--------------------------------------------
               if counter % 5 == 1:
                   pygame.mixer.music.load('Mushroom_sound.wav')
                   pygame.mixer.music.play(1, 0.0)
                   pygame.mixer.music.set_volume(0.2)
               else:
                   pygame.mixer.music.load("coin sound.mp3")
                   pygame.mixer.music.play(1, 0.0)
                   pygame.mixer.music.set_volume(0.1)

               #----set coin score--------------------------------------------
               if counter % 5 == 1:
                   score += 5
               else:
                   score += 1
               counter += 1

               #----set coin sizes--------------------------------------------
               coins_rect.remove(coin)
               coins_xposition = random.randrange(450, 550)
               coin_spawnposition = coins_xposition
               coins_yvelocity = 1
               coin_xsize = 1 + int(0.1*coin[0].y)
               coin_ysize = 1 + int(0.1*coin[0].y)
               coins_rect.append([pygame.Rect(coins_xposition, coins_y, coin_xsize, coin_ysize), coins_yvelocity, coin_spawnposition])

       for coin in coins_rect:
           coin_yposition = coin[0].y
           coin_xposition = coin[0].x
           coin_xsize = 5 + int(0.175*coin[0].y)
           coin_ysize = 5 + int(0.15*coin[0].y)
           if counter % 5 == 1:
               screen.blit(pygame.transform.scale(mushroom_image, (coin_xsize, coin_ysize)),(coin_xposition, coin_yposition))
               counter -= 10
           else:
               screen.blit(pygame.transform.scale(coin_image, (coin_xsize, coin_ysize)), (coin_xposition, coin_yposition))

       #----cloud movement mechanics--------------------------------------------

       for cloud in clouds:
           if cloud[0] == 500:
               cloud_xposition = -200
               cloud_yposition = random.randrange(0, 100)
               clouds.append([cloud_xposition, cloud_yposition])
           if cloud[0] > 1100:
               clouds.remove(cloud)

       for cloud in clouds:
           cloud[0] += 1
           screen.blit(pygame.transform.scale(cloud_image, (200, 100)),(cloud[0], cloud[1]))

       #----tree movement mechanics--------------------------------------------

       for tree in trees:
           if tree[0].y > 600:
               trees.remove(tree)
               tree_position = trees_xposition[random.randint(0 ,1)]
               trees_yvelocity = 1
               trees.append([pygame.Rect(tree_position, trees_y, 20, 20), trees_yvelocity, tree_position])

       for tree in trees:
           tree[1] += 0.05
           tree_xmovement = tree[2] - 500
           if tree_xmovement >= 0:
               tree[0].move_ip(tree[1]*2, tree[1])
           else:
               tree[0].move_ip(-tree[1]*2, tree[1])

       for tree in trees:
           tree_xposition = tree[0].x
           tree_yposition = tree[0].y
           tree_xsize = 100 + int(tree[0].y)
           tree_ysize = 100 + int(tree[0].y)
           screen.blit(pygame.transform.scale(tree_image, (tree_xsize, tree_ysize)), (tree_xposition,  tree_yposition))

       #----score update--------------------------------------------

       screen.blit(score_display, (850, 50))

       # Update display
       pygame.display.update()

#main menu function-----------------------------------------------------------------------------------------------------

def main_menu():

   #----import images--------------------------------------------

   background = pygame.image.load("background.jpg")

   logo_image = pygame.image.load("logo.png")
   instructionsbutton_image = pygame.image.load("instructions button.png")
   playgamebutton_image = pygame.image.load("play game.png")
   instructions_blue = pygame.image.load("instructions blue.png")
   playgame_blue = pygame.image.load("play game blue.png")

   #----set positions and Rects--------------------------------------------

   instructions_xposition = 340
   instructions_yposition = 425
   instructions_xsize = 350
   instructions_ysize = 75
   instructions_rect = pygame.Rect(instructions_xposition, instructions_yposition, instructions_xsize, instructions_ysize)

   playgame_xposition = 365
   playgame_yposition = 500
   playgame_xsize = 300
   playgame_ysize = 75
   playgame_rect = pygame.Rect(playgame_xposition, playgame_yposition, playgame_xsize, playgame_ysize)

   #----set selection variables--------------------------------------------

   instructions_selection = 0
   playgame_selection = 0

   #----set main music--------------------------------------------

   music = "car chase music.wav"
   pygame.mixer.music.load(music)
   pygame.mixer.music.play(-1, 0.0)
   pygame.mixer.music.set_volume(0.5)

   #----event handling--------------------------------------------

   while True:
       clock.tick(60)

       for event in pygame.event.get():
           if event.type == QUIT:
               pygame.quit()
               sys.exit()
           elif event.type == MOUSEBUTTONDOWN:
               if instructions_rect.collidepoint(event.pos):
                   show_instructions()
               if playgame_rect.collidepoint(event.pos):
                   play_game()
           elif event.type == MOUSEMOTION:
               if instructions_rect.collidepoint(event.pos):
                   instructions_selection = 1
               else:
                   instructions_selection = 0
               if playgame_rect.collidepoint(event.pos):
                   playgame_selection = 1
               else:
                   playgame_selection = 0

       #----draw instructions and images--------------------------------------------

       screen.fill((0, 0, 0))
       screen.blit(pygame.transform.scale(background, (1000, 700)), (0,0))
       screen.blit(pygame.transform.scale(logo_image, (600, 600)), (200, 50))
       screen.blit(pygame.transform.scale(instructionsbutton_image,(instructions_xsize, instructions_ysize)),(instructions_xposition, instructions_yposition))
       screen.blit(pygame.transform.scale(playgamebutton_image,(playgame_xsize, playgame_ysize)),(playgame_xposition, playgame_yposition))

       #----selection button mechanics--------------------------------------------

       if instructions_selection == 1:
           screen.blit(pygame.transform.scale(instructions_blue, (instructions_xsize, instructions_ysize)),(instructions_xposition, instructions_yposition))
       else:
           screen.blit(pygame.transform.scale(instructionsbutton_image, (instructions_xsize, instructions_ysize)),(instructions_xposition, instructions_yposition))

       if playgame_selection == 1:
           screen.blit(pygame.transform.scale(playgame_blue, (playgame_xsize, playgame_ysize)), (playgame_xposition, playgame_yposition))
       else:
           screen.blit(pygame.transform.scale(playgamebutton_image, (playgame_xsize, playgame_ysize)), (playgame_xposition, playgame_yposition))

       pygame.display.update()

#----start game at main menu--------------------------------------------

main_menu()


