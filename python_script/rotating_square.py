
import bpy
import math

#initialize
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(True)

#plane_add
bpy.ops.mesh.primitive_plane_add(location=(0,0,0))

bpy.context.scene.objects.active = bpy.data.objects['Plane']
bpy.ops.object.modifier_add(type="WIREFRAME")
bpy.context.object.modifiers["Wireframe"].thickness = 0.01


#lamp add
bpy.ops.object.lamp_add(location=(0.0,0.0,2.0),type="HEMI")

#camera add
bpy.ops.object.camera_add(location=(5.0,0.0,5.0))
bpy.data.objects['Camera'].rotation_euler = (math.pi*1/4, 0,math.pi*1/2)

#world
bpy.context.scene.world.horizon_color=(0.0,0.0,0.0)


#render
bpy.context.scene.render.resolution_x = 500
bpy.context.scene.render.resolution_y = 500
bpy.context.scene.render.resolution_percentage = 100
bpy.context.scene.camera = bpy.context.object
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.data.scenes["Scene"].render.filepath = "デスクトップ/render.png"
bpy.ops.render.render(write_still=True)

