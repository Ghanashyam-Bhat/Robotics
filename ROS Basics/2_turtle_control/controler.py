#!/usr/bin/env python3
import rospy 
from geometry_msgs.msg import Twist 

rospy.init_node('controler',anonymous=True)
pub = rospy.Publisher("turtle1/cmd_vel",Twist,queue_size=10)
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    twist = Twist()
    twist.linear.x = 1.0
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x= 0.0
    twist.angular.y= 0.0
    twist.angular.z= 1.0
    pub.publish(twist)
    rate.sleep()
