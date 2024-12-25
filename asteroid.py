import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(screen, white, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        part_one = self.velocity.rotate(random_angle)
        part_two = self.velocity.rotate(-random_angle)
        # print(f"{part_one}, {part_two}")
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_one.velocity = part_one * 1.2
        new_asteroid_two.velocity = part_two * 1.2
