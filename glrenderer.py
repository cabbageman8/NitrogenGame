import struct
import moderngl
import glcontext
from math import pi, tau, sin, cos, tan, asin, acos, atan, ceil
import time
import pygame

from shaders import simple_vertex_shader, simple_fragment_shader, normal_vertex_shader, normal_fragment_shader, foreground_vertex_shader, foreground_fragment_shader, shadow_vertex_shader, shadow_fragment_shader

class glrenderer():
    def __init__(self, texpack, overlay):
        self.vert_list = []
        self.shadow_list = []
        self.weather_list = []
        self.tile_list = []
        self.light_list = []
        self.foreground_list = []
        self.ctx = moderngl.create_context()
        self.ctx.enable(moderngl.BLEND)
        self.simple_prog = self.ctx.program( vertex_shader=simple_vertex_shader, fragment_shader=simple_fragment_shader)
        self.normal_prog = self.ctx.program( vertex_shader=normal_vertex_shader, fragment_shader=normal_fragment_shader)
        self.foreground_prog = self.ctx.program( vertex_shader=foreground_vertex_shader, fragment_shader=foreground_fragment_shader)
        self.shadow_prog = self.ctx.program( vertex_shader=shadow_vertex_shader, fragment_shader=shadow_fragment_shader)

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
        self.vao = self.ctx.vertex_array(self.normal_prog, self.vao_content, self.ibo)
        self.shadowvao = self.ctx.vertex_array(self.shadow_prog, self.vao_content, self.ibo)
        self.foregroundvao = self.ctx.vertex_array(self.foreground_prog, self.vao_content, self.ibo)
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
        self.instance_data_pos.write(b''.join(struct.pack( '3f', x, y, z ) for x, y, z, w, h, tex in vert_list))
        self.instance_data_size.write(b''.join(struct.pack( '2f', w, h ) for x, y, z, w, h, tex in vert_list))
        self.instance_data_texnum.write(b''.join(struct.pack( '1f', tex ) for x, y, z, w, h, tex in vert_list))

    def render_vert_list(self, vert_list, vao, is_ln=0, is_tex=1, is_shadow=0, is_sorted=0):
        if is_sorted:
            vert_list = sorted(vert_list, key=lambda tup: tup[2])
        self.write_vert_data(vert_list)
        if is_shadow:
            self.texpack_texture.filter = moderngl.LINEAR, moderngl.LINEAR
            if self.r >= 0.03:
                self.shadowvao.render(instances=len(vert_list))
        if is_tex:
            if is_ln:
                self.texpack_texture.filter = moderngl.LINEAR, moderngl.LINEAR
            else:
                self.texpack_texture.filter = moderngl.NEAREST, moderngl.NEAREST
            vao.render(instances=len(vert_list))

    def render(self, mouse_pos, tile_size):
        self.ctx.clear()
        self.texpack_texture.use()
        self.r = min(max(sin((time.time() * tau) / 60 / 10) + 1.32, 0), 1)**4
        self.foreground_prog['mouse_pos'].value = mouse_pos
        self.normal_prog['tile_size'].value = self.foreground_prog['tile_size'].value = self.shadow_prog['tile_size'].value = tile_size/100.0
        self.normal_prog['screen_size'].value = self.foreground_prog['screen_size'].value = self.ctx.screen.size
        self.normal_prog['sunlight'].value = self.foreground_prog['sunlight'].value = self.shadow_prog['sunlight'].value = (max(self.r,0.03), max(self.r**2,0.05), max(self.r**4,0.06))
        self.shadow_prog['sunangle'].value = tan((time.time() * pi) / 60 / 10 - pi/4)/2
        self.normal_prog['lightnum'].value = min(len(self.light_list), 128)
        self.normal_prog['lightpos'].value = (list(l[0] for l in self.light_list)+[(0, 0, 0),]*128)[:128]
        self.normal_prog['lighthue'].value = (list(l[1] for l in self.light_list)+[(0, 0, 0),]*128)[:128]

        # shader progs are ready to use
        self.render_vert_list(vert_list=self.tile_list, vao=self.vao)
        self.render_vert_list(vert_list=self.vert_list, vao=self.vao, is_shadow=1, is_sorted=1)
        self.render_vert_list(vert_list=self.foreground_list, vao=self.foregroundvao, is_shadow=1, is_sorted=1)
        self.render_vert_list(vert_list=self.shadow_list, vao=None, is_tex=0, is_shadow=1)
        self.render_vert_list(vert_list=self.weather_list, vao=self.foregroundvao, is_ln=1, is_tex=1, is_shadow=1)

        self.texpack_texture.filter = (moderngl.NEAREST, moderngl.NEAREST)
        self.overlay_texture.use()
        self.quad_fs.render() # render UI overlay
        self.tile_list = []
        self.vert_list = []
        self.foreground_list = []
        self.shadow_list = []
        self.weather_list = []
        self.light_list = []