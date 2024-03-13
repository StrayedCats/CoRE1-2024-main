from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.conditions import IfCondition

def generate_launch_description():
    core1_2024_bringup_pkg = get_package_share_directory('core1_2024_bringup')
    tags_yaml = core1_2024_bringup_pkg + '/config/tags.yaml'

    use_apriltag = LaunchConfiguration('use_apriltag', default=False)
    use_apriltag_arg = DeclareLaunchArgument('use_apriltag', default_value=use_apriltag, description='Use rosbag')

    return LaunchDescription([
        use_apriltag_arg,
        Node(
            condition=IfCondition(use_apriltag),
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