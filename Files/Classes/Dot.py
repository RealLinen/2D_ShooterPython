import pygame; import sys;
from time import * ; from math import * ; from random import * ;

class ObstacleHandler:
    obstacles = {}
    funcs = {}
    def __init__(self, pygame = pygame, screen = pygame.display.set_mode()):
        self.pygame = pygame
        self.Screen = screen
        pass
    def spawnObstacle(self, image, direction):
        if not self.pygame or not self.Screen or not image: return
        screen = self.Screen; pygame = self.pygame; image = pygame.image.load(image);screenTOP = screen.get_height()
        obstacleY = 0;obstacleX = 0;newInt = self.obstacles.__len__() + 1
        self.obstacles[newInt] = { }
        self.obstacles[newInt][1] = obstacleX
        self.obstacles[newInt][2] = obstacleY

        if(direction=="down"):
            obstacleX = randint(9, screen.get_height())
            obstacleY = 0

            self.obstacles[newInt][1] = obstacleX
            self.obstacles[newInt][2] = obstacleY
            def increase(screen = screen, obstacleY = 0, newInt = 0, removeSpeed = 1):
                if (obstacleY >= screen.get_height()): 
                    self.funcs[newInt] = False;self.obstacles[newInt] = False;return;
                obstacleY = obstacleY + removeSpeed
                self.obstacles[newInt][1] = obstacleX;
                self.obstacles[newInt][2] = obstacleY
                return image, self.obstacles[newInt][1], self.obstacles[newInt][2]
            self.funcs[newInt] = increase
        if(direction=="up"):
            obstacleX = randint(0, screen.get_height())
            obstacleY = screen.get_width()

            self.obstacles[newInt][1] = obstacleX
            self.obstacles[newInt][2] = obstacleY
            def increase(screen = screen, obstacleY = 0, newInt = 0, removeSpeed = 1):
                if (obstacleY >= screen.get_height()): 
                    self.funcs[newInt] = False;self.obstacles[newInt] = False;return;
                obstacleY = obstacleY - removeSpeed
                self.obstacles[newInt][1] = obstacleX;
                self.obstacles[newInt][2] = obstacleY
                return image, self.obstacles[newInt][1], self.obstacles[newInt][2]
            self.funcs[newInt] = increase
        pass;