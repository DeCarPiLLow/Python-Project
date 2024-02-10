import pygame
import math

WIDTH, HEIGHT = 1000, 1000
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

class Planet:
    AU =  149.6e6*1000
    G = 6.67428e-11
    SCALE = 250/AU  #1 AU -> 100px
    TIMESTEP = 3600*24 # 1-DAY

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def Draw(self, win):
        x = self.x * self.SCALE + WIDTH/2
        y = self.y * self.SCALE + HEIGHT/2
        pygame.draw.circle(win, self.color, (x, y), self.radius)