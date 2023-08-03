#include <ros/ros.h>
#include <nav_msgs/Path.h>
#include <geometry_msgs/Quaternion.h>
#include <geometry_msgs/PoseStamped.h>


// 圆点坐标：(x0,y0) 
// 半径：r 
// 角度：a0 

// 则圆上任一点为：（x1,y1） 
// x1   =   x0   +   r   *   cos(ao   *   3.14   /180   ) 
// y1   =   y0   +   r   *   sin(ao   *   3.14   /180   ) 

main (int argc, char **argv)
{
	ros::init (argc, argv, "by_path");

	ros::NodeHandle ph;
	ros::Publisher path_pub = ph.advertise<nav_msgs::Path>("/path_gt",1, true);


	float f = 0.0;
	ros::Rate loop_rate(1);
	while (ros::ok())
	{
		nav_msgs::Path path;
		// nav_msgs::Path path;
		path.header.stamp=ros::Time::now();
		path.header.frame_id="/map";
		// for (uint32_t i = 270; i > 180; i--)
		// {
        //     float x = 1 + cos(i * 3.14/180);
        // 	float y = 1 + sin(i * 3.14/180);
			
		// 	geometry_msgs::PoseStamped this_pose_stamped;
		// 	this_pose_stamped.pose.position.x = x;
		// 	this_pose_stamped.pose.position.y = y;

		// 	//geometry_msgs::Quaternion goal_quat = tf::createQuaternionMsgFromYaw(1);
		// 	this_pose_stamped.pose.orientation.x = 0;
		// 	this_pose_stamped.pose.orientation.y = 0;
		// 	this_pose_stamped.pose.orientation.z = 0;
		// 	this_pose_stamped.pose.orientation.w = 1;

		// 	this_pose_stamped.header.stamp=ros::Time::now();;
		// 	this_pose_stamped.header.frame_id="/map";

		// 	path.poses.push_back(this_pose_stamped);
		// }
        // for (uint32_t i = 180; i > 90; i--)
		// {	
		// 	float x = 1 + cos(i * 3.14/180);
        //     float y = 7 + sin(i * 3.14/180);
		// 	geometry_msgs::PoseStamped this_pose_stamped;
		// 	this_pose_stamped.pose.position.x = x;
		// 	this_pose_stamped.pose.position.y = y;

		// 	//geometry_msgs::Quaternion goal_quat = tf::createQuaternionMsgFromYaw(1);
		// 	this_pose_stamped.pose.orientation.x = 0;
		// 	this_pose_stamped.pose.orientation.y = 0;
		// 	this_pose_stamped.pose.orientation.z = 0;
		// 	this_pose_stamped.pose.orientation.w = 1;

		// 	this_pose_stamped.header.stamp=ros::Time::now();;
		// 	this_pose_stamped.header.frame_id="/map";

		// 	path.poses.push_back(this_pose_stamped);
		// }for (uint32_t i = 90; i > 0; i--)
		// {
        //     float x = 4 + cos(i * 3.14/180);
        // 	float y = 7 + sin(i * 3.14/180);
		// 	geometry_msgs::PoseStamped this_pose_stamped;
		// 	this_pose_stamped.pose.position.x = x;
		// 	this_pose_stamped.pose.position.y = y;

		// 	//geometry_msgs::Quaternion goal_quat = tf::createQuaternionMsgFromYaw(1);
		// 	this_pose_stamped.pose.orientation.x = 0;
		// 	this_pose_stamped.pose.orientation.y = 0;
		// 	this_pose_stamped.pose.orientation.z = 0;
		// 	this_pose_stamped.pose.orientation.w = 1;

		// 	this_pose_stamped.header.stamp=ros::Time::now();;
		// 	this_pose_stamped.header.frame_id="/map";

		// 	path.poses.push_back(this_pose_stamped);
		// }for (uint32_t i = 360; i > 270; i--)
		// {
        //     float x = 4 + cos(i * 3.14/180);
        // 	float y = 1 + sin(i * 3.14/180);
		// 	geometry_msgs::PoseStamped this_pose_stamped;
		// 	this_pose_stamped.pose.position.x = x;
		// 	this_pose_stamped.pose.position.y = y;

		// 	//geometry_msgs::Quaternion goal_quat = tf::createQuaternionMsgFromYaw(1);
		// 	this_pose_stamped.pose.orientation.x = 0;
		// 	this_pose_stamped.pose.orientation.y = 0;
		// 	this_pose_stamped.pose.orientation.z = 0;
		// 	this_pose_stamped.pose.orientation.w = 1;

		// 	this_pose_stamped.header.stamp=ros::Time::now();;
		// 	this_pose_stamped.header.frame_id="/map";

		// 	path.poses.push_back(this_pose_stamped);
		// }
 /////////////////////////////////////////////////////////////////////////////////////////////////////
        geometry_msgs::PoseStamped this_pose_stamped;
        this_pose_stamped.pose.position.x = 1.22;
        this_pose_stamped.pose.position.y = 1.22;

        //geometry_msgs::Quaternion goal_quat = tf::createQuaternionMsgFromYaw(1);
        this_pose_stamped.pose.orientation.x = 0;
        this_pose_stamped.pose.orientation.y = 0;
        this_pose_stamped.pose.orientation.z = 0;
        this_pose_stamped.pose.orientation.w = 1;

        this_pose_stamped.header.stamp=ros::Time::now();;
        this_pose_stamped.header.frame_id="/map";

        path.poses.push_back(this_pose_stamped);
        for (uint32_t i = 180; i > 0; i--)
		{	
			float x = 2.44 + 1.22 * cos(i * 3.14/180);
            // float y = 4.88 + 1.22 * sin(i * 3.14/180);
			float y = 5.5 + 1.22 * sin(i * 3.14/180);
			
			this_pose_stamped.pose.position.x = x;
			this_pose_stamped.pose.position.y = y;

			//geometry_msgs::Quaternion goal_quat = tf::createQuaternionMsgFromYaw(1);
			this_pose_stamped.pose.orientation.x = 0;
			this_pose_stamped.pose.orientation.y = 0;
			this_pose_stamped.pose.orientation.z = 0;
			this_pose_stamped.pose.orientation.w = 1;

			this_pose_stamped.header.stamp=ros::Time::now();;
			this_pose_stamped.header.frame_id="/map";

			path.poses.push_back(this_pose_stamped);
		}for (uint32_t i = 360; i > 270; i--)
		{
            float x = 2.44 + 1.22 * cos(i * 3.14/180);
        	float y = 2.44 + 1.22 * sin(i * 3.14/180);

			this_pose_stamped.pose.position.x = x;
			this_pose_stamped.pose.position.y = y;

			//geometry_msgs::Quaternion goal_quat = tf::createQuaternionMsgFromYaw(1);
			this_pose_stamped.pose.orientation.x = 0;
			this_pose_stamped.pose.orientation.y = 0;
			this_pose_stamped.pose.orientation.z = 0;
			this_pose_stamped.pose.orientation.w = 1;

			this_pose_stamped.header.stamp=ros::Time::now();;
			this_pose_stamped.header.frame_id="/map";

			path.poses.push_back(this_pose_stamped);
		}


/////////////////////////////////////////////////////////////////////////////////////////////////////





        this_pose_stamped.pose.position.x = 1.22;
        this_pose_stamped.pose.position.y = 1.22;

        //geometry_msgs::Quaternion goal_quat = tf::createQuaternionMsgFromYaw(1);
        this_pose_stamped.pose.orientation.x = 0;
        this_pose_stamped.pose.orientation.y = 0;
        this_pose_stamped.pose.orientation.z = 0;
        this_pose_stamped.pose.orientation.w = 1;

        this_pose_stamped.header.stamp=ros::Time::now();;
        this_pose_stamped.header.frame_id="/map";

        path.poses.push_back(this_pose_stamped);
        // float 

		path_pub.publish(path);
		//ros::spinOnce();               // check for incoming messages
		loop_rate.sleep();
		f += 0.04;
	}

	return 0;
}