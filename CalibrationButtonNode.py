#! /usr/bin/env python

import rospy
from std_msgs.msg import Bool

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO23

def talker():
    pub = rospy.Publisher('button', Bool, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        try:
#            while True:
            button_state = GPIO.input(23)
            if button_state == False:
                print('System Calibrated...')
                time.sleep(0.2)
        except:
            GPIO.cleanup
            
        rospy.loginfo(button_state)
        pub.publish(button_state)
        rate.sleep()
        

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    




