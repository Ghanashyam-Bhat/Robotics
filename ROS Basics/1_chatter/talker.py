#!/usr/bin/env python3
import rospy
rospy.init_node('talker',anonymous=True)

from std_msgs.msg import String
pub = rospy.Publisher('chatter',String,queue_size=10)

rate = rospy.Rate(1)
i = 0
while not rospy.is_shutdown():
    hello_str = "Hello world "+str(i)
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
    i+=1