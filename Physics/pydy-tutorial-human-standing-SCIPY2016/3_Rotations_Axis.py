from sympy.physics.vector import ReferenceFrame , dot , cross
from sympy.abc import * 

A = ReferenceFrame("A")
B = A.orientnew("B","Axis",(theta,A.z)) # <- make new axis from A, rotate theta about axis Z

a = c * A.x + d * A.y + e * A.z
b = f * B.x + g * B.y + h * B.z

print(f"\nA + B : {a+b}\n\nDot : {dot(a,b)}\n\nCross : {cross(a,b)}\n\nExpress :\n\n\t{(a+b).express(A)}\n\t{(a+b).express(B)}\n")
print(f"Shows B Matrix of Rotation :\n{B.dcm(A)}\n")