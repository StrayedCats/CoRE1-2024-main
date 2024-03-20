from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    use_viewer = LaunchConfiguration('use_viewer', default='false')
    use_viewer_arg = DeclareLaunchArgument('use_viewer', default_value=use_viewer, description='Use viewer')


    detector_2d = ComposableNode(
        package='detector2d_node',
        plugin='detector2d_node::Detector2dNode',
        name='detector2d_node',
        namespace='',
        parameters=[
            {'load_target_plugin': 'detector2d_plugins::PanelDetectorHsv'},
            {'debug': True},
        ],
        remappings=[
            ('image_raw', 'camera/color/image_raw'),
            ('positions', 'detector/positions')
        ]
    )

    bbox2d_to_3d_node = Node(
        package='bbox2d_to_3d_node',
        executable='bbox2d_to_3d_quick_node_exec',
        name='bbox2d_to_3d_node',
        namespace='',
        parameters=[
            {'imshow_isshow': False},
            {'broadcast_tf': False},
        ],
        remappings=[
            ('camera_info', 'camera/color/camera_info'),
            ('color', 'camera/color/image_raw'),
            ('depth', 'camera/aligned_depth_to_color/image_raw'),
            ('bbox2d', '/detector/positions'),
            ('bbox3d', 'tracker/bounding_boxes_3d')
        ]
    )

    return LaunchDescription([
        use_viewer_arg,
        ComposableNodeContainer(
            name='detector2d_node_container',
            namespace='',
            package='rclcpp_components',
            executable='component_container',
            composable_node_descriptions=[
                detector_2d,
            ],
            output='screen'
        ),
        bbox2d_to_3d_node
    ])
