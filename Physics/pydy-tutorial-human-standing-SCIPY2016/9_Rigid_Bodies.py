# %%
from sympy.printing.pretty.pretty import pretty_print
from notebooks.solution.kinematics import * 
from sympy.physics.mechanics import inertia , RigidBody
from sympy import symbols
from sympy.physics.vector import init_vprinting

init_vprinting(use_latex = "mathjax" , pretty_print = False)

lower_leg_mass  = symbols("m_L")
upper_leg_mass  = symbols("m_U")
torso_mass      = symbols("m_T")

lower_leg_inertia   = symbols("I_Lz")
upper_leg_inertia   = symbols("I_Uz")
torso_inertia       = symbols("I_Tz")

lower_leg_inertia_dyadic = inertia(lower_leg_frame,0,0,lower_leg_inertia)
lower_leg_inertia_dyadic
lower_leg_inertia_dyadic.to_matrix(lower_leg_frame)
lower_leg_central_inertia = (lower_leg_inertia_dyadic , lower_leg_mass_center)

upper_leg_inertia_dyadic = inertia(upper_leg_frame,0,0,upper_leg_inertia)
upper_leg_inertia_dyadic.to_matrix(upper_leg_frame)
upper_leg_central_inertia = (upper_leg_inertia_dyadic , upper_leg_mass_center)

torso_inertia_dyadic = inertia(torso_frame,0,0,torso_mass_center)
torso_central_inertia = (torso_inertia_dyadic , torso_mass_center)
# %%
upper_leg = RigidBody("Upper leg" , upper_leg_mass_center , upper_leg_frame , upper_leg_mass , upper_leg_central_inertia)
torso = RigidBody("Torso" , torso_mass_center , torso_frame , torso_mass , torso_central_inertia)
