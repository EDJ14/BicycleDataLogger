#! /usr/bin/env python

import rospy
from std_msgs.msg import UInt32
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1015()
GAIN = 1
adc.start_adc(0, gain=GAIN)

print("Read the A/D")
print("Ctrl C to stop")

def talker():
    pub = rospy.Publisher('steerangle', UInt32, queue_size=50)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        value = adc.get_last_result()
        rospy.loginfo(value)
        pub.publish(value)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
