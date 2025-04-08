# ros2_tutorial

## Installation

Create a ros workspace:

```
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
```
Then go the src folder then clone the repo:

```
cd ~/ros2_ws/src
git clone https://github.com/Kramoth/ros2_tutorial.git
```

Then go back to the root of your ros workspace:

```
cd ~/ros2_ws/
colcon build
```

## run the nodes

To run the differents nodes:

```
cd ~/ros2_ws
source install/setup.bash
ros2 run my_py_pkg first_node 
#or 
ros2 run my_py_pkg first_oop_node 
#or 
ros2 run my_py_pkg first_sub_node 
#or 
ros2 run my_py_pkg first_pub_node 
```
When you open a new terminal make sure that you have sourced the setup.bash file every time
## test publisher

In a terminal run the first_pub node then open a second terminal then type this command:

```
ros2 topic echo /published_topic
```

## test subscriber


In a terminal run the first_sub node then open a second terminal then type this command:

```
ros2 topic pub /subscribed_topic example_interfaces/msg/String "data: 'hello'"
```

## connect publisher and subscriber

If you noticed correctly, you will see that the publisher publishes on /published_topic and the subscriber on /subscribed_topic to connect them we need to do a remap.

In a terminal run the publisher node
```
ros2 run my_py_pkg first_pub_node
```
In another terminal 
```
ros2 run my_py_pkg first_sub_node --ros-args --remap /subscribed_topic:=/published_topic
``` 

