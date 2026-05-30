import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


# Asteroid class that inherits from CircleShape and implements drawing and updating methods
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    # Method to draw the asteroid on the screen
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)
    
    # Method to update the asteroid's position based on its velocity and the time delta
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    # Method to split the asteroid into smaller asteroids when it is hit, creating two new asteroids with half the radius and random velocities
    def split(self):
        self.kill()  # Remove the original asteroid

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        else:
            log_event("asteroid_split")
            # Generate random velocities for the new asteroids by rotating the original velocity by a random angle between 20 and 80 degrees
            random_angle = random.uniform(20, 50)
            a = self.velocity.rotate(random.uniform(20, 50))
            b = self.velocity.rotate(random.uniform(50, 80))

            # Calculate the new radius for the smaller asteroids by subtracting the minimum radius from the original radius
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # Create two new asteroids with half the radius and random velocities
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = a * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = b * 1.2

