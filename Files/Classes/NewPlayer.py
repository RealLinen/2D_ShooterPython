import pygame
import math

class GamePlayer:
    playerX = 0;playerY = 330
    def __init__(self, pygame = pygame, screen = pygame.display.set_mode(), playerImage = ""):
        self.Player = pygame.image.load(playerImage)
        self.Screen = screen
        self.pygame = pygame
        self.playerX = screen.get_width()/2.5
        self.updatePlayer()
        
    def special_collide(coinX, coinY, playerX, playerY):
        distance_square = (math.pow(coinX - playerX, 2) + math.pow(coinY - playerY, 2))**.5
        if distance_square <= 27: return True
        else:
            return False
    def SpecialCollideWith(self, objX, objY):
        if not self.Player or not self.Screen: return;
        return self.special_collide(objX, objY, self.playerX, self.playerY)
    def CollideWith(self, objX, objY):
        subY = abs(self.playerY - objY)
        subX = abs(self.playerX - objX)
        if(subX < 27 and subY < 17):
            return True

    def updateY(self, updateBy = 1):
        if not self.Player or not self.Screen: return;
        height = self.Screen.get_height() - (self.playerY+updateBy) 
        if(height > self.Screen.get_height() or height < 60): return;
        self.playerY+=updateBy


    def updateX(self, updateBy = 1):
        if not self.Player or not self.Screen: return;
        width = self.Screen.get_width() - (self.playerX+updateBy) 
        if(width > self.Screen.get_width() or width < 71): return;
        self.playerX+=updateBy


    def setX(self, to = 1):
        if not self.Player or not self.Screen: return;
        width = self.Screen.get_width() - (self.playerX+to) 
        if(width > self.Screen.get_width() or width < 71): return;
        self.playerX = to


    def setY(self, to = 1):
        if not self.Player or not self.Screen:
            return;
        height = self.Screen.get_height() - (to) 
        if(height > self.Screen.get_height() or height < 60): return;
        self.playerY = to


    def updatePlayer(self):
        if not self.Player or not self.Screen:
            return;
        self.Screen.blit(self.Player, (self.playerX, self.playerY))