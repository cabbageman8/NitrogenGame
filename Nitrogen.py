# Nitrogen Alpha 0.00

# to compile; run
# py -m nuitka --standalone --include-data-dir=data=data --include-data-dir=save=save Nitrogen.py

# to build Docker image of server; run
# docker build -t cabbageman/nitrogenserver .

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
import socket
import base64
from objects import *

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

clock = pygame.time.Clock()
text = ["connecting to server"]

try: os.mkdir("save")
except: pass
try:
    sav = open(os.path.join("save", "settings.txt"), 'r')
    txt = sav.read()
    sav.close()
except FileNotFoundError:
    txt = '''FPS = 60
window_size = 1920, 1080
fullscreen = True
vsyncenabled = True
tile_size = 75
ip = cabbageserver.ddns.net
port = 27448'''
    sav = open(os.path.join("save", "settings.txt"), 'w')
    sav.write(txt)
    sav.close()
    text.append('could not find settings file, defaults loaded')

try:
    txt = txt.replace(" ", "").replace("\n\n", '\n').replace("\n\n", '\n')
    print(txt)
    txt = {line.split('=')[0] : line.split('=')[1] for line in txt.split('\n') }
    FPS = int(txt["FPS"])
    window_size = (int(txt["window_size"].split(',')[0]), int(txt["window_size"].split(',')[1]))
    fullscreen = txt["fullscreen"] != "False"
    vsyncenabled = txt["vsyncenabled"] != "False"
    tile_size = int(txt["tile_size"])
    ip = txt["ip"]
    port = int(txt["port"])
except:
    print("improper settings file")

pygame.display.set_mode(size=window_size, flags=DOUBLEBUF|OPENGL, vsync=vsyncenabled)

if fullscreen:
    pygame.display.toggle_fullscreen()
    window_size = pygame.display.get_window_size()
    overlay = pygame.Surface(window_size).convert_alpha()

silombol = pygame.font.Font(os.path.join("data", "SilomBol.ttf"), ceil(window_size[1]/32))
textures_img = []
texd = {}

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
        file.close()

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
        file.close()
        fileb.close()
load_textures()
def get_tex(name, index):
    return texd[name][int(index)%len(texd[name])]

