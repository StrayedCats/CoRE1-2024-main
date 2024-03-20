from ament_index_python.packages import get_package_share_directory
import launch
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

import os

def generate_launch_description():
    core1_bt_node = get_package_share_directory('core1_bt_node')
    core1_bt_node_trees = os.path.join(core1_bt_node, 'trees')

    use_bt = LaunchConfiguration('use_bt', default='false')
    use_bt_arg = DeclareLaunchArgument('use_bt', default_value=use_bt, description='Use rosbag')

    return launch.LaunchDescription([
        use_bt_arg,
        Node(
            package="auto_driver_interface",
            executable="move_to_target_deg_server_exec",
            name="move_to_target_deg_server",
            output="screen",
        ),
        Node(
            condition=IfCondition(use_bt),
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
            condition=IfCondition(use_bt),
            package="core1_bt_node",
            executable="main",
            name="core1_bt_node",
            output="screen",
            parameters=[
                {"bt_xml_path": os.path.join(core1_bt_node_trees, "test_panel.xml")}
            ],
        ),
        Node(
            condition=IfCondition(use_bt),
            package="core1_bt_server_py",
            executable="tar_server",
            name="tar_server"
        ),
    ])