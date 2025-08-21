import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800
CAPTION = "Overlapping Shapes"

# Colors
RED   = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE  = (0, 0, 255)
WHITE = (255, 255, 255)

# Top-center reference point
CENTER_X = WIDTH // 2
TOP_Y = 180   # base height for placement

# Shapes Data
RECT_W, RECT_H = 250, 150
CIRCLE_RADIUS = 120

def draw_triangle():
    # Triangle slightly above & wider
    points = [
        (CENTER_X - 180, TOP_Y + 200),   # bottom-left
        (CENTER_X + 180, TOP_Y + 60),   # bottom-right
        (CENTER_X, TOP_Y - 140)         # top
    ]
    pygame.draw.polygon(screen, GREEN, points)

def draw_circle():
    # Circle centered slightly lower
    pygame.draw.circle(screen, BLUE, (CENTER_X, TOP_Y + 40), CIRCLE_RADIUS)

def draw_rectangle():
    # Rectangle slightly shifted down
    rect = pygame.Rect(CENTER_X - RECT_W // 2, TOP_Y + 80, RECT_W, RECT_H)
    pygame.draw.rect(screen, RED, rect)

SHAPE_DRAWERS = {"T": draw_triangle, "C": draw_circle, "R": draw_rectangle}

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption(CAPTION)

def main():
    sequence = "RCT"  # change order to control overlap
    running = True

    while running:
        screen.fill(WHITE)

        # Draw shapes in sequence order
        for ch in sequence:
            SHAPE_DRAWERS[ch]()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
