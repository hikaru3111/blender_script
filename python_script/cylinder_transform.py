import bpy
import math

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(True)

bpy.ops.mesh.primitive_cylinder_add()
obj = bpy.data.objects["Cylinder"]

obj.data.shape_keys.key_blocks[1].value = 0.2
obj.data.shape_keys.key_blocks["Key 1"].value = 0.8