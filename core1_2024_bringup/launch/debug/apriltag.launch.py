from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.conditions import UnlessCondition

def generate_launch_description():
    core1_2024_bringup_pkg = get_package_share_directory('core1_2024_bringup')
    tags_yaml = core1_2024_bringup_pkg + '/config/tags.yaml'

    use_rosbag = LaunchConfiguration('use_rosbag', default='false')
    use_rosbag_arg = DeclareLaunchArgument('use_rosbag', default_value=use_rosbag, description='Use rosbag')

    return LaunchDescription([
        use_rosbag_arg,
        Node(
            condition=UnlessCondition(use_rosbag),
            package='apriltag_ros',
            executable='apriltag_node',
            name='apriltag_node',
            namespace='',
            output='screen',
            parameters=[tags_yaml],
            remappings=[
                ('image_rect', '/camera/color/image_raw'),
                ('camera_info', '/camera/color/camera_info')
            ]
        )
    ])