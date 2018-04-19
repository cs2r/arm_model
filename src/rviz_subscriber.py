#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64

class Gripper():

    def callback(self, data, joint):
        joint_cmd = JointState()
        now = rospy.Time.now()
        joint_cmd.header.stamp = now
        joint_cmd.name = [joint]
        joint_cmd.position = [data.data]
        self.pub.publish(joint_cmd)

    def __init__(self):
        self.cmd = {}
        self.joints = ["shoulder", "elbow", "wrist_pitch", "wrist_rol", "gripper"]
        rospy.init_node('Robot_controller')
        self.pub = rospy.Publisher("robot_joint_command", JointState, queue_size=10)
        for joint in self.joints:
            rospy.Subscriber(joint, Float64, self.callback, callback_args=joint)
        rospy.spin()


if __name__ == '__main__':
    gripper = Gripper()