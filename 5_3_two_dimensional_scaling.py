import pygame
import sys

def draw_polygon(screen, color, x, y):
    points = [(x[i], y[i]) for i in range(len(x))]
    pygame.draw.polygon(screen, color, points, 3)

def scale_polygon(x, y, n, sfx, sfy):
    for i in range(n):
        x[i] = x[i] * sfx
        y[i] = y[i] * sfy

def main():
    n = 4
    x = [150, 150, 250, 250]
    y = [130, 230, 230, 130] 

    # Scaling factors
    sfx, sfy = 2, 2

    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Polygon Two Dimentional Scaling")
    screen.fill((255, 255, 255))

    # Draw original polygon in blue
    draw_polygon(screen, (0, 0, 255), x[:], y[:])

    # Scale polygon
    scale_polygon(x, y, n, sfx, sfy)

    # Draw scaled polygon in magenta
    draw_polygon(screen, (255, 0, 255), x, y)

    pygame.display.flip()

    # Keep window open
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
