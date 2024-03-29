import pygame
import datetime
import math

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

WHITE = (255,255,255)
GREY = (105,105,105)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.image.load("clock.png")
clock = pygame.transform.scale(screen,(600,600))

center = (300,300)

def draw_clock(hour_cor,minute_cor,second_cor):
    pygame.draw.circle(screen,GREY,center,300)
    pygame.draw.circle(screen,WHITE,center,280)
    pygame.draw.circle(screen,BLACK,center,10) 
    pygame.draw.line(screen,RED,(300,300),(hour_cor),15)
    pygame.draw.line(screen,BLUE,(300,300),(minute_cor),9)
    pygame.draw.line(screen,BLACK,(300,300),(second_cor),5)
    
   
run = True
while run :
    screen.fill(BLACK)
    time = datetime.datetime.now()
    draw_clock( ( 300 + math.sin(math.pi * time.hour/6) * 220 , 300 - math.cos(math.pi*time.hour/6) * 220 ),
                ( 300 + math.sin(math.pi * time.minute/30) * 270 , 300 - math.cos(math.pi * time.minute/30) * 270 ),
                 ( 300 + math.sin(math.pi * time.second/30) * 300 , 300 - math.cos(math.pi * time.second/30) * 300 ))    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
    
pygame.quit()