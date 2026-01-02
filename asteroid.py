import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, asteroidField):
        super().__init__(x, y, radius)
        self.asteroidField = asteroidField

    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            split_angle = random.uniform(20, 50)
            new_velocity_asteroid1 = self.velocity.rotate(split_angle) * 1.2
            new_velocity_asteroid2 = self.velocity.rotate(-split_angle) * 1.2
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

            self.asteroidField.spawn(
                new_asteroid_radius, self.position, new_velocity_asteroid1
            )
            self.asteroidField.spawn(
                new_asteroid_radius, self.position, new_velocity_asteroid2
            )
