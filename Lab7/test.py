import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
 
player = pygame.Rect(300,250,50,50)
luffy = pygame.image.load('Lab7\luffy.jpg')

luffyy = pygame.transform.scale(luffy,(80,100))
def luffy_display(x,y):
    screen.blit(luffyy,(x,y))

omar_murunbok = False
run = True
clock = pygame.time.Clock()
luffy_x = 300
luffy_y = 400 
while run :
    screen.fill(( 0 ,0 ,0 )) 
     
    pygame.draw.rect(screen,(255,125,215), player)
    key = pygame.key.get_pressed()
    
    if key[pygame.K_a] == True :
        player.x -= 1
    elif key[pygame.K_d] == True :
        player.move_ip(1,0)
    elif key[pygame.K_w] == True :
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True :
        player.move_ip(0,1)
    elif key[pygame.K_r] == True :
        player.x = 400
        player.y = 300
    elif key[pygame.K_o] == True and key[pygame.K_p] == True :
        luffy_x = 350
        luffy_y = 400
        omar_murunbok = True
    elif key[pygame.K_LEFT] == True and omar_murunbok:
        luffy_x -= 1
    elif key[pygame.K_RIGHT] == True and omar_murunbok:
        luffy_x += 1
    elif key[pygame.K_UP] == True and omar_murunbok:
        luffy_y -= 1
    elif key[pygame.K_DOWN] == True and omar_murunbok:
        luffy_y += 1
    
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False
    luffy_display(luffy_x,luffy_y)
    pygame.display.update()
    
    clock.tick(60)
            
pygame.quit()