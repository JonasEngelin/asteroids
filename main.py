import pygame
from constants import *
import player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ticker = pygame.time.Clock()
    dt = 0

    ship = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        color = (0, 0, 0)
        screen.fill(color)
        ship.draw(screen)
        ship.update(dt)
        pygame.display.flip()
        dt = ticker.tick(60) / 1000


if __name__ == "__main__":
    main()
