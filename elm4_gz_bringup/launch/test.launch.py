from os import environ
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch.actions import ExecuteProcess


ARGUMENTS = [
    DeclareLaunchArgument('world', default_value='elm4map',
                          description='GZ World'),
]


def generate_launch_description():

    synapse_ros = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([PathJoinSubstitution(
            [get_package_share_directory('synapse_ros'), 'launch', 'synapse_ros.launch.py'])]),
        launch_arguments=[('host', ['192.0.2.2']),
                          ('port', '4242')]
    )

    synapse_gz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([PathJoinSubstitution(
            [get_package_share_directory('synapse_gz'), 'launch', 'synapse_gz.launch.py'])]),
        launch_arguments=[('host', ['127.0.0.1']),
                          ('port', '4241')],
    )

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([PathJoinSubstitution(
            [get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py'])]),
        launch_arguments=[('gz_args', [LaunchConfiguration('world'), '.sdf', ' -v 1', ' -r'])
        ]
    )

    cerebri = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([PathJoinSubstitution(
            [get_package_share_directory('cerebri_bringup'), 'launch', 'cerebri.launch.py'])])
    )

    return LaunchDescription(ARGUMENTS + [
        synapse_ros,
        synapse_gz,
        gz_sim,
        cerebri,
    ])
