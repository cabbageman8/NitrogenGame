import struct
import moderngl
import pygame
from pygame.locals import *
from PIL import Image
import pickle
import numpy as np
from math import pi, tau, sin, cos, tan, asin, acos, atan, ceil, floor
import cProfile
import random
from quadtree import root_node
from glrenderer import glrenderer
pygame.init()

FPS=60
clock = pygame.time.Clock()
#window_size=(1000, 1000)
#window_size=(1440, 1440)
window_size=(2560, 1440)
tile_size = 75

pygame.display.set_mode(window_size, DOUBLEBUF|OPENGL)

materials = ["Dirt16", "Water", "tiles16", "dirt16", "Cabbage16"]
materials_img = []
sprites = ["selection", "charb32", "Grass", "TreeStump", "DeadTree", "treeb128"]
sprites_img = []
solids = {"Water", "treeb128", "tree128"}
def load_textures():
    global materials_img
    global sprites_img
    materials_img = []
    sprites_img = []
    for mat in materials:
        frame_list = []
        file = Image.open("data/" + mat + ".png")
        for i in range(file.height//file.width):
            frame_list.append(pygame.image.fromstring(file.crop(Rect(0,file.width*i,file.width,file.width*(i+1))).resize([128, 128], resample=Image.NEAREST).tobytes(), [128, 128], "RGB").convert_alpha())
        materials_img.append(frame_list)
    for spr in sprites:
        file = Image.open("data/" + spr + ".png")
        sprites_img.append(pygame.image.fromstring(file.resize([128, 128], resample=Image.NEAREST).tobytes(), [128, 128], "RGBA").convert_alpha())
    for i in range(4):
        file = Image.open("data/char32.png")
        sprites_img.append(pygame.image.fromstring(file.resize([128, 128], resample=Image.NEAREST).rotate(90*i).tobytes(), [128, 128], "RGBA").convert_alpha())
        file = Image.open("data/charb32.png")
        sprites_img.append(pygame.image.fromstring(file.resize([128, 128], resample=Image.NEAREST).rotate(90*i).tobytes(), [128, 128], "RGBA").convert_alpha())
load_textures()

texpack = pygame.Surface((128*(len(materials)+len(sprites_img)), 128), flags=pygame.SRCALPHA).convert_alpha()
for i, m in enumerate(materials_img):
    texpack.blit(m[0], (128*i,0))
for i, s in enumerate(sprites_img):
    texpack.blit(s, (128*len(materials)+128*i,0))
overlay = pygame.Surface(window_size).convert_alpha()
Renderer = glrenderer(texpack, overlay)

def seeded_random(a):
    output = (41406202+14874235*a)%79493069
    output = (43915416+77751829*output)%76741089
    output = (66947287+44145130*output)%90370934
    output = (64705634+34405431*output)%23928528
    output = (24300417+80810414*output)%10000
    return output/10000
def point_to_random(x, y):
    return seeded_random(x + x * x * y * y * y + y)

try:
    sav = open('quadtree.pickle' , 'rb')
    data = pickle.load(sav)
    map = data['map']
    pos = data['pos']
    sav.close()
except:
    map = root_node()
    pos = [0.5, 0.5]
    sav = open('quadtree.pickle' , 'wb')
    data = {'map': map, 'pos': pos}
    pickle.dump(data, sav)
    sav.close()
    print('could not load, blank save loaded')

def get_mat(x, y):
    map_data = map.get_data(x, y)
    if (map_data != None):
        mat = map_data
    else:
        r = sin(0.546354 * y/5) * sin(0.876964 * y/5) * sin(1.45638 * y/5 + 1.82266 * x/5) + cos(1.94367 * x/5 - 1.743247 * y/5) * cos(0.869632 * x/5)
        if (r < -.9):
            mat = 1
        elif (r < -.5):
            mat = 0
        elif (r > 0.5):
            mat = 0
        elif (abs(r) < 0.1):
            mat = 3
        else:
            mat = 4
        map.cache_data(x, y, mat)
    return mat
def decorate(x, y, mat):
    r = point_to_random(x, y)
    if r < 0.7 and mat == 4:
        return 2
    if r < 0.001 and mat == 0:
        return 4
    if r > 0.98 and mat == 0:
        return 5
    return None

def draw_tile(mat, x, y, screen_coords):
    # blits material texture using int tile coords relitive to the screen
    Renderer.vert_list.append(((1 - screen_coords[0] % tile_size + tile_size * x)/window_size[0]*2, (1 - screen_coords[1] % tile_size + tile_size * y)/window_size[1]*2, 0.0, tile_size/window_size[0]*2, tile_size/window_size[1]*2, mat))
def draw_sprite(spr, x, y, z, w, h):
    # blits sprite texture using float pixel coords relitive to the screen
    Renderer.vert_list.append((x/window_size[0]*2, (y)/window_size[1]*2, z, w/window_size[0]*2, h/window_size[1]*2, len(materials)+spr))
def draw_object(decor, x, y, w, h, screen_coords):
    # blits sprite texture using tile coords relitive to the world
    draw_sprite( decor,
        1 - screen_coords[0] % tile_size + tile_size*(x-w/2+0.5)-screen_coords[0]//tile_size*tile_size - cos(curtime / 1000 + x+y*y) * tile_size / 20,
        1 - screen_coords[1] % tile_size + tile_size*(y-h/2+0.5)-screen_coords[1]//tile_size*tile_size - sin(curtime / 300  + x+y*y) * tile_size / 20,
        0.35+sin(curtime / 300 + x+y*y)/50,
        w * tile_size + int(cos(curtime / 1000 + x+y*y) * tile_size / 10),
        h * tile_size + int(sin(curtime / 300 + x+y*y) * tile_size / 10))
def draw_object_foreground(decor, x, y, w, h, screen_coords):
    # blits sprite texture using tile coords relitive to the world
    draw_sprite( decor,
        1 - screen_coords[0] % tile_size + tile_size*(x-w/2+0.5)-screen_coords[0]//tile_size*tile_size - cos(curtime / 1000 + x+y*y) * tile_size / 10,
        1 - screen_coords[1] % tile_size + tile_size*(y-h/2+0.5)-screen_coords[1]//tile_size*tile_size - sin(curtime / 300  + x+y*y) * tile_size / 10,
        1.0,
        w * tile_size + int(cos(curtime / 1000 + x+y*y) * tile_size / 5),
        h * tile_size + int(sin(curtime / 300 + x+y*y) * tile_size / 5))

velocity = [0, 0]
acceleration = 1/1000

keydown_set = set()
mouse_pos = pygame.mouse.get_pos()
def handle_keys():
    global running
    global mouse_pos
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            else:
                keydown_set.add(event.key)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False
            else:
                keydown_set.remove(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            keydown_set.add("mouse"+str(event.button))
        elif event.type == pygame.MOUSEBUTTONUP:
            keydown_set.remove("mouse"+str(event.button))
            if (event.button == 1):
                keydown_set.add("unclick1")

running=True
frame = 0
curtime = pygame.time.get_ticks()
char_direction = 0

def main():
    global frame
    global velocity
    global curtime
    global tile_size
    global surf
    global Foreground_texture
    global screen
    global char_direction
    frame += 1
    dt = pygame.time.get_ticks() - curtime
    curtime = pygame.time.get_ticks()
    #frag_time.value = curtime
    handle_keys()
    if pygame.K_w in keydown_set:
        velocity[1] -= acceleration * dt
        char_direction = 0
    if pygame.K_a in keydown_set:
        char_direction = 2
        if pygame.K_w in keydown_set:
            char_direction = 3
        velocity[0] -= acceleration * dt
    if pygame.K_s in keydown_set:
        char_direction = 4
        if pygame.K_a in keydown_set:
            char_direction = 5
        velocity[1] += acceleration * dt
    if pygame.K_d in keydown_set:
        char_direction = 6
        if pygame.K_w in keydown_set:
            char_direction = 1
        if pygame.K_s in keydown_set:
            char_direction = 7
        velocity[0] += acceleration * dt
    if pygame.K_t in keydown_set:
        map.tree()
    if pygame.K_UP in keydown_set:
        tile_size += 2
    if pygame.K_DOWN in keydown_set:
        tile_size -= 2
        if (tile_size < 10):
            tile_size = 10
    if "unclick1" in keydown_set:
        print("pickling")
        sav = open('quadtree.pickle', 'wb')
        data = {'map': map, 'pos': pos}
        pickle.dump(data, sav)
        sav.close()
        keydown_set.remove("unclick1")
    velocity[0] -= velocity[0] / 10
    velocity[1] -= velocity[1] / 10
    screen_coords = [pos[0] * tile_size - window_size[0] // 2, pos[1] * tile_size - window_size[1] // 2]
    mat = get_mat(ceil(pos[0] - 1), ceil(pos[1] - 1))
    spr = decorate(ceil(pos[0] - 1), ceil(pos[1] - 1), mat)
    if (materials[mat] in solids or spr != None and sprites[spr] in solids):
        pos[1] += 1
        velocity = [0, 0]
    else:
        mat2 = get_mat(ceil(pos[0] - 1 + velocity[0]), ceil(pos[1] - 1 + velocity[1]))
        spr2 = decorate(ceil(pos[0] - 1 + velocity[0]), ceil(pos[1] - 1 + velocity[1]), mat2)
        if (materials[mat2] in solids or spr2 != None and sprites[spr2] in solids):
            velocity = [0, 0]
        else:
            pos[0] += velocity[0]
            pos[1] += velocity[1]
    selected_tile = [mouse_pos[0] + screen_coords[0] % tile_size,
                     mouse_pos[1] + screen_coords[1] % tile_size]
    selected_tile = [-screen_coords[0] % tile_size + tile_size * ceil(selected_tile[0] / tile_size) - window_size[0] // 2,
                     -screen_coords[1] % tile_size + tile_size * ceil(selected_tile[1] / tile_size) - window_size[1] // 2]
    selected_tile = [pos[0] + ceil(selected_tile[0] / tile_size) - 3,
                     pos[1] + ceil(selected_tile[1] / tile_size) - 3]
    if "mouse1" in keydown_set:
        map.set_data(selected_tile[0], selected_tile[1], 2)
    for y in range(2 + window_size[1] // tile_size):
        for x in range(2 + window_size[0] // tile_size):
            tile_coords = [ceil(screen_coords[0] / tile_size) + x - 1,
                           ceil(screen_coords[1] / tile_size) + y - 1]
            mat = get_mat(tile_coords[0], tile_coords[1])
            draw_tile(mat, x, y, screen_coords)
    for y in range(2 + window_size[1] // tile_size):
        for x in range(2 + window_size[0] // tile_size):
            tile_coords = [ceil(screen_coords[0] / tile_size) + x - 1,
                           ceil(screen_coords[1] / tile_size) + y - 1]
            mat = get_mat(tile_coords[0], tile_coords[1])
            decor = decorate(tile_coords[0], tile_coords[1], mat)
            if decor == 2:
                draw_object(decor, tile_coords[0], tile_coords[1], 2, 2, screen_coords)
            if decor == 4 or decor == 5:
                draw_object(3, tile_coords[0], tile_coords[1], 1, 1, screen_coords)
    draw_sprite(6+char_direction, window_size[0] / 2 - tile_size, window_size[1] / 2 - tile_size, 0.75, 2 * tile_size, 2 * tile_size)
    for y in range(7 + window_size[1] // tile_size):
        for x in range(7 + window_size[0] // tile_size):
            tile_coords = [ceil(screen_coords[0] / tile_size) + x - 4,
                           ceil(screen_coords[1] / tile_size) + y - 4]
            mat = get_mat(tile_coords[0], tile_coords[1])
            decor = decorate(tile_coords[0], tile_coords[1], mat)
            if decor == 4 or decor == 5:
                draw_object_foreground(decor, tile_coords[0], tile_coords[1], 8, 8, screen_coords)
    draw_object(0, selected_tile[0] + 1 - pos[0] % 1, selected_tile[1] + 1 - pos[1] % 1, 2, 2, screen_coords)
    Renderer.render( curtime, (mouse_pos[0]/window_size[0]*2-1, 1-mouse_pos[1]/window_size[1]*2))
    pygame.display.flip()
    clock.tick(FPS)

while running:
    #cProfile.run('main()')
    main()