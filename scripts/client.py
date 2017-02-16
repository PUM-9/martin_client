#!/usr/bin/env python

import sys
import rospy
from martin_client.msg import Message


def callback(data):
    if data.message and data.sender != "martin":
        print(data.sender + ": " + data.message)

if __name__ == "__main__":    
    rospy.init_node('martin_client', anonymous=False)        
    
    pub = rospy.Publisher('chat_in', Message, queue_size=1000)
    sub = rospy.Subscriber('chat_out', Message, callback)
    
    send_msg = Message()
    send_msg.sender = "martin"
    
    while not rospy.is_shutdown():
        send_msg.message = raw_input()
        pub.publish(send_msg)
