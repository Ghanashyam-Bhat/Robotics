#!/usr/bin/env python3
import rospy
rospy.init_node('iot_out',anonymous=True)

def chatter_out(message):
    print("Id ="+str(message.id)+"\nName ="+str(message.name)+"\ntemp = "+str(message.temperature)+"\nhumidity ="+str(message.humidity))

from ros_basics_tutorials.msg import IoTsensor
rospy.Subscriber('IOT',IoTsensor,chatter_out)

rospy.spin()