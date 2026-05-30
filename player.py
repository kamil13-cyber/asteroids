import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS,SHOT_RADIUS, PLAYER_SHOT_SPEED
from shot import Shot

# Player class that inherits from CircleShape and implements drawing, rotating, moving, and updating methods
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.gun_cooldown = 0

    # Method to calculate the vertices of the player's triangle shape based on its position and rotation
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # Method to draw the player on the screen as a triangle
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # Method to move the player in the direction it is facing based on its rotation and speed
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    # Method to update the player's state based on user input for rotation and movement
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            # Handle shooting by checking the gun cooldown and creating a new shot if the cooldown has expired  
            if self.gun_cooldown <= 0:
                shot = self.shoot()
                shot.add(Shot.containers)
                self.gun_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        if self.gun_cooldown > 0:
            self.gun_cooldown -= dt

    def shoot(self):
        # Calculate the velocity of the shot based on the player's rotation and a defined shot speed
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        velocity = rotated_vector * PLAYER_SHOT_SPEED
        return Shot(self.position.x, self.position.y, velocity)
