import pygame ; import os ; import sys ; from time import * ; from math import * ; from random import * ;
from pygame.locals import *;from pygame import *;
from Files.Classes.ScrollingBackground import ScrollingBackground ; from Files.Classes.NewPlayer import GamePlayer ; from Files.Classes.Dot import ObstacleHandler; from Files.Classes.Levels import Levels
#==============================================#
pygame.init();clock = pygame.time.Clock()
screenwidth, screenheight, framerate = (500, 400, 120)
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.mouse.set_visible(1);pygame.display.set_caption('Space Age Game')
#==============================================#
Obstacles = ObstacleHandler(pygame, screen)
Background = ScrollingBackground(pygame, screenheight, "Files/Images/background.png")
Player = GamePlayer(pygame, screen, "Files/Images/maincharacter.png")
Player.increaseYBy = 5;Player.increaseXBy = 5;Levels = Levels();
#==============================================#
def getCount(t,NotTrueThenRemove=False):
	count=0
	for i in t:
		value=t[i]
		if NotTrueThenRemove:
			if value:count+=1
		elif value is not None:count+=1
	return count
###########################################################
def StartGame():
    currentLevel, passedItems, gameOver, increaseDivisionBy = 1, 0, False, 2;
    Levels.add(currentLevel, [ 10, "Files/Images/dot.png", 1 ])
    LevelDetails = Levels.get(currentLevel)
    pickedSpeed = 5

    while (gameOver is False): 
        clock.tick(framerate);time = clock.tick(framerate)/1000.0;LevelDetails = Levels.get(currentLevel);mouseX, mouseY = pygame.mouse.get_pos();Keys=pygame.key.get_pressed()
        for event in pygame.event.get():   
            if event.type == pygame.QUIT: sys.exit()
        if Keys[K_a]: Player.updateX(-Player.increaseXBy)
        if Keys[K_d]: Player.updateX(Player.increaseXBy)
        if(currentLevel>1):
            pass
            #print(LevelDetails[0], getCount(Obstacles.obstacles, True), (LevelDetails[2] or 2))
        #if Keys[K_w]: Player.updateY(-Player.increaseXBy)
        #if Keys[K_s]: Player.updateY(Player.increaseXBy)
        #======================== Drawing new Items
        if passedItems >= LevelDetails[0]:
            currentLevel+=1
            iconPath = (os.path.exists("Files/Images/dot"+str(currentLevel)+".png") and "Files/Images/dot"+str(currentLevel)+".png" or "Files/Images/dot.png")
            Levels.add(currentLevel, [ randint(LevelDetails[0]+5, LevelDetails[0]*2), iconPath, randint(LevelDetails[2], LevelDetails[2]+1) ])
            passedItems = 0;Obstacles.obstacles = {};Obstacles.funcs = {};increaseDivisionBy+=.5;pickedSpeed+=randint(1, 3)
            continue;
        if getCount(Obstacles.obstacles, True) < (LevelDetails[2] or 1):
            Obstacles.spawnObstacle((LevelDetails[1] or "Files/Images/dot.png"), "down")
        #======================== Ending
        Background.UpdateCoords(100, time);Background.Show(screen);Player.updatePlayer();
        for i in Obstacles.funcs:
            file = Obstacles.funcs[i];
            file2 = Obstacles.obstacles[i];
            if (not file or not file2): 
                if(not Obstacles.funcs[i]=="yes"):
                    Obstacles.funcs[i] = "yes"
                    passedItems+=1
                continue

            try:
                surface, x1, y2 = file(screen, file2[2], i, pickedSpeed)
                if(Player.CollideWith(x1, y2)): #Game Over
                    gameOver = True
                    break;
                screen.blit(surface, (x1, y2))
            except:
                pass;

        pygame.display.flip()
    ############################################
    print("Game over!")
    

###############################################################
###############################################################
###############################################################
###############################################################
StartGame()