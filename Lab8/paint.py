import pygame


pygame.init()

colours = [ (255,0,255),
            (102,0,0),
            (153,0,0),
            (204,0,0),
            (255,102,102),
            (254,104,104),
            (51,25,0),
            (254,28,108),
            (0,255,0),
            (70,0,0),
            (255,255,0),
            (0,0,255),
            (0,255,255),
            (160,160,160),
            (140,0,140),
            (255,0,0),
            (0,0,0),
    ]
buttons = []

WHITE = (255,255,255)
GREY2 = (160,160,160)
GREY = (140,140,140)
RED = (255,0,0)
BLACK = (0,0,0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
MARGIN_TOP = 100

l = 3
x = 2
size = 21

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT+MARGIN_TOP))
pygame.display.set_caption("Paint")

eraser = 0
rect_button = pygame.Rect(1,1,40,40)
circle_button = pygame.Rect(45,1,40,40)
eraser_button = pygame.Rect(180,1,40,40)
triangle_button = pygame.Rect(70,1,40,40)
eq_triangle_button = pygame.Rect(115,1,40,40)
for i in range(len(colours)):
    buttons.append(pygame.Rect(SCREEN_WIDTH - l - (i // 4 + 1) * size -  (i // 4) * x, l + i % 4 * (x + size),size,size))

curent_color = "red"
curent_shape = "rect"
pos = (0,100)
width = 10
height = 10
is_draw = False
coor = [[0,0],[0,0]]
nup = ndown = nleft = nright = True

def draw(shape,colur,cor,width,height,coor):
    if shape == "rect":
        pygame.draw.rect(screen,colur,pygame.Rect(cor[0],cor[1],width,height))
    if shape == "circle": 
        pygame.draw.circle(screen,colur,(cor[0],cor[1]),width//2)
    if shape == "triangle":
        pygame.draw.polygon(screen,colur,([cor[0],cor[1]],[coor[0][0],coor[0][1]],[coor[1][0],coor[1][1]]))
    if shape == "eq_triangle":
        pygame.draw.polygon(screen,colur,([ cor[0] - width // 2  , cor[1]+ int( width // 2  * ( 3 ** 0.5))] , [cor[0]  , cor[1] - width // 2  // 3], [cor[0] + width // 2 ,cor[1]+ int( width // 2  * ( 3 ** 0.5)) ] )) 


screen.fill(WHITE)
run = True
while run : 
    pygame.draw.rect(screen,'grey',(0,0,SCREEN_WIDTH,MARGIN_TOP))
    for i in range(len(colours)):
        pygame.draw.rect(screen,colours[i],buttons[i])
    
    if "rect" == curent_shape:
        pygame.draw.rect(screen,curent_color,(1,1,40,40))
    else :
        pygame.draw.rect(screen,'white',(1,1,40,40))
    if "circle" == curent_shape:
        pygame.draw.circle(screen,curent_color,(65,21),20)
    else :
        pygame.draw.circle(screen,"white",(65,21),20)  
    if eraser != 0 :
        pygame.draw.rect(screen,'grey',(180,1,40,40))
        pygame.draw.rect(screen,"red",(180,1,40,40),3)
    else :
        pygame.draw.rect(screen,'white',(180,1,40,40))
    if curent_shape == 'triangle':
        pygame.draw.polygon(screen,curent_color,([85,40],[105,1],[125,41]))
    else :
        pygame.draw.polygon(screen,"white",([85,40],[105,1],[125,41]))
    if curent_shape == "eq_triangle":
        pygame.draw.polygon(screen,curent_color,([128,40],[148,1],[168,41]))  
    else:
        pygame.draw.polygon(screen,'white',([128,40],[148,1],[168,41]))  
        
    for event in pygame.event.get()  :
        if event.type == pygame.QUIT:
            run = False
        pos = pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()
        if mouse_button[0]:
            if mouse_button[0] and pos[1] > 100 :
                is_draw = True
            elif mouse_button[0] and rect_button.collidepoint(pos):
                curent_shape = 'rect'
            elif mouse_button[0] and circle_button.collidepoint(pos) :
                curent_shape = 'circle'
            elif mouse_button[0] and eraser_button.collidepoint(pos) :
                if eraser == 0:
                    eraser = curent_color
                else :
                    eraser = 0
            elif mouse_button[0] and triangle_button.collidepoint(pos):
                curent_shape = "triangle"
            elif mouse_button[0] and eq_triangle_button.collidepoint(pos):
                curent_shape = "eq_triangle"
            for i in range(len(colours)):
                if mouse_button[0] and buttons[i].collidepoint(pos):
                    curent_color = colours[i]
            if curent_shape == "triangle" and is_draw:
                is_draw = False
                if coor[0] == [0,0]:
                    coor[0] = pos
                elif coor[1] == [0,0]:
                    coor[1] = pos
                else :
                    is_draw = True  
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and nup :
                width += 10
                nup = False
            if event.key == pygame.K_DOWN and ndown :
                width -= 10
                ndown = False
            if event.key == pygame.K_LEFT and nleft :
                height -= 10
                nleft = False
            if event.key == pygame.K_RIGHT and nright :
                height += 10
                nright = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP :
                nup = True
            elif event.key == pygame.K_DOWN :
                ndown = True
            elif event.key == pygame.K_RIGHT :
                nright = True
            elif event.key == pygame.K_LEFT :
                nleft = True
                
                
            
    if is_draw:
        if eraser != 0 :
            draw(curent_shape,WHITE,pos,width,height,coor)     
        else :
            draw(curent_shape,curent_color,pos,width,height,coor)
            coor[0] = [0,0]
            coor[1] = [0,0]
        is_draw = False 
                 
    pygame.display.flip()
pygame.quit()
quit

