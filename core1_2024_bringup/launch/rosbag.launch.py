import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition

def generate_launch_description():
    home_dir = os.path.expanduser('~')

    use_rosbag = LaunchConfiguration('use_rosbag', default='false')
    bag_file = LaunchConfiguration('bag_file', default=os.path.join(home_dir, 'rosbag2_2024_02_25-03_32_06'))

    bag_file_arg = DeclareLaunchArgument('bag_file', default_value=bag_file, description='Full path to bag file to play')
    use_rosbag_arg = DeclareLaunchArgument('use_rosbag', default_value=use_rosbag, description='Use rosbag')
    
    bag_play_exec = ExecuteProcess(
        condition=IfCondition(use_rosbag),
        cmd=['ros2', 'bag', 'play', bag_file],
        output='screen'
    )

    return LaunchDescription([
        bag_file_arg,
        use_rosbag_arg,
        bag_play_exec,
    ])