import pygame
import sys
from Player import Player

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Set up the square
player = Player(screen_width // 2, screen_height // 2)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # Update the square
    player.update()

    # Check if the square has fallen below the screen
    if player.is_off_screen(screen_height):
        pygame.quit()
        sys.exit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the square
    player.draw(screen)

    # Update the screen
    pygame.display.flip()
    clock.tick(60)
