import pygame
import math
from planet import Planet

pygame.init()

WIDTH, HEIGHT = 1000, 1000
Window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

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