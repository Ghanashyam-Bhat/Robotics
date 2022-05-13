#!/usr/bin/env python3
import rospy 
from turtlesim.msg import Pose
def locator_callback(message):
    print("x:%.2f",message.x)
    print("y:%.2f",message.y)
    print("theta:%.2f",message.theta)
    print("linear_velocity:%.2f",message.linear_velocity)
    print("angular_velocity:%.2f",message.angular_velocity)
    print("-------------------------------")
rospy.init_node('locator',anonymous=True)
rospy.Subscriber('turtle1/pose',Pose,locator_callback)
rospy.spin()