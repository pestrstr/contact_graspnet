# Build the .PCD from color (RGB) and raw depth data using Open3D
import open3d as o3d
import numpy as np
import os

pcd_data = np.load(os.path.join(os.environ['IHANNES_PCD_PRED_DATA'], 'pred_0_0.npy'), allow_pickle=True).item()

color_raw = pcd_data['rgb']
depth_raw = (pcd_data['depth'] * 1000).astype(np.uint16)

color_raw = o3d.geometry.Image(color_raw)
depth_raw = o3d.geometry.Image(depth_raw)
K = pcd_data['K']

# Create an RGBDImage
rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
    color_raw,
    depth_raw,
    depth_scale=1000.0,  # adjust this parameter according to your depth scale
    depth_trunc=3.0,     # adjust this parameter to set the maximum depth
    convert_rgb_to_intensity=False
)

# Create a point cloud from the RGBD image
pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
    rgbd_image,
    o3d.camera.PinholeCameraIntrinsic(
        640, 480, K[0,0], K[1,1], K[0, 2], K[1, 2]
    )
)

# Optionally, flip the point cloud if it is upside down
pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])

# Save the point cloud in PCD format
o3d.io.write_point_cloud("pcd_data/pcd_files/output_point_cloud.pcd", pcd)