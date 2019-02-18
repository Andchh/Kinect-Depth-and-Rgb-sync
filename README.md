# Kinect-Depth-and-Rgb-sync
A python script to capture with a turtlebot using ros the rgb and depth images synchronized.


HOW TO USE:
put the script on the folder where you want the images to be saved.
navigate to the folder and execute with: $python record.py
messages with "receiving depth" and "receiving rgb" will appear on the prompt.
stop with ctrl c.

update:
more detailed instructions.
with this you can turn on the turtlebot, control him with tele-operation prompt and save rgb and depth images

Turtlebot
-- terminal 1 --
$ roscore

-- terminal 2 --
# conect white-netbook to turtlebot
$ roslaunch turtlebot_bringup minimal.launch
&& Listing BIP

-- terminal 3 --
# run kinect’s cam
$ roslaunch freenect_launch freenect.launch

PC #terminal to control turtlebot, it can be in the same as before.

-- terminal 1 --
# conect pc to turtlebot
$ ssh turtlebot@10.42.0.1
# run tele-operation
$ roslaunch turtlebot_teleop keyboard_teleop.launch

-- terminal 2 --
$ ssh turtlebot@10.42.0.1
# go to folder and execute record.py
$ python record.py
