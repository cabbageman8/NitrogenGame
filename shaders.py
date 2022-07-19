simple_vertex_shader='''
#version 330
in vec2 vert;
in vec2 in_text;
uniform vec3 sunlight;
uniform sampler2D overlay;
out vec3 sun;
out vec2 v_text;
void main() {
    sun = sunlight;
    gl_Position = vec4(vert.x*2.0-1.0, 1.0-vert.y*2.0 , -1.0 , 1.0);
    v_text = in_text;
}
'''
simple_fragment_shader='''
#version 330
precision mediump float;
uniform sampler2D overlay;
in vec2 v_text;
in vec3 sun;
out vec4 f_color;
vec4 incolour;
void main() {
    incolour = texture(overlay,v_text);
    f_color = vec4(incolour.r*min(1.0, sun.r), incolour.g*min(1.0, sun.g), incolour.b*min(1.0, sun.b), incolour.a);
}
'''
normal_vertex_shader='''
#version 330
in vec2 vert;
in vec2 in_text;
in vec3 pos;
in vec2 size;
in float texnum;
in float sway;
uniform vec2 screen_size;
uniform vec2 player_offset;
uniform float tile_size;
uniform float time;
uniform sampler2D texpack;
out vec2 v_text;
out float thetexnum;
out vec3 screenpos;
vec2 packsize;
float zpos;
vec2 trans_pos;
vec2 trans_size;
float sway_translation;
vec2 sway_factor;
void main() {
    sway_translation = texnum+sway;
    sway_factor = vec2(sway/screen_size.x*7.0*cos(sway*time/700.0+sway_translation), 
                       sway/screen_size.y*7.0*sin(sway*time/700.0+sway_translation));
    trans_pos = vec2((pos.x-player_offset.x)/(screen_size.x/tile_size)*2.0-sway_factor.x, 
                     (pos.y-player_offset.y)/(screen_size.y/tile_size)*2.0-sway_factor.y);
    trans_size = vec2(size.x/screen_size.x*2.0+2.0*sway_factor.x, size.y/screen_size.y*2.0+2.0*sway_factor.y);
    packsize = vec2(textureSize(texpack, 0).xy);
    zpos = (pos.z>1.0) ? mod(pos.z, 1.0) : pos.z;
    zpos = (size.x==0.0) ? vert.x*zpos : ((size.y==0.0) ? (1.0-vert.y)*zpos : zpos);
    screenpos = vec3((trans_pos.x+vert.x*trans_size.x-1.0)*(1.0+zpos), (1.0-trans_pos.y-vert.y*trans_size.y)*(1.0+zpos), -pos.z);
    thetexnum = texnum;

    gl_Position = vec4(screenpos.x, screenpos.y, -pos.z/4.0, 1.0);
    v_text = vec2((in_text.x*0.98+0.01+mod(texnum, 128.0))*(128.0/packsize.x), (in_text.y*0.98+0.01+floor(texnum/128.0))*(128.0/packsize.y));
}
'''
normal_fragment_shader='''
#version 330
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
    if (incolour.a < 0.5) { discard; }
    light_value = sunlight;
    for (i=0;i<lightnum;i++) {
        light_dist = 0.1+(pow(lightpos[i].x/tile_size-screenpos.x/tile_size, 2.0)+
                          pow(lightpos[i].y/tile_size-screenpos.y/tile_size, 2.0))*20000.0;
        light_value = vec3(light_value.r + lighthue[i].r*(1.0/light_dist), light_value.g + lighthue[i].g*(1.0/light_dist), light_value.b + lighthue[i].b*(1.0/light_dist));
    }
    f_color = vec4(incolour.r*min(1.0, light_value.r), incolour.g*min(1.0, light_value.g), incolour.b*min(1.0, light_value.b), incolour.a);
}
'''
foreground_vertex_shader=normal_vertex_shader
foreground_fragment_shader='''
#version 330
precision mediump float;
uniform sampler2D texpack;
uniform sampler2D overlay;
uniform vec2 mouse_pos;
uniform float tile_size;
uniform vec2 screen_size;
uniform float time;
uniform vec3 sunlight;
in vec2 v_text;
in float thetexnum;
in vec3 screenpos;
out vec4 f_color;
vec4 incolour;
float mid_dist_2;
float mouse_dist_2;
float seethrough;
vec3 light_value;
void main() {
    incolour = texture(texpack,v_text);
    if (incolour.a < 0.5) { discard; }
    mid_dist_2 = (screenpos.x)*(screenpos.x)*screen_size.x/screen_size.y+(screenpos.y)*(screenpos.y)*screen_size.y/screen_size.x;
    mouse_dist_2 = (mouse_pos.x-screenpos.x)*(mouse_pos.x-screenpos.x)*(screen_size.x/screen_size.y)+(mouse_pos.y-screenpos.y)*(mouse_pos.y-screenpos.y)*(screen_size.y/screen_size.x);
    seethrough = (screenpos.z < -1.0) ? incolour.a*pow(sqrt(mid_dist_2)+sqrt(mouse_dist_2), 2.0) : incolour.a;

    light_value = sunlight;
    f_color = vec4(incolour.r*min(1.0, light_value.r), incolour.g*min(1.0, light_value.g), incolour.b*min(1.0, light_value.b), min(incolour.a,max(0.3*incolour.a, seethrough)));
}
'''
reflection_vertex_shader=normal_vertex_shader
reflection_fragment_shader='''
#version 330
precision mediump float;
uniform sampler2D texpack;
uniform vec3 sunlight;
in vec2 v_text;
out vec4 f_color;
vec4 incolour;
vec3 light_value;

void main() {
    incolour = texture(texpack,v_text);
    if (incolour.a < 0.000001) { discard; }
    light_value = sunlight;
    f_color = vec4(incolour.r*min(1.0, light_value.r), incolour.g*min(1.0, light_value.g), incolour.b*min(1.0, light_value.b), incolour.a);
}
'''
shadow_vertex_shader='''
#version 330
in vec2 vert;
in vec2 in_text;
in vec3 pos;
in vec2 size;
in float texnum;
in float sway;
uniform vec2 screen_size;
uniform vec2 player_offset;
uniform float tile_size;
uniform float time;
uniform sampler2D texpack;
uniform float sunangle;
out vec2 v_text;
out float thetexnum;
out vec3 screenpos;
vec2 packsize;
float zpos;
vec2 trans_pos;
vec2 trans_size;
float sway_translation;
vec2 sway_factor;
void main() {
    sway_translation = texnum+sway;
    sway_factor = vec2(sway/screen_size.x*7.0*cos(sway*time/700.0+sway_translation), 
                       sway/screen_size.y*7.0*sin(sway*time/700.0+sway_translation));
    trans_pos = vec2((pos.x-player_offset.x)/(screen_size.x/tile_size)*2.0-sway_factor.x, 
                     (pos.y-player_offset.y)/(screen_size.y/tile_size)*2.0-sway_factor.y);
    trans_size = vec2(size.x/screen_size.x*2.0+2.0*sway_factor.x, size.y/screen_size.y*2.0+2.0*sway_factor.y);
    packsize = vec2(textureSize(texpack, 0).xy);
    zpos = (pos.z<0.0) ? pos.z+1.0 : pos.z;
    zpos = (pos.z>1.0) ? pos.z-1.0 : pos.z;
    zpos = (size.x==0.0) ? vert.x*zpos : ((size.y==0.0) ? (1.0-vert.y)*zpos : zpos);
    screenpos = vec3((trans_pos.x+vert.x*trans_size.x-1.0)+sunangle*(zpos), (1.0-trans_pos.y-vert.y*trans_size.y)+0.3*(zpos), -pos.z);
    thetexnum = texnum;

    gl_Position = vec4(screenpos.x, screenpos.y, zpos-0.0001, 1.0);
    v_text = vec2((in_text.x*0.98+0.01+mod(texnum, 128.0))*(128.0/packsize.x), (in_text.y*0.98+0.01+floor(texnum/128.0))*(128.0/packsize.y));
}
'''
shadow_fragment_shader='''
#version 330
precision mediump float;
uniform sampler2D texpack;
uniform vec3 sunlight;
in vec2 v_text;
in vec3 screenpos;
vec4 incolour;
out vec4 f_color;
void main() {
    incolour = texture(texpack,v_text);
    if (incolour.a < 0.00001) { discard; }
    f_color = vec4(0, 0.02*sunlight.g, 0.05*sunlight.b, min(incolour.a,min(0.4, sunlight.r)));
}
'''
rain_vertex_shader='''
#version 330
in vec2 vert;
in vec2 in_text;
in vec3 pos;
in vec2 size;
in float texnum;
in float sway;
uniform vec2 screen_size;
uniform vec2 player_offset;
uniform float tile_size;
uniform float time;
uniform sampler2D texpack;
out vec2 v_text;
out float thetexnum;
out vec3 screenpos;
vec2 packsize;
float zpos;
vec2 trans_pos;
vec2 trans_size;
float sway_translation;
vec2 sway_factor;
void main() {
    sway_translation = texnum+sway;
    sway_factor = vec2(sway/screen_size.x*7.0*cos(sway*time/700.0+sway_translation), 
                       sway/screen_size.y*7.0*sin(sway*time/700.0+sway_translation));
    trans_pos = vec2((pos.x-player_offset.x)/(screen_size.x/tile_size)*2.0-sway_factor.x, 
                     (pos.y-player_offset.y)/(screen_size.y/tile_size)*2.0-sway_factor.y);
    trans_size = vec2(size.x/screen_size.x*2.0+2.0*sway_factor.x, size.y/screen_size.y*2.0+2.0*sway_factor.y);
    packsize = vec2(textureSize(texpack, 0).xy);
    zpos = mod(pos.z-time/400.0, 1.0);
    screenpos = vec3((trans_pos.x+vert.x*trans_size.x-1.0)*(1.0+zpos), (1.0-trans_pos.y-vert.y*trans_size.y)*(1.0+zpos), -pos.z);
    thetexnum = texnum;

    gl_Position = vec4(screenpos.x, screenpos.y, -pos.z/4.0, 1.0);
    v_text = vec2((in_text.x*0.98+0.01+mod(texnum, 128.0))*(128.0/packsize.x), (in_text.y*0.98+0.01+floor(texnum/128.0))*(128.0/packsize.y));
}
'''
rain_fragment_shader=reflection_fragment_shader