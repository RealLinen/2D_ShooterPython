import pygame ; import os ; import sys ; 
from pygame.locals import *
from Files.Classes.ScrollingBackground import ScrollingBackground ; from Files.Classes.NewPlayer import GamePlayer
#==============================================#
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 480))
pygame.mouse.set_visible(0)
pygame.display.set_caption('Space Age Game')
#==============================================#
StarField = ScrollingBackground(pygame, screenheight, "Files/Images/background.png")
Player = GamePlayer(pygame, screen, os.path.join("Files/Images/maincharacter.png"))
#==============================================#
while True: 
    clock.tick(60)
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #======================== Drawing new Items


    #======================== Drawing new Items
    Player.updatePlayer()
    pygame.display.update()