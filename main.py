import pygame
from settings import WIDTH, HEIGHT, FPS, CYAN, BLACK, BLUE
from models import Field, Grid, Column, Row


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT + 50))
clock = pygame.time.Clock()

grid_width = WIDTH // 3
grid_height = HEIGHT // 3

field_width = WIDTH // 9
field_height = HEIGHT // 9

grids = []
for x in range(0, WIDTH, grid_width):
    for y in range(0, HEIGHT, grid_height):
        if len(grids) < 9:
            grids.append(Grid((x, y, grid_width, grid_height)))

fields = []
for x in range(0, WIDTH - field_width, field_width):
    for y in range(0, HEIGHT - field_height, field_height):
        fields.append(Field((x, y, field_width, field_height)))

fields_length = len(fields)
column_length = fields_length // 9

columns = []
for index in range(0, fields_length, column_length):
    columns.append(Column([n for n in range(index, index + column_length)]))

rows = [Row() for _ in range(column_length)]
for index, row in enumerate(rows):
    row.field_indexes = [n for n in range(index, fields_length, column_length)]

for_grids = []
for row in rows:
    for index in range(0, column_length, column_length // 3):
        for_grids.append(row.field_indexes[index:(index + 3)])

for index, grid in enumerate(grids):
    if index > 2 and index < 6:
        index += 6
    elif index > 5:
        index += 12

    grid.field_indexes = [for_grids[chunk] for chunk in range(index, len(for_grids), column_length // 3)]
    grid.field_indexes = grid.field_indexes[:3]
    grid.field_indexes = [item for chunk in grid.field_indexes for item in chunk]


def main():
    running = True
    while running:
        #poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = event.dict['pos']
                
                # Highlight clicked field
                for field in fields:
                    if position[0] in range(field.x, field.x + field.width) and position[1] in range(field.y, field.y + field.height):
                        pygame.draw.rect(window, CYAN, pygame.Rect(field.x, field.y, field.width, field.height))
                        pygame.display.flip()
                        
                        listening = True
                        while listening:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    input = event.dict['unicode']

                                    # if escape key clicked, turn off highlight
                                    if event.dict['key'] == 27:
                                        listening = False

                                    try:
                                        int(input)
                                    except ValueError:
                                        break

                                    field.value = input
                                    if check_conditions(field, grids) and check_conditions(field, rows) and check_conditions(field, columns) and int(input) > 0:
                                        update_values(field, grids)
                                        update_values(field, rows)
                                        update_values(field, columns)

                                        listening = False
                                    else:
                                        field.value = None

        # Fill background with color
        window.fill("white")

        # Render game here
        draw_board()

        for field in fields:
            if field.value:
                display_number(field.value, (field.x + field.width // 3, field.y + field.height // 3))             

        # display work on screen
        pygame.display.flip()

        # limit fps
        clock.tick(FPS)
    
    pygame.quit()

# Functions
def draw_board():
    # draw fields
    for field in fields:
        pygame.draw.rect(window, BLACK, pygame.Rect(field.x, field.y, field.width, field.height), 1)

    # draw grids
    for grid in grids:
        pygame.draw.rect(window, BLUE, pygame.Rect(grid.dimensions), 2)

def display_number(value, position):
    font = pygame.font.SysFont('arial', 32)
    text = font.render(str(value), True, BLACK)
    window.blit(text, position)

def check_conditions(field, area):
    for element in area:
        if fields.index(field) in element.field_indexes:
            if field.value in element.field_values:
                return False
    return True

def update_values(field, area):
    for element in area:
        if fields.index(field) in element.field_indexes:
            element.field_values.append(field.value)

if __name__ == "__main__":
    main()