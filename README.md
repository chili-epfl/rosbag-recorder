## rosbag_recorder

ROS service to start/stop recording selected topics to a named bag file.
Includes `*.srv` definitions necessary to issue requests.

## Building

 - Clone the repo into the `src` directory of your catkin workspace
 - Run `catkin_make` from the root of your catkin workspace
 - Run `make install` or simply copy `*.h` files to the `include` folder of your ROS installation
 
## Running

 - In the root of your catkin workspace, source the setup script (`. devel/setup.bash`)
 - Start the service: `rosrun rosbag_recorder rosbag_recorder_server.py`
