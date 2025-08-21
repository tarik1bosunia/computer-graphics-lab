import pygame
import sys
import math

def draw_polygon(screen, color, x, y):
    points = [(x[i], y[i]) for i in range(len(x))]
    pygame.draw.polygon(screen, color, points, 3)

def rotate_polygon(x, y, n, angle, xp, yp):
    radian = math.radians(angle)
    sin_t = math.sin(radian)
    cos_t = math.cos(radian)

    for i in range(n):
        x_shift = x[i] - xp
        y_shift = y[i] - yp
        x[i] = xp + (x_shift * cos_t) - (y_shift * sin_t)
        y[i] = yp + (x_shift * sin_t) + (y_shift * cos_t)

def main():
    n = 4
    x = [300, 300, 500, 500]
    y = [250, 450, 450, 250]  

    angle = 30
    x_pivot, y_pivot = 500, 450 

    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Polygon Two Dimensional Rotation")
    screen.fill((255, 255, 255))

    # Draw original polygon in green
    draw_polygon(screen, (0, 255, 0), x[:], y[:])

    # Rotate once and draw in purple
    rotate_polygon(x, y, n, angle, x_pivot, y_pivot)
    draw_polygon(screen, (128, 0, 128), x, y)

    # Rotate again and draw in orange
    rotate_polygon(x, y, n, angle, x_pivot, y_pivot)
    draw_polygon(screen, (255, 165, 0), x, y)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
