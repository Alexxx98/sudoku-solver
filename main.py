import pygame
from pygame.locals import MOUSEBUTTONDOWN
from settings import WIDTH, HEIGHT, FPS

import time


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

grid_width = WIDTH // 3
grid_height = HEIGHT // 3

field_width = WIDTH // 9
field_height = HEIGHT // 9

grids = []
for x in range(0, WIDTH, grid_width):
    for y in range(0, HEIGHT, grid_height):
        grids.append((x, y, grid_width, grid_height))

fields = []
for x in range(0, WIDTH, field_width):
    for y in range(0, HEIGHT, field_height):
        fields.append((x, y, field_width, field_height))

def main():
    running = True
    while running:
        #poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                position = event.dict['pos']
                print(position)

                for index, field in enumerate(fields):
                    try:
                        if position[0] in range(field[0], fields[index + 1][0]) and position[1] in range(field[1], fields[index + 1][1]):
                            pygame.draw.rect(window, "purple", pygame.Rect(field))
                            print(field)
                            break
                    except IndexError:
                        pygame.draw.rect(window, "purple", pygame.Rect(fields[-1]))
                        print("error")

        window.fill("white")

        # Render game here

        # draw fields
        for field in fields:
            pygame.draw.rect(window, (0, 0, 0), pygame.Rect(field), 1)

        # draw grids
        for grid in grids:
            pygame.draw.rect(window, (0, 0, 255), pygame.Rect(grid), 2)

        # display work on screen
        pygame.display.flip()

        # limit fps
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()