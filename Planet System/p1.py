import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 1000
Window = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Planet Simulation")

def main():
    run = True