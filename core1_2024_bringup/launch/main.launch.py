from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription as IncLaunch
from launch.launch_description_sources import PythonLaunchDescriptionSource as PyLaunch

def generate_launch_description():
    this_launch_pkg = get_package_share_directory('core1_2024_bringup')

    return LaunchDescription([
        IncLaunch(PyLaunch([this_launch_pkg, '/launch/rosbag.launch.py'])),
        IncLaunch(PyLaunch([this_launch_pkg, '/launch/sim_detector.launch.py'])),
        # IncLaunch(PyLaunch([this_launch_pkg, '/launch/detector_bringup.launch.py']))
    ])
