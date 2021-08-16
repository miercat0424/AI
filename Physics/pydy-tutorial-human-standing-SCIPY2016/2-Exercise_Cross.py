from sympy.physics.vector import ReferenceFrame , cross
from sympy.abc import * 

N = ReferenceFrame("N")

p1 = 23 * N.x - 12 * N.y 
p2 = 16 * N.x + 2 * N.y  - 4 * N.z
p3 = 1 * N.x + 0 * N.y  + 14 * N.z

v1 = p2 - p1
v2 = p3 - p1 

triangle_area = cross(v1,v2).magnitude() / 2 

print(f"Triangle of Area : {triangle_area}")
