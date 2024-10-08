import open3d as o3d
import numpy as np
from copy import deepcopy
from matplotlib import pyplot as plt

bunny = o3d.data.BunnyMesh()
mesh = o3d.io.read_triangle_mesh(bunny.path)

# Resize the mesh to 2 times larger
mesh.scale(800, center=np.zeros(3))

# Compute the normals of the mesh
mesh.compute_vertex_normals()

# Add a 10 mm XYZ coordinate at the origin
coord = o3d.geometry.TriangleMesh.create_coordinate_frame(size=10)

# rotate along x axis by 90 degrees
R = mesh.get_rotation_matrix_from_xyz((np.pi/2, 0, 0))
mesh.rotate(R, center=(0,0,0))
# move the bottom of the mesh to the origin
mesh.translate((0,0,-mesh.get_min_bound()[2]-1.5))
# remove meshed below z = 0

# Sample the mesh to create a point cloud
point_cloud = mesh.sample_points_uniformly(number_of_points=500000)

# point cloud remove points with z<0
point_cloud = point_cloud.select_by_index(np.where(np.asarray(point_cloud.points)[:,2]>0)[0])

# cluster the point cloud
with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
    labels = np.array(point_cloud.cluster_dbscan(eps=1, min_points=10, print_progress=True))
# remove points that are not in the first cluster
point_cloud = point_cloud.select_by_index(np.where(labels==0)[0])

# save mesh and point cloud to folder
o3d.io.write_triangle_mesh("bunny.ply", mesh)
o3d.io.write_point_cloud("bunny.pcd", point_cloud)

# Visualize the mesh with normals
drawing_objects = [point_cloud,coord]
o3d.visualization.draw_geometries(drawing_objects)