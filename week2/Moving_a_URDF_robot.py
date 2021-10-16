# 2.201 Moving a URDF robot

# run week2/starter3.py
import pybullet as p
import pybullet_data as pd

p.connect(p.GUI)
p.setPysicsEngineParameter(enableFileCaching=0)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
plane_shape = p.createCollisionShape(p.GEOM_PLANE)
floor = p.createMultiBody(plane_shape, plane_shape)
p.setGravity(0, 0, -10)
# run week2/starter3.py


rob1 = p.loadURDF('week2/102.urdf')

p.setRealTimeSimulation(1)  # doesn't work for mac

import time
"""
while True:
    p.stepSimulation()
    time.sleep(1.0/240)
"""

p.resetBasePositionAndOrientation(rob1, [0, 0, 0.2], [0, 0, 0, 1])

p.setJointMotorControl2(rob1, 0, controlMode=p.VELOCITY_CONTROL, targetVelocity=0.25)

p.setJointMotorControl2(rob1, 0, controlMode=p.VELOCITY_CONTROL, targetVelocity=5)

p.setJointMotorControl2(rob1, 0, controlMode=p.POSITION_CONTROL, targetVelocity=5, targetPosition=0.5)

p.setJointMotorControl2(rob1, 0, controlMode=p.VELOCITY_CONTROL, targetVelocity=0)


p.getJointInfo(rob1, 0)

rob1 = p.loadURDF('week2/101_links.urdf')
rob2 = p.loadURDF('week2/102.urdf')  # Added another sublink

p.setJointMotorControl2(rob2, 0, controlMode=p.VELOCITY_CONTROL, targetVelocity=0.5)
p.setJointMotorControl2(rob2, 1, controlMode=p.VELOCITY_CONTROL, targetVelocity=0.5)



