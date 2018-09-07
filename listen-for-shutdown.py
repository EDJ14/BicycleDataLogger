#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess
import os
import signal
# import rosnode


GPIO.setmode(GPIO.BCM)

# This shoul turn on the LED
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.HIGH)

# subprocess.Popen(["rosbag", "record", "-O", "/home/pi/my_bag", "/button"])

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(16, GPIO.FALLING)

def terminate_ros_node(s):
    list_command = subprocess.Popen("rosnode list", shell=True, stdout=subprocess.PIPE)
    list_output = list_command.stdout.read()
    retcode = list_command.wait()
    assert retcode == 0, "List command returned %d" % retcode
    for str in list_output.split("/n"):
        if (str.startswith(s)):
           os.system("rosnode kill " + str)

terminate_ros_node("/record")

# subprocess.call(['mkdir', '/home/pi/Desktop/start'])


# bagtopic = rosnode.get_node_names()
# bagtopics = bagtopic[2]
# rosnode.kill_nodes([bagtopics])
# subprocess.call(['mkdir', '/home/pi/Desktop/finish'])


# -h stands for --power-off
# subprocess.call(['shutdown', '-h', 'now'], shell=False)

