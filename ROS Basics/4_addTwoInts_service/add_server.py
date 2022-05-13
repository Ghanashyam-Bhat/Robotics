#!/usr/bin/env python3
from ros_basics_tutorials.srv import AddTwoInts
from ros_basics_tutorials.srv import AddTwoIntsRequest
from ros_basics_tutorials.srv import AddTwoIntsResponse
import rospy

def handle_two_ints(req):
    print("Returning [%d+%d = %d]"%(req.a,req.b,(req.a+req.b)))
    return AddTwoIntsResponse(req.a+req.b)

def server():
    rospy.init_node("add_two_ints_server")
    s = rospy.Service('add_two_ints',AddTwoInts,handle_two_ints)
    print("Ready to add two ints")
    rospy.spin()

if __name__=='__main__':
    server()