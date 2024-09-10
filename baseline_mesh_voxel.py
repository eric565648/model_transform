import open3d as o3d
import numpy as np
from copy import deepcopy

# Load the STL file
mesh = o3d.io.read_triangle_mesh("meshes/horse.STL")

# Resize the mesh to 2 times larger
mesh.scale(1.5, center=np.zeros(3))

# Compute the normals of the mesh
mesh.compute_vertex_normals()

# Add a 10 mm XYZ coordinate at the origin
coord = o3d.geometry.TriangleMesh.create_coordinate_frame(size=10)

# voxelize the mesh
voxel_sizes = [10, 5, 3]
mesh_vox = []
translations = [[210, 0, 0], [140, 0, 0], [70, 0, 0]]
for i, voxel_size in enumerate(voxel_sizes):
    mesh_in = deepcopy(mesh)
    mesh_smp = mesh_in.simplify_vertex_clustering(
        voxel_size=voxel_size,
        contraction=o3d.geometry.SimplificationContraction.Average)
    print(
    f'Simplified mesh has {len(mesh_smp.vertices)} vertices and {len(mesh_smp.triangles)} triangles')

    mesh_vox.append(mesh_smp)
    mesh_vox[i].translate(translations[i])

# Visualize the mesh with normals
drawing_objects = [mesh, coord]
drawing_objects.extend(mesh_vox)
o3d.visualization.draw_geometries(drawing_objects)

# mesh decimation (bad results)
target_triangles = [1079,4245,11431]
mesh_vox = []
translations = [[210, 0, 0], [140, 0, 0], [70, 0, 0]]
for i, target_triangle in enumerate(target_triangles):
    mesh_in = deepcopy(mesh)
    mesh_smp = mesh_in.simplify_quadric_decimation(target_number_of_triangles=target_triangle)
    print(
    f'Simplified mesh has {len(mesh_smp.vertices)} vertices and {len(mesh_smp.triangles)} triangles')

    mesh_vox.append(mesh_smp)
    mesh_vox[i].translate(translations[i])

drawing_objects = [mesh, coord]
drawing_objects.extend(mesh_vox)
o3d.visualization.draw_geometries(drawing_objects)