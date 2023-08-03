# Indoor_Positioning

This code is tested on Ubuntu 18.04 with ROS Melodic.

### Installation

    cd ~/catkin_ws/src
    
    git clone https://github.com/kellen080/Indoor_positioning.git
    
    cd ~/catkin_ws
    
    catkin_make_isolated

### Open All 

    roslaunch mypkg traj.launch

---

### Open Isolated Positioning Devices

#### UWB

Pose Topic: /nlt_nodeframe2_pose

    roslaunch nlink_parser linktrack.launch
    
    roslaunch nlink_parser linktrack_rviz.launch
    
    /nlt_nodeframe2_pose


#### QVIO

Pose Topic: /qvio/pose

    source my_ros_env.sh
    
    roslaunch voxl_mpa_to_ros voxl_mpa_to_ros.launch

#### AprilTag
    
Pose Topic: /tag_odometry
    
    roslaunch realsense2_camera rs_camera.launch camera:=camera2 serial_no:=035722250476
    
    roslaunch apriltag_ros continuous_detection.launch
    

#### RTAB-Map

    roslaunch realsense2_camera rs_camera.launch camera:=camera serial_no:=832112072181 align_depth:=true
