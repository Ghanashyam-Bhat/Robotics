#!/usr/bin/env python3
import rospy 
import math
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose
import time

"""
from go_to_goal_motion import locator_callback
from go_to_goal_motion import goto 
from linear_motion import move
from orient_motion import orient
from rotation_motion import rotate 
from spiral_motion import spiral
"""

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

    goto(pub,1,1)
    orient(pub,30,0)
    for i in range(4):
        move(pub,3,8,1)
        rotate(pub,30,90,0)
    goto(pub,5,5)
    orient(pub,30,360)
    spiral(pub,1.0)
    goto(pub,5,5)
    orient(pub,30,360)