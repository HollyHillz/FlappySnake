import pygame
import screensetup as ss

class Obsticle:
    def __init__(self, x, W, H, topOrBottom):
        self.width = W
        self.height = H
        self.x = x
        self.speed=10
        self.toporbottom = topOrBottom

    def update(self):
        self.x += self.x - self.speed

    def draw(self, screen):
        if self.toporbottom == "top":
            pygame.draw.rect(screen, (0, 0, 0), (self.x, ss.screen_height, self.width, self.height))
        elif self.toporbottom == "bottom":
            pygame.draw.rect(screen, (0, 0, 0), (self.x, self.height, self.width, 0))
