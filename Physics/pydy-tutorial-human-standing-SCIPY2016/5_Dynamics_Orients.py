# %%
from IPython.display import Image
from sympy.printing.pretty.pretty import pretty, pretty_print
from sympy import symbols , simplify
from sympy.physics.mechanics import dynamicsymbols , ReferenceFrame , Point
from sympy.physics.vector import init_vprinting

init_vprinting(use_latex = "mathjax" , pretty_print=False)
Image("notebooks/figures/human_balance_diagram.png")

# %%
inertial_frame  = ReferenceFrame("I")   # --> Feet Vector 
lower_leg_frame = ReferenceFrame("L")   # --> Legs 1 Vector
upper_leg_frame = ReferenceFrame("U")   # --> Legs 2 Vector

theta1 , theta2 , theta3 = dynamicsymbols("theta1 , theta2 , theta3")
Image("notebooks/figures/ankle_joint.png")

# %% Set Same Z Axis , inertial_frame & Lower legs frames 
lower_leg_frame.orient(inertial_frame,"Axis",(theta1,inertial_frame.z))
# %%
lower_leg_frame.dcm(inertial_frame)
# %% Same value different direction
inertial_frame.dcm(lower_leg_frame)
# %%
Image("notebooks/figures/knee_joint.png")
# %% Set Same Z Axis , Lower legs frames & Upper legs frames
upper_leg_frame.orient(lower_leg_frame,"Axis",(theta2,lower_leg_frame.z)) 
# %% 
upper_leg_frame.dcm(inertial_frame)
# %% Can change dcm results to look clear
simplify(upper_leg_frame.dcm(inertial_frame))
# %%
Image("notebooks/figures/hip_joint.png")
# %%
torso_frame = ReferenceFrame("T")
torso_frame.orient(upper_leg_frame,"Axis",(theta3,upper_leg_frame.z))
simplify(torso_frame.dcm(inertial_frame))
# %% The position is set with the Point.set_pos() method , giving the ref point and the vector
ankle = Point("A")
knee = Point("K")
lower_leg_length = symbols("l_L")                           # --> make variable letters 
knee.set_pos(ankle,lower_leg_length * lower_leg_frame.y)    # --> point K + point A 
knee.pos_from(ankle)                                        # --> can find any other points
# %% It is also possible to express the returned vector in another reference frame.
knee.pos_from(ankle).express(inertial_frame).simplify()
# %% knee + upper 
upper_leg_length = symbols("l_U")
hip = Point("H")
hip.set_pos(knee,upper_leg_length * upper_leg_frame.y)
hip.pos_from(ankle)
# %% express hip point about inertial_frame
hip.pos_from(ankle).express(inertial_frame).simplify()
# %%
