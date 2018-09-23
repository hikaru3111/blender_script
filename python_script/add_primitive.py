import bpy

#initialize
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(True)

bpy.ops.mesh.primitive_circle_add()
bpy.ops.mesh.primitive_cone_add()
bpy.ops.mesh.primitive_cube_add()
bpy.ops.mesh.primitive_monkey_add()
bpy.ops.mesh.primitive_cylinder_add()
bpy.ops.mesh.primitive_ico_sphere_add()
bpy.ops.mesh.primitive_grid_add()
bpy.ops.mesh.primitive_torus_add()
bpy.ops.mesh.primitive_uv_sphere_add()