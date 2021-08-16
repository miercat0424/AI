import pygame , pymunk , sys

from pymunk.shapes import Circle

def create_apple(space,pos) :
    body = pymunk.Body(1,               # MASS
                       100,             # Inerhit
                       body_type = pymunk.Body.DYNAMIC) # Static or Dynamic or Kinetic

    # body.position = (400,0)             # how body looks
    body.position = pos                 # how body looks // click on the screen becomes position
    shape = pymunk.Circle(body , 65)    # (put the physics of body , radius)
    space.add(body,shape)               # add a body with shpae in our virtual space 

    return shape                        # to make visible we have to set return shpae

def draw_apples(apples) : 
    for apple in apples : 

        pos_x = int(apple.body.position.x) 
        pos_y = int(apple.body.position.y)
        # // Warning those variables are from World variable 
        apple_rect = apple_surface.get_rect(center = (pos_x,pos_y)) # make a imgae object with positions
        screen.blit(apple_surface,apple_rect)                       # add on my screen

        # pygame.draw.circle(screen,              # draw on screen
        #                    (0,0,0),             # color (black)
        #                    (pos_x,pos_y),       # center of circle -> shape
        #                    80)                  # radius 

# ------------------------------------------------------------------------------------------------------------------

def static_ball(space,pos) :    # Making a Static body which is fixed on screen

    body = pymunk.Body(body_type = pymunk.Body.STATIC)  # 1. Create Body
    # body.position = (500,500)                           # 2. Set where it is
    body.position = pos                       
    shape = pymunk.Circle(body,50)                      # 3. Make shape how it looks // size
    space.add(body,shape)                               # 4. Add to screen

    return shape                                        # 5. return to shape to see 

def draw_static_ball(balls) :

    for ball in balls : 

        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen,(210,120,10),(pos_x,pos_y),50)




pygame.init()                                       # initiating pygame
screen  = pygame.display.set_mode((800,800))        # creating the display surface
clock   = pygame.time.Clock()                       # creating the game clock
space   = pymunk.Space()

space.gravity = (0,500)                              # Horizental , Vertical Gravity setting

apple_surface = pygame.image.load("pictures/apple_red.png")  # load image from pygame

apples = []                         # create empty list
# apples.append(create_apple(space))  # 

balls = []
balls.append(static_ball(space,(500,500)))
balls.append(static_ball(space,(250,400)))

while True : # Game loop

    for event in pygame.event.get():    # checking for user input
        if event.type == pygame.QUIT :  # input to close the game
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN :           # if we click mouse then create apples
            apples.append(create_apple(space,event.pos))    # set our create_apple func on screen

    screen.fill((217,217,217))          # background color

    draw_apples(apples)
    draw_static_ball(balls)

    space.step(1/50)                    # 0.02 sec
    pygame.display.update()             # rendering the frame
    clock.tick(120)                     # limiting the frames per second to 120

