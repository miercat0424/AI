# %%
from sympy.physics.mechanics import dynamicsymbols , ReferenceFrame , Point
from sympy import symbols , simplify
from sympy.physics.vector import init_vprinting
from IPython.display import Image

init_vprinting(use_latex = "mathjax" , pretty_print=False)
Image("notebooks/figures/human_balance_diagram.png")
# %%

inertial_frame  = ReferenceFrame("I")   # --> Feet Vector 
lower_leg_frame = ReferenceFrame("L")   # --> Legs 1 Vector
upper_leg_frame = ReferenceFrame("U")   # --> Legs 2 Vector
torso_frame     = ReferenceFrame("T")

theta1 , theta2 , theta3 = dynamicsymbols("theta1 , theta2 , theta3")

ankle   = Point("A")
knee    = Point("K")
hip     = Point("H")

lower_leg_mass_center = Point("L_o")
upper_leg_mass_center = Point("U_o")
torso_mass_center     = Point("T_o")

# Image("notebooks/figures/ankle_joint.png")
lower_leg_frame.orient(inertial_frame,"Axis",(theta1,inertial_frame.z))
lower_leg_frame.dcm(inertial_frame)
inertial_frame.dcm(lower_leg_frame)
# Image("notebooks/figures/knee_joint.png")
upper_leg_frame.orient(lower_leg_frame,"Axis",(theta2,lower_leg_frame.z)) 
upper_leg_frame.dcm(inertial_frame)
simplify(upper_leg_frame.dcm(inertial_frame))
# Image("notebooks/figures/hip_joint.png")
torso_frame.orient(upper_leg_frame,"Axis",(theta3,upper_leg_frame.z))
simplify(torso_frame.dcm(inertial_frame))
lower_leg_length = symbols("l_L")                           # --> make variable letters 
knee.set_pos(ankle,lower_leg_length * lower_leg_frame.y)    # --> point K + point A 
knee.pos_from(ankle)                                        # --> can find any other points
knee.pos_from(ankle).express(inertial_frame).simplify()
upper_leg_length = symbols("l_U")
hip.set_pos(knee,upper_leg_length * upper_leg_frame.y)
hip.pos_from(ankle)
hip.pos_from(ankle).express(inertial_frame).simplify()
# ---------------------------------------------------------------------------------------------------------
lower_leg_com_length , upper_leg_com_length , torso_com_length = symbols("d_L , d_U , d_T")

lower_leg_mass_center.set_pos(ankle,lower_leg_com_length * lower_leg_frame.y)   # --> Setting center points on one line
upper_leg_mass_center.set_pos(knee,upper_leg_com_length * upper_leg_frame.y)
torso_mass_center.set_pos(hip, torso_com_length * torso_frame.y)

lower_leg_mass_center.pos_from(ankle)   # --> show center points
upper_leg_mass_center.pos_from(ankle)
torso_mass_center.pos_from(ankle)
# ---------------------------------------------------------------------------------------------------------
omega1 , omega2 , omega3 = dynamicsymbols("omega1 , omega2 , omega3")

kinematical_differential_equations = [omega1 - theta1.diff() , 
                                      omega2 - theta2.diff() ,
                                      omega3 - theta3.diff() ]
kinematical_differential_equations 

lower_leg_frame.set_ang_vel(inertial_frame, omega1 * inertial_frame.z)
lower_leg_frame.ang_vel_in(inertial_frame)

upper_leg_frame.set_ang_vel(lower_leg_frame, omega2 * inertial_frame.z)
upper_leg_frame.ang_vel_in(inertial_frame)

torso_frame.set_ang_vel(upper_leg_frame, omega3 * inertial_frame.z)
torso_frame.ang_vel_in(inertial_frame)
# %% Setting Velocities
ankle.set_vel(inertial_frame, 0)
# v2pt --> velocity to point (?)
lower_leg_mass_center.v2pt_theory(ankle,inertial_frame,lower_leg_frame) # set start of vel point and define two frame
lower_leg_mass_center.vel(inertial_frame)                               # --> display velocity about inertial_frame
# %% knee
knee.v2pt_theory(ankle, inertial_frame, lower_leg_frame)
knee.vel(inertial_frame)
# %%
upper_leg_mass_center.v2pt_theory(knee,inertial_frame,upper_leg_frame)
upper_leg_mass_center.vel(inertial_frame)
# %%
hip.v2pt_theory(knee,inertial_frame,upper_leg_frame)
hip.vel(inertial_frame)
# %%
torso_mass_center.v2pt_theory(hip,inertial_frame,torso_frame)
torso_mass_center.vel(inertial_frame)
# %%
