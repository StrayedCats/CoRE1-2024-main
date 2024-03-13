from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="realsense2_camera",
            namespace="camera",
            executable="realsense2_camera_node",
            name="realsense2_camera_node",
            output="screen",
            parameters=[
                {"depth_module.profile": "848x480x60"},
                {"rgb_camera.profile": "848x480x60"},
                {"enable_color": True},
                {"enable_depth": True},
                {"enable_infra": False},
                {"enable_infra1": False},
                {"enable_infra2": False},
                {"enable_sync": False},
                {"enable_rgbd": False},
                {"enable_gyro": False},
                {"enable_accel": False},
                {"publish_tf": True},
                {"tf_publish_rate": 0.0},
                {"pointcloud.enable": False},
                {"align_depth.enable": True},
                {"colorizer.enable": False},
                {"decimation_filter.enable": False},
                {"spatial_filter.enable": False},
                {"temporal_filter.enable": False},
                {"disparity_filter.enable": False},
                {"hole_filling_filter.enable": False},
                {"hdr_merge.enable": False},
                {"wait_for_device_timeout": -1.0},
                {"reconnect_timeout": 6.0},

            ],
            emulate_tty=True,
        ),
    ])


