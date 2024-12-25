import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(screen, white, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt