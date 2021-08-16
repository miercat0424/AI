## Exercise 

"""
Create three vectors that lie in the $XY$ plane where each vector is:

1. of length $l$ that is at an angle of $\frac{\pi}{4}$ degrees from the $X$ axis
2. of length $10$ and is in the $-Y$ direction
3. of length $l$ and is $\theta$ radians from the $Y$ axis

Finally, add vectors 1 and 2 and substract $5$ times the third vector.

*Hint: SymPy has variables and trigonometic functions, for example `from sympy import tan, pi`*
"""

from sympy import cos, sin, pi
from sympy.abc import l , theta
from sympy.physics.vector import ReferenceFrame

N = ReferenceFrame("N")

v1 = l * cos(pi/4) * N.x + l * sin(pi/4) * N.y
v2 = -10 * N.y
v3 = -l * sin(theta) * N.x + l * cos(theta) * N.y

Answer = v1 + v2 - (5*v3)
print(f"\nAnswer : {Answer}\n")



