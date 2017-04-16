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

# How many times to turn the pin on and off each second
Frequency = 50

# How long the pin stays on each cycle, as a percent
DutyCycleA = 30
DutyCycleB = 30

# Setting the duty cycle to zero means the motors will not turn
Stop = 0

# Set the GPIO Pin mode 
GPIO.setup(pinMotorAForwards, GPIO.OUT) 
GPIO.setup(pinMotorABackwards, GPIO.OUT) 
GPIO.setup(pinMotorBForwards, GPIO.OUT) 
GPIO.setup(pinMotorBBackwards, GPIO.OUT) 

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

# Turn all motors off 
def StopMotors(): 
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(Stop) 
	pwmMotorBForwards.ChangeDutyCycle(Stop) 
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
	blueled.off()
	redled.off()
	
# Turn both motors forwards 
def Forwards():
	redled.off()
	blueled.blink() 
	pwmMotorAForwards.ChangeDutyCycle(DutyCycleA) 
	pwmMotorABackwards.ChangeDutyCycle(Stop) 
	pwmMotorBForwards.ChangeDutyCycle(DutyCycleB) 
	pwmMotorBBackwards.ChangeDutyCycle(Stop)	

# Turn both motors backwards 
def Backwards(): 
	blueled.off()
	redled.blink()
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycleA) 
	pwmMotorBForwards.ChangeDutyCycle(Stop) 
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

# Turn left 
def Left(): 
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycleA) 
	pwmMotorBForwards.ChangeDutyCycle(DutyCycleB) 
	pwmMotorBBackwards.ChangeDutyCycle(Stop)	

# Turn Right 
def Right(): 
	pwmMotorAForwards.ChangeDutyCycle(DutyCycleA) 
	pwmMotorABackwards.ChangeDutyCycle(Stop) 
	pwmMotorBForwards.ChangeDutyCycle(Stop) 
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

# Robot movement code goes here
time.sleep(2)
	
Forwards()
time.sleep(8)

Left()
time.sleep(0.5)

Forwards()
time.sleep(1)

Right()
time.sleep(0.5)

Backwards()
time.sleep(4)

StopMotors()

GPIO.cleanup()
