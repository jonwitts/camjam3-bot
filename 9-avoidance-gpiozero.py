#!/usr/bin/env python3

from gpiozero import CamJamKitRobot, LED, DistanceSensor # Import our devices
import time # Import the Time library 

# Distance Variables
HowNear = 0.25
ReverseTime = 0.75
TurnTime = 0.75

# Set the default speed for the motors
DefaultSpeed = 0.4
#DefaultSpeed = 1

# set up our devices
robot = CamJamKitRobot()
redled = LED(23)
blueled = LED(24)
sensor = DistanceSensor(18, 17, max_distance=2, threshold_distance=HowNear)

# Define our functions

# Return True if the ultrasonic sensor sees an obstacle
def IsNearObstacle(localHowNear):
	Distance = Measure()
	print("IsNearObstacle: "+str(Distance))
	if Distance < localHowNear:
		return True
	else:
		return False

# Take a distance measurement
def Measure():
	Distance = sensor.distance
	return Distance

# Move back a little, then turn right
def AvoidObstacle():
	# Back off a little
	print("Backwards")
	Backwards(ReverseTime)
	StopMotors()
	# Turn right
	print("Right")
	Right(TurnTime)
	StopMotors()

# Turn all motors off 
def StopMotors(): 
	robot.stop()
	blueled.off()
	redled.off()
	
# Turn both motors forwards 
def Forwards(moveTime):
	redled.off()
	blueled.blink() 
	robot.backward(DefaultSpeed)
	time.sleep(moveTime)

# Turn both motors backwards 
def Backwards(moveTime): 
	blueled.off()
	redled.blink()
	robot.forward(DefaultSpeed)
	time.sleep(moveTime)

# Turn left 
def Left(moveTime): 
	robot.left(DefaultSpeed)
	time.sleep(moveTime)

# Turn Right 
def Right(moveTime): 
	robot.right(DefaultSpeed)
	time.sleep(moveTime)

# Flash LEDs
def Flash():
	for i in range(4):
		redled.toggle()
		time.sleep(0.5)
		blueled.toggle()
		time.sleep(0.5)
	redled.off()
	blueled.off()

# Robot movement code goes here

Flash()
try:
	# Allow module to settle
	time.sleep(0.1)

	# Repeat the next indented block forever
	while True:
		Forwards(0.1)
		if IsNearObstacle(HowNear):
			StopMotors()
			AvoidObstacle()

# If you press CTRL+C stop
except KeyboardInterrupt:
	StopMotors()
