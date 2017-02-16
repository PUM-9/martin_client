#!/usr/bin/env python

import rospy
from martin_client.msg import Message


def callback(data):
    print(data.sender)
    print(data.message)

if __name__ == "__main__":
    rospy.init_node('martin_client', anonymous=False)
    pub = rospy.Publisher('chat_in', Message, queue_size=10)
    sub = rospy.Subscriber('chat_out', Message, callback)
    send_msg = Message()
    send_msg.sender = "martin"

    while not rospy.is_shutdown():
        input = str(input("Enter msg: "))
        pub.publish(send_msg)
