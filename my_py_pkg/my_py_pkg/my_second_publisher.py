#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_custom_interfaces.msg import SensorStatus
    
    
class MyPublisherNode(Node):
    def __init__(self):
        super().__init__("second_pub")
        self.publisher_=self.create_publisher(SensorStatus, "published_topic", 10)
        self.create_timer(0.5, self.publisher_callback)
        self.get_logger().info("publisher has started")

    def publisher_callback(self):
        msg=SensorStatus()
        msg.enable=False
        msg.value=12.3
        msg.status="idle"
        self.publisher_.publish(msg)
    
    
def main(args=None):
    rclpy.init(args=args)
    node = MyPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()

    