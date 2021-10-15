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

import time

while True:
    p.stepSimulation()
    time.sleep(1.0/240)

