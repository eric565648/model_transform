import open3d as o3d
import numpy as np
from copy import deepcopy

# Load the STL file
# mesh = o3d.io.read_triangle_mesh("meshes/horse.STL")
bunny = o3d.data.BunnyMesh()
mesh = o3d.io.read_triangle_mesh(bunny.path)

# Resize the mesh to 2 times larger
mesh.scale(1.5, center=np.zeros(3))

# Compute the normals of the mesh
mesh.compute_vertex_normals()

# Add a 10 mm XYZ coordinate at the origin
coord = o3d.geometry.TriangleMesh.create_coordinate_frame(size=10)

# Taubin filter
filter_iterations = [1000, 100, 10]
mesh_vox = []
translations = [[1.5, 0, 0], [1, 0, 0], [0.5, 0, 0]]
for i, filter_iter in enumerate(filter_iterations):
    mesh_in = deepcopy(mesh)
    mesh_smp = mesh_in.filter_smooth_taubin(number_of_iterations=filter_iter)
    mesh_smp.compute_vertex_normals()
    print(
    f'Simplified mesh has {len(mesh_smp.vertices)} vertices and {len(mesh_smp.triangles)} triangles')

    mesh_vox.append(mesh_smp)
    mesh_vox[i].translate(translations[i])

# Visualize the mesh with normals
drawing_objects = [mesh]
drawing_objects.extend(mesh_vox)
o3d.visualization.draw_geometries(drawing_objects)