import pybullet as p
p.connect(p.GUI)
plane_shape = p.createCollisionShape(p.GEOM_PLANE)
floor = p.createMultiBody(plane_shape, plane_shape)

box_shape = p.createCollisionShape(p.GEOM_BOX, halfExtents = [1, 1, 1])
box_object1 = p.createMultiBody(box_shape,box_shape)
box_object2 = p.createMultiBody(box_shape,box_shape)

p.resetBasePositionAndOrientation(box_object1, [0, -1, 2], [0, 0, 0, 1])
p.resetBasePositionAndOrientation(box_object2, [0, 1, 2], [0, 0, 0, 1])

p.setGravity(0, 0, -10)
# this does not work for mac, use the loop
p.setRealTimeSimulation(1)

"""
Note that we are sending three arguments to the resetBasePositionAndOrientation function: the id of an object in the world, the x, z, y position (yes, x, z, y)
and the orientation.
Try picking them up and throwing them around by clicking and dragging.
"""