import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Flag")

# Colors (R, G, B)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
WHITE = (0, 0, 0)

# Fill background
screen.fill((255, 255, 255))

# Draw green rectangle (flag body)
pygame.draw.rect(screen, GREEN, (50, 50, 300, 180))

# Draw red circle (flag symbol)
pygame.draw.circle(screen, RED, (200, 140), 60)

# Draw white rectangle (flag pole)
pygame.draw.rect(screen, WHITE, (40, 40, 10, 390))

# Update display
pygame.display.flip()

# Wait until user closes window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
