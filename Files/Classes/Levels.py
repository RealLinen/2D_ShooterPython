import math;
class Levels: # Obstacles, ObstacleImage, Speed, ... || more soon
    Levels = {}
    def __init__(self):
        pass;
    def getTable(self):
        return Levels
    def get(self, int):
        return self.Levels[(int or 1)]
    def add(self, int, v):
        self.Levels[(int or 1)] = (v or {})
        return True