import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1600, 1600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Travel Effect")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Star class
class Star:
    def __init__(self):
        self.reset()

    def reset(self):
        # print("Resetting star position")  # Debugging output
        self.x = random.uniform(-WIDTH, WIDTH)
        self.y = random.uniform(-HEIGHT, HEIGHT)
        self.z = random.uniform(1, WIDTH)   # depth

    def update(self, speed):
        self.z -= speed
        if self.z <= 0:
            self.reset()

    def draw(self, surface):
        # Perspective projection
        sx = int((self.x / self.z) * WIDTH/2 + WIDTH/2)
        sy = int((self.y / self.z) * HEIGHT/2 + HEIGHT/2)
        # print(f"sx = {sx}, sy = {sy}, z = {self.z}")  # Debugging output

        if 0 <= sx < WIDTH and 0 <= sy < HEIGHT:
            r = int(max(1, (1 - self.z / WIDTH) * 5))  # size increases as star gets closer
            pygame.draw.circle(surface, WHITE, (sx, sy), r)


def main():
    clock = pygame.time.Clock()
    stars = [Star() for _ in range(400)]
    speed = 11

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update & draw stars
        for star in stars:
            star.update(speed)
            star.draw(screen)
            print(f"Star position: ({star.x}, {star.y}, {star.z})")

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
