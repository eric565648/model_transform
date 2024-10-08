import open3d as o3d
import numpy as np
from copy import deepcopy
from matplotlib import pyplot as plt

# read bunny point cloud
pcd_in = o3d.io.read_point_cloud("meshes/bunny.pcd")

# Add a 10 mm XYZ coordinate at the origin
coord = o3d.geometry.TriangleMesh.create_coordinate_frame(size=10)

# layer height parameter
h = 1.5

# # get a bound box with zmin = 0 and zmax = h
# pcd_voxs = []
# max_height = int(np.ceil(np.max(np.asarray(pcd_in.points)[:,2])/h))
# color_map = plt.get_cmap('viridis')
# for i in range(0, max_height):
    
#     pcd_vox = pcd_in.select_by_index(np.where(np.logical_and(np.asarray(pcd_in.points)[:,2]>=i*h, np.asarray(pcd_in.points)[:,2]<(i+1)*h))[0])
#     if len(pcd_vox.points) == 0:
#         break
#     pcd_vox.paint_uniform_color(color_map(i/max_height)[:3])
#     pcd_voxs.append(pcd_vox)

# first layer
pcd_first = pcd_in.select_by_index(np.where(np.asarray(pcd_in.points)[:,2]<h)[0])



# Visualize
drawing_objects = [pcd_first,coord]
# drawing_objects.extend(pcd_voxs)
o3d.visualization.draw_geometries(drawing_objects)