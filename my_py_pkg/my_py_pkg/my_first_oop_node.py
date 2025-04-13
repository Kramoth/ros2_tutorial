#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyFirstOOPNode(Node):
    def __init__(self):
        super().__init__("my_first_oop")
        self.get_logger().info("Hello info 2")
        self.counter=0
        self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        self.counter+=1
        self.get_logger().info(f"Hello {self.counter}")


def main():
    rclpy.init()
    node=MyFirstOOPNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()