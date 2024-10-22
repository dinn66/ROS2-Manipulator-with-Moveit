import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult
from rclpy.parameter import ParameterType

class SimpleParameter(Node):
    def __init__(self):
        super().__init__("parameter_node")
        self.declare_parameter("simple_int_param", 28)
        self.declare_parameter("simple_string_param", "Din")
        self.add_on_set_parameters_callback(self.paramChangeCallback)

    
    def paramChangeCallback(self, params):
        result = SetParametersResult()
        for param in params:
            if param == "simple_int_param" and param.type ==ParameterType.PARAMETER_INTEGER:
                self.get_logger().info("Param Simple_init_param has been changed to %d", param.value)
                result.successful =True
            if param == "simple_string_param" and param.type ==ParameterType.PARAMETER_STRING:
                self.get_logger().info("Param Simple_string_param has been changed to %d", param.value)
                result.successful = True

    
def main():
    rclpy.init()
    simple_param = SimpleParameter()
    rclpy.spin(simple_param)
    simple_param.destroy_node()
    rclpy.shutdown

if __name__ == "__main__":
    main()

