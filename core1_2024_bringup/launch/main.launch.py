from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription as IncLaunch
from launch.launch_description_sources import PythonLaunchDescriptionSource as PyLaunch

def generate_launch_description():
    this_launch_pkg = get_package_share_directory('core1_2024_bringup')
    auto_driver_pkg = get_package_share_directory('auto_driver_bringup')
    core_viewer_launch_pkg = get_package_share_directory('core_viewer_launch')

    return LaunchDescription([
        IncLaunch(PyLaunch([this_launch_pkg, '/launch/sim_detector.launch.py'])),
        IncLaunch(PyLaunch([this_launch_pkg, '/launch/behavior.launch.py'])),
        IncLaunch(PyLaunch([this_launch_pkg, '/launch/realsense.launch.py'])),
        IncLaunch(PyLaunch([auto_driver_pkg, '/launch/auto2024.launch.py'])),

        IncLaunch(PyLaunch([this_launch_pkg, '/launch/debug/apriltag.launch.py'])),
        IncLaunch(PyLaunch([this_launch_pkg, '/launch/debug/rosbag.launch.py'])),

        IncLaunch(PyLaunch([core_viewer_launch_pkg, '/launch/viewer.launch.py'])),
    ])
