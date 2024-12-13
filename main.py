from asteroidfield import AsteroidField
import pygame
from constants import *
from player import Player
from asteroid import Asteroid


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ticker = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Add to Groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    # Instanciate
    AsteroidField()
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        color = (0, 0, 0)
        screen.fill(color)
        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = ticker.tick(60) / 1000


if __name__ == "__main__":
    main()
