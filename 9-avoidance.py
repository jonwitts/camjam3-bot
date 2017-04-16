#!/usr/bin/env python3

# CamJam EduKit 3 - Robotics 
# Worksheet 9 - Obstacle Avoidance

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library 

# Set the GPIO modes 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 

# Set variables for the GPIO motor pins 
pinMotorAForwards = 10 
pinMotorABackwards = 9 
pinMotorBForwards = 8 
pinMotorBBackwards = 7 

# set the variables for the ultrasonic sensors
pinTrigger = 17
pinEcho = 18

# Distance Variables
HowNear = 25.0
ReverseTime = 0.75
TurnTime = 0.5

# How many times to turn the pin on and off each second
Frequency = 50

# How long the pin stays on each cycle, as a percent
DutyCycleA = 40
DutyCycleB = 40

# Setting the duty cycle to zero means the motors will not turn
Stop = 0

# Set the GPIO Pin mode 
GPIO.setup(pinMotorAForwards, GPIO.OUT) 
GPIO.setup(pinMotorABackwards, GPIO.OUT) 
GPIO.setup(pinMotorBForwards, GPIO.OUT) 
GPIO.setup(pinMotorBBackwards, GPIO.OUT) 
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

# Set the GPIO to software PWM at 'Frequency' Hertz 
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency) 
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency) 
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency) 
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency) 

# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(Stop) 
pwmMotorABackwards.start(Stop) 
pwmMotorBForwards.start(Stop) 
pwmMotorBBackwards.start(Stop)

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
	GPIO.output(pinTrigger, True)
	time.sleep(0.00001)
	GPIO.output(pinTrigger, False)
	StartTime = time.time()
	StopTime = StartTime

	while GPIO.input(pinEcho)==0:
		StartTime = time.time()
		StopTime = StartTime

	while GPIO.input(pinEcho)==1:
		StopTime = time.time()
		# If the sensor is too close to an object, the Pi cannot
		# see the echo quickly enough, so it has to detect that
		# problem and say what happened
		if StopTime-StartTime >= 0.04:
			print("Hold on there! You're too close for me to see.")
			StopTime = StartTime
			break

	ElapsedTime = StopTime - StartTime
	Distance = (ElapsedTime * 34326)/2

	return Distance

# Move back a little, then turn right
def AvoidObstacle():
	# Back off a little
	print("Backwards")
	Backwards()
	time.sleep(ReverseTime)
	StopMotors()

	# Turn right
	print("Right")
	Right()
	time.sleep(TurnTime)
	StopMotors()

# Turn all motors off 
def StopMotors(): 
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(Stop) 
	pwmMotorBForwards.ChangeDutyCycle(Stop) 
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
	
# Turn both motors forwards 
def Forwards():
	pwmMotorAForwards.ChangeDutyCycle(DutyCycleA) 
	pwmMotorABackwards.ChangeDutyCycle(Stop) 
	pwmMotorBForwards.ChangeDutyCycle(DutyCycleB) 
	pwmMotorBBackwards.ChangeDutyCycle(Stop)	

# Turn both motors backwards 
def Backwards(): 
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycleA) 
	pwmMotorBForwards.ChangeDutyCycle(Stop) 
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

# Turn left 
def Left(): 
	pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
	pwmMotorABackwards.ChangeDutyCycle(Stop) 
	pwmMotorBForwards.ChangeDutyCycle(Stop) 
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)	

# Turn Right 
def Right(): 
	pwmMotorAForwards.ChangeDutyCycle(Stop) 
	pwmMotorABackwards.ChangeDutyCycle(DutyCycleA) 
	pwmMotorBForwards.ChangeDutyCycle(DutyCycleB) 
	pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Robot movement code goes here
try:
	# Set trigger to False (low)
	GPIO.output(pinTrigger, False)
	
	# Allow module to settle
	time.sleep(0.1)

	# Repeat the next indented block forever
	while True:
		Forwards()
		time.sleep(0.1)
		if IsNearObstacle(HowNear):
			StopMotors()
			AvoidObstacle()

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
	GPIO.cleanup()
