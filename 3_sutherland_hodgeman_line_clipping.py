import pygame
import sys

clip_window = [(150, 150), (450, 150), (450, 350), (150, 350)]  # Rectangle

def inside(p, edge_start, edge_end):
    (x, y) = p
    (x1, y1) = edge_start
    (x2, y2) = edge_end
    return (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1) >= 0

def compute_intersection(p1, p2, e1, e2):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = e1
    x4, y4 = e2

    a1 = y2 - y1
    b1 = x1 - x2
    c1 = a1 * x1 + b1 * y1

    a2 = y4 - y3
    b2 = x3 - x4
    c2 = a2 * x3 + b2 * y3

    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None  # Parallel lines

    x = (b2 * c1 - b1 * c2) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    return (x, y)

def suth_hodg_clip(subject_polygon, clip_window):
    output_list = subject_polygon
    for i in range(len(clip_window)):
        input_list = output_list
        output_list = []
        A = clip_window[i]
        B = clip_window[(i + 1) % len(clip_window)]
        if not input_list:
            break
        P1 = input_list[-1]
        for P2 in input_list:
            if inside(P2, A, B):
                if not inside(P1, A, B):
                    inter = compute_intersection(P1, P2, A, B)
                    if inter:
                        output_list.append(inter)
                output_list.append(P2)
            elif inside(P1, A, B):
                inter = compute_intersection(P1, P2, A, B)
                if inter:
                    output_list.append(inter)
            P1 = P2
    return output_list

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Sutherland-Hodgman Polygon Clipping")
    screen.fill((255, 255, 255))

    subject_polygon = [(100, 100), (500, 200), (300, 400)]

    # Draw Clip Window (Blue rectangle)
    pygame.draw.polygon(screen, (0, 0, 255), clip_window, 3)

    # Draw Subject Polygon (Green outline)
    pygame.draw.polygon(screen, (0, 200, 0), subject_polygon, 3)

    # Perform Clipping
    clipped_polygon = suth_hodg_clip(subject_polygon, clip_window)

    # Draw Clipped Polygon (Yellow filled with border)
    if clipped_polygon:
        pygame.draw.polygon(screen, (255, 255, 0), clipped_polygon, 0)
        pygame.draw.polygon(screen, (200, 150, 0), clipped_polygon, 3)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
