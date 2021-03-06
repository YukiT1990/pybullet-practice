# import pybullet_data as pd

# pd.getDataPath()
print(pd.getDataPath())  # move to this path
"""
or do something like this
rob1 = p.loadURDF(pd.getDataPath() + "/cartpole.urdf")
"""

# more starter.py (run starter.py)

import pybullet as p
import pybullet_data as pd

p.connect(p.GUI)
plane_shape = p.createCollisionShape(p.GEOM_PLANE)
floor = p.createMultiBody(plane_shape, plane_shape)
p.setGravity(0, 0, -10)

robot = p.loadURDF('URL of .urdf file')

sam = p.loadURDF('URL of .urdf file')