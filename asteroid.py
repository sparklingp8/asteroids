from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        r = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, r)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, r)
        asteroid.velocity = b * 1.2
        
        