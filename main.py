import pygame ; import os ; import sys ; from Files.Classes.ScrollingBackground import ScrollingBackground ;
pygame.init();
#==============================================# Setting up game
clock = pygame.time.Clock()
screenwidth, screenheight = (480, 640)
screen = pygame.display.set_mode((screenheight, screenwidth))
pygame.display.set_caption('2D Shooter Game')
#==============================================#
background = pygame.image.load(os.path.join("Files/Images/background.png"))
player = pygame.image.load(os.path.join("Files/Images/maincharacter.png"))
#==============================================#
playerPositionData = { };playerPositionData["X"] = 10; playerPositionData["Y"] = 100
#==============================================#
StarField = ScrollingBackground(screenheight, "Files/Images/background.png")

#==============================================#
while True:
    KeysDown = pygame.key.get_pressed();clock.tick(60);
    time = clock.tick(60)/1000.0

    StarField.UpdateCoords(250, time)
    StarField.Show(screen)

    screen.blit(player, ( playerPositionData["X"], playerPositionData["Y"] ))

    if KeysDown[pygame.K_w]:
        playerPositionData["Y"]+=1
    if KeysDown[pygame.K_s]:
        playerPositionData["Y"]-=1
    #======================== Drawing new Items
    pygame.display.update()