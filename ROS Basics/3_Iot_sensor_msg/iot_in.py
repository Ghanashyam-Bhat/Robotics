#!/usr/bin/env python3
import rospy
import random
rospy.init_node('iot_in',anonymous=True)

from ros_basics_tutorials.msg import IoTsensor
pub = rospy.Publisher('IOT',IoTsensor,queue_size=10)

rate = rospy.Rate(1)
i = 0
while not rospy.is_shutdown():
    iot = IoTsensor()
    iot.id = i 
    iot.name = "IoT Message "+str(i)
    iot.temperature = random.randint(20,40)
    iot.humidity = random.randint(50,100)
    rospy.loginfo(iot)
    pub.publish(iot)
    rate.sleep()
    i+=1