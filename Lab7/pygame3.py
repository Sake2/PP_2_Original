import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

ball = pygame.Rect(360,400,50,50)
clock = pygame.time.Clock()

run = True
while run :
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(255,0,0),(ball.x,ball.y),25)
    key = pygame.key.get_pressed()
    
    if key[pygame.K_LEFT] == True and ball.x >= 40:
        ball.x -= 20;
    elif key[pygame.K_RIGHT] == True and ball.x <= 760:
        ball.x += 20;
    elif key[pygame.K_UP] == True and ball.y >= 40:
        ball.y -= 20;
    elif key[pygame.K_DOWN] == True and ball.y <= 560:
        ball.y += 20;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    clock.tick(60)
    pygame.display.flip()
    
pygame.quit()
    