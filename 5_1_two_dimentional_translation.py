import pygame
import sys

def draw_polygon(screen, color, x, y):
    points = [(x[i], y[i]) for i in range(len(x))]
    pygame.draw.polygon(screen, color, points, 3)

def translate_polygon(x, y, tx, ty):
    for i in range(len(x)):
        x[i] += tx
        y[i] += ty

def main():
    # Predefined polygon coordinates
    n = 4
    x = [100, 100, 200, 200]
    y = [100, 200, 200, 100]

    # Translation values
    tx, ty = 150, 150

    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Polygon Two Dimensional Translation")
    screen.fill((255, 255, 255))

    # Draw original polygon in black
    draw_polygon(screen, (0, 0, 0), x[:], y[:])

    # Translate polygon
    translate_polygon(x, y, tx, ty)

    # Draw translated polygon in red
    draw_polygon(screen, (0, 255, 0), x, y)

    pygame.display.flip()

    # Keep the window open
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
