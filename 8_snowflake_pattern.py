import pygame
import sys
import math
import time

def snowflake(screen, x1, y1, x5, y5, iteration, color=(0, 0, 0)):
    if iteration > 0:
        dx = (x5 - x1) / 3
        dy = (y5 - y1) / 3

        x0, y0 = x1, y1
        x1a, y1a = x1 + dx, y1 + dy
        x2a = (x1 + x5) / 2 + math.sqrt(3) * (y1 - y5) / 6
        y2a = (y1 + y5) / 2 + math.sqrt(3) * (x5 - x1) / 6
        x3a, y3a = x1 + 2 * dx, y1 + 2 * dy
        x4, y4 = x5, y5

        snowflake(screen, x0, y0, x1a, y1a, iteration - 1, color)
        snowflake(screen, x1a, y1a, x2a, y2a, iteration - 1, color)
        snowflake(screen, x2a, y2a, x3a, y3a, iteration - 1, color)
        snowflake(screen, x3a, y3a, x4, y4, iteration - 1, color)
    else:
        pygame.draw.line(screen, color, (x1, y1), (x5, y5))
        pygame.display.update()
        time.sleep(0.01)  # small delay to visualize drawing


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    iteration = 4
    pygame.display.set_caption(f"Snowflake Pattern With {iteration} iterations")
    screen.fill((255, 255, 255)) 

    points = [(375, 140), (175, 475), (575, 475)]

    for i in range(3):
        snowflake(screen,
                  points[i][0], points[i][1],
                  points[(i + 1) % 3][0], points[(i + 1) % 3][1],
                  iteration,
                  (0, 0, 0)) 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
