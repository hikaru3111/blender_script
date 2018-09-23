import mathutils
from mathutils import Vector
import bpy

#initialize
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(True)

verts = []
verts.append((0,0,0))
verts.append((0,1,0))
verts.append((1,1,0))
verts.append((1,0,0))
verts.append((0,0,1))
verts.append((0,1,1))

faces = [[0,1,2,3],[0,1,5,4]]
edges = []

mesh = bpy.data.meshes.new(name="Mesh")
mesh.from_pydata(verts,edges,faces)
obj = bpy.data.objects.new('Object',mesh)
#obj.location(0,0,0)
bpy.context.scene.objects.link(obj)

edges2 = [[0,1],[1,2],[2,3],[3,0]]
faces2 = []

mesh2 = bpy.data.meshes.new(name = "mesh2")
mesh2.from_pydata(verts,edges2,faces2)
obj2 = bpy.data.objects.new("object2",mesh2)
bpy.context.scene.objects.link(obj2)



