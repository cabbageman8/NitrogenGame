import pygame
from pygame.locals import *
from PIL import Image
import pickle
from math import pi, tau, sin, cos, tan, asin, acos, atan, ceil, floor, remainder
import cProfile
from quadtree import root_node
from glrenderer import glrenderer
import sys
import os
pygame.init()
pygame.font.init()

FPS=60
clock = pygame.time.Clock()
#window_size=(1000, 1000)
#window_size=(1920, 1080)
window_size=(2560, 1440)
tile_size = 75

pygame.display.set_mode(window_size, DOUBLEBUF|OPENGL, vsync=1)
silombol = pygame.font.Font(os.path.join("data", "SilomBol.ttf"), ceil(window_size[1]/32))
textures = ["null", "selection", "water", "planks", "dirt", "tiles", "weeds", "cabbage", "grass", "deadtree", "normaltree",
            "treelog", "treestump", "treetrunk", "wall", "block", "hexpavers", "roughseedgrass", "stones",
            "lushundergrowth", "gravillearobustadirt", "basil", "bottlebrushdirt", "sheoakdirt", "mushrooms", "fern",
            "bush", "tarragon", "lawn", "gravilearobustatree"]
textures_img = []
texd = {}
solids = {"water", "deadtree", "normaltree", "gravilearobustatree", "treelog", "treestump", "wall"}
animated = {"water"}
blocks = {"block", "wall"}
#          materials,                             shrubs,               trees
biomes = ((("water","weeds","dirt","weeds","dirt"), ("grass", "bush"), ("normaltree",)),
          (("gravillearobustadirt", "roughseedgrass"), ("grass", "fern"), ("gravilearobustatree",)),
          (("bottlebrushdirt","roughseedgrass"), ("grass", "mushrooms"), ("normaltree",)),
          (("sheoakdirt","roughseedgrass"), ("mushrooms", "fern"), ("normaltree",)),
          (("water","stones"), (), ()))
