import bpy
import math

#initialize
bpy.ops.object.select_all(action = "SELECT")
bpy.ops.object.delete(True)

bpy.ops.mesh.primitive_uv_sphere_add()
obj = bpy.context.selected_objects[0]

mods = obj.modifiers
mod = mods.new(name = "subsurf", type = "SUBSURF")
mod.render_levels = 4
mod.levels = 4