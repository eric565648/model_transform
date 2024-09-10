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

# Sample the mesh to create a point cloud
point_cloud = mesh.sample_points_uniformly(number_of_points=500000)


# test_cubic = o3d.geometry.TriangleMesh.create_box(width=5, height=5, depth=5)
# test_cubic.compute_vertex_normals()
# test_cubic.translate([0, 0, 0])
# point_cloud_cubic = test_cubic.sample_points_uniformly(number_of_points=10000)
# point_cloud_cubic_down = point_cloud_cubic.voxel_down_sample(voxel_size=4)
# point_cloud_cubic.paint_uniform_color([0, 0, 1])
# circles = []
# circles_org = []
# for point in point_cloud_cubic_down.points:
#     circle = o3d.geometry.TriangleMesh.create_sphere(radius=0.3)
#     circle.compute_vertex_normals()
#     circle.translate(point)
#     circle.paint_uniform_color([1, 0, 0])
#     circles.append(circle)

#     point_org = np.round(np.asarray(point)/1)*1
#     print(point_org)
#     circle_org = o3d.geometry.TriangleMesh.create_sphere(radius=0.3)
#     circle_org.compute_vertex_normals()
#     circle_org.translate(point_org)
#     circle_org.paint_uniform_color([0, 1, 0])
#     circles_org.append(circle_org)

# print("==============")
# print(np.asarray(point_cloud_cubic_down.points))
# print(len(np.asarray(point_cloud_cubic_down.points)))
# drawing_objects = [test_cubic,point_cloud_cubic,point_cloud_cubic_down]
# drawing_objects.extend(circles)
# drawing_objects.extend(circles_org)
# o3d.visualization.draw_geometries(drawing_objects)

# Voxelize the coordinates of the mesh
voxel_sizes = [10, 5, 3]
mesh_vox = []
cubics = []
translations = [[210, 0, 0], [140, 0, 0], [70, 0, 0]]
for i, voxel_size in enumerate(voxel_sizes):
    mesh_vox.append(point_cloud.voxel_down_sample(voxel_size))
    mesh_vox[i].translate(translations[i])

    for point in mesh_vox[i].points:
        cubic = o3d.geometry.TriangleMesh.create_box(width=voxel_size, height=voxel_size, depth=voxel_size)
        cubic.compute_vertex_normals()
        cubic.translate(np.round(np.asarray(point)/voxel_size)*voxel_size-np.array([voxel_size/2, voxel_size/2, voxel_size/2]))
        cubics.append(cubic)

# Visualize the mesh with normalso3d.visualization.draw_geometries([mesh, point_cloud] + mesh_vox + [coord])
# Visualize the mesh with normals
drawing_objects = [mesh, point_cloud, coord]
drawing_objects.extend(cubics)
o3d.visualization.draw_geometries(drawing_objects)