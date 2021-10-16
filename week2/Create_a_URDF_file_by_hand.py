# Create a URDF file by hand

# Load in some ready-made URDF files

import pybullet as p
import pybullet_data as pd
print(pd.getDataPath())

# /Users/yuki.t/Python/pybullet37/lib/python3.7/site-packages/pybullet_data

# cd /Users/yuki.t/Python/pybullet37/lib/python3.7/site-packages/pybullet_data

# ls

p.connect(p.GUI)
rob1 = p.loadURDF(pd.getDataPath() + "/cartpole.urdf")


# complete code

import pybullet as p
import pybullet_data as pd
p.connect(p.GUI)
plane_shape = p.createCollisionShape(p.GEOM_PLANE)
floor = p.createMultiBody(plane_shape, plane_shape)
rob1 = p.loadURDF(pd.getDataPath() + "/cartpole.urdf")

p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)  # this does not work for mac

import time
"""
while True:
  p.stepSimulation()
  time.sleep(1.0/240)
"""




# Create a one link robot (same as in the class)

import pybullet as p
p.connect(p.GUI)
# configuration of the engine:
p.setPhysicsEngineParameter(enableFileCaching=0)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
plane_shape = p.createCollisionShape(p.GEOM_PLANE)
floor = p.createMultiBody(plane_shape, plane_shape)
p.setGravity(0, 0, -10)

# run starter.py
# sorry mac users - you also need to run
import time
while True:
  p.stepSimulation()
  time.sleep(1.0/240)




