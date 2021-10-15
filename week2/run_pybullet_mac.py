
import pybullet as p
p.connect(p.GUI)
plane_shape = p.createCollisionShape(p.GEOM_PLANE)
floor = p.createMultiBody(plane_shape, plane_shape)



"""
If you are using macos, the pybullet window will open but you will see the mouse
pointer turn into a beachball when you mouse over it. So you cannot interact
with it. Do not worry - if you run this code:
"""

import time

while True:
    p.stepSimulation()
    time.sleep(1.0/240)

"""
press return twice
"""
"""
You should now be able to interact with the pybullet GUI. If you then want to
run some more python commands, you need to exit this loop by pressing ctrl-c
in your python terminal. Run your python commands, then re-run that while
loop to put the sim back into interactive mode.
"""
"""
If you are running Windows or Linux, try ctrl-clicking on the floor and moving
the nouse pointer. The camera angle should change.
Try the scroll action on your mouse/trackpad. The view should zoom in and
out.
"""

# open terminal
# ipython

# Here is the complete code to create a box in the world:
import pybullet as p
p.connect(p.GUI)
plane_shape = p.createCollisionShape(p.GEOM_PLANE)
floor = p.createMultiBody(plane_shape, plane_shape)
box_shape = p.createCollisionShape(p.GEOM_BOX, halfExtents = [1, 1, 1])
box_object = p.createMultiBody(box_shape,box_shape)

p.setGravity(0, 0, -10)
# this does not work for mac
p.setRealTimeSimulation(1)

"""
Mac users note: setRealTimeSimulation does not work the same way on a mac.
You do not need to call setRealTimeSimulation. Instead, use the while loop
from before to set things running.
"""