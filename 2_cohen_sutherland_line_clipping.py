import pygame
import sys

x_left, x_right = 120, 500
y_bottom, y_top = 100, 350

LEFT, RIGHT, BOTTOM, TOP = 1, 2, 4, 8


def region_code(x, y):
    code = 0
    if x > x_right:
        code |= RIGHT
    elif x < x_left:
        code |= LEFT
    if y > y_top:
        code |= TOP
    elif y < y_bottom:
        code |= BOTTOM
    return code


def cohen_sutherland(screen, x1, y1, x2, y2, color=(255, 255, 255)):
    code1 = region_code(x1, y1)
    code2 = region_code(x2, y2)

    while True:
        if not (code1 | code2): 
            pygame.draw.line(screen, color, (int(x1), int(y1)), (int(x2), int(y2)))
            return
        elif code1 & code2:  
            return
        else:  
            if code1:
                code = code1
            else:
                code = code2

            if code & TOP:
                y = y_top
                x = x1 + (x2 - x1) / (y2 - y1) * (y - y1)
            elif code & BOTTOM:
                y = y_bottom
                x = x1 + (x2 - x1) / (y2 - y1) * (y - y1)
            elif code & LEFT:
                x = x_left
                y = y1 + (y2 - y1) / (x2 - x1) * (x - x1)
            elif code & RIGHT:
                x = x_right
                y = y1 + (y2 - y1) / (x2 - x1) * (x - x1)

            if code == code1:
                x1, y1 = x, y
                code1 = region_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = region_code(x2, y2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Cohen-Sutherland Line Clipping")
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x_left, y_bottom, x_right - x_left, y_top - y_bottom), 3)
    pygame.draw.line(screen, (255, 255, 0), (50, 200), (500, 400))
    cohen_sutherland(screen, 50, 200, 500, 400, (255, 0, 255))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
