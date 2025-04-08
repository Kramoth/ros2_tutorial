#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

def main():
    rclpy.init()
    node=Node("my_first_node")
    node.get_logger().info("hello info 2")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()