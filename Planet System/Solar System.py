import pygame
from Planets import Planet

pygame.init()

WIDTH, HEIGHT = 1300, 1000
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)

Window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

def main():
    run = True
    clock = pygame.time.Clock()

    Sun = Planet(0, 0, 40, YELLOW, 1.98892 * 10**30)
    Sun.sun = True

    Earth = Planet(-1*Planet.AU, 0, 20, BLUE, 5.9742 * 10**24)
    Earth.y_vel = 29.783 * 1000

    # Moon = Planet(-1.02*Planet.AU, 0, 5, WHITE, 7.4 * 10**22)
    # Moon.y_vel = 30 * 1000

    Mars = Planet(-1.524*Planet.AU, 0, 10, RED, 6.39 * 10**23)
    Mars.y_vel = 24.4 * 1000

    planets = [Sun, Earth, Mars]

    while run:
        clock.tick(60)
        Window.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.Draw(Window)

        pygame.display.update()

    pygame.quit()

main()