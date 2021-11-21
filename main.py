import struct
import moderngl
import pygame
from pygame.locals import *
from PIL import Image
import pickle
import numpy as np
from math import pi, tau, sin, cos, tan, asin, acos, atan, ceil, floor, remainder
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

textures = ["dirt", "water", "tiles", "cabbage", "selection", "grass", "deadtree", "tree", "treelog", "treestump"]
textures_img = []
texd = {}
def load_textures():
    global texd
    global textures_img
    textures_img = []
    for mat in textures:
        file = Image.open("data/" + mat + ".png").convert("RGBA")
        frame_list = []
        for i in range(file.height//file.width):
            frame = pygame.image.fromstring( file.crop(Rect(0,file.width*i,file.width,file.width*(i+1))).resize([128, 128], resample=Image.NEAREST).tobytes(), [128, 128], "RGBA").convert_alpha()
            frame_list.append(len(textures_img))
            textures_img.append(frame)
        texd.update({mat : frame_list})

    file = Image.open("data/char32.png").convert("RGBA")
    fileb = Image.open("data/charb32.png").convert("RGBA")
    for i in range(4):
        frame_list = []
        for j in range(file.height // file.width):
            frame = pygame.image.fromstring( file.crop(Rect(0, file.width * j, file.width, file.width * (j + 1))).resize([128, 128], resample=Image.NEAREST).rotate(90*i).tobytes(), [128, 128], "RGBA").convert_alpha()
            frame_list.append(len(textures_img))
            textures_img.append(frame)
        texd.update({"char"+str(i*2): frame_list})
        frame_list = []
        for j in range(fileb.height // fileb.width):
            frame = pygame.image.fromstring( fileb.crop(Rect(0, fileb.width * j, file.width, file.width * (j + 1))).resize([128, 128], resample=Image.NEAREST).rotate(90*i).tobytes(), [128, 128], "RGBA").convert_alpha()
            frame_list.append(len(textures_img))
            textures_img.append(frame)
        texd.update({"char" + str(i*2+1): frame_list})

        textures_img.append(pygame.image.fromstring(file.resize([128, 128], resample=Image.NEAREST).rotate(90*i).tobytes(), [128, 128], "RGBA").convert_alpha())
load_textures()
def get_tex(name, index):
    return texd[name][int(index)%len(texd[name])]

solids = {"water", "deadtree", "tree"}

texpack = pygame.Surface((128*(len(textures_img)), 128), flags=pygame.SRCALPHA).convert_alpha()
for i, m in enumerate(textures_img):
    texpack.blit(m, (128*i,0))
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

def save_game():
    print("saving game")
    sav = open('quadtree.pickle', 'wb')
    data = {'map': map, 'pos': pos}
    pickle.dump(data, sav)
    sav.close()

def get_mat(x, y):
    map_data = map.get_data(int(x), int(y))
    if (map_data != None):
        mat = map_data[0]
    else:
        r = sin(0.546354 * y/5) * sin(0.876964 * y/5) * sin(1.45638 * y/5 + 1.82266 * x/5) + cos(1.94367 * x/5 - 1.743247 * y/5) * cos(0.869632 * x/5)
        if (r < -.9):
            mat = "water"
        elif (r < -.5):
            mat = "dirt"
        elif (r > 0.5):
            mat = "dirt"
        elif (abs(r) < 0.1):
            mat = "cabbage"
        else:
            mat = "cabbage"
        map.cache_data(int(x), int(y), (mat, -1))
    return mat
def decorate(x, y, mat):
    map_data = map.get_data(int(x), int(y))
    dec = None
    if (map_data != None and map_data[1] != -1):
        dec = map_data[1]
    else:
        r = point_to_random(x, y)
        if r < 0.7 and mat == "cabbage":
            dec = "grass"
        if r < 0.001 and mat == "dirt":
            dec = "deadtree"
        if r > 0.98 and mat == "dirt":
            dec = "tree"
        map.cache_data(int(x), int(y), (mat, dec))
    return dec

def draw_tile(mat, x, y, screen_coords):
    # render material texture using int tile coords relitive to the screen
    Renderer.vert_list.append(((1 - screen_coords[0] % tile_size + tile_size * x)/window_size[0]*2,
                               (1 - screen_coords[1] % tile_size + tile_size * y)/window_size[1]*2,
                               0.0, tile_size/window_size[0]*2, tile_size/window_size[1]*2, mat))
def draw_sprite(spr, x, y, z, w, h):
    # render sprite texture using float pixel coords relitive to the screen
    Renderer.vert_list.append((x/window_size[0]*2, (y)/window_size[1]*2, z, w/window_size[0]*2, h/window_size[1]*2, spr))
def draw_object(decor, x, y, z, w, h, screen_coords):
    # render sprite texture using tile coords relitive to the world
    draw_sprite( decor,
        1 - screen_coords[0] % tile_size + tile_size*(x-w/2+0.5)-screen_coords[0]//tile_size*tile_size - cos(curtime / 1000 + x+y*y) * tile_size / 20,
        1 - screen_coords[1] % tile_size + tile_size*(y-h/2+0.5)-screen_coords[1]//tile_size*tile_size - sin(curtime / 300  + x+y*y) * tile_size / 20,
        z+sin(curtime / 300 + x+y*y)/50,
        w * tile_size + int(cos(curtime / 1000 + x+y*y) * tile_size / 10),
        h * tile_size + int(sin(curtime / 300 + x+y*y) * tile_size / 10))
def draw_object_foreground(decor, x, y, w, h, screen_coords):
    # render sprite texture using tile coords relitive to the world
    draw_sprite( decor,
        1 - screen_coords[0] % tile_size + tile_size*(x-w/2+0.5)-screen_coords[0]//tile_size*tile_size - cos(curtime / 1000 + x+y*y) * tile_size / 10,
        1 - screen_coords[1] % tile_size + tile_size*(y-h/2+0.5)-screen_coords[1]//tile_size*tile_size - sin(curtime / 300  + x+y*y) * tile_size / 10,
        1.0,
        w * tile_size + int(cos(curtime / 1000 + x+y*y) * tile_size / 5),
        h * tile_size + int(sin(curtime / 300 + x+y*y) * tile_size / 5))

velocity = [0, 0]
acceleration = 1/20000

keydown_set = set()
mouse_pos = pygame.mouse.get_pos()
def handle_keys():
    global running
    global mouse_pos
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                save_game()
                running = False
            else:
                keydown_set.add(event.key)
        elif event.type == pygame.KEYUP:
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
        save_game()
        keydown_set.remove("unclick1")
    velocity[0] -= velocity[0] / 10
    velocity[1] -= velocity[1] / 10
    mat = get_mat(ceil(pos[0] - 1), ceil(pos[1] - 1))
    spr = decorate(ceil(pos[0] - 1), ceil(pos[1] - 1), mat)
    if (mat in solids or spr != None and spr in solids):
        pos[1] += 1
        velocity = [0, 0]
    else:
        mat2 = get_mat(ceil(pos[0] - 1 + dt*velocity[0]), ceil(pos[1] - 1 + dt*velocity[1]))
        spr2 = decorate(ceil(pos[0] - 1 + dt*velocity[0]), ceil(pos[1] - 1 + dt*velocity[1]), mat2)
        if (mat2 in solids or spr2 != None and spr2 in solids):
            velocity = [0, 0]
        else:
            pos[0] += dt*velocity[0]
            pos[1] += dt*velocity[1]
    screen_coords = [pos[0] * tile_size - window_size[0] // 2, pos[1] * tile_size - window_size[1] // 2]
    selected_tile = [mouse_pos[0] + screen_coords[0] % tile_size,
                     mouse_pos[1] + screen_coords[1] % tile_size]
    selected_tile = [-screen_coords[0] % tile_size + tile_size * ceil(selected_tile[0] / tile_size) - window_size[0] // 2,
                     -screen_coords[1] % tile_size + tile_size * ceil(selected_tile[1] / tile_size) - window_size[1] // 2]
    selected_tile = [ceil(pos[0] + ceil(selected_tile[0] / tile_size) - 3),
                     ceil(pos[1] + ceil(selected_tile[1] / tile_size) - 3)]
    if "mouse1" in keydown_set:
        map.set_data(int(selected_tile[0]), int(selected_tile[1]), ("tiles", None))
    for y in range(2 + window_size[1] // tile_size):
        for x in range(2 + window_size[0] // tile_size):
            tile_coords = [ceil(screen_coords[0] / tile_size) + x - 1,
                           ceil(screen_coords[1] / tile_size) + y - 1]
            mat = get_mat(tile_coords[0], tile_coords[1])
            draw_tile(get_tex(mat, curtime/200+tile_coords[0]+tile_coords[0]+tile_coords[1]), x, y, screen_coords)
    for y in range(2 + window_size[1] // tile_size):
        for x in range(2 + window_size[0] // tile_size):
            tile_coords = [ceil(screen_coords[0] / tile_size) + x - 1,
                           ceil(screen_coords[1] / tile_size) + y - 1]
            mat = get_mat(tile_coords[0], tile_coords[1])
            decor = decorate(tile_coords[0], tile_coords[1], mat)
            if decor == "grass":
                draw_object(get_tex(decor, 0), tile_coords[0], tile_coords[1], 0.35, 2, 2, screen_coords)
            if decor == "tree":
                draw_object(get_tex("treestump", 0), tile_coords[0], tile_coords[1], 0.35, 1, 1, screen_coords)
            if decor == "deadtree":
                treelog = get_tex("treelog", 0)
                draw_object(treelog, tile_coords[0], tile_coords[1], 0.1, 1, 1, screen_coords)
                draw_object(treelog, tile_coords[0], tile_coords[1], 0.45, 1, 1, screen_coords)
                draw_object(treelog, tile_coords[0], tile_coords[1], 0.66, 1, 1, screen_coords)
                draw_object(treelog, tile_coords[0], tile_coords[1], 0.8, 1, 1, screen_coords)
                draw_object(treelog, tile_coords[0], tile_coords[1], 0.9, 1, 1, screen_coords)
    draw_sprite(get_tex("char"+str(char_direction),curtime), window_size[0] / 2 - tile_size, window_size[1] / 2 - tile_size, 0.75, 2 * tile_size, 2 * tile_size)
    for y in range(7 + window_size[1] // tile_size):
        for x in range(7 + window_size[0] // tile_size):
            tile_coords = [ceil(screen_coords[0] / tile_size) + x - 4,
                           ceil(screen_coords[1] / tile_size) + y - 4]
            mat = get_mat(tile_coords[0], tile_coords[1])
            decor = decorate(tile_coords[0], tile_coords[1], mat)
            if decor == "tree" or decor == "deadtree":
                draw_object_foreground(get_tex(decor, 0), tile_coords[0], tile_coords[1], 8, 8, screen_coords)
    draw_tile(get_tex("selection",0), selected_tile[0] - screen_coords[0]//tile_size, selected_tile[1] - screen_coords[1]//tile_size, screen_coords)
    Renderer.render( curtime, (mouse_pos[0]/window_size[0]*2-1, 1-mouse_pos[1]/window_size[1]*2))
    pygame.display.flip()
    clock.tick(FPS)

while running:
    #cProfile.run('main()')
    main()