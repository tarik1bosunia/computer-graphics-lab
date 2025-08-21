import pygame
import sys

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def bezier_function(k, n, u):
    return nCr(n, k) * (u ** k) * ((1 - u) ** (n - k))

def bezier_curve(screen, points, color=(0, 0, 0)):
    n = len(points) - 1
    eps = 0.001  

    u = 0
    while u <= 1:
        x = 0
        y = 0
        for k in range(n + 1):
            bez = bezier_function(k, n, u)
            x += points[k][0] * bez
            y += points[k][1] * bez
        screen.set_at((int(x), int(y)), color)
        u += eps

    for px, py in points:
        pygame.draw.circle(screen, color, (px, py), 5)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Bezier Curve")
    screen.fill((255, 255, 255))

    points = [(227, 393), (301, 197), (524, 347), (637, 173)]
    bezier_curve(screen, points, (0, 0, 0))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
