import pygame
import random

pygame.init()
pygame.font.get_init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

black = ( 0 , 0 , 0 , 0)

road = pygame.image.load("road.png").convert_alpha()
road = pygame.transform.scale(road, (800,600))

score = 0

font1 = pygame.font.SysFont(None,200)
fontscore = pygame.font.SysFont(None,30)
font1_tex = font1.render("GAME OVER",True,"red")
font_scoretex =fontscore.render("SCORE : " + str(score),True,"red")
font1_sur = font1_tex.get_rect()
font1_sur.center = (400,300)
font2_sur = font_scoretex.get_rect()
font2_sur.center = (50,30)

right = False

changing = 10
cor_x = 400
cor_y = 380

scroll = 0
scroll_speed = 10
acceleration = 0.0015

left = right = False

ACCELRATION = pygame.USEREVENT + 1
pygame.time.set_timer(ACCELRATION,5000)

player = pygame.image.load("our_car.png")
player = pygame.transform.scale(player,(90,200))
player_rect = pygame.Rect((cor_x,cor_y,90,200))

enemies = pygame.image.load("enemy_car.png")
enemies = pygame.transform.scale(enemies,(90 * 5 + 9 ,200))
enemy_pack = []
draw_enemies = False

def draw_enemy(speed,draw_enemies):
    if draw_enemies:
        car_index = random.randrange(0,5)
        x = random.randrange(0,4)
        y = -200
        enemy_pack.append(list((enemies,[x * 116 +180 ,y ],(car_index * 93,0,90,200),(pygame.Rect(x * 116 + 180 +20,y+16,90-20,200 -8 ))) ))
        draw_enemies = False
    for x in enemy_pack:
        x[1][1] += scroll_speed
        x[3].y = x[1][1]
        screen.blit(x[0],(x[1][0] , x[1][1] ),x[2])
        if x[1][1] > SCREEN_HEIGHT:
             enemy_pack.remove(x)
    return draw_enemies

def draw_car(x,y):
    screen.blit(player,(x,y))

def draw_road(scroll):
    screen.fill(black)
    for x in range(scroll // SCREEN_HEIGHT + 3):
        screen.blit(road,(0, - SCREEN_HEIGHT * x + scroll))

ENEMY_SPAWNING = pygame.USEREVENT + 1
pygame.time.set_timer(ENEMY_SPAWNING,scroll_speed *150)

run = True
while run:
    draw_road(int(scroll) )
    
    draw_car(cor_x,cor_y)
    
    draw_enemies = draw_enemy(int(scroll_speed),draw_enemies )
    
    screen.blit(font_scoretex,font2_sur)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.type == player_rect.colliderect:
                pass
        if event.type == ENEMY_SPAWNING:
            pygame.time.set_timer(ENEMY_SPAWNING,int(scroll_speed * 600))
            draw_enemies = True
    for x in enemy_pack:
        if x[3].colliderect(player_rect):
            pygame.display.flip()
            pygame.time.delay(2000)
            run = False
    if left and cor_x > 130 :
        cor_x -= changing
    if right  and cor_x < 580:
        cor_x  += changing 
    player_rect.x = cor_x
    
    scroll += scroll_speed
    scroll_speed += acceleration
    score  += 0.2
    pygame.display.flip() 
    
    clock.tick(60)
    print(int(score))
pygame.quit()