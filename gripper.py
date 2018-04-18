#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

class Gripper():

    def callback(self, data):
        self.R_G_pub.publish(data.data)
        self.L_G_pub.publish(data.data)

    def __init__(self):
        rospy.init_node('Gripper')
        self.R_G_pub = rospy.Publisher("/R_gripper", Float64, queue_size=10)
        self.L_G_pub = rospy.Publisher("/L_gripper", Float64, queue_size=10)
        rospy.Subscriber("/gripper", Float64, self.callback)
        rospy.spin()


if __name__ == '__main__':
    gripper = Gripper()