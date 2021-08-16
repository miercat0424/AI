## Exercise

from sympy.abc import *
from sympy.physics.vector import ReferenceFrame , dot  
from sympy import acos 

N = ReferenceFrame("N")

v1 = a * N.x + b * N.y + a * N.z
v2 = b * N.x + a * N.y + b * N.z

"""
find the angles between the two vectors using dot product
"""

angle = acos(dot(v1,v2))//(v1.magnitude()*v2.magnitude()) # <-- acos = arc cos

print(f"\nAngle : {angle}\n")