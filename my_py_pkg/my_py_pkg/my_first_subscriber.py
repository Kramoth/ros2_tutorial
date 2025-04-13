#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String    
    
class MySubNode(Node):
    def __init__(self):
        super().__init__("sub_node")
        self.create_subscription(String, "subscribed_topic",self.sub_callback,10)
        self.get_logger().info("Subscriber has started")

    def sub_callback(self, msg):
        self.get_logger().info(msg.data)
    
    
def main(args=None):
    rclpy.init(args=args)
    node = MySubNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()