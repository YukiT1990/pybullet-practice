# ipython
# run week2/starter3.py

rob1 = p.loadURDF('week2/peer_review/robot1.urdf')

rob2 = p.loadURDF('week2/robot2.urdf')

rob3 = p.loadURDF('week2/sphere.urdf')

p.setJointMotorControl2(rob3, 0, controlMode=p.VELOCITY_CONTROL, targetVelocity=1.3)
p.setJointMotorControl2(rob3, 1, controlMode=p.VELOCITY_CONTROL, targetVelocity=1.3)
p.setJointMotorControl2(rob3, 2, controlMode=p.VELOCITY_CONTROL, targetVelocity=1.3)
p.setJointMotorControl2(rob3, 3, controlMode=p.VELOCITY_CONTROL, targetVelocity=1.3)

p.setJointMotorControl2(rob2, 0, controlMode=p.VELOCITY_CONTROL, targetVelocity=1.2)
p.setJointMotorControl2(rob2, 1, controlMode=p.VELOCITY_CONTROL, targetVelocity=1.5)

p.setJointMotorControl2(rob1, 0, controlMode=p.VELOCITY_CONTROL, targetVelocity=1.0)

import time
"""
while True:
    p.stepSimulation()
    time.sleep(1.0/240)
"""