import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from  logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        updatable.update(dt)
        asteroids.update(dt)
        asteroid_field.update(dt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
