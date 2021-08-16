from sympy.physics.vector import ReferenceFrame , cross , dot   
from sympy.abc import * 
from sympy import pi 

keyboard_frame = ReferenceFrame("K")
intermediate_frame = ReferenceFrame("I")
screen_frame = ReferenceFrame("S")

intermediate_frame.orient(keyboard_frame,"Axis",(theta,-keyboard_frame.z))
screen_frame.orient(intermediate_frame,"Axis",(pi,intermediate_frame.y))

v = l * keyboard_frame.y + w * keyboard_frame.z - l * screen_frame.y 
v.express(keyboard_frame)

print(f"\n{v.express(keyboard_frame)}\n")