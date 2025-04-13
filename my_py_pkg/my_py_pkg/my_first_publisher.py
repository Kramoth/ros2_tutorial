#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
    
    
class MyPublisherNode(Node):
    def __init__(self):
        super().__init__("first_pub")
        self.publisher_=self.create_publisher(String, "published_topic", 10)
        self.create_timer(0.5, self.publisher_callback)
        self.get_logger().info("publisher has started")

    def publisher_callback(self):
        msg=String()
        msg.data=f"hello from {self.get_clock().now().nanoseconds}"
        self.publisher_.publish(msg)
    
    
def main(args=None):
    rclpy.init(args=args)
    node = MyPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()