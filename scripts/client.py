#!/usr/bin/env python

import rospy
from martin_client.msg import Message

if __name__ == "__main__":
    pub = rospy.Publisher('chat_in', Message, queue_size=10)
    rospy.init_node('martin_client', anonymous=False)
    rate = rospy.Rate(1)
    msg = Message()
    msg.sender = "martin"
    msg.message = "hej"

    while not rospy.is_shutdown():
        pub.publish(msg)
        print("Published msg")
        rate.sleep()
    
