import sys
from asteroidfield import AsteroidField
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot


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
    shots = pygame.sprite.Group()

    # Add to Groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # Instanciate
    AsteroidField()
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        color = (0, 0, 0)
        screen.fill(color)
        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            for shot_in_air in shots:
                if asteroid.collision(shot_in_air):
                    asteroid.kill()
                    shot_in_air.kill()

            if asteroid.collision(ship):
                print("Game Over!")
                sys.exit()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = ticker.tick(60) / 1000


if __name__ == "__main__":
    main()