texpack = pygame.Surface((min(128*128, 128*(len(textures_img))), 128*(1+len(textures_img)//128)), flags=pygame.SRCALPHA).convert_alpha()
for i, m in enumerate(textures_img):
    texpack.blit(m, (128*(i%128),128*(i//128)))

overlay = pygame.Surface(window_size).convert_alpha()
overlay.fill((255,255,255,155))
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
grass_step_sfx.set_volume(0.2)
hit_sfx = pygame.mixer.Sound('data/hit.wav')
hit_sfx.set_volume(0.5)
fish_sfx = pygame.mixer.Sound('data/fish.wav')
fish_sfx.set_volume(0.2)
crumple_sfx = pygame.mixer.Sound('data/crumple.wav')
crumple_sfx.set_volume(0.5)
jump_into_water_sfx = pygame.mixer.Sound('data/jump-into-water.wav')
jump_into_water_sfx.set_volume(0.2)

def seeded_random(a):
    output = (41406202+14874235*a     )%79493069
    output = (43915416+77751829*output)%76741089
    output = (66947287+44145130*output)%90370934
    output = (64705634+34405431*output)%23928528
    output = (24300417+80810414*output)%10000
    return output/10000
def point_to_random(x, y):
    return seeded_random(x + x * x * y * y * y + y * y)

server_address = (ip, port)

# Create socket for server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.setblocking(False)

text = ["visit cabbage.moe", "Nitrogen Alpha", "wasd for movement", "esc for save and quit", "F4 for fullscreen", "scroll to select item", "LM place block", "RM place decoration", "press h to start"]
# get local data
try:
    sav = open(os.path.join("save", "savedata.pickle"), 'r')
    data = pickle.loads(base64.b64decode(sav.read()))
    pos = data['pos']
    hotbar = data['hotbar']
    player_number = data['player_number']
    sav.close()
    text.append('loaded local save')
except FileNotFoundError:
    pos = [pi, tau]
    hotbar = [[None, 0,0], [None, 0,0], [None, 0,0], [None, 0,0], [None, 0,0], [None, 0,0], [None, 0,0], [None, 0,0], [None, 0,0]]
    player_number = int(seeded_random(time.time()%100000000)*10000)
    sav = open(os.path.join("save", "savedata.pickle") , 'wb')
    data = {'pos': pos, 'hotbar': hotbar, 'player_number':player_number}
    sav.write(base64.b64encode(pickle.dumps(data)))
    sav.close()
    text.append('could not find local save, blank save loaded')

screen_coords = [pos[0] * tile_size - window_size[0] // 2, pos[1] * tile_size - window_size[1] // 2]
# get server data
map = root_node()
try:
    sock.sendto('world_download '.encode('utf-8'), server_address)
    downl_time = time.time()
    while time.time() - downl_time < 1:
        try:
            byt, address = sock.recvfrom(2**16)
            data = pickle.loads(byt)
            print("received", len(data), "tiles (", len(byt), "bytes )")
            for key, value in data.items():
                payload = (key, value)
                map.apply_data(payload[0][0], payload[0][1], payload[1])
        except BlockingIOError:
            pass
    text.append('loaded save from server')
except ConnectionResetError:
    text.append('could not reach server')
    text.append('progress will not be saved')
except socket.gaierror:
    text.append('the ip you have entered is not valid')
    text.append('progress will not be saved')
except pickle.UnpicklingError:
    text.append('data received is not valid, the server or client is likely out of date')
    text.append('progress will not be saved')

titlescreen = pygame.image.load(os.path.join("data", "titlescreen.png"))

def render_text(text):
    global overlay
    global Renderer
    overlay.fill((0, 0, 0, 0))
    file = Image.open(os.path.join("data", "titlescreen.png")).convert("RGBA")
    img = pygame.image.fromstring( file.resize(window_size, resample=Image.NEAREST).tobytes(), window_size, "RGBA").convert_alpha()
    overlay.blit(img, (0, 0))
    for i, t in enumerate(text):
        overlay.blit(silombol.render(t, True, (0, 0, 0)), (0, silombol.size(t)[1]*i))
    Renderer.update_overlay(overlay)
render_text(text)

#hotbar = [["treestump", 1, 1], ["treestump", 1, 1], ["birchtreestump", 1, 1], ["treestump", 1, 1], ["wall", 1, 1000], ["tiles", 1, 1000], ["dirt", 0, 1], ["lushundergrowth", 0, 1], ["bottlebrushdirt", 0, 1]]
#hotbar[0] = ["glass", 1, 9999]
#hotbar[1] = ["spade", 1, 1]
#hotbar[1] = ["dirt", 0, 999]
print("hotbar:", hotbar)
def save_game():
    print("saving game")
    sav = open(os.path.join("save", "savedata.pickle"), 'wb')
    data = {'pos': pos, 'hotbar': hotbar, 'player_number':player_number}
    sav.write(base64.b64encode(pickle.dumps(data)))
    sav.close()
    if len(map.save_buffer) > 0:
        sock.sendto(str('save_to_server '+str(base64.b64encode(pickle.dumps(map.save_buffer)))).encode('utf-8'), server_address)
        map.save_buffer.clear()
selected_item_slot = 0

def construct_overlay():
    overlay.fill((0, 0, 0, 0))
    overlay.blit(textures_img[texd["selection"][0]], (0, 128 * selected_item_slot - 128 * 4.5 + overlay.get_size()[1] / 2))
    for i in range(9):
        if hotbar[i][0] != None and hotbar[i][2] > 0:
            overlay.blit(textures_img[texd[hotbar[i][0]][0]], (0, 128 * i - 128 * 4.5 + overlay.get_size()[1] / 2))
    slot = hotbar[int(selected_item_slot)]
    overlay.blit(silombol.render(get_biome(pos[0], pos[1])[0]+str(get_climate(pos[0], pos[1])), True, (0, 0, 0)), (0, 0))
    if slot[0] != None and slot[2] > 0:
        t = str(slot[0])
        if slot[2] > 1:
            t += " " + str(slot[2])
        overlay.blit(silombol.render(t, True, (0, 0, 0)), (10, 50+128 * selected_item_slot - 128 * 4.5 + overlay.get_size()[1] / 2+silombol.size(t)[1]))
    Renderer.update_overlay(overlay)

last_climate = (None, None, None)
biome_size = 100
def get_climate(x, y):
    global last_climate
    if last_climate[0] == x and last_climate[1] == y:
        return last_climate[2]
    else:
        x /= biome_size
        y /= biome_size
        temp     = ((sin(0.70688 * y) * sin(0.08321 * y) * sin(1.20191 * y + 1.07952 * x) + sin(1.83391 * x / 5 - 1.00643 * y / 5) * sin(0.27705 * x / 5))/2+0.5)
        moisture = ((sin(0.56554 * y) * sin(0.49491 * y) * sin(1.63167 * y + 1.36682 * x) + sin(1.19063 * x / 7 - 1.52815 * y / 7) * sin(0.13701 * x / 7))/2+0.5)
        temp, moisture = max(0, min(0.999, temp))*35+10, max(0, min(0.999, moisture))*75
        last_climate = (x, y, (temp, moisture))
        return temp, moisture
last_biome = (None, None, None)
def get_biome(x, y):
    global last_biome
    if last_biome[0] == x and last_biome[1] == y:
        return last_biome[2]
    else:
        temp, moisture = get_climate(x, y)
        biome_num = biome_map[int(temp/45*4)][int(moisture/100*6)]
        biome = biomes[biome_num]
        last_biome = (x,y, biome)
        return biome
def get_mat(x, y):
    map_data = map.get_data(int(x), int(y))
    if (map_data != None):
        mat = map_data[0]
    else:
        local = max(-1, min(1, sin(0.546354 * y/5) * sin(0.876964 * y/5) * sin(1.45638 * y/5 + 1.82266 * x/5) + cos(1.94367 * x/5 - 1.743247 * y/5) * cos(0.869632 * x/5) ))
        biome = get_biome(x, y)
        temp, moisture = get_climate(x, y)
        mat_list = biome[1][int(len(biome[1])*point_to_random(int(temp / 45 * len(biome[1])), int(moisture / 100 * len(biome[1])) ))]
        mat = mat_list[int((local+1)/2*(len(mat_list)-1))]
    return mat

def decorate(x, y, mat):
    map_data = map.get_data(int(x), int(y))
    dec = None
    if map_data != None:
        if len(map_data) > 1:
            dec = map_data[1]
    else:
        r = point_to_random(x, y)
        if r < 0.5:
            r *= 2
            dec = list(OBJ)[int(r*len(OBJ))]
            temp, moisture = get_climate(x, y)
            if mat not in OBJ[dec]["substrate"] or temp < OBJ[dec]["temperiture"][0] or temp > OBJ[dec]["temperiture"][1] or moisture < OBJ[dec]["moisture"][0] or moisture > OBJ[dec]["moisture"][1]:
                dec = None
        if dec == None:
            map.cache_data(int(x), int(y), (mat, ))
        else:
            map.cache_data(int(x), int(y), (mat, dec))
    return dec

def get_tile_info(x, y):
    mat = get_mat(x, y)
    dec = decorate(x, y, mat)
    return (mat, dec)

def screen_transform(x, y, z, w, h, tex):
    # convert pixel coords to shader coords
    return (x/window_size[0]*2,
            y/window_size[1]*2,
            z,
            w/window_size[0]*2,
            h/window_size[1]*2,
            tex)

def geom_tile(x, y, z, tex):
    # return element for rendering a tile using int tile coords relitive to the screen
    global screen_coords
    return screen_transform((1 - screen_coords[0] % tile_size + tile_size * x),
                            (1 - screen_coords[1] % tile_size + tile_size * y),
                            z,
                            tile_size,
                            tile_size,
                            tex)

def geom_object(x, y, z, w, h, tex):
    # return element for rendering a texture using int tile coords relitive to the world
    global screen_coords
    return screen_transform(1 - screen_coords[0] % tile_size + tile_size * (x - w / 2 + 0.5) - screen_coords[0] // tile_size * tile_size,
                            1 - screen_coords[1] % tile_size + tile_size * (y - h / 2 + 0.5) - screen_coords[1] // tile_size * tile_size,
                            z,
                            w * tile_size,
                            h * tile_size,
                            tex)

def geom_shrub(x, y, z, w, h, tex):
    # return element for rendering a texture using int tile coords relitive to the world with added sway
    sway_translation = (x + y * y) % 1024
    return geom_object(x - cos(curtime / 1000 + sway_translation) / 80,
                            y - sin(curtime / 700 + sway_translation) / 80,
                            z,
                            w + (cos(curtime / 1000 + sway_translation) / 10),
                            h + (sin(curtime / 700 + sway_translation) / 10),
                            tex)

def draw_shrub(tex, x, y, z, w, h):
    Renderer.vert_list.append(geom_shrub(x, y, z + sin(x + y * y) / 50, w, h, tex))
def draw_shrub_foreground(tex, x, y, z, w, h):
    Renderer.vert_list.append(geom_shrub(x, y, 1+z, w, h, tex))
    Renderer.tile_list.insert(0, geom_shrub(x, y, -z, w, h, tex))
def draw_shadow(tex, x, y, z, w, h):
    Renderer.tile_list.insert(0, geom_shrub(x, y, -z, w, h, tex))
    Renderer.shadow_list.append(geom_shrub(x, y, -z, w, h, tex))
def draw_weather(tex, x, y, z, w, h):
    Renderer.weather_list.append(geom_shrub(x, y, 1+z, w, h, tex))
def draw_object(tex, x, y, z, w, h):
    Renderer.vert_list.append(geom_object(x, y, z, w, h, tex))
    if w * h == 0:
        Renderer.tile_list.insert(0, geom_object(x, y, -z, w, h, tex))

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
            if (event.key in (pygame.K_F2,)):
                keydown_set.add("press"+str(event.key))
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
                    if mouse_pos[0] < 0 or mouse_pos[0] > window_size[0]:
                        mouse_pos = [mouse_pos[0] - state * 7, mouse_pos[1]]
                elif a == 4:
                    mouse_pos = [mouse_pos[0], mouse_pos[1]+state*7]
                    if mouse_pos[1] < 0 or mouse_pos[1] > window_size[1]:
                        mouse_pos = [mouse_pos[0], mouse_pos[1] - state * 7]
        for b in range(g.get_numbuttons()):
            state = g.get_button(b)
            if state:
                gamepad_set.add("button"+str(b))
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
world_text = {}
player_text = {}
last_server_update = 0
server_fails = 0

def main():
    global frame
    global velocity
    global curtime
    global tile_size
    global screen_coords
    global selected_tile
    global char_direction
    global overlay
    global window_size
    global selected_item_slot
    global steptime
    global char_anim
    global world_text
    global player_text
    global last_server_update
    global server_fails
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
    selected_data = get_tile_info(int(selected_tile[0]), int(selected_tile[1]))
    if "click1" in keydown_set or "button8" in gamepad_set and not "button8" in old_gamepad_set:
        if Rect(0, overlay.get_size()[1] / 2 - 110 * 4.5, 110, 110*9).collidepoint(mouse_pos):
            selected_item_slot = (mouse_pos[1]-(overlay.get_size()[1] / 2 - 110 * 4.5))//110
        else:
            if selected_data != None and len(selected_data) > 1 and selected_data[1] != None:
                if hotbar[int(selected_item_slot)][2] == 0 or (selected_data[1] == hotbar[int(selected_item_slot)][0] and hotbar[int(selected_item_slot)][1] == 1):
                    shovel_sfx.play()
                    print("get dec")
                    hotbar[int(selected_item_slot)] = [selected_data[1], 1, hotbar[int(selected_item_slot)][2] + 1]
                    map.set_data(int(selected_tile[0]), int(selected_tile[1]), (selected_data[0], ))
            else:
                if hotbar[int(selected_item_slot)][2] == 0 or (selected_data[0] == hotbar[int(selected_item_slot)][0] and hotbar[int(selected_item_slot)][1] == 0):
                    shovel_sfx.play()
                    print("get mat")
                    hotbar[int(selected_item_slot)] = [selected_data[0], 0, hotbar[int(selected_item_slot)][2] + 1]
                    map.set_data(int(selected_tile[0]), int(selected_tile[1]), (get_biome(int(selected_tile[0]), int(selected_tile[1]))[1][0][0], ))
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
                map.set_data(int(selected_tile[0]), int(selected_tile[1]), (hotbar[int(selected_item_slot)][0],) + selected_data[1:])
                hotbar[int(selected_item_slot)][2] -= 1
            if hotbar[int(selected_item_slot)][1] == 1 and selected_data[0] in OBJ[hotbar[int(selected_item_slot)][0]]["substrate"]:
                crumple_sfx.play()
                map.set_data(int(selected_tile[0]), int(selected_tile[1]), (selected_data[0], hotbar[int(selected_item_slot)][0], time.time()))
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
                        matindex = int(index+(curtime//200+tile_coords[0]*tile_coords[0]+tile_coords[1]))
                    elif (mat == "hexpavers"):
                        matindex = int(tile_coords[0]*13 + tile_coords[1] * tile_coords[1]*7)*2+tile_coords[0]
                    else:
                        matindex = index
                    Renderer.tile_list.append(geom_tile(x2, y2, 0.0, get_tex(mat, matindex)))

                    decor = decorate(tile_coords[0], tile_coords[1], mat)
                    if decor == None:
                        pass
                    elif decor == "mushrooms":
                        draw_shrub(get_tex(decor, index), tile_coords[0], tile_coords[1], 0.01, 1, 1)
                    elif decor == "normaltree" or decor == "birchtreelog":
                        draw_object(get_tex("birchtreelog", 0), tile_coords[0], tile_coords[1], 0.01, 1, 1)
                    elif decor == "gravilearobustatree" or decor == "bottlebrushtree" or decor == "sheoaktree" or decor == "deadtree" or decor == "treelog":
                        draw_object(get_tex("treelog", 0), tile_coords[0], tile_coords[1], 0.01, 1, 1)
                    elif decor == "birchtreestump":
                        draw_object(get_tex("birchtreelog", 0), tile_coords[0], tile_coords[1], 0.01, 1, 1)
                        draw_object(get_tex("birchtreestump", 0), tile_coords[0], tile_coords[1], 0.05, 1, 1)
                    elif decor == "treestump":
                        draw_object(get_tex("treelog", 0), tile_coords[0], tile_coords[1], 0.01, 1, 1)
                        draw_object(get_tex("treestump", 0), tile_coords[0], tile_coords[1], 0.05, 1, 1)
                    elif decor in blocks:
                        wall = get_tex(decor, 0)
                        draw_object(wall, tile_coords[0], tile_coords[1]-((y2>window_size[1]//tile_size//2)-.5), 0.13, 1, 0)
                        draw_object(wall, tile_coords[0]-((x2>window_size[0]//tile_size//2)-.5), tile_coords[1], 0.13, 0, 1)
                        draw_object(wall, tile_coords[0], tile_coords[1], 0.13, 1, 1)
                    elif decor in roofing:
                        draw_object(get_tex(decor, 0), tile_coords[0], tile_coords[1], 1.13, 1, 1)
                    elif decor == "cactus" or decor == "greencactus":
                        draw_shrub(get_tex(decor, index), tile_coords[0], tile_coords[1], 0.03, 2*(int(index+tile_coords[0])%2*2-1), 2*(int(index+tile_coords[1])%2*2-1))
                    elif decor == "lillypad":
                        draw_shrub(get_tex(decor, index), tile_coords[0], tile_coords[1], 0.001, 1.5*(int(index+tile_coords[0])%2*2-1), 1.5*(int(index+tile_coords[1])%2*2-1))
                    elif decor == "talldrygrass":
                        draw_object(get_tex(decor, index), tile_coords[0]+cos(curtime/1000)/10, tile_coords[1]+sin(curtime/1000)/10, 0.05, 1, 1)
                    elif decor == "hole":
                        draw_object(get_tex(decor, 0), tile_coords[0], tile_coords[1], 0.01, 2, 2)
                    elif decor == "flytrap":
                        if i==1 and j==1 and y==ceil((2+i2+window_size[1] // tile_size) / 2)-2 and x==ceil((2+j2+window_size[0] // tile_size) / 2)-2:
                            index = curtime/200+tile_coords[0]*tile_coords[0]+tile_coords[1]
                        draw_shrub(get_tex(decor, index), tile_coords[0], tile_coords[1], 0.03, 1.5*(tile_coords[0]%2*2-1), 1.5*(tile_coords[1]%2*2-1))
                    else:
                        draw_shrub(get_tex(decor, 0), tile_coords[0], tile_coords[1], 0.035, -2, -2)
                        draw_shrub(get_tex(decor, 0), tile_coords[0], tile_coords[1], 0.05, 2, 2)
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
            sock.sendto(str("player_update "+str(player_number)+','+str(pos[0])+','+str(pos[1])+','+str(char_direction)+','+str(char_anim)+','+str(char_speed)+','+str(time.time())).encode('utf-8'), server_address)
            data, address = sock.recvfrom(8192)
            text = data.decode('utf-8')
            text = text.split("&")
            world_text = pickle.loads(base64.b64decode(text[1][2:-1]))
            player_text = pickle.loads(base64.b64decode(text[0][2:-1]))
            for key in world_text.keys():
                map.apply_data(key[0], key[1], world_text[key])
            server_fails = 0
        except BlockingIOError:
            server_fails += 1
            if server_fails > 60:
                render_text(["Error reaching server", "progress will not be saved"])
                server_fails = 0
        last_server_update = time.time()

    for number in player_text.keys():
        if int(number) != player_number:
            values = player_text[number]
            coords = [float(values[0])-.5, float(values[1])-.5]
            direc = int(values[2])
            anim = float(values[3])
            speed = float(values[4])
            t = float(values[5])
            dt = 1000*(time.time()-last_server_update)
            anim += dt/20 * speed*20
            if direc%2:
                dx, dy = dt*speed*cos(-direc*tau/8), dt*speed*sin(-direc*tau/8)
            else:
                dx, dy = dt*speed*cos(direc*tau/8+tau/4), dt*speed*sin(direc*tau/8-tau/4)
            draw_shrub(get_tex("charlegs"+str(direc), anim), coords[0]+dx, coords[1]+dy, 0.05, 2, 2)
            draw_shrub(get_tex("charhands"+str(direc), anim), coords[0]+dx, coords[1]+dy, 0.07, 2, 2)
            draw_shrub(get_tex("charhead"+str(direc), number), coords[0]+dx, coords[1]+dy, 0.08, 2, 2)
    # add player textures to vertex list
    Renderer.vert_list.append(screen_transform(window_size[0] / 2 - tile_size, window_size[1] / 2 - tile_size, 0.05, 2 * tile_size, 2 * tile_size, get_tex("charlegs"+str(char_direction),char_anim)))
    Renderer.vert_list.append(screen_transform(window_size[0] / 2 - tile_size, window_size[1] / 2 - tile_size, 0.07, 2 * tile_size, 2 * tile_size, get_tex("charhands"+str(char_direction),char_anim)))
    Renderer.vert_list.append(screen_transform(window_size[0] / 2 - tile_size, window_size[1] / 2 - tile_size, 0.08, 2 * tile_size, 2 * tile_size, get_tex("charhead"+str(char_direction),player_number)))
    for y in range(14 + window_size[1] // tile_size):
        for x in range(18 + window_size[0] // tile_size):
            tile_coords = [ceil(screen_coords[0] / tile_size) + x - 9,
                           ceil(screen_coords[1] / tile_size) + y - 8]
            mat = get_mat(tile_coords[0], tile_coords[1])
            decor = decorate(tile_coords[0], tile_coords[1], mat)
            if decor == "normaltree":
                tree_height = 0.4 + sin(tile_coords[0] + tile_coords[1] * tile_coords[1]) / 20
                draw_object(get_tex("birchtreetrunk", 0), tile_coords[0], tile_coords[1], tree_height, 0, -1)
                draw_object(get_tex("birchtreetrunk", 0), tile_coords[0], tile_coords[1], tree_height, 1, 0)
                draw_object(get_tex("birchtreestump", 0), tile_coords[0], tile_coords[1], tree_height, 1, 1)
                draw_shrub_foreground(get_tex(decor, tile_coords[0]+10*tile_coords[1]), tile_coords[0], tile_coords[1], tree_height, 8*(tile_coords[0]%2*2-1), 8*(tile_coords[1]%2*2-1))
            if decor == "gravilearobustatree" or decor == "bottlebrushtree" or decor == "sheoaktree" or decor == "deadtree":
                tree_height = 0.4 + sin(tile_coords[0] + tile_coords[1] * tile_coords[1]) / 20
                draw_object(get_tex("treetrunk", 0), tile_coords[0], tile_coords[1], tree_height, 0, -1)
                draw_object(get_tex("treetrunk", 0), tile_coords[0], tile_coords[1], tree_height, 1, 0)
                draw_object(get_tex("treestump", 0), tile_coords[0], tile_coords[1], tree_height, 1, 1)
                draw_shrub_foreground(get_tex(decor, tile_coords[0]+10*tile_coords[1]), tile_coords[0], tile_coords[1], tree_height, 8*(tile_coords[0]%2*2-1), 8*(tile_coords[1]%2*2-1))
    draw_object(get_tex("selection",0), selected_tile[0], selected_tile[1], 3, 1, 1)
    for c in range(10):
        draw_shadow(get_tex("cloud", c),
                    screen_coords[0] / tile_size + (time.time()*2+5647*c-screen_coords[0] / tile_size)%(400+c)-100,
                    screen_coords[1] / tile_size + (time.time()/5+4674*c-screen_coords[1] / tile_size)%(300+c)-100,
                    1,
                    100*(int(c)%2*2-1),
                    100*(int(c//2)%2*2-1))
    for c in range(5):
        draw_weather(get_tex("cloud", c),
                     screen_coords[0] / tile_size + (time.time()/10+48634*c-screen_coords[0] / tile_size)%(400+c)-100,
                     screen_coords[1] / tile_size + (time.time()/40+873356*c-screen_coords[1] / tile_size)%(300+c)-100,
                     1,
                     100*(int(c)%2*2-1),
                     100*(int(c//2)%2*2-1))
    Renderer.tile_list.insert(0, (0, 0, 0, 2, 2, get_tex("sky", 0)))

    Renderer.render((mouse_pos[0]/window_size[0]*2-1, 1-mouse_pos[1]/window_size[1]*2), tile_size)
    if "press"+str(pygame.K_F2) in keydown_set:
        try: os.mkdir("screenshots")
        except: pass
        file_name = os.path.join("screenshots", "screenshot"+str(int(time.time()))+".png")
        file = open(file_name, "wb")
        pygame.image.save(pygame.transform.flip(pygame.image.fromstring(Renderer.ctx.screen.read(), Renderer.ctx.screen.size, "RGB"), False, True), file, "PNG")
        file.close()
        keydown_set.remove("press"+str(pygame.K_F2))
    pygame.display.flip()
    clock.tick(FPS)

i = 60
while i>0 and running:
    i-=1
    main()
cProfile.run('main()', sort=2)
while running:
    main()
