#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from nav_msgs.msg import Path
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose

# PoseStamped.pose.position.x
def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.pose.position.x)

    odom = Odometry()

    # uwb_pose.pose = data.pose
    
    # odom = data
    odom.pose.pose.position.x = float(data.pose.pose.position.y)
    odom.pose.pose.position.y = float(data.pose.pose.position.x)
    odom.pose.pose.position.z = float(data.pose.pose.position.z)

    odom.pose.pose.orientation.x = float(data.pose.pose.orientation.x)
    odom.pose.pose.orientation.y = float(data.pose.pose.orientation.y)
    odom.pose.pose.orientation.z = float(data.pose.pose.orientation.w)
    odom.pose.pose.orientation.w = float(data.pose.pose.orientation.z)

    # odom.pose.pose.orientation.x = 0.707
    # odom.pose.pose.orientation.y = 0.707
    # odom.pose.pose.orientation.z = 0
    # odom.pose.pose.orientation.w = 0

    odom.header.frame_id = data.header.frame_id
    # odom

    pub.publish(odom)
    return odom


    odom.pose.append(pose)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('proc_qvio_odom', anonymous=True)

    odom = Odometry()

    rospy.Subscriber('/qvio/odometry', Odometry, callback)

    pub = rospy.Publisher('/odom_qvio', Odometry, queue_size=1)

    # rospy.loginfo("hello_str")
    rate = rospy.Rate(50)  # 30hz

    try:
        while not rospy.is_shutdown():
            # rospy.spin()
            # rospy.loginfo("hello_str")
            rate.sleep()
    except rospy.ROSInterruptException:
        pass

