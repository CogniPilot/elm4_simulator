from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution

from launch_ros.actions import Node


def generate_launch_description():

    synapse_ros = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([PathJoinSubstitution(
            [get_package_share_directory('synapse_ros'), 'launch', 'synapse_ros.launch.py'])]),
        launch_arguments=[('host', ['127.0.0.1']),
                          ('port', '4241')],
    )

    synapse_gz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([PathJoinSubstitution(
            [get_package_share_directory('synapse_gz'), 'launch', 'synapse_gz.launch.py'])]),
        launch_arguments=[('host', ['192.0.2.2']),
                          ('port', '4242')]
    )

    return LaunchDescription([
        synapse_ros,
        synapse_gz
    ])
