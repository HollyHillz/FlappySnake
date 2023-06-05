import pygame

class Player:
    def __init__(self, x, y):
        self.size = 50
        self.x = x - self.size // 2
        self.y = y - self.size // 2
        self.dy = 0
        self.gravity = 0.5

    def jump(self):
        self.dy = -10

    def update(self):
        self.dy += self.gravity
        self.y += self.dy

    def is_off_screen(self, screen_height):
        return self.y > screen_height or self.y < 0

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.size, self.size))
