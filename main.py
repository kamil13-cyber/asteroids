import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from  logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot


def main() -> None:
    # Initialize Pygame and set up the display
    pygame.init()

    # Set up the display and clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create the player at the center of the screen
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    # Create sprite groups for updatable and drawable objects
    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    dt = 0.0

    # Set the containers for the Player and Asteroid classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Create an instance of the AsteroidField to manage asteroid spawning and updates
    asteroid_field = AsteroidField()

    while True:
        # Update the game state
        log_state()
        updatable.update(dt)
        asteroids.update(dt)
        asteroid_field.update(dt)

        # Check for collisions between the player and asteroids, and handle game over if a collision occurs
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game Over!")
                pygame.quit()
                sys.exit()

        # Check for collisions between shots and asteroids, and handle the destruction of asteroids and shots when a collision occurs
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
            
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Draw everything
        screen.fill("black")

        # Draw the asteroids and player
        for draw in drawable:
            draw.draw(screen)

        # Update the display and tick the clock
        pygame.display.flip()

        dt = clock.tick(60) / 1000

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
