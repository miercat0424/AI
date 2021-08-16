from sympy.abc import * 
from sympy.physics.vector import ReferenceFrame , dot 

N = ReferenceFrame("N")

a = c * N.x + d * N.y + e * N.z
b = f * N.x + g * N.y + h * N.z

dots0 = dot(a,b)
dots1 = a.dot(b)

print(f"\nDot Product : \n\t{dots0}\n\t{dots1}\n")

