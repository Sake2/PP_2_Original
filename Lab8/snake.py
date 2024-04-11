import pygame
import random


#initialize the pygames
pygame.init()
pygame.font.get_init()

colours = [ (255,255,0),
            (255,0,0),
            (0,0,255),
            (255,255,255),
            (110,0,0),
            (165,45,15),
                      
    ]

# SCREEN SIZES
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Colours
WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0,0,0)
GREY = pygame.Color(200,200,200)
GREEN = pygame.Color(0,255,0)
RED = pygame.Color(255,0,0)

# FPS 
speed = 10
FPS = pygame.time.Clock()

#direction
direction = change = 'RIGHT'

#food loose
food = True
special_food = False
loose = False

#making screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Snake")

#score
score  = 0

# TExts
font1 = pygame.font.SysFont(None,50) 
font2 = pygame.font.SysFont(None,100)
text1 = font1.render("SCORE : " + str(score),True,RED )
text2 = font2.render("GAME OVER" ,True,RED)
text_sur = text1.get_rect()
text2_sur = text2.get_rect()
text_sur.center = (100 , 30)
text2_sur.center = (400,300)


#making snake
head_defolt = [105,150]
head = [105,150];
defolt = [[105, 150 ],
          [90 , 150],
          [75 , 150],
          [60, 150]
          ]
snake_coor = defolt.copy()

#fruit creating
fruit_pos = [random.randrange(1,SCREEN_WIDTH-1)//15 *15 ,random.randrange(1 ,SCREEN_HEIGHT-1) // 15 *15]
fruit_weight = random.randrange(5,10)
specific_chance = 0
SPECIFIC_EVENT = pygame.USEREVENT + 1
disapear = False

pygame.time.set_timer(SPECIFIC_EVENT,1000)
process = True
while process:
    #cjanging score and bliting it
    text1 = font1.render("SCORE : " + str(score),True,RED )
    screen.blit(text1,text_sur)

    #after loosing
    if loose :
        screen.fill(BLACK)
        screen.blit(text2,text2_sur)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                process = False
            #to restart game
            mouse_button = pygame.mouse.get_pressed()
            if mouse_button[0]:
                loose = False
                score = 0
                speed = 10
                #seting defolt atributes
                snake_coor = defolt.copy()
                head = head_defolt.copy()
                direction =change= "RIGHT"
        continue
        
    #upgrade display event
    pygame.display.flip()
    
    
    # inputing keybord
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process = False
        #seting direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT : 
                change = "RIGHT"
            elif event.key == pygame.K_LEFT :
                change = "LEFT"
            elif event.key == pygame.K_UP :
                change = "UP"
            elif event.key == pygame.K_DOWN:
                change = "DOWN"
        if special_food and event.type == SPECIFIC_EVENT:
            if not disapear :
                disapear = True
                pygame.time.set_timer(SPECIFIC_EVENT,4000)
            else :
                food = False
                special_food = False
                fruit_weight = random.randrange(5,10)
                pygame.time.set_timer(SPECIFIC_EVENT,1000)
            
    # change direction 
    if direction != "UP" and change == "DOWN":
        direction = "DOWN"
    elif direction != "DOWN" and change == "UP":
        direction = "UP"
    elif direction != "LEFT" and change == "RIGHT":
        direction = "RIGHT"
    elif direction != "RIGHT" and change == "LEFT":
        direction = "LEFT"
        
    #moving
    if direction == "UP":
        head[1] -= 15
    elif direction == "DOWN":          
        head[1] += 15
    elif direction == "RIGHT" :
        head[0] += 15
    elif direction == "LEFT":
        head[0] -= 15
        
    #growing
    snake_coor.insert(0,list(head))
    if not food : # if you eat fruit 
        while  fruit_pos in snake_coor : #spawn new fruit
            fruit_pos = [random.randrange(1,SCREEN_WIDTH-1) // 15 *15  ,random.randrange(1,SCREEN_HEIGHT-1) //15 *15 ]  
        specific_chance = random.randrange(5,10) 
        speed += 1
        score += fruit_weight
        fruit_weight = random.randrange(5,10)
        disapear = False
        if specific_chance == 6 :
             special_food = True
             fruit_weight = 40
        
        
    else :
        snake_coor.pop()
       
    food = True
    if head[0] == fruit_pos[0] and head[1] == fruit_pos[1] and not special_food:
        food = False
    if special_food and  head[0] == fruit_pos[0]  and head[1] == fruit_pos[1] :  
        special_food = False
        food = False
    
    #losing conditions
    if not (0 <= head[0] <= SCREEN_WIDTH and 0 <= head[1] < SCREEN_HEIGHT) :
        loose = True
    if head in snake_coor[1:]:
        loose = True
     # filling screen 
    screen.fill(BLACK)
    
    # drawing snake and fruit
    for part in snake_coor:
        pygame.draw.rect(screen, GREEN,pygame.Rect(part[0], part[1],15,15) )
    if not special_food and fruit_weight != 40 :
        pygame.draw.rect(screen,colours[fruit_weight - 4],pygame.Rect(fruit_pos[0], fruit_pos[1],15,15))   
    else :
        pygame.draw.rect(screen,colours[0],pygame.Rect(fruit_pos[0] , fruit_pos[1] ,15,15))
    # seting up fps or speed of snake
    FPS.tick(speed)
    
pygame.quit()



