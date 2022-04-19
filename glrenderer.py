import struct
import moderngl
import glcontext
from math import pi, tau, sin, cos, tan, asin, acos, atan, ceil
import time
import pygame

class glrenderer():
    def __init__(self, texpack, overlay):
        self.vert_list = []
        self.shadow_list = []
        self.weather_list = []
        self.tile_list = []
        self.light_list = []
        self.ctx = moderngl.create_context()
        self.ctx.enable(moderngl.BLEND)
        self.simple_prog = self.ctx.program(
            vertex_shader='''
#version 300 es
in vec2 vert;
in vec2 in_text;
uniform sampler2D overlay;
out vec2 v_text;
void main() {
    gl_Position = vec4(vert.x*2.0-1.0, 1.0-vert.y*2.0 , 1.0 , 1.0);
    v_text = in_text;
}
''',
    fragment_shader='''
#version 300 es
precision mediump float;
uniform sampler2D overlay;
in vec2 v_text;
out vec4 f_color;
vec4 incolour;
void main() {
    incolour = texture(overlay,v_text);
    f_color = vec4(incolour.r, incolour.g, incolour.b, incolour.a);
}
        ''')
        self.prog = self.ctx.program(
    vertex_shader='''
#version 300 es
in vec2 vert;
in vec2 in_text;
in vec3 pos;
in vec2 size;
in float texnum;
uniform float tile_size;
uniform sampler2D texpack;
uniform sampler2D overlay;
out vec2 v_text;
out float thetexnum;
out vec3 screenpos;
vec2 packsize;
float zpos;
void main() {
    packsize = vec2(textureSize(texpack, 0).xy);
    zpos = (pos.z>1.0) ? mod(pos.z, 1.0) : pos.z;
    zpos = (size.x==0.0) ? vert.x*zpos : ((size.y==0.0) ? vert.y*zpos : zpos);
    screenpos = vec3((pos.x+vert.x*size.x-1.0)*(1.0+zpos*tile_size), (1.0-pos.y-vert.y*size.y)*(1.0+zpos*tile_size), -pos.z);
    thetexnum = texnum;
    
    gl_Position = vec4(screenpos.x, screenpos.y, -zpos, 1.0);
    v_text = vec2((in_text.x*0.98+0.01+mod(texnum, 128.0))*(128.0/packsize.x), (in_text.y*0.98+0.01+floor(texnum/128.0))*(128.0/packsize.y));
}
''',
    fragment_shader='''
#version 300 es
precision mediump float;
uniform sampler2D texpack;
uniform sampler2D overlay;
uniform vec2 mouse_pos;
uniform float tile_size;
uniform vec2 screen_size;
uniform float time;
uniform vec3 sunlight;
uniform int lightnum;
uniform vec3 lightpos[128];
uniform vec3 lighthue[128];
in vec2 v_text;
in float thetexnum;
in vec3 screenpos;
out vec4 f_color;
vec4 incolour;
float mid_dist_2;
float mouse_dist_2;
float seethrough;
float light_dist;
int i;
vec3 light_value;
void main() {
    incolour = texture(texpack,v_text);
    mid_dist_2 = (screenpos.x)*(screenpos.x)*screen_size.x/screen_size.y+(screenpos.y)*(screenpos.y)*screen_size.y/screen_size.x;
    mouse_dist_2 = (mouse_pos.x-screenpos.x)*(mouse_pos.x-screenpos.x)*(screen_size.x/screen_size.y)+(mouse_pos.y-screenpos.y)*(mouse_pos.y-screenpos.y)*(screen_size.y/screen_size.x);
    seethrough = (screenpos.z < -1.0) ? incolour.a*mid_dist_2*mouse_dist_2*50.0 : incolour.a;
    
    light_value = sunlight;
    for(i=0;i<lightnum;i++){
        if (-screenpos.z <= lightpos[i].z) {
            light_dist = 0.1+((lightpos[i].x-screenpos.x)*(lightpos[i].x-screenpos.x)*(screen_size.x/screen_size.y)/(tile_size*tile_size)+(lightpos[i].y-screenpos.y)*(lightpos[i].y-screenpos.y)*(screen_size.y/screen_size.x)/(tile_size*tile_size))*5.0;
            light_value = vec3(light_value.r + lighthue[i].r*(1.0/light_dist), light_value.g + lighthue[i].g*(1.0/light_dist), light_value.b + lighthue[i].b*(1.0/light_dist));
        }
    }
    f_color = vec4(incolour.r*min(1.0, light_value.r), incolour.g*min(1.0, light_value.g), incolour.b*min(1.0, light_value.b), min(incolour.a,max(0.3*incolour.a, seethrough)));
}
''')
        self.shadowprog = self.ctx.program(
    vertex_shader='''
#version 300 es
in vec2 vert;
in vec2 in_text;
in vec3 pos;
in vec2 size;
in float texnum;
uniform float tile_size;
uniform sampler2D texpack;
out vec2 v_text;
out float thetexnum;
out vec3 screenpos;
vec2 packsize;
float zpos;
void main() {
    packsize = vec2(textureSize(texpack, 0).xy);
    zpos = (pos.z>1.0) ? pos.z-1.0 : pos.z;
    zpos = (size.x==0.0) ? vert.x*zpos : ((size.y==0.0) ? vert.y*zpos : zpos);
    screenpos = vec3((pos.x+vert.x*size.x-1.0)+0.3*(zpos*tile_size), (1.0-pos.y-vert.y*size.y)+0.3*(zpos*tile_size), -pos.z);
    thetexnum = texnum;

    gl_Position = vec4(screenpos.x, screenpos.y, -zpos, 1.0);
    v_text = vec2((in_text.x*0.98+0.01+mod(texnum, 128.0))*(128.0/packsize.x), (in_text.y*0.98+0.01+floor(texnum/128.0))*(128.0/packsize.y));
}
''',
    fragment_shader='''
#version 300 es
precision mediump float;
uniform sampler2D texpack;
uniform vec3 sunlight;
in vec2 v_text;
in vec3 screenpos;
vec4 incolour;
out vec4 f_color;
void main() {
    incolour = texture(texpack,v_text);
    f_color = vec4(0, 0.02*sunlight.g, 0.05*sunlight.b, min(incolour.a,min(0.4, sunlight.r)));
}
''')
        self.frag_texpack = self.prog['texpack']
        self.prog_tile_size = self.prog['tile_size']

        self.texpack_texture = self.ctx.texture(
            texpack.get_size(), 4,
            pygame.image.tostring(texpack, "RGBA", 1))
        self.texpack_texture.filter = moderngl.NEAREST, moderngl.NEAREST
        self.texpack_texture.repeat_x = False
        self.texpack_texture.repeat_y = False
        self.texpack_texture.swizzle = 'BGRA'
        self.overlay_texture = self.ctx.texture(
            overlay.get_size(), 4,
            pygame.image.tostring(overlay, "RGBA", 1))
        self.overlay_texture.filter = moderngl.NEAREST, moderngl.NEAREST
        self.overlay_texture.repeat_x = False
        self.overlay_texture.repeat_y = False
        self.overlay_texture.swizzle = 'BGRA'

        texture_data = texpack.get_view('1')
        self.texpack_texture.write(texture_data)
        texture_data = overlay.get_view('1')
        self.overlay_texture.write(texture_data)

        self.instance_data_pos = self.ctx.buffer(struct.pack(
            '3f', 0.0, 0.0, 0.0) * (2 ** 16))
        self.instance_data_size = self.ctx.buffer(struct.pack(
            '2f', 0.0, 0.0)      * (2 ** 16))
        self.instance_data_texnum = self.ctx.buffer(struct.pack(
            '1f', 0.0)           * (2 ** 16))

        self.vbo = self.ctx.buffer(struct.pack('8f', 0, 0, 1, 0,
                                                     0, 1, 1, 1))

        self.uvmap = self.ctx.buffer(struct.pack('8f', 0, 0, 1, 0,
                                                       0, 1, 1, 1))

        self.ibo = self.ctx.buffer(struct.pack('6I', 0, 1, 2,
                                                     1, 2, 3))

        self.vao_content = [
            (self.vbo, '2f', 'vert'),
            (self.uvmap, '2f', 'in_text'),
            (self.instance_data_pos, '3f/i', 'pos'),
            (self.instance_data_size, '2f/i', 'size'),
            (self.instance_data_texnum, 'f/i', 'texnum')
        ]
        self.vao = self.ctx.vertex_array(self.prog, self.vao_content, self.ibo)
        self.shadowvao = self.ctx.vertex_array(self.shadowprog, self.vao_content, self.ibo)
        self.quad_fs = self.ctx.vertex_array(self.simple_prog, [(self.vbo, '2f', 'vert'), (self.uvmap, '2f', 'in_text')], self.ibo)

    def update_overlay(self, overlay):
        self.overlay_texture.release()
        self.overlay_texture = self.ctx.texture(
            overlay.get_size(), 4,
            pygame.image.tostring(overlay, "RGBA", 1))
        self.overlay_texture.filter = moderngl.NEAREST, moderngl.NEAREST
        self.overlay_texture.repeat_x = False
        self.overlay_texture.repeat_y = False
        self.overlay_texture.swizzle = 'BGRA'
        texture_data = overlay.get_view('1')
        self.overlay_texture.write(texture_data)

    def write_vert_data(self, vert_list):
        enum_list = range(len(vert_list))
        self.instance_data_pos.write(b''.join(struct.pack(
            '3f',
            x, y, z
        ) for x, y, z in [vert_list[i][0:3] for i in enum_list]))
        self.instance_data_size.write(b''.join(struct.pack(
            '2f',
            w, h
        ) for w, h in [vert_list[i][3:5] for i in enum_list]))
        self.instance_data_texnum.write(b''.join(struct.pack(
            '1f',
            tex
        ) for tex in [vert_list[i][5] for i in enum_list]))

    def render(self, mouse_pos, tile_size):
        self.ctx.clear()
        self.texpack_texture.use()
        #self.prog['time'].value = curtime/1000.0
        self.prog['mouse_pos'].value = mouse_pos
        self.prog['tile_size'].value = tile_size/100.0
        self.prog['screen_size'].value = self.ctx.screen.size
        r = max(sin((time.time()*tau)/60/10)+0.16,0)
        g = r**2
        b = g**2
        self.prog['sunlight'].value = (max(r,0.03), max(g,0.05), max(b,0.06))
        self.prog['lightnum'].value = min(len(self.light_list), 128)
        self.prog['lightpos'].value = (list(l[0] for l in self.light_list)+[(0, 0, 0),]*128)[:128]
        self.prog['lighthue'].value = (list(l[1] for l in self.light_list)+[(0, 0, 0),]*128)[:128]
        self.shadowprog['tile_size'].value = tile_size/100.0
        self.shadowprog['sunlight'].value = (max(r, 0.03), max(g, 0.05), max(b, 0.06))
        self.write_vert_data(self.tile_list)
        self.vao.render(instances=len(self.tile_list)) # render tiles (unordered)

        self.vert_list = sorted(self.vert_list, key=lambda tup: tup[2])
        self.write_vert_data(self.vert_list)
        #print(len(self.vert_list),"instances")
        self.texpack_texture.filter = moderngl.LINEAR, moderngl.LINEAR
        if r >= 0.03:
            self.shadowvao.render(instances=len(self.vert_list)) # render object shadows (ordered)
        self.texpack_texture.filter = moderngl.NEAREST, moderngl.NEAREST
        self.vao.render(instances=len(self.vert_list)) # render objects (ordered)
        self.write_vert_data(self.shadow_list)
        self.texpack_texture.filter = moderngl.LINEAR, moderngl.LINEAR
        self.shadowvao.render(instances=len(self.shadow_list)) # render non-object shadows (unordered)
        self.write_vert_data(self.weather_list)
        self.vao.render(instances=len(self.weather_list)) # render weather (unordered)
        self.texpack_texture.filter = moderngl.NEAREST, moderngl.NEAREST
        self.overlay_texture.use()
        self.quad_fs.render() # render UI overlay
        self.vert_list = []
        self.shadow_list = []
        self.weather_list = []
        self.tile_list = []
        self.light_list = []