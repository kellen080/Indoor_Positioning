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

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped

def myPath():
    # pub = rospy.Publisher('path_gt', Path, queue_size=10)
    # rospy.init_node('proc_gt', anonymous=True)
    # rate = rospy.Rate(10) # 10hz
    pose = PoseStamped()
    
    for x in range (0, 3):
        pose.pose.position.x = x
        pose.pose.position.y = x
        pose.pose.position.z = 0
        pose.pose.orientation.x = 0
        pose.pose.orientation.y = 0
        pose.pose.orientation.z = 0
        pose.pose.orientation.w = 1
        pose.header.stamp = rospy.Time.now()
        pose.header.frame_id = "/map"
        path.poses.append(pose)

    # x = 0
    # y = 0
    
    # pose.pose.position.x = x
    # pose.pose.position.y = y
    # pose.pose.position.z = 0
    # pose.pose.orientation.x = 0
    # pose.pose.orientation.y = 0
    # pose.pose.orientation.z = 0
    # pose.pose.orientation.w = 1
    # pose.header.stamp = rospy.Time.now()
    # pose.header.frame_id = "/map"
    

    # path.poses.append(pose)
    
    # # x = 1
    # # y = 1
    
    # pose.pose.position.x = x
    # pose.pose.position.y = y
    # pose.header.stamp = rospy.Time.now()
    # pose.header.frame_id = "/map"
   
    # path.poses.append(pose)
    
    path.header.stamp = rospy.Time.now()
    path.header.frame_id = "/map"
    


def talker():
    # pub = rospy.Publisher('path_gt', Path, queue_size=10)
    # rospy.init_node('proc_gt', anonymous=True)
    # rate = rospy.Rate(10) # 10hz

    # pose = PoseStamped()

    # x = 0
    # y = 0
    
    # pose.pose.position.x = x
    # pose.pose.position.y = y
    # pose.pose.position.z = 0
    # pose.pose.orientation.x = 0
    # pose.pose.orientation.y = 0
    # pose.pose.orientation.z = 0
    # pose.pose.orientation.w = 1
    # pose.header.stamp = rospy.Time.now()
    # pose.header.frame_id = "map"
    # pose.header.seq = 0
    # path.poses.append(pose)
    
    # x = 1
    # y = 1
    
    # pose.pose.position.x = x
    # pose.pose.position.y = y
    # pose.header.stamp = rospy.Time.now()
    # pose.header.frame_id = "map"
    # pose.header.seq = 1 
    # path.poses.append(pose)
 
    # path.header.frame_id = "map"
    # path.header.stamp = rospy.Time.now()
    # pose.header.stamp = path.header.stamp


    # path.poses.append(pose)
    

    while not rospy.is_shutdown():
        pub.publish(path)
        rate.sleep()

if __name__ == '__main__':
    pub = rospy.Publisher('path_gt', Path, queue_size=10)
    rospy.init_node('proc_gt', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    path = Path()
    print(path.poses)
    myPath()
    # while not rospy.is_shutdown():
    #     pub.publish(path)
    #     rate.sleep()
    # try:
    #     talker()
    # except rospy.ROSInterruptException:
    #     pass
