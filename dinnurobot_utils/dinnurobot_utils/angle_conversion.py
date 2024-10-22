#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from dinnurobot_msgs.srv import EulertoQuaternion
from dinnurobot_msgs.srv import QuaterniontoEuler
from tf_transformations import quaternion_from_euler, euler_from_quaternion

class AnglesConverter(Node):
    def __init__(self):
        super().__init__("angle_converter")
        self.eulerservice_ = self.create_service(QuaterniontoEuler, "Quaternion_to_euler", self.quaterniontoeulerCallback)
        self.quaternionservice_ = self.create_service(EulertoQuaternion, "euler_to_quaternion", self.eulertoquaternionCallback)
        self.get_logger().info("Service for converting the angles is ready")

    def quaterniontoeulerCallback(self, req, res):
        self.get_logger().info("Request to convert Quaternion to euler angles x: %f , y: %f , z: %f , w: %f" % (req.x, req.y, req.z, req.w))
        (res.roll, res.pitch, res.yaw) = euler_from_quaternion([req.x, req.y, req.z, req.w])
        self.get_logger().info("Resulted Quaternion to euler conversion is yaw: %f, pitch: %f, roll: %f" % (res.roll, res.pitch, res.yaw))
        return res
    
    def eulertoquaternionCallback(self, req, res):
        self.get_logger().info("Request to convert euler angles to Quaternions yaw: %f , pitch: %f , roll: %f " % (req.roll, req.pitch, req.yaw))
        (res.x, res.y, res.z, res.w) = quaternion_from_euler(req.roll, req.pitch, req.yaw)
        self.get_logger().info("Resulted Quaternion to euler conversion is x: %f, y: %f, z: %f , w:%f" % (res.x, res.y, res.z, res.w))
        return res
    

def main():
    rclpy.init()
    angle_converter = AnglesConverter()
    rclpy.spin(angle_converter)
    angle_converter.destroy_node()
    rclpy.shutdown()

if __name__ =="__main__":
    main()
