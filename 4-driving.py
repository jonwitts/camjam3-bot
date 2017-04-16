#!/usr/bin/env python3

# CamJam EduKit 3 - Robotics 
# Worksheet 4 – Driving and Turning 

import RPi.GPIO as GPIO # Import the GPIO Library
from gpiozero import LED # we want some flashing lights!
import time # Import the Time library 

# Set the GPIO modes 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 

# Set variables for the GPIO motor pins 
pinMotorAForwards = 10 
pinMotorABackwards = 9 
pinMotorBForwards = 8 
pinMotorBBackwards = 7 

# set the variables for the LEDs
redled = LED(23)
blueled = LED(24)

# Set the GPIO Pin mode 
GPIO.setup(pinMotorAForwards, GPIO.OUT) 
GPIO.setup(pinMotorABackwards, GPIO.OUT) 
GPIO.setup(pinMotorBForwards, GPIO.OUT) 
GPIO.setup(pinMotorBBackwards, GPIO.OUT) 

# Turn all motors off 
def StopMotors(): 
	GPIO.output(pinMotorAForwards, 0) 
	GPIO.output(pinMotorABackwards, 0) 
	GPIO.output(pinMotorBForwards, 0) 
	GPIO.output(pinMotorBBackwards, 0) 
	blueled.off()
	redled.off()
	
# Turn both motors forwards 
def Forwards():
	redled.off()
	blueled.blink() 
	GPIO.output(pinMotorAForwards, 1) 
	GPIO.output(pinMotorABackwards, 0) 
	GPIO.output(pinMotorBForwards, 1) 
	GPIO.output(pinMotorBBackwards, 0) 
	
# Turn both motors backwards 
def Backwards(): 
	blueled.off()
	redled.blink()
	GPIO.output(pinMotorAForwards, 0) 
	GPIO.output(pinMotorABackwards, 1) 
	GPIO.output(pinMotorBForwards, 0) 
	GPIO.output(pinMotorBBackwards, 1) 

# Turn left 
def Left(): 
	GPIO.output(pinMotorAForwards, 0) 
	GPIO.output(pinMotorABackwards, 1) 
	GPIO.output(pinMotorBForwards, 1) 
	GPIO.output(pinMotorBBackwards, 0) 
	
# Turn Right 
def Right(): 
	GPIO.output(pinMotorAForwards, 1) 
	GPIO.output(pinMotorABackwards, 0) 
	GPIO.output(pinMotorBForwards, 0) 
	GPIO.output(pinMotorBBackwards, 1)

#time.sleep(20)
	
Forwards()
time.sleep(4)

Left()
time.sleep(0.5)

Forwards()
time.sleep(1)

Right()
time.sleep(0.5)

Backwards()
time.sleep(2)

StopMotors()

GPIO.cleanup()
