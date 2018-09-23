import bpy
import math

#reset objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(True)

#world
bpy.context.scene.world.horizon_color=(0.0,0.0,0.0)

#plane_add
for i in range(0,100):
    bpy.ops.mesh.primitive_plane_add(radius = (i*1.1/100),location=(0,0,0),rotation=(math.pi*1/2,math.pi*i*8.2/360,math.pi*i*10/360))

for item in bpy.context.scene.objects:
    if item.type == 'MESH':
        bpy.context.scene.objects.active = bpy.data.objects[item.name]
        bpy.ops.object.modifier_add(type='WIREFRAME')
        bpy.context.object.modifiers['Wireframe'].thickness = 0.0025
        bpy.context.object.modifiers['Wireframe'].use_boundary = True

#lamp add
bpy.ops.object.lamp_add(type='HEMI',location=(0.0,0.0,2.0))

#camera add
bpy.ops.object.camera_add(location=(5.0,0.0,0.0))
bpy.data.objects['Camera'].rotation_euler = (math.pi*1/2, 0, math.pi*1/2)

#render
bpy.context.scene.render.resolution_x = 1000
bpy.context.scene.render.resolution_y = 1000
bpy.context.scene.render.resolution_percentage = 100
bpy.context.scene.camera = bpy.context.object
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.data.scenes["Scene"].render.filepath = "tmp/plane.png"
bpy.ops.render.render(write_still=True)