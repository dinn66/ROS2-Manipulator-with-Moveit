from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command, LaunchConfiguration
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    dinnurobot_description_dir = get_package_share_directory('dinnurobot_description')
    model_arg =DeclareLaunchArgument(name = "model",
                                      default_value= os.path.join(dinnurobot_description_dir, "urdf", "dinnurobot.urdf.xacro"), 
                                      description = "Absolute path to the robot URDF file")
    robot_description = ParameterValue(Command(["xacro ", LaunchConfiguration("model")]), value_type=str)
    robot_state_publisher_node = Node(package = "robot_state_publisher",
                                  executable = "robot_state_publisher", 
                                  parameters = [{"robot_description": robot_description}] )
    
    joint_state_publisher_gui_node = Node(package = "joint_state_publisher_gui", 
                                     executable = "joint_state_publisher_gui")
    
    rviz_node = Node(
        package = "rviz2",
        executable = "rviz2",
        name = "rviz2",
        output = "screen",
        arguments = ["-d", os.path.join(dinnurobot_description_dir, "rviz", "display.rviz")]
    )


    return LaunchDescription([
        model_arg,
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ])