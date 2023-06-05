import pygame
import sys
from Player import Player
import screensetup as ss
#import Obsticlez as obz

class Obsticle:
    def __init__(self, x, H, topOrBottom):
        self.width = 50
        self.height = H
        self.x = x
        self.speed=5
        self.toporbottom = topOrBottom

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        if self.toporbottom == "top":
            pygame.draw.rect(screen, (0, 0, 0), (self.x, 0, self.width, self.height))
        elif self.toporbottom == "bottom":
            pygame.draw.rect(screen, (0, 0, 0), (self.x, ss.screen_height - self.height, self.width, ss.screen_height))
        elif self.toporbottom == "floating":
            pygame.draw.rect(screen, (0, 0, 0), (self.x, self.height, 50, 50))



# Initialize Pygame
pygame.init()

# Set up the Player
player = Player(ss.screen_width // 2, 300)

ob = Obsticle(ss.screen_width, 250, "bottom")

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

        

    # Update the player
    player.update()
    ob.update()


    # Check if the square has fallen below the screen
    if player.is_off_screen(ss.screen_height):
        pygame.quit()
        sys.exit()

    # Clear the screen
    ss.screen.fill((50, 100, 50))

    # Draw the square
    player.draw(ss.screen)
    ob.draw(ss.screen)

    # Update the screen
    pygame.display.flip()
    ss.clock.tick(60)
