import struct
import moderngl
import numpy as np
from math import pi, tau, sin, cos, tan, asin, acos, atan, ceil
import pygame

class glrenderer():
    def __init__(self, texpack, overlay):
        self.vert_list = []
        self.ctx = moderngl.create_context()
        self.prog = self.ctx.program(
    vertex_shader='''
#version 300 es
in vec2 vert;
in vec2 in_text;
in vec2 pos;
in vec2 size;
in float texnum;
uniform sampler2D texpack;
uniform sampler2D overlay;
out vec2 v_text;
void main() {
    vec2 packsize = vec2(textureSize(texpack, 0).xy);
    
    gl_Position = vec4(pos.x+vert.x*size.x-1.0, 1.0-pos.y+vert.y*size.y, 1.0/(texnum+2.0), 1.0);
    v_text = vec2(in_text.x*(packsize.y/packsize.x)+texnum*(packsize.y/packsize.x), in_text.y);
}
''',
    fragment_shader='''
#version 300 es
precision mediump float;
uniform sampler2D texpack;
uniform sampler2D overlay;
in vec2 v_text;
in float texnum;
out vec4 f_color;
vec4 incolour = texture(texpack,v_text).rgba;
vec4 incolour2 = texture(overlay,v_text).rgba;
void main() {
    f_color = vec4(incolour.r, incolour.g, incolour.b, incolour.a);
}
''')
        self.frag_texpack = self.prog['texpack']
        self.frag_overlay = self.prog['overlay']

        self.texpack_texture = self.ctx.texture(
            texpack.get_size(), 4,
            pygame.image.tostring(texpack, "RGBA", 1))
        self.texpack_texture.filter = moderngl.NEAREST, moderngl.NEAREST
        self.texpack_texture.swizzle = 'RGBA'
        self.overlay_texture = self.ctx.texture(
            overlay.get_size(), 4,
            pygame.image.tostring(overlay, "RGBA", 1))

        texture_data = texpack.get_view('1')
        self.texpack_texture.write(texture_data)
        self.overlay = overlay

        self.instance_data_pos = self.ctx.buffer(struct.pack(
            '2f', 0.0, 0.0) * (2 ** 16))
        self.instance_data_size = self.ctx.buffer(struct.pack(
            '2f', 0.0, 0.0) * (2 ** 16))
        self.instance_data_texnum = self.ctx.buffer(struct.pack(
            'f', 0.0)       * (2 ** 16))

        self.vbo = self.ctx.buffer(struct.pack('8f', 0, 1, 1, 1,
                                                     0, 0, 1, 0))

        self.uvmap = self.ctx.buffer(struct.pack('8f', 0, 0, 1, 0,
                                                       0, 1, 1, 1))

        self.ibo = self.ctx.buffer(struct.pack('6I', 0, 1, 2,
                                                     1, 2, 3))

        self.vao_content = [
            (self.vbo, '2f', 'vert'),
            (self.uvmap, '2f', 'in_text'),
            (self.instance_data_pos, '2f/i', 'pos'),
            (self.instance_data_size, '2f/i', 'size'),
            (self.instance_data_texnum, 'f/i', 'texnum')
        ]
        self.vao_wrapper = self.ctx.vertex_array(self.prog, self.vao_content, self.ibo)
        self.vao = self.ctx.vertex_array(self.prog, self.vao_content, self.ibo)

    def render(self):
        texture_data = self.overlay.get_view('1')
        self.overlay_texture.write(texture_data)
        self.ctx.clear(0 / 255, 0 / 255, 0 / 255, 0 / 255)
        self.ctx.enable(moderngl.DEPTH_TEST)
        self.texpack_texture.use(0)
        self.overlay_texture.use(1)
        self.instance_data_pos.write(b''.join(struct.pack(
            '2f',
            x, y
        ) for x, y, w, h, tex in self.vert_list))
        self.instance_data_size.write(b''.join(struct.pack(
            '2f',
            w, h
        ) for x, y, w, h, tex in self.vert_list))
        self.instance_data_texnum.write(b''.join(struct.pack(
            'f',
            tex
        ) for x, y, w, h, tex in self.vert_list))
        #print(len(self.vert_list),"instances")
        self.vao.render(instances=len(self.vert_list))
        self.vert_list = []
        pygame.display.flip()