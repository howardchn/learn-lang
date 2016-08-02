import math

rotation = 90 * math.pi / 180
scalex = 2
scaley = 2
offsetx = 5
offsety = 2

m11 = scalex * math.cos(rotation)
m12 = scaley * math.sin(rotation)
m21 = scalex * -math.sin(rotation)
m22 = scaley * math.cos(rotation)
ox = offsetx
oy = offsety

print('{0},{1},{2},{3},{4},{5}', m11, m12, m21, m22, ox, oy)
