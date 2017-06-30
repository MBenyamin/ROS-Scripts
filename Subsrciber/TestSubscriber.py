#!/usr/bin/env python
import rospy
import tf.transformations
from geometry_msgs.msg import Twist

def callback(msg):
	rospy.loginfo("Reveived a /cmd_vel message!")
	#rospy.loginfo("Linear : [%f, %f, %f]"%(msg.Linear.x, msg.Linear.y, msg.Linear.z))
	rospy.loginfo("Angular : [%f, %f, %f]"%(msg.Angular.x, msg.Angular.y. msg.Angular.z))

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber('/turtle1/cmd_vel', Twist, callback)

	rospy.spin()

if __name__ =='__main__':
	listener()