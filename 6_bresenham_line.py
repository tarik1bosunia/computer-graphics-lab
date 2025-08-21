import pygame
import sys

def draw_line(screen, x1, y1, x2, y2, color=(0, 0, 0)):
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = abs(y2 - y1)
    p = 2 * dy - dx

    y = y1
    y_step = 1 if y1 < y2 else -1

    for x in range(x1, x2 + 1):
        screen.set_at((x, y), color) 
        if p >= 0:
            y += y_step
            p += 2 * (dy - dx)
        else:
            p += 2 * dy

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Bresenham Line Drawing")

    screen.fill((255, 255, 255))

    x1, y1 = 200, 150
    x2, y2 = 600, 520
    draw_line(screen, x1, y1, x2, y2, (255, 0, 0)) 

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
