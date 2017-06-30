# 6-29-17
# nat
# first rpg

import pygame, sys, time
from scripts.textures import *
from scripts.map_engine import *
from scripts.fps_tracker import *

def create_window(window_width, window_height):
    pygame.display.set_caption("RPG")
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)
    return window

def make_sky(window_width, window_height, sky, window):
    for x in range(0, window_width, sky.size):
        for y in range(0, window_height, sky.size):
            window.blit(sky.instance, (x, y))

def make_earth(window, earth, camera_x, camera_y):
    for x in range(0, earth.width, earth.size):
        for y in range(0, earth.height, earth.size):
            window.blit(earth.instance, (x + camera_x, y + camera_y))

def main():
    pygame.init()
    color = pygame.Color
    fps = FPS_Tracker()
    sky = Texture("sky")
    earth = Earth("grass")
    # world_map = Map()
    # terrain = world_map.load_map("maps/map.map", tiles)
    window_width, window_height = 800, 600
    camera_x, camera_y = 0, 0
    camera_move = 0
    window = create_window(window_width, window_height)
    
    #RENDER GRAPHICS
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    camera_y += 10
                elif event.key == pygame.K_s:
                    camera_y -= 10
                elif event.key == pygame.K_a:
                    camera_x += 10
                elif event.key == pygame.K_d:
                    camera_x -= 10

            # elif event.type == pygame.KEYUP:
            #     camera_x = camera_x
            #     camera_y = camera_y
        
        new_sky = make_sky(window_width, window_height, sky, window)
        new_terrain = make_earth(window, earth, camera_x, camera_y)

        new_count = fps.count()
        new_display = fps.display(window)

        pygame.display.update()

    pygame.quit()
    sys.exit

main()