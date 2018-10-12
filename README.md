# Description

This is the repository for the 2018 UC Davis mechanical engineering senior design project to build a Bicyle Data Logger utilizing ROS on a 
Raspberry Pi. The repository contains all necessary files and the instructions for their use, as well as instructions for the configuration
of the Raspberry Pi. Once the Pi is set up and the proper hardware connections are made, the Pi will be activated and shut
down by a button that also launches/terminates the ROS nodes that collect and process data from an IMU, GPS, potentiometer, and 
calibration button.

# Software
Once the Raspberry Pi is running Raspian Jessie, run the following commands to install ROS Kinetic from source on the 
Raspberry Pi. This link provides more information: http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi

```bash
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

$ sudo apt-get update
$ sudo apt-get upgrade

$ sudo apt-get install -y python-rosdep python-rosinstall-generator python-wstool python-rosinstall build-essential cmake

$ sudo rosdep init
$ rosdep update

$ mkdir -p ~/ros_catkin_ws
$ cd ~/ros_catkin_ws

$ rosinstall_generator ros_comm --rosdistro kinetic --deps --wet-only --tar > kinetic-ros_comm-wet.rosinstall
$ wstool init src kinetic-ros_comm-wet.rosinstall
```
If wstool fails or is interrupted, run
```bash
wstool update -j4 -t src
```
Next, run:

```bash
mkdir -p ~/ros_catkin_ws/external_src
cd ~/ros_catkin_ws/external_src
wget http://sourceforge.net/projects/assimp/files/assimp-3.1/assimp-3.1.1_no_test_models.zip/download -O assimp-3.1.1_no_test_models.zip
unzip assimp-3.1.1_no_test_models.zip
cd assimp-3.1.1
cmake .
make
sudo make install

$ cd ~/ros_catkin_ws
$ rosdep install -y --from-paths src --ignore-src --rosdistro kinetic -r --os=debian:jessie

$ sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/kinetic
```


Add the following two lines to the .bashrc file:

```bash
source /opt/ros/kinetic/setup.bash
```
```bash
source /home/pi/ros_catkin_ws/devel/setup.bash
```


Once ROS is installed, the following ROS packages must be downloaded:

https://github.com/ros-drivers/nmea_navsat_driver/tree/c457319ecbb4ccd97c559a801d552fdc486b927c (GPS)

https://github.com/RTIMULib/RTIMULib2/tree/3d62821fef0f2252c39c14321a68d8cf3a63b9ae (IMU)

https://github.com/romainreignier/rtimulib_ros/tree/325a3893fa65abd99bd4bbc6e604a18470854ad2 (IMU)


To download and initialize a ROS package, first navigate into the /home/pi/ros_catkin_ws/src/ folder and clone the github repository:

```bash
cd ~/ros_catkin_ws/src
git clone https://github.com/RTIMULib/RTIMULib2/tree/3d62821fef0f2252c39c14321a68d8cf3a63b9ae
git clone https://github.com/RTIMULib/RTIMULib2/tree/3d62821fef0f2252c39c14321a68d8cf3a63b9ae
git clone https://github.com/romainreignier/rtimulib_ros/tree/325a3893fa65abd99bd4bbc6e604a18470854ad2 
```
The packages for the steering angle and calibration button must be made manually. To do this, run the following commands to create a package called "potread":
```bash
cd ~/ros_catkin_ws/src
catkin_create_pkg potread std_msgs rospy
```
and
```bash
catkin_create_pkg pushbutton std_msgs rospy
```
to make the calibration button package. Once all the packages are downloaded or manually created, execute the following:
```bash
cd ~/ros_catkin_ws
catkin_make
```
Run the following commands to install software for use with the Adafruit ADS1015 analog-to-digital converter, which reads
the potentiometer:
```bash
sudo apt-get install git build-essential python-dev
cd ~
git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
cd Adafruit_Python_ADS1x15
sudo python setup.py install
```

# Using this repository

The next step is to put the files in this repository into the correct locations. First, clone the repository:
```bash
cd ~
git clone https://github.com/mechmotum/BicycleDataLogger.git
```

Copy the adafruitros.py and potreadsmbus.py files from this repository into the /home/pi/ros_catkin_ws/src/potread/scripts folder. Also in /home/pi/ros_catkin_ws/src/potread/ create a folder called launch, and copy the allnodes.launch file from this repository into the folder:
```bash
cp /home/pi/BicycleDataLogger/adafruitros.py /home/pi/ros_catkin_ws/src/potread/scripts/
cp /home/pi/BicycleDataLogger/potreadsmbus.py /home/pi/ros_catkin_ws/src/potread/scripts/
mkdir /home/pi/ros_catkin_ws/src/potread/launch/
cp /home/pi/BicycleDataLogger/allnodes.launch /home/pi/ros_catkin_ws/src/potread/launch/
```

Copy the buttoncalibration.py file in this repository into the /home/pi/ros_catkin_ws/src/pushbutton/scripts folder.
```bash
cp /home/pi/BicycleDataLogger/buttoncalibration.py /home/pi/ros_catkin_ws/src/pushbutton/scripts/
```

In the /home/pi/ros_catkin_ws/src/nmea_navsat_driver/scripts folder, replace the nmea_serial_driver, nmea_topic_driver, and 
nmea_topic_serial_reader files with the ones in this repository.
```bash
rm /home/pi/BicycleDataLogger/nmea_serial_driver /home/pi/BicycleDataLogger/nmea_topic_driver /home/pi/BicycleDataLogger/nmea_topic_serial_reader

cp /home/pi/BicycleDataLogger/nmea_serial_driver /home/pi/BicycleDataLogger/nmea_topic_drver /home/pi/BicycleDataLogger/nmea_topic_serial_reader /home/pi/ros_catkin_ws/src/nmea_navsat_driver/scripts/
```

```bash
rm /home/pi/ros_catkin_ws/src/rtimulib_ros/config/RTIMULib.ini
cp /home/pi/BicycleDataLogger/RTIMULib.ini /home/pi/ros_catkin_ws/src/rtimulib_ros/config/
```

Next, copy the listen-for-shutdown.py file into the /usr/local/bin directory.
```bash
cp /home/pi/BicycleDataLogger/listen-for-shutdown.py /usr/local/bin/
```
Then run the following to make it executable:
```bash
cd /usr/local/bin
sudo chmod +x listen-for-shutdown.py
```
In the /etc/init.d directory, copy both the loggerbuttontwo.sh and listen-for-shutdown.sh files, and run the following to make the sytem respond to the button and create/terminate the rosbag to collect data:
```bash
cp /home/pi/BicycleDataLogger/loggerbuttontwo.sh /home/pi/BicycleDataLogger/listen-for-shutdown.sh /etc/init.d/
cd /etc/init.d
sudo chmod +x loggerbuttontwo.sh && sudo update-rc.d loggerbuttontwo.sh defaults
sudo chmod +x listen-for-shutdown.sh && sudo update-rc.d listen-for-shutdown.sh defaults
```


# Raspberry Pi Configuration
Enable i2c on the Pi by going to Preferences -> Raspberry Pi Configuration -> Interfaces

In the /etc/modules file, make sure the lines i2c-dev and i2c-bcm2708 are uncommented

To configure the GPIO serial port used by the GPS, add the line "enable_uart=1" to the bottom of the /boot/config.txt file, then run the
following:
```bash
sudo systemctl stop serial-getty@ttyAMA0.service
sudo systemctl disable serial-getty@ttyAMA0.service
```
Next, remove the line console=serial0,115200 from the /boot/cmdline.txt file.
