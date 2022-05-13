#!/usr/bin/env python3
import rospy 
import math
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose
import time

def locator_callback(message):
    global x,y,theta 
    x = message.x
    y = message.y
    theta = message.theta

def move(velocity_publisher,speed,distance,is_forward):
    rate = rospy.Rate(10)
    total_distance = 0.0

    global x,y
    x0 = x
    y0 = y

    message = Twist()
    if (is_forward):
        message.linear.x = abs(speed)
    else:
        message.linear.x = -abs(speed)

    while not rospy.is_shutdown():
        velocity_publisher.publish(message)
        rate.sleep()
        total_distance = abs(math.sqrt(((x-x0)**2)+((y-y0)**2)))
        if total_distance>=distance:
            print(total_distance)
            message.linear.x = 0
            velocity_publisher.publish(message)
            break

if __name__ =='__main__':
    rospy.init_node('controler',anonymous=True)
    pub = rospy.Publisher("turtle1/cmd_vel",Twist,queue_size=10)
    rospy.Subscriber('turtle1/pose',Pose,locator_callback)

    time.sleep(1) #What is the importance of Sleep function here? 
    #Is it to give 2 seconds for subscriber to get started?
    
    move(pub,1.0,4.0,False)