import pygame
import math


def get_signal(win):
    # get points on path drawn by user
    points = []
    while True:
        for event in pygame.event.get():
            # draw while mouse pressed
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                points.append((pos[0], pos[1]))
            if event.type == pygame.KEYDOWN:
                # space to complete drawing
                if event.key == pygame.K_SPACE:
                    return_points = []
                    for i in range(1, len(points)):
                        if (
                            math.hypot(
                                points[i][0] - points[i - 1][0],
                                points[i][1] - points[i - 1][1],
                            )
                            > 1
                        ):
                            return_points.append(points[i])
                    points, return_points = return_points, []

                    # remove duplicates
                    for i in range(len(points) - 1):
                        if points[i] != points[i + 1]:
                            return_points.append(points[i])
                    x = return_points
                    x.append(x[0])
                    return ["NO GAP", [{"x": i[0], "y": i[1]} for i in x]]
                # reset drawing
                if event.key == pygame.K_r:
                    points = []

        # draw paths
        if len(points) > 1:
            pygame.draw.lines(win, (0, 0, 0), False, [*points, points[0]])

        pygame.display.flip()
        win.fill((255, 255, 255))
