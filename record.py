#!/usr/bin/env python
import sys
import message_filters ### ADD THIS
import rospy
import numpy as np
import math
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2


cont = 0
conty = 0
bridge = CvBridge()
rgb_sub = message_filters.Subscriber("/camera/rgb/image_color", Image)
depth_sub = message_filters.Subscriber("/camera/depth/image", Image)

#------Start of Class
def callback(rgb, depth):
    global cont
    global conty
    
    rgb_sub = message_filters.Subscriber("/camera/rgb/image_color", Image)
    depth_sub = message_filters.Subscriber("/camera/depth/image", Image)
    #get depth
    if conty != 100000000:
	NewImg = bridge.imgmsg_to_cv2(depth, "passthrough")
	depth_array = np.array(NewImg, dtype=np.float32)
	cv2.normalize(depth_array, depth_array, 0, 1, cv2.NORM_MINMAX)
	print('receiving depth')		
	cv2.imwrite('camera_depth' +str(conty)+'.png', depth_array*255)
	conty = conty + 1

    '''NewImg = bridge.imgmsg_to_cv2(depth, "passthrough")
    depth_array = np.array(NewImg, dtype=np.float32)
    cv2.normalize(depth_array, depth_array, 0, 1, cv2.NORM_MINMAX)
    cv2.imwrite('camera_depth'++str(conty)+'.png', depth_array*255)
    conty = conty + 1'''
    #get rgb
    if cont != 100000000:
	print('receiving rgb')
	frame = bridge.imgmsg_to_cv2(rgb, "bgr8")
        cv2.imwrite('camera_image' +str(cont)+'.png', frame)
        cont = cont + 1  
    '''frame = bridge.imgmsg_to_cv2(rgb, "bgr8")
    cv2.imwrite('camera_image' + str(cont) + '.png', frame)
    cont = cont + 1'''
	
    

def main():
    #bridge = CvBridge()
    rospy.init_node('record')	
    #rospy.init_node('image_converter', anonymous=True)
    #img_cvt = image_converter()
    try:
        ts = message_filters.ApproximateTimeSynchronizer([rgb_sub, depth_sub],10,0.1)
	#ts = message_filters.ApproximateTimeSynchronizer(["/camera/rgb/image_color","/camera/depth/image"],10,0.1)        
	ts.registerCallback(callback)
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

if __name__ == '__main__':
    main()
