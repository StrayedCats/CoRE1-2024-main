import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition

def generate_launch_description():
    home_dir = os.path.expanduser('~')

    use_rosbag = LaunchConfiguration('use_rosbag', default='false')
    rosbag_dir = LaunchConfiguration('rosbag_dir', default=os.path.join(home_dir, 'example.bag'))

    use_rosbag_arg = DeclareLaunchArgument('use_rosbag', default_value=use_rosbag, description='Use rosbag')
    rosbag_dir_arg = DeclareLaunchArgument('rosbag_dir', default_value=rosbag_dir, description='Path to rosbag file')
    
    bag_play_exec = ExecuteProcess(
        condition=IfCondition(use_rosbag),
        cmd=['ros2', 'bag', 'play', rosbag_dir],
        output='screen'
    )

    return LaunchDescription([
        rosbag_dir_arg,
        use_rosbag_arg,
        bag_play_exec,
    ])