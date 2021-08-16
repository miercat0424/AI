from sympy import init_printing
from sympy.physics.vector import ReferenceFrame
from sympy.abc import c, d, e, f, g, h 

init_printing(use_latex="mathjax", pretty_print=False)

N = ReferenceFrame("N")                 # --> Units Vectors 
M = ReferenceFrame("M")                 # --> Units Vectors 

a = c * N.x + d * N.y + e * N.z         # --> set 3 types of Unit Vectors (Nx,Ny,Nz)
b = f * M.x + g * M.y + h * M.z         # --> set 3 types of Unit Vectors (Nx,Ny,Nz)

print(f"\nHow it looks : {a}\ncoefficients : {a.to_matrix(N)}\nMagnitude : {a.magnitude()}\n")
print(f"\nHow it looks : {b}\ncoefficients : {b.to_matrix(M)}\nMagnitude : {b.magnitude()}\n")

# Add Vetors // +
print(f"Adding each Vectors :\n\t{a+b}\n\t{a+a}\n" )

# Scaling Vetors with constant // *
print(f"Scaling each Vectors :\n\t{2*a}\n\t{20*b}\n" )
