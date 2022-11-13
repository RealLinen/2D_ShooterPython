
class ScrollingBackground:

    def __init__(self, pygame, screenheight, imagefile):

        self.img = pygame.image.load(imagefile)

        self.coord = [0, 0]

        self.coord2 = [0, -screenheight]

        self.y_original = self.coord[1]

        self.y2_original = self.coord2[1]

    def Show(self, surface):

        surface.blit(self.img, self.coord)

        surface.blit(self.img, self.coord2)
    def UpdateCoords(self, speed_y, time):

        distance_y = speed_y * time

        self.coord[1] += distance_y

        self.coord2[1] += distance_y

        if self.coord2[1] >= 0:

            self.coord[1] = self.y_original

            self.coord2[1] = self.y2_original
