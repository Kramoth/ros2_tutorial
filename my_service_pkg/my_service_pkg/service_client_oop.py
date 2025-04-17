#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial
    
    
class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.client=self.create_client(AddTwoInts, "add_two_ints")

    def add_two_ints(self, a, b):
        while not self.client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for the service to be available")
        request=AddTwoInts.Request()
        request.a=a
        request.b=b
        
        future=self.client.call_async(request)

        future.add_done_callback(self.add_two_ints_callback)
        #future.add_done_callback(partial(self.add_two_ints_callback, request=request))

    def add_two_ints_callback(self, future):
        response=future.result()
        self.get_logger().info(f"server responds with: {response.sum}")

    # def add_two_ints_callback(self, future, request):
    #     response=future.result()
    #     self.get_logger().info(f"{request.a} + {request.b} = {response.sum}")
def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClient()
    node.add_two_ints(12,30)
    node.add_two_ints(15,35)    
    node.add_two_ints(64,65454)
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()