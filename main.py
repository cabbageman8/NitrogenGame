# Nitrogen Alpha
# to compile; run
# py -m nuitka --standalone --follow-imports --include-data-dir=data=data main.py
import pygame
from pygame.locals import *
from PIL import Image
import pickle
from math import pi, tau, sin, cos, tan, asin, acos, atan, ceil, floor, sqrt, log
import cProfile
from quadtree import root_node
from glrenderer import glrenderer
import sys
import os
import time
import datetime
import requests
import base64

logfile = open("log.txt", 'w')
sys.stderr = logfile
sys.stdout = logfile

pygame.init()
pygame.font.init()
pygame.joystick.init()

print("number of gamepads:", pygame.joystick.get_count())
gamepads = []
for i in range(pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    gamepads.append(joystick)


FPS=60
clock = pygame.time.Clock()
#window_size=(1000, 1000)
window_size=(1920, 1080)
#window_size=(2560, 1440)
tile_size = 75

pygame.display.set_mode(window_size, DOUBLEBUF|OPENGL)
silombol = pygame.font.Font(os.path.join("data", "SilomBol.ttf"), ceil(window_size[1]/32))
textures = ["None", "selection", "water", "planks", "dirt", "tiles", "weeds", "cabbage", "grass", "deadtree", "normaltree",
            "treelog", "treestump", "treetrunk", "wall", "block", "hexpavers", "roughseedgrass", "stones",
            "lushundergrowth", "gravillearobustadirt", "basil", "bottlebrushdirt", "sheoakdirt", "mushrooms", "fern",
            "bush", "tarragon", "lawn", "gravilearobustatree", "bottlebrushtree", "sheoaktree", "fossil", "sand", "cactus",
            "flytrap", "birchtreelog", "birchtreetrunk", "birchtreestump", "lillypad",
            "freshwater", "axe", "spade", "cloud", "talldrygrass"]
textures_img = []
texd = {}
solids = {"deadtree", "normaltree", "gravilearobustatree", "bottlebrushtree", "sheoaktree", "treelog", "birchtreelog", "treestump", "birchtreestump", "wall", "cactus"}
entities = ["charhands","charhandstouch", "charhead", "charlegs"]
animated = {"water", "freshwater"}
blocks = {"block", "wall"}
roofing = {"tiles", "planks"}
difficult_terrain = {"water", "flytrap", "freshwater"}
#          materials,                             shrubs,               trees
biomes = ((("freshwater","weeds","dirt","weeds","dirt"), ("grass", "bush"), ("normaltree",)),
            (("gravillearobustadirt", "roughseedgrass"), ("grass", "fern"), ("normaltree", "gravilearobustatree",)),
            (("bottlebrushdirt","roughseedgrass"), ("grass",), ("normaltree", "bottlebrushtree",)),
            (("sheoakdirt","roughseedgrass"), ("mushrooms", "fern"), ("deadtree", "sheoaktree", "sheoaktree",)),
            (("freshwater","weeds","freshwater"), ("grass", "bush", "flytrap", "lillypad",), ("normaltree",)),
            (("sand", "fossil"), ("grass","grass", "cactus",), ("normaltree",)),
            (("water","stones"), (None, ), (None, )))
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

    for e in entities:
        file = Image.open(os.path.join("data", "entities", e+".png")).convert("RGBA")
        fileb = Image.open(os.path.join("data", "entities", e+"45.png")).convert("RGBA")
        for i in range(4):
            frame_list = []
            for j in range(file.height // file.width):
                frame = pygame.image.fromstring( file.crop(Rect(0, file.width * j, file.width, file.width * (j + 1))).resize([128, 128], resample=Image.NEAREST).rotate(90*i).tobytes(), [128, 128], "RGBA").convert_alpha()
                frame_list.append(len(textures_img))
                textures_img.append(frame)
            texd.update({e+str(i*2): frame_list})
            frame_list = []
            for j in range(fileb.height // fileb.width):
                frame = pygame.image.fromstring( fileb.crop(Rect(0, fileb.width * j, file.width, file.width * (j + 1))).resize([128, 128], resample=Image.NEAREST).rotate(90*i).tobytes(), [128, 128], "RGBA").convert_alpha()
                frame_list.append(len(textures_img))
                textures_img.append(frame)
            texd.update({e+str(i*2+1): frame_list})
load_textures()
def get_tex(name, index):
    return texd[name][int(index)%len(texd[name])]

texpack = pygame.Surface((min(128*128, 128*(len(textures_img))), 128*(1+len(textures_img)//128)), flags=pygame.SRCALPHA).convert_alpha()
for i, m in enumerate(textures_img):
    texpack.blit(m, (128*(i%128),128*(i//128)))
pygame.image.save(texpack, "texpack.png")
overlay = pygame.Surface(window_size).convert_alpha()
overlay.fill((255,255,255,155))
text = ["connecting to server"]
for i, t in enumerate(text):
    overlay.blit(silombol.render(t, True, (0, 0, 0)), (0, silombol.size(t)[1]*i))
Renderer = glrenderer(texpack, overlay)

Renderer.render((0, 0), tile_size)
pygame.display.flip()

pygame.mixer.music.load('data/ambience.wav')
pygame.mixer.music.play(-1)
shovel_sfx = pygame.mixer.Sound('data/shovel.wav')
shovel_sfx.set_volume(0.5)
grass_step_sfx = pygame.mixer.Sound('data/grass-step.wav')
grass_step_sfx.set_volume(0.5)
hit_sfx = pygame.mixer.Sound('data/hit.wav')
hit_sfx.set_volume(0.5)
fish_sfx = pygame.mixer.Sound('data/fish.wav')
fish_sfx.set_volume(0.5)
crumple_sfx = pygame.mixer.Sound('data/crumple.wav')
crumple_sfx.set_volume(0.5)
jump_into_water_sfx = pygame.mixer.Sound('data/jump-into-water.wav')
jump_into_water_sfx.set_volume(0.5)

def seeded_random(a):
    output = (41406202+14874235*a     )%79493069
    output = (43915416+77751829*output)%76741089
    output = (66947287+44145130*output)%90370934
    output = (64705634+34405431*output)%23928528
    output = (24300417+80810414*output)%10000
    return output/10000
def point_to_random(x, y):
    return seeded_random(x + x * x * y * y * y + y * y)

text = ["visit cabbage.moe", "CabbageGame Alpha", "wasd for movement", "esc for save and quit", "F4 for fullscreen", "scroll to select item", "LM place block", "MM pick-block", "RM place decoration", "press h to start"]
# get local data
try:
    sav = open(os.path.join("data", "savedata.pickle"), 'rb')
    data = pickle.load(sav)
    pos = data['pos']
    hotbar = data['hotbar']
    player_number = data['player_number']
    sav.close()
    text.append('loaded local save')
except:
    pos = [pi, tau]
    hotbar = [[None, 0,0], [None, 0,0], [None, 0,0], [None, 0,0], [None, 0,0], [None, 0,0], [None, 0,0], [None, 0,0], [None, 0,0]]
    player_number = int(seeded_random(time.time()%100000000)*10000)
    sav = open(os.path.join("data", "savedata.pickle") , 'wb')
    data = {'pos': pos, 'hotbar': hotbar, 'player_number':player_number}
    pickle.dump(data, sav)
    sav.close()
    text.append('could not find local save, blank save loaded')
# get server data
try:
    resp = requests.get("http://cabbageserver.ddns.net:27448/bin", timeout=2)
    sav = data = pickle.loads(base64.b64decode(resp.content))
    map = data['map']
    text.append('loaded save from server')
except:
    map = root_node()
    text.append('could not reach server, blank save loaded, progress will not be saved')

def render_text(text):
    global overlay
    global Renderer
    overlay.fill((255,255,255,155))
    for i, t in enumerate(text):
        overlay.blit(silombol.render(t, True, (0, 0, 0)), (0, silombol.size(t)[1]*i))
    Renderer.update_overlay(overlay)
render_text(text)

#hotbar = [["treestump", 1, 1], ["treestump", 1, 1], ["birchtreestump", 1, 1], ["treestump", 1, 1], ["wall", 1, 1000], ["tiles", 1, 1000], ["dirt", 0, 1], ["lushundergrowth", 0, 1], ["bottlebrushdirt", 0, 1]]
#hotbar[0] = ["axe", 1, 1]
#hotbar[1] = ["spade", 1, 1]
#hotbar[1] = ["talldrygrass", 1, 999]
def save_game():
    print("saving game")
    sav = open(os.path.join("data", "savedata.pickle"), 'wb')
    data = {'pos': pos, 'hotbar': hotbar, 'player_number':player_number}
    pickle.dump(data, sav)
    sav.close()
    map.save_to_server()
selected_item_slot = 0

def construct_overlay():
    overlay.fill((0, 0, 0, 0))
    overlay.blit(textures_img[texd["selection"][0]], (0, 128 * selected_item_slot - 128 * 4.5 + overlay.get_size()[1] / 2))
    for i in range(9):
        #overlay.blit(textures_img[texd["block"][0]], (0, 110 * i - 110 * 4.5 + overlay.get_size()[1] / 2))
        #overlay.blit(textures_img[texd["selection"][0]], (0, 110 * i - 110 * 4.5 + overlay.get_size()[1] / 2))
        if hotbar[i][0] != None and hotbar[i][2] > 0:
            overlay.blit(textures_img[texd[hotbar[i][0]][0]], (0, 128 * i - 128 * 4.5 + overlay.get_size()[1] / 2))
        #overlay.blit(textures_img[1], (100*i-450+overlay.get_size()[0]/2, overlay.get_size()[1]-100))
    #overlay.blit(silombol.render(str(selected_tile), True, (0, 0, 0)), mouse_pos)
    slot = hotbar[int(selected_item_slot)]
    if slot[0] != None and slot[2] > 0:
        t = str(slot[0])
        if slot[2] > 1:
            t += " " + str(slot[2])
        overlay.blit(silombol.render(t, True, (0, 0, 0)), (10, 50+128 * selected_item_slot - 128 * 4.5 + overlay.get_size()[1] / 2+silombol.size(t)[1]))
    Renderer.update_overlay(overlay)

biome_size = 100
def get_biome(x, y):
    temp = sin(0.70688 * y/biome_size) * sin(0.08321 * y/biome_size) * sin(1.20191 * y/biome_size + 1.07952 * x/biome_size) + cos(1.83391 * x/biome_size / 5 - 1.00643 * y/biome_size / 5) * cos(0.27705 * x/biome_size / 5)
    moisture = sin(0.56554 * y/biome_size) * sin(0.49491 * y/biome_size) * sin(1.63167 * y/biome_size + 1.36682 * x/biome_size) + cos(1.19063 * x/biome_size / 7 - 1.52815 * y/biome_size / 7) * cos(0.13701 * x/biome_size / 7)
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
        if ((r < 0.7 and (mat == "weeds" or mat == "roughseedgrass"))) or (r < 0.1 and ("dirt" in mat or "sand" in mat)) or "water" in mat:
            dec = biome[1][int(r * 100) % len(biome[1])]
            if "water" in mat and dec != "lillypad" or not "water" in mat and dec == "lillypad":
                dec = None
        if r > 0.98 and "dirt" in mat:
            dec = biome[2][int(r * 100) % len(biome[2])]
        map.cache_data(int(x), int(y), (mat, dec))
    return dec

def draw_tile(mat, x, y, screen_coords):
    # render material texture using int tile coords relitive to the screen
    Renderer.tile_list.append(((1 - screen_coords[0] % tile_size + tile_size * x)/window_size[0]*2,
                               (1 - screen_coords[1] % tile_size + tile_size * y)/window_size[1]*2,
                               0.0, tile_size/window_size[0]*2, tile_size/window_size[1]*2, mat))
def draw_sprite(spr, x, y, z, w, h):
    # render sprite texture using float pixel coords relitive to the screen
    Renderer.vert_list.append((x/window_size[0]*2, (y)/window_size[1]*2, z, w/window_size[0]*2, h/window_size[1]*2, spr))
def draw_object(decor, x, y, z, w, h, screen_coords):
    # render sprite texture using tile coords relitive to the world
    draw_sprite( decor,
        1 - screen_coords[0] % tile_size + tile_size*(x-w/2+0.5)-screen_coords[0]//tile_size*tile_size - cos(curtime / 1000 + (x+y*y)%1024) * tile_size / 20,
        1 - screen_coords[1] % tile_size + tile_size*(y-h/2+0.5)-screen_coords[1]//tile_size*tile_size - sin(curtime / 300  + (x+y*y)%1024) * tile_size / 20,
        z+sin(x+y*y)/50,
        w * tile_size + int(cos(curtime / 1000 + (x+y*y)%1024) * tile_size / 10),
        h * tile_size + int(sin(curtime / 300 + (x+y*y)%1024) * tile_size / 10))
def draw_object_foreground(decor, x, y, z, w, h, screen_coords):
    # render sprite texture using tile coords relitive to the world
    draw_sprite( decor,
        1 - screen_coords[0] % tile_size + tile_size*(x-w/2+0.5)-screen_coords[0]//tile_size*tile_size - cos(curtime / 1000 + (x+y*y)%1024) * tile_size / 20,
        1 - screen_coords[1] % tile_size + tile_size*(y-h/2+0.5)-screen_coords[1]//tile_size*tile_size - sin(curtime / 300  + (x+y*y)%1024) * tile_size / 20,
        1+z,
        w * tile_size + int(cos(curtime / 1000 + (x+y*y)%1024) * tile_size / 10),
        h * tile_size + int(sin(curtime / 300 + (x+y*y)%1024) * tile_size / 10))
    Renderer.tile_list.insert(0, ((1 - screen_coords[0] % tile_size + tile_size*(x-w/2+0.5)-screen_coords[0]//tile_size*tile_size - cos(curtime / 1000 + (x+y*y)%1024) * tile_size / 20)/window_size[0]*2, (1 - screen_coords[1] % tile_size + tile_size*(y-h/2+0.5)-screen_coords[1]//tile_size*tile_size - sin(curtime / 300  + (x+y*y)%1024) * tile_size / 20)/window_size[1]*2, -z, (w * tile_size + int(cos(curtime / 1000 + (x+y*y)%1024) * tile_size / 10))/window_size[0]*2, (h * tile_size + int(sin(curtime / 300 + (x+y*y)%1024) * tile_size / 10))/window_size[1]*2, decor))
def draw_shadow(decor, x, y, z, w, h, screen_coords):
    # render sprite texture using tile coords relitive to the world
    Renderer.tile_list.insert(0, ((1 - screen_coords[0] % tile_size + tile_size*(x-w/2+0.5)-screen_coords[0]//tile_size*tile_size - cos(curtime / 1000 + (x+y*y)%1024) * tile_size / 20)/window_size[0]*2, (1 - screen_coords[1] % tile_size + tile_size*(y-h/2+0.5)-screen_coords[1]//tile_size*tile_size - sin(curtime / 300  + (x+y*y)%1024) * tile_size / 20)/window_size[1]*2, -z, (w * tile_size + int(cos(curtime / 1000 + (x+y*y)%1024) * tile_size / 10))/window_size[0]*2, (h * tile_size + int(sin(curtime / 300 + (x+y*y)%1024) * tile_size / 10))/window_size[1]*2, decor))
    Renderer.shadow_list.insert(0, ((1 - screen_coords[0] % tile_size + tile_size*(x-w/2+0.5)-screen_coords[0]//tile_size*tile_size - cos(curtime / 1000 + (x+y*y)%1024) * tile_size / 20)/window_size[0]*2, (1 - screen_coords[1] % tile_size + tile_size*(y-h/2+0.5)-screen_coords[1]//tile_size*tile_size - sin(curtime / 300  + (x+y*y)%1024) * tile_size / 20)/window_size[1]*2, -z, (w * tile_size + int(cos(curtime / 1000 + (x+y*y)%1024) * tile_size / 10))/window_size[0]*2, (h * tile_size + int(sin(curtime / 300 + (x+y*y)%1024) * tile_size / 10))/window_size[1]*2, decor))
def draw_structure(decor, x, y, z, w, h, screen_coords):
    # render sprite texture using tile coords relitive to the world
    draw_sprite( decor,
        1 - screen_coords[0] % tile_size + tile_size*(x-w/2+0.5)-screen_coords[0]//tile_size*tile_size,
        1 - screen_coords[1] % tile_size + tile_size*(y-h/2+0.5)-screen_coords[1]//tile_size*tile_size,
        z,
        w * tile_size,
        h * tile_size)
    if w * h == 0:
        Renderer.tile_list.insert(0, ((1 - screen_coords[0] % tile_size + tile_size*(x-w/2+0.5)-screen_coords[0]//tile_size*tile_size)/window_size[0]*2, (1 - screen_coords[1] % tile_size + tile_size*(y-h/2+0.5)-screen_coords[1]//tile_size*tile_size)/window_size[1]*2, -z, (w * tile_size)/window_size[0]*2, (h * tile_size )/window_size[1]*2, decor))


velocity = [0, 0]
acceleration = 1/300

keydown_set = set()
gamepad_set = set()
old_gamepad_set = set()
mouse_pos = pygame.mouse.get_pos()
def handle_keys():
    global running
    global mouse_pos
    global old_gamepad_set
    mouse_rel = pygame.mouse.get_rel()
    if mouse_rel[0] + mouse_rel[1]:
        mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                save_game()
                running = False
            keydown_set.add(event.key)
        elif event.type == pygame.KEYUP and event.key != pygame.K_F4:
            keydown_set.remove(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            keydown_set.add("mouse"+str(event.button))
            if (event.button in (1,)):
                keydown_set.add("click"+str(event.button))
        elif event.type == pygame.MOUSEBUTTONUP:
            keydown_set.remove("mouse"+str(event.button))
            if (event.button in (4, 5)):
                keydown_set.add("unclick"+str(event.button))
    old_gamepad_set = set(gamepad_set)
    gamepad_set.clear()
    for g in gamepads:
        for a in range(g.get_numaxes()):
            state = g.get_axis(a)
            if abs(state) > 0.333:
                if a == 0:
                    gamepad_set.add("stickx"+str(floor(state)*+2+1))
                elif a == 1:
                    gamepad_set.add("sticky"+str(floor(state)*-2-1))
                elif a == 3:
                    mouse_pos = [mouse_pos[0]+state*7, mouse_pos[1]]
                elif a == 4:
                    mouse_pos = [mouse_pos[0], mouse_pos[1]+state*7]
        for b in range(g.get_numbuttons()):
            state = g.get_button(b)
            if state:
                gamepad_set.add("button"+str(b))
                print("button"+str(b))
        for d in range(g.get_numhats()):
            x, y = g.get_hat(d)
            if x:
                gamepad_set.add("d-padx"+str(x))
            if y:
                gamepad_set.add("d-pady"+str(y))

running=True
frame = 0
curtime = pygame.time.get_ticks()
char_direction = 0
char_speed = 0
char_anim = 0
steptime = curtime
req = []
#req = grequests.post("http://cabbageserver.ddns.net:27448/player_update", data={str(player_number):str([pos[0], pos[1], char_direction, char_anim, char_speed])}, timeout=2)
#req.send()
player_text = []
last_server_update = 0

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
    global steptime
    global char_anim
    global req
    global player_text
    global last_server_update
    frame += 1
    dt = pygame.time.get_ticks() - curtime
    curtime = pygame.time.get_ticks()
    #frag_time.value = curtime
    handle_keys()
    if pygame.K_w in keydown_set or "sticky1" in gamepad_set:
        if pygame.K_a in keydown_set or "stickx-1" in gamepad_set:
            velocity[0] -= acceleration * 0.707106781187
            velocity[1] -= acceleration * 0.707106781187
            char_direction = 3
        elif pygame.K_d in keydown_set or "stickx1" in gamepad_set:
            velocity[0] += acceleration * 0.707106781187
            velocity[1] -= acceleration * 0.707106781187
            char_direction = 1
        else:
            velocity[1] -= acceleration
            char_direction = 0
    elif pygame.K_s in keydown_set or "sticky-1" in gamepad_set:
        if pygame.K_a in keydown_set or "stickx-1" in gamepad_set:
            velocity[0] -= acceleration * 0.707106781187
            velocity[1] += acceleration * 0.707106781187
            char_direction = 5
        elif pygame.K_d in keydown_set or "stickx1" in gamepad_set:
            velocity[0] += acceleration * 0.707106781187
            velocity[1] += acceleration * 0.707106781187
            char_direction = 7
        else:
            velocity[1] += acceleration
            char_direction = 4
    else:
        if pygame.K_a in keydown_set or "stickx-1" in gamepad_set:
            velocity[0] -= acceleration
            char_direction = 2
        elif pygame.K_d in keydown_set or "stickx1" in gamepad_set:
            velocity[0] += acceleration
            char_direction = 6
    if pygame.K_UP in keydown_set or "d-padx1" in gamepad_set:
        tile_size += 2
        if (tile_size > 75):
            tile_size = 75
    if pygame.K_DOWN in keydown_set or "d-padx-1" in gamepad_set:
        tile_size -= 2
        if (tile_size < 10):
            tile_size = 10
    if pygame.K_h in keydown_set:
        construct_overlay()
    if pygame.K_c in keydown_set:
        map.cache.clear()
    if pygame.K_F4 in keydown_set:
        pygame.display.toggle_fullscreen()
        window_size = pygame.display.get_window_size()
        overlay = pygame.Surface(window_size).convert_alpha()
        construct_overlay()
        keydown_set.remove(pygame.K_F4)

    mat = get_mat(ceil(pos[0] - 1), ceil(pos[1] - 1))
    spr = decorate(ceil(pos[0] - 1), ceil(pos[1] - 1), mat)
    if (spr != None and spr in solids):
        pos[1] += 1
        velocity = [0, 0]
    else:
        mat2 = get_mat(ceil(pos[0] - 1 + dt*velocity[0]), ceil(pos[1] - 1 + dt*velocity[1]))
        spr2 = decorate(ceil(pos[0] - 1 + dt*velocity[0]), ceil(pos[1] - 1 + dt*velocity[1]), mat2)
        if (not "water" in mat) and "water" in mat2:
            jump_into_water_sfx.stop()
            jump_into_water_sfx.play()
        if (spr2 != None and spr2 in solids):
            velocity = [0, 0]
        else:
            if (mat in difficult_terrain or spr2 != None and spr2 in difficult_terrain):
                dnom = 2
            else:
                dnom = 3
            velocity[0] -= velocity[0] / dnom
            velocity[1] -= velocity[1] / dnom
            pos[0] += dt * velocity[0]
            pos[1] += dt * velocity[1]
    screen_coords = [pos[0] * tile_size - window_size[0] // 2, pos[1] * tile_size - window_size[1] // 2]
    selected_tile = [mouse_pos[0] + screen_coords[0] % tile_size,
                     mouse_pos[1] + screen_coords[1] % tile_size]
    selected_tile = [-screen_coords[0] % tile_size + tile_size * ceil(selected_tile[0] / tile_size) - window_size[0] // 2,
                     -screen_coords[1] % tile_size + tile_size * ceil(selected_tile[1] / tile_size) - window_size[1] // 2]
    selected_tile = [ceil(pos[0] + ceil(selected_tile[0] / tile_size) - 3),
                     ceil(pos[1] + ceil(selected_tile[1] / tile_size) - 3)]
    selected_data = map.get_data(int(selected_tile[0]), int(selected_tile[1]))
    if "click1" in keydown_set or "button8" in gamepad_set and not "button8" in old_gamepad_set:
        if Rect(0, overlay.get_size()[1] / 2 - 110 * 4.5, 110, 110*9).collidepoint(mouse_pos):
            selected_item_slot = (mouse_pos[1]-(overlay.get_size()[1] / 2 - 110 * 4.5))//110
        else:
            if selected_data[1] != None:
                if hotbar[int(selected_item_slot)][2] == 0 or (selected_data[1] == hotbar[int(selected_item_slot)][0] and hotbar[int(selected_item_slot)][1] == 1):
                    shovel_sfx.play()
                    hotbar[int(selected_item_slot)] = [selected_data[1], 1, hotbar[int(selected_item_slot)][2] + 1]
                    map.set_data(int(selected_tile[0]), int(selected_tile[1]), (selected_data[0], None))
            elif selected_data[0] != None:
                if hotbar[int(selected_item_slot)][2] == 0 or (selected_data[0] == hotbar[int(selected_item_slot)][0] and hotbar[int(selected_item_slot)][1] == 0):
                    shovel_sfx.play()
                    hotbar[int(selected_item_slot)] = [selected_data[0], 0, hotbar[int(selected_item_slot)][2] + 1]
                    map.set_data(int(selected_tile[0]), int(selected_tile[1]), (get_biome(int(selected_tile[0]), int(selected_tile[1]))[0][0], None))
        construct_overlay()
        if "click1" in keydown_set:
            keydown_set.remove("click1")
    if "mouse2" in keydown_set:
        hotbar[int(selected_item_slot)] = [selected_data[0], 0, 1]
        construct_overlay()
    if "mouse3" in keydown_set or "button9" in gamepad_set:
        if hotbar[int(selected_item_slot)][2] > 0 and selected_data[hotbar[int(selected_item_slot)][1]] != hotbar[int(selected_item_slot)][0]:
            if hotbar[int(selected_item_slot)][1] == 0:
                hit_sfx.play()
                map.set_data(int(selected_tile[0]), int(selected_tile[1]), (hotbar[int(selected_item_slot)][0], selected_data[1]))
            if hotbar[int(selected_item_slot)][1] == 1:
                crumple_sfx.play()
                map.set_data(int(selected_tile[0]), int(selected_tile[1]), (selected_data[0], hotbar[int(selected_item_slot)][0]))
            hotbar[int(selected_item_slot)][2] -= 1
            construct_overlay()
    if "unclick4" in keydown_set or "d-pady1" in gamepad_set and not "d-pady1" in old_gamepad_set:
        selected_item_slot = (selected_item_slot-1)%9
        construct_overlay()
        if "unclick4" in keydown_set:
            keydown_set.remove("unclick4")
    if "unclick5" in keydown_set or "d-pady-1" in gamepad_set and not "d-pady-1" in old_gamepad_set:
        selected_item_slot = (selected_item_slot+1)%9
        construct_overlay()
        if "unclick5" in keydown_set:
            keydown_set.remove("unclick5")
    for i2, i in enumerate((1, -1)):
        for y in range(ceil((1+i2+window_size[1] // tile_size) / 2)):
            y2 = ((y+(i==1))*i)%(window_size[1]//tile_size+2)
            for j2, j in enumerate((1, -1)):
                for x in range(ceil((1+j2+window_size[0] // tile_size)/2)):
                    x2 = ((x+(j==1)) * j) % (window_size[0] // tile_size+2)
                    tile_coords = [ceil(screen_coords[0] / tile_size) + x2 - 1,
                                   ceil(screen_coords[1] / tile_size) + y2 - 1]
                    mat = get_mat(tile_coords[0], tile_coords[1])
                    index = int(point_to_random(tile_coords[0], tile_coords[1]) * 1000)
                    if (mat in animated):
                        matindex = index+(curtime//200+tile_coords[0]*tile_coords[0]+tile_coords[1])
                    elif (mat == "hexpavers"):
                        matindex = int(tile_coords[0]*13 + tile_coords[1] * tile_coords[1]*7)*2+tile_coords[0]
                    else:
                        matindex = index
                        #index = (tile_coords[0]*13 + tile_coords[1] * tile_coords[1]*7)
                    draw_tile(get_tex(mat, matindex), x2, y2, screen_coords)

                    decor = decorate(tile_coords[0], tile_coords[1], mat)
                    if decor == None:
                        pass
                    elif decor == "mushrooms":
                        draw_object(get_tex(decor, index), tile_coords[0], tile_coords[1], 0.01, 1, 1, screen_coords)
                    elif decor == "normaltree" or decor == "birchtreelog":
                        draw_structure(get_tex("birchtreelog", 0), tile_coords[0], tile_coords[1], 0.01, 1, 1, screen_coords)
                    elif decor == "gravilearobustatree" or decor == "bottlebrushtree" or decor == "sheoaktree" or decor == "deadtree" or decor == "treelog":
                        draw_structure(get_tex("treelog", 0), tile_coords[0], tile_coords[1], 0.01, 1, 1, screen_coords)
                    elif decor == "birchtreestump":
                        draw_structure(get_tex("birchtreelog", 0), tile_coords[0], tile_coords[1], 0.01, 1, 1, screen_coords)
                        draw_structure(get_tex("birchtreestump", 0), tile_coords[0], tile_coords[1], 0.05, 1, 1, screen_coords)
                    elif decor == "treestump":
                        draw_structure(get_tex("treelog", 0), tile_coords[0], tile_coords[1], 0.01, 1, 1, screen_coords)
                        draw_structure(get_tex("treestump", 0), tile_coords[0], tile_coords[1], 0.05, 1, 1, screen_coords)
                    elif decor in blocks:
                        wall = get_tex(decor, 0)
                        draw_structure(wall, tile_coords[0], tile_coords[1]-((y2>window_size[1]//tile_size//2)-.5), 0.13, 1, 0, screen_coords)
                        draw_structure(wall, tile_coords[0]-((x2>window_size[0]//tile_size//2)-.5), tile_coords[1], 0.13, 0, 1, screen_coords)
                        draw_structure(wall, tile_coords[0], tile_coords[1], 0.13, 1, 1, screen_coords)
                    elif decor in roofing:
                        draw_structure(get_tex(decor, 0), tile_coords[0], tile_coords[1], 1.13, 1, 1, screen_coords)
                    elif decor == "cactus":
                        draw_object(get_tex(decor, index), tile_coords[0], tile_coords[1], 0.03, 2*(int(index+tile_coords[0])%2*2-1), 2*(int(index+tile_coords[1])%2*2-1), screen_coords)
                    elif decor == "lillypad":
                        draw_object(get_tex(decor, index), tile_coords[0], tile_coords[1], 0.001, 1.5*(int(index+tile_coords[0])%2*2-1), 1.5*(int(index+tile_coords[1])%2*2-1), screen_coords)
                    elif decor == "talldrygrass":
                        draw_structure(get_tex(decor, index), tile_coords[0]+cos(curtime/1000)/10, tile_coords[1]+sin(curtime/1000)/10, 0.05, 1, 1, screen_coords)
                    elif decor == "flytrap":
                        if i==1 and j==1 and y==ceil((2+i2+window_size[1] // tile_size) / 2)-2 and x==ceil((2+j2+window_size[0] // tile_size) / 2)-2:
                            index = curtime/200+tile_coords[0]*tile_coords[0]+tile_coords[1]
                        draw_object(get_tex(decor, index), tile_coords[0], tile_coords[1], 0.03, 1.5*(tile_coords[0]%2*2-1), 1.5*(tile_coords[1]%2*2-1), screen_coords)
                    else:
                        draw_object(get_tex(decor, 0), tile_coords[0], tile_coords[1], 0.035, -2, -2, screen_coords)
                        draw_object(get_tex(decor, 0), tile_coords[0], tile_coords[1], 0.05, 2, 2, screen_coords)
    char_speed = (sqrt(velocity[0]*velocity[0]+velocity[1]*velocity[1]))
    if (abs(velocity[0])+abs(velocity[1])) > 0.001 and curtime-steptime > 2/char_speed:
        steptime = curtime
        if "water" in get_mat(ceil(pos[0]-1), ceil(pos[1]-1)):
            fish_sfx.play()
        else:
            grass_step_sfx.play()
    char_anim += char_speed*20
    if char_speed < 0.001:
        char_anim = 0
    if last_server_update+0.1 < time.time():
        if len(map.save_buffer) > 0:
            save_game()
        try:
            resp = requests.post("http://cabbageserver.ddns.net:27448/player_update", data={str(player_number):str([pos[0], pos[1], char_direction, char_anim, char_speed, time.time()])}, timeout=2)
            text = resp.text.split("&")
            world_text = text[1].replace("{", "").replace("}", "").replace("(", "").replace(")", "").replace("'", "").replace(" ", "").replace(":", ",").split(",")
            player_text = text[0].split("]'")[:-1]
            for i in range(len(world_text)//4):
                #print(world_text[4*i+0],world_text[4*i+1],world_text[4*i+2],world_text[4*i+3])
                if world_text[4*i+3] == "None":
                    world_text[4*i+3] = None
                map.apply_data(int(world_text[4*i+0]), int(world_text[4*i+1]), (world_text[4*i+2],world_text[4*i+3]))
        except:
            render_text(["Error reaching server"])
        last_server_update = time.time()

    for p in player_text:
        kv = p.split("'")
        number = int(kv[1])
        if int(number) != player_number:
            values = kv[3][1:].split(",")
            coords = [float(values[0])-.5, float(values[1])-.5]
            direc = int(values[2][1:])
            anim = float(values[3][1:])
            speed = float(values[4][1:])
            t = float(values[5][1:])
            dt = 1000*(time.time()-t)
            anim += dt/20 * speed*20
            if direc%2:
                dx, dy = dt*speed*cos(-direc*tau/8), dt*speed*sin(-direc*tau/8)
            else:
                dx, dy = dt*speed*cos(direc*tau/8+tau/4), dt*speed*sin(direc*tau/8-tau/4)
            draw_object(get_tex("charlegs"+str(direc), anim), coords[0]+dx, coords[1]+dy, 0.05, 2, 2, screen_coords)
            draw_object(get_tex("charhands"+str(direc), anim), coords[0]+dx, coords[1]+dy, 0.07, 2, 2, screen_coords)
            draw_object(get_tex("charhead"+str(direc), number), coords[0]+dx, coords[1]+dy, 0.08, 2, 2, screen_coords)
    draw_sprite(get_tex("charlegs"+str(char_direction),char_anim), window_size[0] / 2 - tile_size, window_size[1] / 2 - tile_size, 0.05, 2 * tile_size, 2 * tile_size)
    draw_sprite(get_tex("charhands"+str(char_direction),char_anim), window_size[0] / 2 - tile_size, window_size[1] / 2 - tile_size, 0.07, 2 * tile_size, 2 * tile_size)
    draw_sprite(get_tex("charhead"+str(char_direction),player_number), window_size[0] / 2 - tile_size, window_size[1] / 2 - tile_size, 0.08, 2 * tile_size, 2 * tile_size)
    for y in range(14 + window_size[1] // tile_size):
        for x in range(18 + window_size[0] // tile_size):
            tile_coords = [ceil(screen_coords[0] / tile_size) + x - 9,
                           ceil(screen_coords[1] / tile_size) + y - 8]
            mat = get_mat(tile_coords[0], tile_coords[1])
            decor = decorate(tile_coords[0], tile_coords[1], mat)
            if decor == "normaltree":
                tree_height = 0.4 + sin(tile_coords[0] + tile_coords[1] * tile_coords[1]) / 20
                draw_structure(get_tex("birchtreetrunk", 0), tile_coords[0], tile_coords[1], tree_height, 0, -1, screen_coords)
                draw_structure(get_tex("birchtreetrunk", 0), tile_coords[0], tile_coords[1], tree_height, 1, 0, screen_coords)
                draw_structure(get_tex("birchtreestump", 0), tile_coords[0], tile_coords[1], tree_height, 1, 1, screen_coords)
                draw_object_foreground(get_tex(decor, tile_coords[0]+10*tile_coords[1]), tile_coords[0], tile_coords[1], tree_height, 8*(tile_coords[0]%2*2-1), 8*(tile_coords[1]%2*2-1), screen_coords)
            if decor == "gravilearobustatree" or decor == "bottlebrushtree" or decor == "sheoaktree" or decor == "deadtree":
                tree_height = 0.4 + sin(tile_coords[0] + tile_coords[1] * tile_coords[1]) / 20
                draw_structure(get_tex("treetrunk", 0), tile_coords[0], tile_coords[1], tree_height, 0, -1, screen_coords)
                draw_structure(get_tex("treetrunk", 0), tile_coords[0], tile_coords[1], tree_height, 1, 0, screen_coords)
                draw_structure(get_tex("treestump", 0), tile_coords[0], tile_coords[1], tree_height, 1, 1, screen_coords)
                draw_object_foreground(get_tex(decor, tile_coords[0]+10*tile_coords[1]), tile_coords[0], tile_coords[1], tree_height, 8*(tile_coords[0]%2*2-1), 8*(tile_coords[1]%2*2-1), screen_coords)
    draw_tile(get_tex("selection",0), selected_tile[0] - screen_coords[0]//tile_size, selected_tile[1] - screen_coords[1]//tile_size, screen_coords)
    for c in range(10):
        draw_shadow(get_tex("cloud", 0), screen_coords[0] / tile_size + (time.time()*2+5647*c-screen_coords[0] / tile_size)%(400+c)-100, screen_coords[1] / tile_size + (time.time()/5+4674*c-screen_coords[1] / tile_size)%(300+c)-100, 1, 100*(int(c)%2*2-1), 100*(int(c//2)%2*2-1), screen_coords)

    #draw_shadow(get_tex("cloud", 0), screen_coords[0] / tile_size+20, screen_coords[1] / tile_size+8, 1, 1000, 1000, screen_coords)

    Renderer.render((mouse_pos[0]/window_size[0]*2-1, 1-mouse_pos[1]/window_size[1]*2), tile_size)
    pygame.display.flip()
    clock.tick(FPS)

for i in range(60):
    main()
cProfile.run('main()', sort=2)
while running:
    main()
