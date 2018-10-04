#! /bin/bash

### BEGIN INIT INFO
# Provides:          listen-for-shutdown.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

source /home/pi/ros_catkin_ws/devel/setup.bash
roslaunch potread allnodes.launch