def load_textures():
    global texd
    global textures_img
    textures_img = []
    for mat in textures:
        file = Image.open(os.path.join("data", mat + ".png")).convert("RGBA")
        frame_list = []
        for i in range(file.height//file.width):
            frame = pygame.image.fromstring( file.crop(Rect(0,file.width*i,file.width,file.width*(i+1))).resize([128, 128], resample=Image.NEAREST).tobytes(), [128, 128], "RGBA").convert_alpha()
            frame_list.append(len(textures_img))
            textures_img.append(frame)
        texd.update({mat : frame_list})

    file = Image.open(os.path.join("data", "char32.png")).convert("RGBA")
    fileb = Image.open(os.path.join("data", "charb32.png")).convert("RGBA")
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
load_textures()
def get_tex(name, index):
    return texd[name][int(index)%len(texd[name])]

texpack = pygame.Surface((min(128*128, 128*(len(textures_img))), 128*(1+len(textures_img)//128)), flags=pygame.SRCALPHA).convert_alpha()
for i, m in enumerate(textures_img):
    texpack.blit(m, (128*(i%128),128*(i//128)))
pygame.image.save(texpack, "texpack.png")
overlay = pygame.Surface(window_size).convert_alpha()
overlay.fill((255,255,255,155))
text = ["CabbageGame Alpha", "wasd for movement", "up/down for zoom", "esc for save and quit", "F4 for fullscreen", "scroll to select item", "LM place block", "MM pick-block", "RM place decoration", "press h to start"]
for i, t in enumerate(text):
    overlay.blit(silombol.render(t, True, (0, 0, 0)), (0, silombol.size(t)[1]*i))
Renderer = glrenderer(texpack, overlay)

Renderer.render((0, 0))
pygame.display.flip()

def seeded_random(a):
    output = (41406202+14874235*a)%79493069
    output = (43915416+77751829*output)%76741089
    output = (66947287+44145130*output)%90370934
    output = (64705634+34405431*output)%23928528
    output = (24300417+80810414*output)%10000
    return output/10000
def point_to_random(x, y):
    return seeded_random(x + x * x * y * y * y + y * y)

try:
    sav = open(os.path.join("data", "savedata.pickle") , 'rb')
    data = pickle.load(sav)
    map = data['map']
    pos = data['pos']
    hotbar = data['hotbar']
    sav.close()
except:
    map = root_node()
    pos = [0.0, 0.0]
    hotbar = [("null", None), ("water", None), ("hexpavers", None), ("planks", "tiles"), ("wall", "wall"), ("dirt", None), ("weeds", None), ("dirt", "tree"), ("dirt", "deadtree")]
    sav = open(os.path.join("data", "savedata.pickle") , 'wb')
    data = {'map': map, 'pos': pos, 'hotbar': hotbar}
    pickle.dump(data, sav)
    sav.close()
    print('could not load, blank save loaded')
hotbar = [("lawn", "mushrooms"), ("stones", None), ("hexpavers", None), ("lawn", None), ("wall", "block"), ("dirt", "bush"), ("dirt", "tarragon"), ("lushundergrowth", "basil"), ("bottlebrushdirt", None)]
def save_game():
    print("saving game")
    sav = open(os.path.join("data", "savedata.pickle"), 'wb')
    data = {'map': map, 'pos': pos, 'hotbar': hotbar}
    pickle.dump(data, sav)
    sav.close()

selected_item_slot = 0

def construct_overlay():
    overlay.fill((0, 0, 0, 0))
    for i in range(9):
        overlay.blit(textures_img[texd[hotbar[i][0]][0]], (0, 110 * i - 110 * 4.5 + overlay.get_size()[1] / 2))
        overlay.blit(textures_img[texd["selection"][0]], (0, 110 * i - 110*4.5 + overlay.get_size()[1] / 2))
        #overlay.blit(textures_img[1], (100*i-450+overlay.get_size()[0]/2, overlay.get_size()[1]-100))
    overlay.blit(textures_img[texd["selection"][0]], (0, 110 * selected_item_slot - 110 * 4.5 + overlay.get_size()[1] / 2))
    overlay.blit(silombol.render(str(selected_tile), True, (0, 0, 0)), (100, 100))
    slot = hotbar[int(selected_item_slot)]
    if slot[1]:
        t = str(slot[0]) + " with " + str(slot[1])
    else:
        t = str(slot[0])

    overlay.blit(silombol.render(t, True, (0, 0, 0)), (100, 100+silombol.size(t)[1]))
    Renderer.update_overlay(overlay)

def get_biome(x, y):
    temp = sin(0.70688 * y/40) * sin(0.08321 * y/40) * sin(1.20191 * y/40 + 1.07952 * x/40) + cos(1.83391 * x/40 / 5 - 1.00643 * y/40 / 5) * cos(0.27705 * x/40 / 5)
    moisture = sin(0.56554 * y/80) * sin(0.49491 * y/80) * sin(1.63167 * y/80 + 1.36682 * x/80) + cos(1.19063 * x/80 / 5 - 1.52815 * y/80 / 5) * cos(0.13701 * x/80 / 5)
    biome = biomes[int(point_to_random(int((temp+1)/2*len(biomes)), int((moisture+1)/2*len(biomes)))*len(biomes))]
    return biome
def get_mat(x, y):
    map_data = map.get_data(int(x), int(y))
    if (map_data != None):
        mat = map_data[0]
    else:
        local = max(-1, min(1, sin(0.546354 * y/5) * sin(0.876964 * y/5) * sin(1.45638 * y/5 + 1.82266 * x/5) + cos(1.94367 * x/5 - 1.743247 * y/5) * cos(0.869632 * x/5) ))
        biome = get_biome(x, y)
        mat = biome[0][int((local+1)/2*(len(biome[0])-1))]
        map.cache_data(int(x), int(y), (mat, -1))
    return mat
def decorate(x, y, mat):
    map_data = map.get_data(int(x), int(y))
    dec = None
    if (map_data != None and map_data[1] != -1):
        dec = map_data[1]
    else:
        r = point_to_random(x, y)
        biome = get_biome(x, y)
        if (r < 0.7 and (mat == "weeds" or mat == "roughseedgrass")) or (r < 0.1 and "dirt" in mat):
            dec = biome[1][int(r * (len(biome[1])))]
        if r > 0.98 and "dirt" in mat:
            dec = biome[2][int(r * (len(biome[2])))]
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
        z+sin(x+y*y)/50,
        w * tile_size + int(cos(curtime / 1000 + x+y*y) * tile_size / 10),
        h * tile_size + int(sin(curtime / 300 + x+y*y) * tile_size / 10))
def draw_object_foreground(decor, x, y, w, h, screen_coords):
    # render sprite texture using tile coords relitive to the world
    draw_sprite( decor,
        1 - screen_coords[0] % tile_size + tile_size*(x-w/2+0.5)-screen_coords[0]//tile_size*tile_size - cos(curtime / 1000 + x+y*y) * tile_size / 20,
        1 - screen_coords[1] % tile_size + tile_size*(y-h/2+0.5)-screen_coords[1]//tile_size*tile_size - sin(curtime / 300  + x+y*y) * tile_size / 20,
        2.0,
        w * tile_size + int(cos(curtime / 1000 + x+y*y) * tile_size / 10),
        h * tile_size + int(sin(curtime / 300 + x+y*y) * tile_size / 10))
def draw_structure(decor, x, y, z, w, h, screen_coords):
    # render sprite texture using tile coords relitive to the world
    draw_sprite( decor,
        1 - screen_coords[0] % tile_size + tile_size*(x-w/2+0.5)-screen_coords[0]//tile_size*tile_size,
        1 - screen_coords[1] % tile_size + tile_size*(y-h/2+0.5)-screen_coords[1]//tile_size*tile_size,
        z,
        w * tile_size,
        h * tile_size)

velocity = [0, 0]
acceleration = 1/6000

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
        elif event.type == pygame.KEYUP and event.key != pygame.K_F4:
            keydown_set.remove(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            keydown_set.add("mouse"+str(event.button))
        elif event.type == pygame.MOUSEBUTTONUP:
            keydown_set.remove("mouse"+str(event.button))
            if (event.button in (1, 4, 5)):
                keydown_set.add("unclick"+str(event.button))

running=True
frame = 0
curtime = pygame.time.get_ticks()
char_direction = 0

def main():
    global frame
    global velocity
    global curtime
    global tile_size
    global selected_tile
    global char_direction
    global overlay
    global window_size
    global selected_item_slot
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
        if (tile_size < 30):
            tile_size = 30
    if pygame.K_h in keydown_set:
        construct_overlay()
    if pygame.K_c in keydown_set:
        map.cache.clear()
    if "unclick1" in keydown_set:
        save_game()
        keydown_set.remove("unclick1")
        construct_overlay()
    if pygame.K_F4 in keydown_set:
        pygame.display.toggle_fullscreen()
        window_size = pygame.display.get_window_size()
        overlay = pygame.Surface(window_size).convert_alpha()
        construct_overlay()
        keydown_set.remove(pygame.K_F4)

    velocity[0] -= velocity[0] / 3
    velocity[1] -= velocity[1] / 3
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
    selected_data = map.get_data(int(selected_tile[0]), int(selected_tile[1]))
    if "mouse1" in keydown_set:
        if Rect(0, overlay.get_size()[1] / 2 - 110 * 4.5, 110, 110*9).collidepoint(mouse_pos):
            selected_item_slot = (mouse_pos[1]-(overlay.get_size()[1] / 2 - 110 * 4.5))//110
            construct_overlay()
        else:
            map.set_data(int(selected_tile[0]), int(selected_tile[1]), (hotbar[int(selected_item_slot)][0], None))
    if "mouse2" in keydown_set:
        hotbar[int(selected_item_slot)] = selected_data
        construct_overlay()
    if "mouse3" in keydown_set:
        map.set_data(int(selected_tile[0]), int(selected_tile[1]), (selected_data[0], hotbar[int(selected_item_slot)][1]))
    if "unclick4" in keydown_set:
        selected_item_slot = (selected_item_slot-1)%9
        construct_overlay()
        keydown_set.remove("unclick4")
    if "unclick5" in keydown_set:
        selected_item_slot = (selected_item_slot+1)%9
        construct_overlay()
        keydown_set.remove("unclick5")
    for i2, i in enumerate((1, -1)):
        for y in range(ceil((2+i2+window_size[1] // tile_size) / 2)):
            y2 = (y*i)%(window_size[1]//tile_size+2)
            for j2, j in enumerate((1, -1)):
                for x in range(ceil((2+j2+window_size[0] // tile_size)/2)):
                    x2 = (x * j) % (window_size[0] // tile_size+2)
                    tile_coords = [ceil(screen_coords[0] / tile_size) + x2 - 1,
                                   ceil(screen_coords[1] / tile_size) + y2 - 1]
                    mat = get_mat(tile_coords[0], tile_coords[1])
                    if (mat in animated):
                        index = curtime/200+tile_coords[0]*tile_coords[0]+tile_coords[1]
                    elif (mat == "hexpavers"):
                        index = int(tile_coords[0]*13 + tile_coords[1] * tile_coords[1]*7)*2+tile_coords[0]
                    else:
                        index = (tile_coords[0]*13 + tile_coords[1] * tile_coords[1]*7)
                    draw_tile(get_tex(mat, index), x2, y2, screen_coords)

                    decor = decorate(tile_coords[0], tile_coords[1], mat)
                    if decor == None:
                        pass
                    elif decor == "mushrooms":
                        draw_object(get_tex(decor, index), tile_coords[0], tile_coords[1], 0.1, 1, 1, screen_coords)
                    elif decor == "normaltree" or decor == "gravilearobustatree" or decor == "treestump" or decor == "deadtree" or decor == "treelog":
                        draw_structure(get_tex("treelog", 0), tile_coords[0], tile_coords[1], 0.1, 1, 1, screen_coords)
                        draw_structure(get_tex("treetrunk", 0), tile_coords[0], tile_coords[1], 1.0, 0, -1, screen_coords)
                        draw_structure(get_tex("treetrunk", 0), tile_coords[0], tile_coords[1], 1.0, 1, 0, screen_coords)
                        draw_structure(get_tex("treestump", 0), tile_coords[0], tile_coords[1], 1.0, 1, 1, screen_coords)
                    elif decor in blocks:
                        wall = get_tex(decor, 0)
                        draw_structure(wall, tile_coords[0], tile_coords[1]-((y2>window_size[1]//tile_size//2)-.5), 0.8, 1, 0, screen_coords)
                        draw_structure(wall, tile_coords[0]-((x2>window_size[0]//tile_size//2)-.5), tile_coords[1], 0.8, 0, 1, screen_coords)
                        draw_structure(wall, tile_coords[0], tile_coords[1], 0.8, 1, 1, screen_coords)
                    elif decor == "tiles":
                        draw_structure(get_tex("tiles", 0), tile_coords[0], tile_coords[1], 1.8, 1, 1, screen_coords)
                    else:
                        draw_object(get_tex(decor, 0), tile_coords[0], tile_coords[1], 0.35, -2, -2, screen_coords)
                        draw_object(get_tex(decor, 0), tile_coords[0], tile_coords[1], 0.5, 2, 2, screen_coords)
    draw_sprite(get_tex("char"+str(char_direction),(abs(velocity[0])+abs(velocity[1]) > 0.001)*curtime/200), window_size[0] / 2 - tile_size, window_size[1] / 2 - tile_size, 0.75, 2 * tile_size, 2 * tile_size)
    for y in range(7 + window_size[1] // tile_size):
        for x in range(7 + window_size[0] // tile_size):
            tile_coords = [ceil(screen_coords[0] / tile_size) + x - 4,
                           ceil(screen_coords[1] / tile_size) + y - 4]
            mat = get_mat(tile_coords[0], tile_coords[1])
            decor = decorate(tile_coords[0], tile_coords[1], mat)
            if decor == "normaltree" or decor == "gravilearobustatree" or decor == "deadtree":
                draw_object_foreground(get_tex(decor, 0), tile_coords[0], tile_coords[1], 8, 8, screen_coords)
    draw_tile(get_tex("selection",0), selected_tile[0] - screen_coords[0]//tile_size, selected_tile[1] - screen_coords[1]//tile_size, screen_coords)

    Renderer.render((mouse_pos[0]/window_size[0]*2-1, 1-mouse_pos[1]/window_size[1]*2))
    pygame.display.flip()
    clock.tick(FPS)

while running:
    #cProfile.run('main()')
    main()