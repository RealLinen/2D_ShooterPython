import pygame
class GamePlayer:
    playerX = 0;playerY = 0
    def __init__(self, pygame = pygame, screen = pygame.display.set_mode(), playerImage = ""):
        self.Player = pygame.image.load(playerImage)
        self.Screen = screen
        pass 
    def updateY(self, updateBy = 1):
        if not self.Player or not self.Screen:
            return;
        self.playerY+=updateBy

    def updateX(self, updateBy = 1):
        if not self.Player or not self.Screen:
            return;
        self.playerX+=updateBy

    def setX(self, to = 1):
        if not self.Player or not self.Screen:
            return;
        self.playerX = to

    def setY(self, to = 1):
        if not self.Player or not self.Screen:
            return;
        self.playerY = to

    def updatePlayer(self):
        if not self.Player or not self.Screen:
            return;
        self.Screen.blit(self.Player, (self.playerX, self.playerY))