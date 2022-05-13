#!/usr/bin/env python3
import rospy 
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose
import time

def locator_callback(message):
    global x,y,theta 
    x = message.x
    y = message.y
    theta = message.theta

def spiral(velocity_publisher,linear):
    rate = rospy.Rate(5)
    global x,y

    message = Twist()
    angular = 1.5
    constant = 0.1
    message.angular.z = angular

    while not rospy.is_shutdown() and x<10.5 and y<10.5:
        message.linear.x = linear
        linear+= constant

        velocity_publisher.publish(message)
        rate.sleep()

if __name__ =='__main__':
    rospy.init_node('controler',anonymous=True)
    pub = rospy.Publisher("turtle1/cmd_vel",Twist,queue_size=10)
    rospy.Subscriber('turtle1/pose',Pose,locator_callback)
    time.sleep(1)
    
    spiral(pub,0.5)