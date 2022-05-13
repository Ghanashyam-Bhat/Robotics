#!/usr/bin/env python3
import rospy
rospy.init_node('listener',anonymous=True)

def chatter_out(message):
    print("I heard %s",message.data)

from std_msgs.msg import String
rospy.Subscriber('chatter',String,chatter_out)

rospy.spin()