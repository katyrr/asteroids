from CircleShape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20, 50)
        child_1_velocity = self.velocity.rotate(split_angle)
        child_2_velocity = self.velocity.rotate(-split_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        child_1 = Asteroid(self.position.x, self.position.y, new_radius)
        child_2 = Asteroid(self.position.x, self.position.y, new_radius)

        child_1.velocity = child_1_velocity*1.2
        child_2.velocity = child_2_velocity*1.2
        