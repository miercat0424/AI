from sympy.physics.vector import ReferenceFrame , cross
from sympy.abc import *

N = ReferenceFrame("N")

a = c * N.x + d * N.y + e * N.z
b = f * N.x + g * N.y + h * N.z

cross0 = cross(a,b)         # --> 외적
cross1 = a.cross(b)

print(f"\nCross Product : \n\t{cross0}\n\t{cross1}\n")