import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # 1. Trouver le chemin exact du package
    pkg_path = get_package_share_directory('humanoid_robot')
    urdf_file = os.path.join(pkg_path, 'urdf', 'humanoid.urdf')

    # 2. Lire le fichier URDF proprement
    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    # 3. Lancer les 3 outils
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),
        Node(
            package='rviz2',
            executable='rviz2'
        )
    ])
