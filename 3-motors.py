#!/usr/bin/python3

# CamJam EduKit 3 - Robotics 
# Worksheet 3 - Motor Test Code 
# GPIOZero version

from gpiozero import CamJamKitRobot
from time import sleep

robot = CamJamKitRobot()

# Turn all motors off 
robot.stop()

# Turn the right motor forwards 
robot.right()

# Wait for 1 second 
sleep(1)

# Turn the left motor forwards 
robot.left()

# Wait for 1 second 
sleep(1) 

# Turns off motors
robot.stop()
