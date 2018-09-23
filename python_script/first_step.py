import bpy
import math

#access data
print(bpy.data.objects)
print(bpy.data.scenes)
print(bpy.data.materials)

#access to  a present data
print(list(bpy.data.objects))
print(bpy.data.objects[0])

obj = bpy.data.objects[0]

print(obj.name)

#add material
print(list(bpy.data.materials))
bpy.data.materials.new("MyMaterials")
print(list(bpy.data.materials))

#add mesh
print(list(bpy.data.meshes))
mesh = bpy.data.meshes.new(name = "MyMesh")
print(list(bpy.data.meshes))
bpy.data.meshes.remove(mesh)
print(list(bpy.data.meshes))
bpy.data.meshes.new(name = "MyMesh")
print(list(bpy.data.meshes))
bpy.data.meshes.remove(bpy.data.meshes["MyMesh"])
print(list(bpy.data.meshes))

#usage of bpy.context( this is operation on user's selection)
print(bpy.context.object)
print(bpy.context.selected_objects)
print(bpy.context.visible_bones)

#usage of bpy.ops(operators) button, shortcut and others 
#print(bpy.ops.mesh.flip_normals())
#print(bpy.ops.mesh.hide(unselected = False))
#print(bpy.ops.object.scale_apply())

#animation
#obj = bpy.context.object
#obj.location[2] = 0.0
#obj.keyframe_insert(data_path = "location", frame = 10.0, index = 2)
#obj.location[2] = 1.0
#obj.keyframe_insert(data_path = "location", frame = 20.0, index = 2)

#another way of animating
obj = bpy.context.object
obj.animation_data_create()
obj.animation_data.action = bpy.data.actions.new(name="MyAction")
fcu_z = obj.animation_data.action.fcurves.new(data_path = "location", index = 2)
fcu_z.keyframe_points.add(2)
fcu_z.keyframe_points[0].co = 10.0, 0.0
fcu_z.keyframe_points[1].co = 20.0, 1.0