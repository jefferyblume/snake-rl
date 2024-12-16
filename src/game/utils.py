import pygame

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (200,0,0)
GREEN = (0,200,0)

TILE_SIZE = 20
BOARD_WIDTH = 20
BOARD_HEIGHT = 20

FONT_SIZE = 24
font_cache = None

def get_font():
    global font_cache
    if font_cache is None:
        pygame.font.init()
        font_cache = pygame.font.SysFont("Arial", FONT_SIZE)
    return font_cache

def draw_text(surface, text, color, x, y):
    font = get_font()
    img = font.render(text, True, color)
    surface.blit(img, (x, y))
