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
            {'load_target_plugin': 'detector2d_plugins::YoloxTrt'},
            {'yolox_trt_plugin.model_path': '/home/core2024/yolox_tiny.trt'},
            {'yolox_trt_plugin.imshow_isshow': True},
        ],
        remappings=[
            ('image_raw', '/color/image_raw')
        ]
    )

    bytetrack_cpp = ComposableNode(
        package='bytetrack_cpp_node',
        plugin='bytetrack_cpp_node::ByteTrackNode',
        name='bytetrack_cpp_node',
        namespace=''
    )

    bbox2d_to_3d_node = Node(
        package='bbox2d_to_3d_node',
        executable='bbox2d_to_3d_quick_node_exec',
        name='bbox2d_to_3d_node',
        namespace='',
        parameters=[
            {'imshow_isshow': False}
        ],
        remappings=[
            ('camera_info', 'color/camera_info'),
            ('color', 'color/image_raw'),
            ('depth', 'aligned_depth_to_color/image_raw'),
            ('bbox2d', 'bytetrack/bounding_boxes')
        ]
    )

    bytetrack_viewer = ComposableNode(
        condition=IfCondition(use_viewer),
        package='bytetrack_viewer',
        plugin='bytetrack_viewer::ByteTrackViewer',
        name='bytetrack_viewer',
        namespace='',
        remappings=[
            ('image_raw', '/color/image_raw')
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
                bytetrack_cpp,
                bytetrack_viewer
            ],
            output='screen'
        ),
        bbox2d_to_3d_node
    ])
