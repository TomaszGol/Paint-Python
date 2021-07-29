import pygame
from settings import *
from Button import *

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint-Python")


def make_grid(rows, columns, color):
    grid = []
    for i in range(rows):
        grid.append([])
        for _ in range(columns):
            grid[i].append(color)
    return grid


def draw_grid(windows, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(windows, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(windows, BLACK, (0, i * PIXEL_SIZE), (SCREEN_WIDTH, i * PIXEL_SIZE))
        for i in range(COLUMNS + 1):
            pygame.draw.line(windows, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, SCREEN_HEIGHT - TOOLBAR_HEIGHT))


def draw_background(window, grid):
    window.fill(BACKGROUND_COLOR)
    draw_grid(window, grid)
    for button in buttons:
        button.draw(window)
    pygame.display.update()


def get_mouse_position(position):
    x, y = position
    row = y // PIXEL_SIZE
    column = x // PIXEL_SIZE
    if row >= ROWS:
        raise IndexError

    return row, column


clock = pygame.time.Clock()
grid = make_grid(ROWS, COLUMNS, BACKGROUND_COLOR)
run = True
drawing_color = BLACK
rubber_color = WHITE

button_y = SCREEN_HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, RED),
    Button(130, button_y, 50, 50, GREEN),
    Button(190, button_y, 50, 50, BLUE),
    Button(250, button_y, 50, 50, WHITE, "Clear", BLACK)
]

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            try:
                rows, columns = get_mouse_position(position)
                grid[rows][columns] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(position):
                        continue
                    drawing_color = button.color
                    if button.text == "Clear":
                        grid = make_grid(ROWS, COLUMNS, BACKGROUND_COLOR)
                        drawing_color = BLACK
        if pygame.mouse.get_pressed()[2]:
            position = pygame.mouse.get_pos()
            try:
                rows, columns = get_mouse_position(position)
                grid[rows][columns] = rubber_color
            except IndexError:
                pass
    draw_background(WINDOW, grid)
pygame.quit()
