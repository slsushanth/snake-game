
import pygame
import time
import random
import pygame_widgets as pw
import pyttsx3

pygame.init()

white = (255,255,255)
yellow =(255,255,102)
black = (0,0,0)
red = (213,50,80)
green = (0,255,0)
blue = (50,153,213)

dis_widht = 600
dis_height = 500

dis = pygame.display.set_mode((dis_widht,dis_height))
nameqqq = pygame.display.set_caption('snake game')

clock = pygame.time.Clock()

snackblock = 10
snackspeed =15

font_style =pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms",35)
smallfont = pygame.font.SysFont('Corbel', 35)



def game_snake (snakeblock,snake_list):
  for x in snake_list:
     pygame.draw.rect(dis,blue,[x[0], x[1],snakeblock,snakeblock])

def message(msg, color):
    message =font_style.render(msg,True,color)
    dis.blit(message,[dis_widht / 8 ,dis_height / 4])

def gameloop():
    gameover = False
    gameclose = False
    button = False


    x1 = dis_widht /2
    y1 = dis_height /2

    x1_change = 0
    y1_change = 0

    snakeList = []
    lengthofthesnake = 1

    foodx = round(random.randrange(0,dis_widht - snackblock) / 10.0) *10.0
    foody = round(random.randrange(0,dis_height - snackblock ) / 10.0)*10.0

    while not gameover:

      while gameclose == True:
         dis.fill(green)
         message('you lose the game press Q for quit and C for play again', red,)

         pygame.display.update()

         for event in pygame.event.get():
             if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_c:
                    gameloop()
                if event.key == pygame.K_q:

                   gameover = True
                   gameclose = False

      for event in pygame.event.get():
          if event == pygame.QUIT:
              gameover = True

          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                 x1_change = - snackblock
                 y1_change = 0

              elif event.key == pygame.K_RIGHT:
                  x1_change = snackblock
                  y1_change = 0

              elif event.key == pygame.K_UP:
                  y1_change = -snackblock
                  x1_change = 0

              elif event.key == pygame.K_DOWN:
                  y1_change  = snackblock
                  x1_change = 0

      if x1 >= dis_widht or x1 < 0 or y1 >= dis_height or y1 < 0:
          gameclose = True

      x1 += x1_change
      y1 += y1_change
      dis.fill(black)
      pygame.draw.rect(dis,green,[foodx,foody,snackblock,snackblock])
      snackhead = []
      snackhead.append(x1)
      snackhead.append(y1)
      snakeList.append(snackhead)
      if len(snakeList)> lengthofthesnake:
         del snakeList[0]

      for X in snakeList[:-1]:
         if  X == snackhead:
            gameclose = True


      game_snake(snackblock,snakeList   )

      pygame.display.update()
      if  x1 ==foodx and y1 == foody:
         foodx = round(random.randrange(0,dis_widht -snackblock) / 10.0)*10.0
         foody = round(random.randrange(0,dis_height - snackblock)/ 10.0)* 10.0
         lengthofthesnake += 1

      clock.tick(snackspeed)


    pygame.quit()
    quit()

gameloop()




