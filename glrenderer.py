import random
import struct
import moderngl
import glcontext
from math import pi, tau, sin, cos, tan, asin, acos, atan, ceil
import time
import pygame
from array import array

from shaders import simple_vertex_shader, simple_fragment_shader, normal_vertex_shader, normal_fragment_shader, foreground_vertex_shader, foreground_fragment_shader, shadow_vertex_shader, shadow_fragment_shader

class glrenderer():
    def __init__(self, texpack, overlay):
        self.reflection_list = []
        self.vert_list = []
        self.shadow_list = []
        self.weather_list = []
        self.tile_list = []
        self.light_list = []
        self.foreground_list = []
        self.volatile_memory = []
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

        self.reflectvao_instance_data = [
            self.ctx.buffer(struct.pack(
                '3f', 0.0, 0.0, 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '2f', 0.0, 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '1f', 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '1f', 0.0) * (2 ** 16)),
        ]
        self.tilevao_instance_data = [
            self.ctx.buffer(struct.pack(
                '3f', 0.0, 0.0, 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '2f', 0.0, 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '1f', 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '1f', 0.0) * (2 ** 16)),
        ]
        self.objectvao_instance_data = [
            self.ctx.buffer(struct.pack(
                '3f', 0.0, 0.0, 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '2f', 0.0, 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '1f', 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '1f', 0.0) * (2 ** 16)),
        ]
        self.shadowvao_instance_data = [
            self.ctx.buffer(struct.pack(
                '3f', 0.0, 0.0, 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '2f', 0.0, 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '1f', 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '1f', 0.0) * (2 ** 16)),
        ]
        self.foregroundvao_instance_data = [
            self.ctx.buffer(struct.pack(
                '3f', 0.0, 0.0, 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '2f', 0.0, 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '1f', 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '1f', 0.0) * (2 ** 16)),
        ]
        self.weathervao_instance_data = [
            self.ctx.buffer(struct.pack(
                '3f', 0.0, 0.0, 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '2f', 0.0, 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '1f', 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '1f', 0.0) * (2 ** 16)),
        ]
        self.volatilevao_instance_data = [
            self.ctx.buffer(struct.pack(
                '3f', 0.0, 0.0, 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '2f', 0.0, 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '1f', 0.0) * (2 ** 16)),
            self.ctx.buffer(struct.pack(
                '1f', 0.0) * (2 ** 16)),
        ]

        self.vbo = self.ctx.buffer(struct.pack('8f', 0, 0, 1, 0,
                                                     0, 1, 1, 1))

        self.uvmap = self.ctx.buffer(struct.pack('8f', 0, 0, 1, 0,
                                                       0, 1, 1, 1))

        self.ibo = self.ctx.buffer(struct.pack('6I', 0, 1, 2,
                                                     1, 2, 3))

        self.vao_content = [ (self.vbo, '2f', 'vert'), (self.uvmap, '2f', 'in_text') ]
        self.reflectvao = self.ctx.vertex_array(self.normal_prog, self.vao_content + [
            (self.reflectvao_instance_data[0], '3f/i', 'pos'),
            (self.reflectvao_instance_data[1], '2f/i', 'size'),
            (self.reflectvao_instance_data[2], 'f/i', 'texnum'),
            (self.reflectvao_instance_data[3], 'f/i', 'sway')], self.ibo)
        self.reflectvao.extra = [self.reflectvao_instance_data, {}, set(), set()]
        self.tilevao = self.ctx.vertex_array(self.normal_prog, self.vao_content + [
            (self.tilevao_instance_data[0], '3f/i', 'pos'),
            (self.tilevao_instance_data[1], '2f/i', 'size'),
            (self.tilevao_instance_data[2], 'f/i', 'texnum'),
            (self.tilevao_instance_data[3], 'f/i', 'sway')], self.ibo)
        self.tilevao.extra = [self.tilevao_instance_data, {}, set(), set()]
        self.objectvao = self.ctx.vertex_array(self.normal_prog, self.vao_content + [
            (self.objectvao_instance_data[0], '3f/i', 'pos'),
            (self.objectvao_instance_data[1], '2f/i', 'size'),
            (self.objectvao_instance_data[2], 'f/i', 'texnum'),
            (self.objectvao_instance_data[3], 'f/i', 'sway')], self.ibo)
        self.objectvao.extra = [self.objectvao_instance_data, {}, set(), set()]
        self.shadowvao = self.ctx.vertex_array(self.shadow_prog, self.vao_content + [
            (self.shadowvao_instance_data[0], '3f/i', 'pos'),
            (self.shadowvao_instance_data[1], '2f/i', 'size'),
            (self.shadowvao_instance_data[2], 'f/i', 'texnum'),
            (self.shadowvao_instance_data[3], 'f/i', 'sway')], self.ibo)
        self.shadowvao.extra = [self.shadowvao_instance_data, {}, set(), set()]
        self.foregroundvao = self.ctx.vertex_array(self.foreground_prog, self.vao_content + [
            (self.foregroundvao_instance_data[0], '3f/i', 'pos'),
            (self.foregroundvao_instance_data[1], '2f/i', 'size'),
            (self.foregroundvao_instance_data[2], 'f/i', 'texnum'),
            (self.foregroundvao_instance_data[3], 'f/i', 'sway')], self.ibo)
        self.foregroundvao.extra = [self.foregroundvao_instance_data, {}, set(), set()]
        self.weathervao = self.ctx.vertex_array(self.foreground_prog, self.vao_content + [
            (self.weathervao_instance_data[0], '3f/i', 'pos'),
            (self.weathervao_instance_data[1], '2f/i', 'size'),
            (self.weathervao_instance_data[2], 'f/i', 'texnum'),
            (self.weathervao_instance_data[3], 'f/i', 'sway')], self.ibo)
        self.weathervao.extra = [self.weathervao_instance_data, {}, set(), set()]
        self.volatilevao = self.ctx.vertex_array(self.normal_prog, self.vao_content + [
            (self.volatilevao_instance_data[0], '3f/i', 'pos'),
            (self.volatilevao_instance_data[1], '2f/i', 'size'),
            (self.volatilevao_instance_data[2], 'f/i', 'texnum'),
            (self.volatilevao_instance_data[3], 'f/i', 'sway')], self.ibo)
        self.volatilevao.extra = [self.volatilevao_instance_data, {}, set(), set()]
        self.quad_fs = self.ctx.vertex_array(self.simple_prog, self.vao_content, self.ibo)

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

    def find_free_mem(self, vert_list, vao):
        vao.extra[2].clear()
        for vert in vert_list:
            vao.extra[2].add(vert.tobytes())

        for key, value in tuple(vao.extra[1].items()):
            if value >= len(vao.extra[2]):
                del vao.extra[1][key]
            elif key not in vao.extra[2]:
                vao.extra[3].add(value)

    def find_changed_mem(self, vao):
        tail = 0
        update_mem = []
        new_locations = {}
        for byt in vao.extra[2]:
            if byt not in vao.extra[1].keys():
                if vao.extra[3]:
                    location = vao.extra[3].pop()
                else:
                    location = len(vao.extra[1]) + tail
                    tail += 1
                update_mem.append((location, byt))
                new_locations.update({byt: location})
            else:
                new_locations.update({byt: vao.extra[1][byt]})
        return update_mem, new_locations

    def set_memory(self, buffer, update_mem):
        for location, byt in update_mem:
            u = 4
            x, y, z, w, h, tex, sway = struct.unpack('7f', byt)
            buffer[0].write(struct.pack('3f', x, y, z), offset=location * 3 * u)
            buffer[1].write(struct.pack('2f', w, h), offset=location * 2 * u)
            buffer[2].write(struct.pack('f', tex), offset=location * u)
            buffer[3].write(struct.pack('f', sway), offset=location * u)

    def write_vert_data(self, vert_list, vao):
        self.find_free_mem(vert_list, vao)
        update_mem, vao.extra[1] = self.find_changed_mem(vao)
        self.set_memory(vao.extra[0], update_mem)

    def render_vert_list(self, vert_list, vao, is_ln=0, is_tex=1, is_shadow=0):
        self.write_vert_data(vert_list, vao)
        if is_shadow:
            self.texpack_texture.filter = moderngl.LINEAR, moderngl.LINEAR
            if self.r >= 0.03:
                shadowvao = self.ctx.vertex_array(self.shadow_prog, self.vao_content + [
                    (vao.extra[0][0], '3f/i', 'pos'),
                    (vao.extra[0][1], '2f/i', 'size'),
                    (vao.extra[0][2], 'f/i', 'texnum'),
                    (vao.extra[0][3], 'f/i', 'sway')], self.ibo)
                shadowvao.render(instances=len(vert_list))
                shadowvao.release()
        if is_tex:
            if is_ln:
                self.texpack_texture.filter = moderngl.LINEAR, moderngl.LINEAR
            else:
                self.texpack_texture.filter = moderngl.NEAREST, moderngl.NEAREST
            vao.render(instances=len(vert_list))

    def render(self, mouse_pos, screen_coords, tile_size):
        self.ctx.clear()
        self.texpack_texture.use()
        self.r = min(max(sin((time.time() * tau) / 60 / 10) + 1.32, 0), 1)**4
        self.normal_prog['tile_size'].value =     self.foreground_prog['tile_size'].value =     self.shadow_prog['tile_size'].value =     tile_size/100.0
        self.normal_prog['time'].value =          self.foreground_prog['time'].value =          self.shadow_prog['time'].value =          (time.time()*1000)%2**16
        self.normal_prog['screen_size'].value =   self.foreground_prog['screen_size'].value =   self.shadow_prog['screen_size'].value =   self.ctx.screen.viewport[2:]
        self.normal_prog['player_offset'].value = self.foreground_prog['player_offset'].value = self.shadow_prog['player_offset'].value = screen_coords
        self.normal_prog['sunlight'].value =      self.foreground_prog['sunlight'].value =      self.shadow_prog['sunlight'].value =      (max(self.r,0.03), max(self.r**2,0.05), max(self.r**4,0.06))
        self.foreground_prog['mouse_pos'].value = mouse_pos
        self.shadow_prog['sunangle'].value = tan((time.time() * pi) / 60 / 10 - pi/4)/2
        self.normal_prog['lightnum'].value = min(len(self.light_list), 128)
        self.normal_prog['lightpos'].value = (list(l[0] for l in self.light_list)+[(0, 0, 0),]*128)[:128]
        self.normal_prog['lighthue'].value = (list(l[1] for l in self.light_list)+[(0, 0, 0),]*128)[:128]

        # shader progs are ready to use
        self.render_vert_list(vert_list=list(reversed(self.reflection_list)), vao=self.reflectvao)
        self.render_vert_list(vert_list=self.tile_list, vao=self.tilevao)
        self.render_vert_list(vert_list=self.vert_list, vao=self.objectvao, is_shadow=1)
        self.render_vert_list(vert_list=self.foreground_list, vao=self.foregroundvao, is_shadow=1)
        self.render_vert_list(vert_list=self.shadow_list, vao=self.shadowvao, is_tex=0, is_shadow=1)
        self.render_vert_list(vert_list=self.weather_list, vao=self.weathervao, is_ln=1, is_tex=1, is_shadow=1)
        self.render_vert_list(vert_list=self.volatile_memory, vao=self.volatilevao, is_shadow=1)

        self.reflection_list = []
        self.tile_list = []
        self.vert_list = []
        self.foreground_list = []
        self.shadow_list = []
        self.weather_list = []
        self.light_list = []

        self.volatile_memory = []
        self.texpack_texture.filter = (moderngl.NEAREST, moderngl.NEAREST)
        self.overlay_texture.use()
        self.quad_fs.render() # render UI overlay