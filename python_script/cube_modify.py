import bpy
import math

obj = bpy.data.objects["Cube"]
obj.location.x += 1
obj.rotation_euler = (math.radians(15), math.radians(30), math.radians(45))
obj.scale.x = 2