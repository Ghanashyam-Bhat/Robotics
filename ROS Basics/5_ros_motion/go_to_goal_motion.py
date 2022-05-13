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

def goto(velocity_publisher,to_x,to_y):
    rate = rospy.Rate(10)
    global x,y,theta
    #x0 = x ; y0 = y ; theta0 = theta
    K_linear = 1.0
    K_angular = 4.0

    message = Twist()

    while not rospy.is_shutdown():
        distance = abs(math.sqrt((to_x-x)**2+(to_y-y)**2))
        change_angle = math.atan2(to_y-y,to_x-x) #Don't use abs, it might take long route
        angle = change_angle-theta

        linear_speed = K_linear * distance 
        angular_speed = K_angular * angle

        message.linear.x = linear_speed 
        message.angular.z = angular_speed

        velocity_publisher.publish(message)
        rate.sleep()

        if distance<0.01:
            print(f"Reached ({to_x},{to_y})")
            message.linear.x = 0
            message.angular.z = 0
            velocity_publisher.publish(message)
            break

if __name__ == '__main__':
    rospy.init_node('controler',anonymous=True)
    pub = rospy.Publisher("turtle1/cmd_vel",Twist,queue_size=10)
    rospy.Subscriber('turtle1/pose',Pose,locator_callback)
    time.sleep(1)

    goto(pub,1,1)