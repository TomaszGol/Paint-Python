import pygame
pygame.init()
pygame.font.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 1000

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
BACKGROUND_COLOR = WHITE
ROWS = 150
COLUMNS = 150
PIXEL_SIZE = SCREEN_WIDTH // COLUMNS
TOOLBAR_HEIGHT = SCREEN_HEIGHT - SCREEN_WIDTH
DRAW_GRID_LINES = False

def get_font(size):
    return pygame.font.SysFont("comicsans", size)