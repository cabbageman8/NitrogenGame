import random
import struct
import moderngl
from PIL import Image
import os
import glcontext
from math import pi, tau, sin, cos, tan, asin, acos, atan, ceil
import time
import pygame
from array import array

from shaders import simple_vertex_shader, simple_fragment_shader,\
    normal_vertex_shader, normal_fragment_shader,\
    foreground_vertex_shader, foreground_fragment_shader,\
    shadow_vertex_shader, shadow_fragment_shader,\
    reflection_vertex_shader, reflection_fragment_shader,\
    rain_vertex_shader, rain_fragment_shader

class glrenderer():
    def instance_data_factory(self):
        return [
            self.ctx.buffer(struct.pack(
                '3f', 0.0, 0.0, 0.0) * (2 ** 22)),
            self.ctx.buffer(struct.pack(
                '2f', 0.0, 0.0) * (2 ** 22)),
            self.ctx.buffer(struct.pack(
                '1f', 0.0) * (2 ** 22)),
            self.ctx.buffer(struct.pack(
                '1f', 0.0) * (2 ** 22)),
        ]
    def vao_factory(self, program):
        vao_instance_data = self.instance_data_factory()
        vao = self.ctx.vertex_array(program, self.vao_content + [
            (vao_instance_data[0], '3f/i', 'pos'),
            (vao_instance_data[1], '2f/i', 'size'),
            (vao_instance_data[2], 'f/i', 'texnum'),
            (vao_instance_data[3], 'f/i', 'texlen')], self.ibo)
        vao.extra = [vao_instance_data, {}, set(), set()]
        return vao

    def __init__(self, texpack, overlay, max_tex):
        self.max_tex = max_tex
        self.reflection_list = set()
        self.vert_list = set()
        self.shadow_list = set()
        self.weather_list = set()
        self.rain_list = set()
        self.tile_list = set()
        self.light_list = []
        self.light_buffer = []
        self.foreground_list = set()
        self.ontop_list = set()
        self.ctx = moderngl.create_context()
        self.ctx.enable(moderngl.BLEND)
        self.ctx.enable(moderngl.DEPTH_TEST)
        #                       amount from SRC,     amount from DST
        self.ctx.blend_func = (self.ctx.SRC_ALPHA, self.ctx.ONE_MINUS_SRC_ALPHA, # colour
                               self.ctx.SRC_ALPHA, self.ctx.ONE_MINUS_SRC_ALPHA) # alpha
        #                          operation between SRC and DST
        self.ctx.blend_equation = (self.ctx.FUNC_ADD, # colour
                                   self.ctx.FUNC_ADD) # alpha
        self.simple_prog = self.ctx.program( vertex_shader=simple_vertex_shader, fragment_shader=simple_fragment_shader)
        self.normal_prog = self.ctx.program( vertex_shader=normal_vertex_shader, fragment_shader=normal_fragment_shader)
        self.foreground_prog = self.ctx.program( vertex_shader=foreground_vertex_shader, fragment_shader=foreground_fragment_shader)
        self.reflection_prog = self.ctx.program( vertex_shader=reflection_vertex_shader, fragment_shader=reflection_fragment_shader)
        self.shadow_prog = self.ctx.program( vertex_shader=shadow_vertex_shader, fragment_shader=shadow_fragment_shader)
        self.rain_prog = self.ctx.program(vertex_shader=rain_vertex_shader, fragment_shader=rain_fragment_shader)

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

        sky = pygame.image.load(os.path.join("data", "sky.png")).convert_alpha()
        self.sun_texture = self.ctx.texture(sky.get_size(), 4)
        self.sun_texture.swizzle = 'BGRA'
        self.sun_texture.write(sky.get_view('1'))

        moon = pygame.image.load(os.path.join("data", "moon.png")).convert_alpha()
        self.moon_texture = self.ctx.texture(moon.get_size(), 4)
        self.moon_texture.swizzle = 'BGRA'
        self.moon_texture.write(moon.get_view('1'))

        texture_data = texpack.get_view('1')
        self.texpack_texture.write(texture_data)
        texture_data = overlay.get_view('1')
        self.overlay_texture.write(texture_data)

        self.vbo = self.ctx.buffer(struct.pack('8f', 0, 0, 1, 0,
                                          0, 1, 1, 1))

        self.uvmap = self.ctx.buffer(struct.pack('8f', 0, 0, 1, 0,
                                            0, 1, 1, 1))

        self.ibo = self.ctx.buffer(struct.pack('6I', 0, 1, 2,
                                          1, 2, 3))

        self.vao_content = [(self.vbo, '2f', 'vert'), (self.uvmap, '2f', 'in_text')]

        self.cloudvao = self.vao_factory(self.reflection_prog)
        self.reflectvao = self.vao_factory(self.reflection_prog)
        self.tilevao = self.vao_factory(self.normal_prog)
        self.objectvao = self.vao_factory(self.normal_prog)
        self.foregroundvao = self.vao_factory(self.foreground_prog)
        self.rainvao = self.vao_factory(self.rain_prog)
        self.weathervao = self.vao_factory(self.reflection_prog)
        self.ontopvao = self.vao_factory(self.normal_prog)
        self.shadowvao = self.vao_factory(self.shadow_prog)
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

                                                                            # cabbageman's Quick Memory Management (CMQMM)
    def find_free_mem(self, vert_list, vao):
        for byt, location in tuple(vao.extra[1].items()):                   # Check every item in the initial GPU buffer
            if location >= len(vert_list):
                del vao.extra[1][byt]                                       # If initial item is past the end of new data, delete its location
            elif byt not in vert_list:
                vao.extra[3].add(location)                                  # If initial item is not in new data, record its location as a free hole

    def find_changed_mem(self, vert_list, vao):
        tail = 0
        update_mem = []
        new_locations = {}
        for byt in vert_list:                                               # Every input item needs a location
            try:
                new_locations[byt] = vao.extra[1][byt]                      # If item hasn't changed then don't change it
            except KeyError:
                if vao.extra[3]:                                            # else if there are free holes in memory, fill them in any order
                    location = vao.extra[3].pop()
                else:                                                       # if we have a new item and there are no free holes in memory, simply append it to the tail
                    location = len(vao.extra[1]) + tail
                    tail += 1
                update_mem.append((location, byt))                          # Add the memory change to list of changes
                new_locations[byt] = location                               # Keep track of current GPU buffer as we will need it next time
        return update_mem, new_locations

    def set_memory(self, buffer, update_mem):
        for location, byt in update_mem:
            u = 4
            buffer[0].write(byt[0*u:3*u], offset=location * 3 * u)
            buffer[1].write(byt[3*u:5*u], offset=location * 2 * u)
            buffer[2].write(byt[5*u:6*u], offset=location * u)
            buffer[3].write(byt[6*u:7*u], offset=location * u)

    def write_vert_data(self, vert_list, vao):
        self.find_free_mem(vert_list, vao)                                  # Find memory locations which are no longer used
        update_mem, vao.extra[1] = self.find_changed_mem(vert_list, vao)    # Assign each item to a location, without affecting unchanged items
        self.set_memory(vao.extra[0], update_mem)                           # Execute memory changes

    def set_vert_buffers(self, vert_list, vao, is_reset=0):
        vao.extra[2] = vert_list.copy()
        if is_reset:
            self.set_memory(vao.extra[0], enumerate(vert_list))
        else:
            self.write_vert_data(vert_list, vao)

    def render_vert_list(self, vao, is_ln=0, is_tex=1, is_shadow=0, is_depth_test=0):
        if is_shadow:
            self.texpack_texture.filter = moderngl.LINEAR, moderngl.LINEAR
            if self.r >= 0.03:
                self.ctx.disable(moderngl.DEPTH_TEST)
                shadowvao = self.ctx.vertex_array(self.shadow_prog, self.vao_content + [
                    (vao.extra[0][0], '3f/i', 'pos'),
                    (vao.extra[0][1], '2f/i', 'size'),
                    (vao.extra[0][2], 'f/i', 'texnum'),
                    (vao.extra[0][3], 'f/i', 'texlen')], self.ibo)
                shadowvao.render(instances=len(vao.extra[2]))
                shadowvao.release()
        if is_depth_test:
            self.ctx.enable(moderngl.DEPTH_TEST)
        else:
            self.ctx.disable(moderngl.DEPTH_TEST)
        if is_tex:
            if is_ln:
                self.texpack_texture.filter = moderngl.LINEAR, moderngl.LINEAR
            else:
                self.texpack_texture.filter = moderngl.NEAREST, moderngl.NEAREST
            vao.render(instances=len(vao.extra[2]))

    def set_uniforms(self, mouse_pos, screen_coords, tile_size):
        self.ctx.clear()
        self.r = min(max(sin((time.time() * tau) / 60 / 10) + 1.32, 0), 1)**4
        self.normal_prog['tile_size'].value =     self.foreground_prog['tile_size'].value =     self.shadow_prog['tile_size'].value =     self.reflection_prog['tile_size'].value =     self.rain_prog['tile_size'].value =     tile_size
        self.normal_prog['time'].value =          self.foreground_prog['time'].value =          self.shadow_prog['time'].value =          self.reflection_prog['time'].value =          self.rain_prog['time'].value =     (time.time()*1000)%2**16
        self.normal_prog['screen_size'].value =   self.foreground_prog['screen_size'].value =   self.shadow_prog['screen_size'].value =   self.reflection_prog['screen_size'].value =   self.rain_prog['screen_size'].value =     self.ctx.screen.viewport[2:]
        self.normal_prog['player_offset'].value = self.foreground_prog['player_offset'].value = self.shadow_prog['player_offset'].value = self.reflection_prog['player_offset'].value = self.rain_prog['player_offset'].value =     screen_coords
        self.normal_prog['sunlight'].value =      self.foreground_prog['sunlight'].value =      self.shadow_prog['sunlight'].value =      self.reflection_prog['sunlight'].value =      self.rain_prog['sunlight'].value =     (max(self.r,0.03), max(self.r**2,0.05), max(self.r**4,0.06))
        self.normal_prog['max_tex'].value =       self.foreground_prog['max_tex'].value =       self.shadow_prog['max_tex'].value =       self.reflection_prog['max_tex'].value =       self.rain_prog['max_tex'].value =      self.max_tex
        self.foreground_prog['mouse_pos'].value = mouse_pos
        self.shadow_prog['sunangle'].value = tan((time.time() * pi) / 60 / 10 - pi/4)/2
        self.normal_prog['lightnum'].value = min(len(self.light_buffer), 128)
        self.normal_prog['lightpos'].value = (list(l[0] for l in self.light_buffer)+[(0, 0, 0),]*128)[:128]
        self.normal_prog['lighthue'].value = (list(l[1] for l in self.light_buffer)+[(0, 0, 0),]*128)[:128]

    def set_verts(self):
        self.set_vert_buffers(vert_list=self.reflection_list, vao=self.reflectvao)
        self.set_vert_buffers(vert_list=self.tile_list, vao=self.tilevao)
        self.set_vert_buffers(vert_list=self.vert_list, vao=self.objectvao)
        self.set_vert_buffers(vert_list=self.foreground_list, vao=self.foregroundvao)
        self.set_vert_buffers(vert_list=self.rain_list, vao=self.rainvao)
        self.light_buffer = self.light_list.copy()

    def render(self, mouse_pos, screen_coords, tile_size):
        self.set_uniforms(mouse_pos, screen_coords, tile_size)
        # shader progs are ready to use
        if self.r >= 0.03:
            self.simple_prog['sunlight'].value = (max(self.r, 0.03), max(self.r ** 2, 0.05), max(self.r ** 4, 0.06))
            self.sun_texture.use()
        else:
            moon = min(1, 0.01/self.r)
            self.simple_prog['sunlight'].value = (moon, moon, moon)
            self.moon_texture.use()
        self.quad_fs.render()

        self.texpack_texture.use()

        self.set_vert_buffers(vert_list=self.shadow_list, vao=self.cloudvao, is_reset=1)
        self.render_vert_list(vao=self.cloudvao, is_ln=1, is_tex=1, is_shadow=0)

        self.render_vert_list(vao=self.reflectvao, is_ln=1, is_tex=1, is_shadow=0)
        #self.render_vert_list(vao=self.reflectvao, is_ln=1)
        self.render_vert_list(vao=self.tilevao)
        self.render_vert_list(vao=self.objectvao, is_shadow=1, is_depth_test=1)
        self.set_vert_buffers(vert_list=sorted(self.ontop_list, key= lambda n: struct.unpack("f", n[4*2:4*3])), vao=self.ontopvao, is_reset=1)
        self.render_vert_list(vao=self.ontopvao, is_ln=1)
        self.render_vert_list(vao=self.foregroundvao, is_shadow=1, is_depth_test=1)
        self.render_vert_list(vao=self.rainvao, is_ln=1)

        self.set_vert_buffers(vert_list=self.weather_list, vao=self.weathervao, is_reset=1)
        # self.set_vert_buffers(vert_list=self.shadow_list, vao=self.reflectvao, is_reset=1)
        self.set_vert_buffers(vert_list=self.shadow_list, vao=self.shadowvao, is_reset=1)

        self.render_vert_list(vao=self.weathervao, is_ln=1, is_shadow=1)
        self.render_vert_list(vao=self.shadowvao, is_tex=0, is_shadow=1)

        self.shadow_list.clear()
        self.weather_list.clear()
        self.ontop_list.clear()

        self.texpack_texture.filter = (moderngl.NEAREST, moderngl.NEAREST)
        self.simple_prog['sunlight'].value = (1,1,1)
        self.overlay_texture.use()
        self.quad_fs.render() # render UI overlay