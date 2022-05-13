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

def rotate(velocity_publisher,angle_speed,angle,is_clockwise):
    rate = rospy.Rate(10)
    total_angle= 0.0
    angle_speed = abs(math.radians(angle_speed))
    angle = abs(math.radians(angle))
    t0 = rospy.Time.now().to_sec()

    message = Twist()
    if (is_clockwise):
        message.angular.z = -abs(angle_speed)
    else:
        message.angular.z = abs(angle_speed)

    while not rospy.is_shutdown():
        velocity_publisher.publish(message)
        rate.sleep()
        t1 = rospy.Time.now().to_sec()
        total_angle = abs((t1-t0)*angle_speed)
        if total_angle>=angle:
            print(abs(math.degrees(total_angle)))
            message.angular.z = 0
            velocity_publisher.publish(message)
            break

def orient(velocity_publisher,angular_velocity,angle):
    global theta
    relative_angle = math.radians(angle)-theta
    if relative_angle<0:
        is_clockwise = 1
    else:
        is_clockwise = 0
    relative_angle = math.degrees(abs(relative_angle))

    print("The roation angle is: %d"%relative_angle,end=" ")
    if is_clockwise:
        print("Clockwise")
    else:
        print("Anti-clockwise")

    rotate(velocity_publisher,angular_velocity,relative_angle,is_clockwise)

if __name__ =='__main__':
    rospy.init_node('controler',anonymous=True)
    pub = rospy.Publisher("turtle1/cmd_vel",Twist,queue_size=10)
    rospy.Subscriber('turtle1/pose',Pose,locator_callback)
    time.sleep(1)
    orient(pub,30,360)