#!/usr/bin/env python3
from ros_basics_tutorials.srv import AddTwoInts
from ros_basics_tutorials.srv import AddTwoIntsRequest
from ros_basics_tutorials.srv import AddTwoIntsResponse
import rospy
import sys

def add_two_ints_client(x,y):
    rospy.wait_for_service('add_two_ints')
    e  = "error_message"
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints',AddTwoInts)
        respl = add_two_ints(x,y)
        return respl.sum
    except rospy.ServiceException(e):
        print("Service Call Failed"%e)

if __name__ =='__main__':
    if len(sys.argv)==3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print("%s[x y]"%sys.argv[0])
        sys.exit(1)
    print("Requesting %d+%d"%(x,y))
    s  = add_two_ints_client(x,y)
    print("%d + %d = %d"%(x,y,s))