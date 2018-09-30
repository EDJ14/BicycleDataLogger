# Description

This is the repository for the 2018 UC Davis mechanical engineering senior design project to build a Bicyle Data Logger utilizing ROS on a 
Raspberry Pi. The repository contains all necessary files and the instructions for their use, as well as instructions for the configuration
of the Raspberry Pi. Once the Pi is set up and the proper hardware connections are made, the Pi will be activated and shut
down by a button that also launches/terminates the ROS processes to process and collect data from an IMU, GPS, potentiometer, and 
calibration button.

# Software
Once the Raspberry Pi is running Raspian Jessie, follow the instructions in the link below to install ROS Kinetic from source on the 
Raspberry Pi.

http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi

Add the following two lines to the .bashrc file:

```bash
source /opt/ros/kinetic/setup.bash
```
```bash
source /home/pi/ros_catkin_ws/devel/setup.bash
```


Once ROS is installed, the following ROS packages must be downloaded:

http://wiki.ros.org/nmea_navsat_driver (GPS)

https://github.com/richardstechnotes/RTIMULib2/tree/master/RTHost (IMU)

https://github.com/romainreignier/rtimulib_ros (IMU)

To download and initialize a ROS package, navigate into the /home/pi/ros_catkin_ws/src/ folder and clone the github repository:

```bash
git clone htt[s:/...
```

Once this is done, cd into the /home/pi/ros_catkin_ws folder and run the command catkin_make from the terminal.

The packages for the steering angle and calibration button must be made manually. To do this, again navigate into the 
/home/pi/ros_catkin_ws/src folder. Next, run the command "catkin_create_pkg potread std_msgs rospy" to create a package called "potread".
To make the calibration button package, run "catkin_create_pkg pushbutton std_msgs rospy". Navigate back into the /home/pi/ros_catkin_ws
workspace and run catkin_make.

Follow the instructions in the link below to install software for use with the Adafruit ADS1015 analog-to-digital converter, which reads
the potentiometer:
https://github.com/adafruit/Adafruit_Python_ADS1x15

Enable i2c on the Pi by going to Preferences -> Raspberry Pi Configuration -> Interfaces

In the /etc/modules file, make sure the lines i2c-dev and i2c-bcm2708 are uncommented
