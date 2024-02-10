import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 1000
Window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

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
         


def main():
    run = True
    clock = pygame.time.Clock()

    SUN = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    SUN.sun = True

    planets = [SUN]

    while run:
        clock.tick(60)
        # Window.fill(WHITE)
        #pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.Draw(Window)

        pygame.display.update()

    pygame.quit()

main()