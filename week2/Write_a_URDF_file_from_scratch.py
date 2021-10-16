# 2.109 Write a URDF file from scratch

# ipython

import pybullet as p
import pybullet_data as pd

p.connect(p.GUI)
p.setPhysicsEngineParameter(enableFileCaching=0)
plane_shape = p.createCollisionShape(p.GEOM_PLANE)
floor = p.createMultiBody(plane_shape, plane_shape)
p.setGravity(0, 0, -10)


rob1 = p.loadURDF('101.urdf')  # This was no collision tag!
p.setRealTimeSimulation(1)  # This does not work for mac

import time

"""
while True:
    p.stepSimulation()
    time.sleep(1.0/240)
"""



rob2 = p.loadURDF('101.urdf')  # Added collosion tag.

rob3 = p.loadURDF('101_inertial.urdf')

rob4 = p.loadURDF('101_links.urdf')

rob5 = p.loadURDF('101_links.urdf')  # Added axis, limit, origin