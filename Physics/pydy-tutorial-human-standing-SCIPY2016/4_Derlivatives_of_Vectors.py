# %%
from sympy.physics.vector import ReferenceFrame , cross , dot   
from sympy.abc import * 
from sympy import Function

A = ReferenceFrame("A")
B = A.orientnew("B","Axis",(theta,A.z))

a = c * A.x + d * A.y + e * A.z 

theta = Function("theta")(t)

# %%
theta

# %%
theta.diff(t)
# %%
B.ang_vel_in(A)