import struct
import moderngl
import pygame
from pygame.locals import *
from PIL import Image
import pickle
import numpy as np
from math import pi, tau, sin, cos, tan, asin, acos, atan, ceil
import cProfile
import random
from quadtree import root_node
pygame.init()

FPS=60
clock = pygame.time.Clock()
#window_size=(1000, 1000)
window_size=(1440, 1440)
#window_size=(2560, 1440)
tile_size = 75

screen = pygame.Surface(window_size).convert((255, 65280, 16711680, 0))
pygame.display.set_mode(window_size, DOUBLEBUF|OPENGL)
surf = pygame.Surface((window_size[0]+tile_size*5, window_size[1]+tile_size*5)).convert_alpha()

materials = ["Dirt16", "Water", "Planks16", "Mud16", "Cabbage16"]
materials_img = []
sprites = ["selection", "foxchar", "Grass", "DeadTree", "LivingTree", "TreeStump"]
sprites_img = []
solids = set(("Water", "DeadTree", "LivingTree"))
def load_textures():
    global materials_img
    global sprites_img
    materials_img = []
    sprites_img = []
    for mat in materials:
        frame_list = []
        file = Image.open("data/" + mat + ".jpg")
        for i in range(file.height//file.width):
            frame_list.append(pygame.image.fromstring(file.crop(Rect(0,file.width*i,file.width,file.width*(i+1))).resize([tile_size, tile_size], resample=Image.NEAREST).tobytes(), [tile_size, tile_size], "RGB").convert_alpha())
        materials_img.append(frame_list)
    for spr in sprites:
        file = Image.open("data/" + spr + ".png")
        new_size = [ceil(file.width/16*tile_size), ceil(file.height/16*tile_size)]
        sprites_img.append(pygame.image.fromstring(file.resize(new_size, resample=Image.NEAREST).tobytes(), new_size, "RGBA").convert_alpha())
load_textures()

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
            mat = 4
        elif (r > 0.5):
            mat = 4
        elif (abs(r) < 0.1):
            mat = 3
        else:
            mat = 0
        map.cache_data(x, y, mat)
    return mat
def decorate(x, y, mat):
    r = point_to_random(x, y)
    if r < 0.7 and mat == 4:
        return 2
    if r < 0.001 and mat == 0:
        return 3
    if r > 0.98 and mat == 0:
        return 4
    return None

def draw_tile(mat, x, y, screen_coords):
    # blits material texture using int tile coords relitive to the screen
    if Rect((0,0), window_size).colliderect(Rect(x, y, tile_size, tile_size)) and True:
        frame_list = materials_img[mat]
        screen.blit(frame_list[(curtime//200)%len(frame_list)], (1 - screen_coords[0] % tile_size + tile_size * x,
                                   1 - screen_coords[1] % tile_size + tile_size * y))
def draw_sprite(spr, x, y, w, h):
    # blits sprite texture using float pixel coords relitive to the screen
    if Rect((0,0), window_size).colliderect(Rect(x, y, w, h)) and True:
        screen.blit(sprites_img[spr], (x, y))
def draw_object(decor, x, y, w, h, screen_coords):
    # blits sprite texture using tile coords relitive to the world
    draw_sprite( decor,
        1 - screen_coords[0] % tile_size + tile_size*(x-w/2+0.5)-screen_coords[0]//tile_size*tile_size - cos(curtime / 1000 + x+y*y) * tile_size / 20,
        1 - screen_coords[1] % tile_size + tile_size*(y-h/2+0.5)-screen_coords[1]//tile_size*tile_size - sin(curtime / 300  + x+y*y) * tile_size / 20,
        w * tile_size + int(cos(curtime / 1000 + x+y*y) * tile_size / 10),
        h * tile_size + int(sin(curtime / 300 + x+y*y) * tile_size / 10))
def draw_sprite_foreground(spr, x, y, w, h):
    # blits sprite texture using float pixel coords relitive to the screen
    if Rect((0, 0), window_size).colliderect(Rect(x, y, w, h)) and True:
        surf.blit(sprites_img[spr], (x+2.5*tile_size, y+2.5*tile_size))
def draw_object_foreground(decor, x, y, w, h, screen_coords):
    # blits sprite texture using tile coords relitive to the world
    draw_sprite_foreground( decor,
        1 - screen_coords[0] % tile_size + tile_size*(x-w/2)-screen_coords[0]//tile_size*tile_size - cos(curtime / 1000 + x+y*y) * tile_size / 20,
        1 - screen_coords[1] % tile_size + tile_size*(y-h/2)-screen_coords[1]//tile_size*tile_size - sin(curtime / 300  + x+y*y) * tile_size / 20,
        w * tile_size + int(cos(curtime / 1000 + x+y*y) * tile_size / 10),
        h * tile_size + int(sin(curtime / 300 + x+y*y) * tile_size / 10))

velocity = [0, 0]
acceleration = 1/1000

ctx = moderngl.create_context()

prog = ctx.program(
    vertex_shader='''
#version 300 es
in vec2 vert;
in vec2 in_text;
in vec3 in_move;
out vec2 v_text;
in float in_time;
out float v_time;
flat out int ID;
void main() {
    ID = gl_InstanceID;
    gl_Position = vec4(vert.x/5.0+float(ID%5-2)/2.5+in_move.x, vert.y/5.0+float(ID/5-2)/2.5+in_move.y, 0.5, 1.0);
    v_text = vec2(in_text.x, in_text.y);
}
''',

    fragment_shader='''
#version 300 es
precision mediump float;
uniform sampler2D Texture;
uniform sampler2D Foreground;
uniform vec2 screen_pos;
uniform vec2 mouse_pos;
uniform vec2 screen_size;
uniform float tile_size;
uniform float time;
in vec2 v_text;
in float v_time;
flat in int ID;
out vec3 f_color;
vec3 incolour = texture(Texture,v_text).rgb;
vec2 fgoffset = vec2((2.5*tile_size)/(screen_size.x+5.0*tile_size), (2.5*tile_size)/(screen_size.y+5.0*tile_size));
vec2 fgscale = vec2((screen_size.x)/(screen_size.x+5.0*tile_size), (screen_size.y)/(screen_size.y+5.0*tile_size));
vec2 fgcoords = vec2((fgoffset.x+v_text.x)*fgscale.x, (fgoffset.y+v_text.y)*fgscale.y);
vec4 forcolour = texture(Foreground,vec2(fgcoords.x-(v_text.x-0.5)/10.0, fgcoords.y-(v_text.y-0.5)/10.0)).rgba;
void main() {
    float x = (screen_pos.x+v_text.x)*screen_size.x/tile_size-0.5;
    float y = (screen_pos.y+v_text.y)*screen_size.y/tile_size-0.5;
    vec4 forcolour2 = texture(Foreground,fgcoords).rgba;
    float mid_dist_2 = (v_text.x-0.5)*(v_text.x-0.5)+(v_text.y-0.5)*(v_text.y-0.5);
    float mouse_dist_2 = (mouse_pos.x-v_text.x)*(mouse_pos.x-v_text.x)+(mouse_pos.y-v_text.y)*(mouse_pos.y-v_text.y);
    float r = sin(0.546354 * y/5.0) * sin(0.876964 * y/5.0) * sin(1.45638 * y/5.0 + 1.82266 * x/5.0) + cos(1.94367 * x/5.0 - 1.743247 * y/5.0) * cos(0.869632 * x/5.0);
    r = (r < -0.9) ? r : 0.0;
    float alpha = max(0.3, min(1.0, mouse_dist_2*mid_dist_2*screen_size.x/tile_size*10.0));
    float anti = min(1.0, 1.0-alpha+max(0.0, 1.0-forcolour.a-forcolour2.a/2.0));
    f_color = vec3(forcolour.r*alpha+incolour.r*anti+float(ID%5)/5.0, forcolour.g*alpha+incolour.g*anti, forcolour.b*alpha+incolour.b*anti+float(ID/5)/5.0);
}
''')
frag_Texture = prog['Texture']
frag_Foreground = prog['Foreground']
#frag_screen_pos = prog['screen_pos']
frag_mouse_pos = prog['mouse_pos']
frag_screen_size = prog['screen_size']
frag_tile_size = prog['tile_size']
#frag_time = prog['time']

screen_texture = ctx.texture(
    window_size, 3,
    pygame.image.tostring(screen, "RGB", 1))
Foreground_texture = ctx.texture(
    (window_size[0]+tile_size*5, window_size[1]+tile_size*5), 4,
    pygame.image.tostring(surf, "RGBA", 1))

screen_texture.repeat_x = False
screen_texture.repeat_y = False
Foreground_texture.repeat_x = False
Foreground_texture.repeat_y = False

instance_data = ctx.buffer(struct.pack(
            '3f',
            0.0, 0.0, 0.0
        ) * 25)

texture_coordinates = [0, 1,  1, 1,
                       0, 0,  1, 0]

render_indices = [0, 1, 2,
                  1, 2, 3]

vbo = ctx.buffer(struct.pack('8f',
                             -1, -1, 1, -1,
                             -1, 1, 1, 1))

uvmap = ctx.buffer(struct.pack('8f', *texture_coordinates))
ibo= ctx.buffer(struct.pack('6I', *render_indices))

vao_content = [
    (vbo, '2f', 'vert'),
    (uvmap, '2f', 'in_text'),
    (instance_data, '3f', 'in_move')
]
vao = ctx.vertex_array(prog, vao_content, ibo)

def render():
    global surf
    frag_Texture.value = 0
    frag_Foreground.value = 1
    #frag_screen_pos.value = (screen_coords[0]/window_size[0], screen_coords[1]/window_size[1])
    frag_mouse_pos.value = (mouse_pos[0] / window_size[0], mouse_pos[1] / window_size[1])
    frag_screen_size.value = (window_size[0], window_size[1])
    frag_tile_size.value = tile_size
    texture_data = screen.get_view('1')
    screen_texture.write(texture_data)
    texture_data2 = surf.get_view('1')
    Foreground_texture.write(texture_data2)
    ctx.clear(0 / 255, 0 / 255, 0 / 255)
    ctx.enable(moderngl.DEPTH_TEST)
    screen_texture.use(0)
    Foreground_texture.use(1)

    instance_data.write(b''.join(struct.pack(
        '3f',
        x/5+sin(curtime/1000+x+y)/10, y/5+cos(curtime/1000+x+y)/10, 0.0
    ) for x in range(5) for y in range(5)))

    vao.render(instances=25)
    pygame.display.flip()

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

def main():
    global frame
    global velocity
    global curtime
    global tile_size
    global surf
    global Foreground_texture
    global screen
    frame += 1
    dt = pygame.time.get_ticks() - curtime
    curtime = pygame.time.get_ticks()
    #frag_time.value = curtime
    handle_keys()
    if pygame.K_w in keydown_set:
        velocity[1] -= acceleration * dt
    if pygame.K_a in keydown_set:
        velocity[0] -= acceleration * dt
    if pygame.K_s in keydown_set:
        velocity[1] += acceleration * dt
    if pygame.K_d in keydown_set:
        velocity[0] += acceleration * dt
    if pygame.K_t in keydown_set:
        map.tree()
    if pygame.K_UP in keydown_set:
        tile_size += 2
        load_textures()
        surf = pygame.Surface((window_size[0] + tile_size * 5, window_size[1] + tile_size * 5)).convert_alpha()
        Foreground_texture = ctx.texture(
            (window_size[0] + tile_size * 5, window_size[1] + tile_size * 5), 4,
            pygame.image.tostring(surf, "RGBA", 1))
    if pygame.K_DOWN in keydown_set:
        tile_size -= 2
        load_textures()
        surf = pygame.Surface((window_size[0] + tile_size * 5, window_size[1] + tile_size * 5)).convert_alpha()
        Foreground_texture = ctx.texture(
            (window_size[0] + tile_size * 5, window_size[1] + tile_size * 5), 4,
            pygame.image.tostring(surf, "RGBA", 1))
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
    mat = get_mat(ceil(pos[0] - 1), ceil(pos[1]))
    spr = decorate(ceil(pos[0] - 1), ceil(pos[1]), mat)
    if (materials[mat] in solids or spr != None and sprites[spr] in solids):
        pos[1] += 1
        velocity = [0, 0]
    else:
        mat2 = get_mat(ceil(pos[0] - 1 + velocity[0]), ceil(pos[1] + velocity[1]))
        spr2 = decorate(ceil(pos[0] - 1 + velocity[0]), ceil(pos[1] + velocity[1]), mat2)
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
    #screen.fill((0, 0, 0))
    surf.fill((0, 0, 0, 0))
    for y in range(2 + window_size[1] // tile_size):
        for x in range(2 + window_size[0] // tile_size):
            tile_coords = [ceil(screen_coords[0] / tile_size) + x - 1, ceil(screen_coords[1] / tile_size) + y - 1]
            mat = get_mat(tile_coords[0], tile_coords[1])
            draw_tile(mat, x, y, screen_coords)
    for y in range(7 + window_size[1] // tile_size):
        for x in range(7 + window_size[0] // tile_size):
            tile_coords = [ceil(screen_coords[0] / tile_size) + x - 4,
                           ceil(screen_coords[1] / tile_size) + y - 4]
            mat = get_mat(tile_coords[0], tile_coords[1])
            decor = decorate(tile_coords[0], tile_coords[1], mat)
            if decor == 2:
                draw_object(decor, tile_coords[0], tile_coords[1], 2, 2, screen_coords)
            if decor == 3 or decor == 4:
                draw_object_foreground(decor, tile_coords[0], tile_coords[1], 8, 8, screen_coords)
                draw_object(5, tile_coords[0], tile_coords[1], 1, 1, screen_coords)
    draw_sprite(1, window_size[0] / 2 - tile_size, window_size[1] / 2 - tile_size, 2 * tile_size, 2 * tile_size)
    draw_object(0, selected_tile[0] + 1 - pos[0] % 1, selected_tile[1] + 1 - pos[1] % 1, 2, 2, screen_coords)
    render()
    clock.tick(FPS)

while running:
    #cProfile.run('main()')
    main()