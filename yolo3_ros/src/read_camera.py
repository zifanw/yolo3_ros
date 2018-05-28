#!/usr/bin/env python
# license removed for brevity
import argparse
import datetime
import imutils
import time
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def camera():
    rospy.init_node('camera_node', anonymous=True)
    pub = rospy.Publisher('camera_raw', Image, queue_size = 100)
    bridge = CvBridge()
    camera = cv2.VideoCapture(0)
    rate = rospy.Rate(20) # 10hz
    while True:
        (grabbed, frame) = camera.read()
        if not grabbed:
		break
        frame = imutils.resize(frame, width=500)
        pub.publish(bridge.cv2_to_imgmsg(frame, "bgr8"))
    #    cv2.imshow("Image window", frame)
    #    key = cv2.waitKey(1) & 0xFF
        rate.sleep()

if __name__ == '__main__':
    camera()
