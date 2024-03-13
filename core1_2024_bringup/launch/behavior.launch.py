from ament_index_python.packages import get_package_share_directory
import launch
from launch_ros.actions import Node

def generate_launch_description():

    return launch.LaunchDescription([
        Node(
            package="auto_driver_interface",
            executable="move_to_target_deg_server_exec",
            name="move_to_target_deg_server",
            output="screen",
        ),
        Node(
            package="auto_driver_interface",
            executable="tf_to_position_server_exec",
            name="tf_to_position_server",
            parameters=[
                {"z_offset": 0.09}, # 9cm
                {"retry_count": 5}
            ],
            output="screen",
        ),
        Node(
            package="core1_bt_node",
            executable="main",
            name="core1_bt_node",
            output="screen",
        ),
    ])