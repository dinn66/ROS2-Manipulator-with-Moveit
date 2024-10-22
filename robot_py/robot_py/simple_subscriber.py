import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimpleSub(Node):
    def __init__(self):
        super().__init__("Simple_Subscriber")
        self.sub = self.create_subscription(String, "chatter", self.msgCallback, 10)
        self.get_logger().info("Subscription node has been started")
    def msgCallback(self, msg):
        self.get_logger().info(f"I heard {msg.data}")


def main():
    rclpy.init()
    simple_subscriber = SimpleSub()
    rclpy.spin(simple_subscriber)
    simple_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ =="__main__":
    main()