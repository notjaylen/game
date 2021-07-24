import pygame
#have to initialize pygame! ****
pygame.init()


#create screen window              WID  HT
screen = pygame .display.set_mode((800,600))

#Game Window Title and Icon
pygame.display.set_caption("a really good title")
icon = pygame.image.load('superhero.png')
pygame.display.set_icon(icon)

#creating each player image

playerOneImg = pygame.image.load('donatello.png')
playerX = 370
playerY = 480
playerSpeedX = 0
playerSpeedY = 0


def player(x,y):
    #draw on screen after loading image
    screen.blit(playerOneImg,(x,y))

#create game loop
running = True
while running:
    #                R G B
    # screen.fill((255,0,0))


    #check all events
    for event in pygame.event.get():
        #check if program has been exited
        if event.type == pygame.QUIT:
            running = False

        #check <-- or --> key pressed
        if event.type == pygame.KEYDOWN:
            #LEFT
            if event.key == pygame.K_a:
                playerSpeedX = -0.1
            #RIGHT
            if event.key == pygame.K_d:
                playerSpeedX = 0.1
            #UP
            if event.key == pygame.K_w:
                playerSpeedY = -0.1
            #DOWN
            if event.key == pygame.K_s:
                playerSpeedY = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                playerSpeedX = 0
            if event.key == pygame.K_d:
                playerSpeedX = 0
            if event.key == pygame.K_w:
                playerSpeedY = 0
            if event.key == pygame.K_s:
                playerSpeedY = 0



    playerX += playerSpeedX
    playerY += playerSpeedY

    if playerX <= 0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768
    if playerY <= 0:
        playerY = 0
    elif playerY >= 568:
        playerY = 568
    player(playerX,playerY)
    #update display
    pygame.display.update()