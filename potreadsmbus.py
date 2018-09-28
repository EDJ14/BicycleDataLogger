#! /usr/bin/env python

import rospy
from std_msgs.msg import UInt32
from smbus import SMBus

bus = SMBus(1)

print("Read the A/D")
print("Ctrl C to stop")
bus.write_byte_data(0x48, 0x01, 0x60)

def talker():
    pub = rospy.Publisher('chatter', UInt32, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        reading = bus.read_i2c_block_data(0x48, 0x00, 2)
        readingConv = (reading[0] * 256 + (reading[1] & 0xF0)) / 16
        rospy.loginfo(readingConv)
        pub.publish(readingConv)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
