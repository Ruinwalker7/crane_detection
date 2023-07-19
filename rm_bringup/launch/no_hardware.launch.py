import os
import sys
from ament_index_python.packages import get_package_share_directory
sys.path.append(os.path.join(get_package_share_directory('rm_bringup'), 'launch'))


def generate_launch_description():

    from common import launch_params, robot_state_publisher, node_params, solver_node
    from launch_ros.actions import Node
    from launch import LaunchDescription

    detector_node = Node(
        package='armor_detector',
        executable='armor_detector_node',
        emulate_tty=True,
        output='both',
        parameters=[node_params],
        arguments=['--ros-args', '--log-level',
                   'armor_detector:='+launch_params['detector_log_level']],
    )

    video_player_node = Node(
        package='rm_camera_driver',
        executable='video_player_node',
        output='both',
        parameters=[node_params],
    )

    joint_pub_node = Node(
        package='rm_serial_driver',
        executable='virtual_serial_node',
        output='both',
        parameters=[node_params],
    )


    return LaunchDescription([
        robot_state_publisher,
        detector_node,
        solver_node,
        video_player_node,
        joint_pub_node
    ])
