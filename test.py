#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
for m in [1, 2]:
	print "Forward! ", m
	myMotor = mh.getMotor(m)
	myMotor.run(Adafruit_MotorHAT.FORWARD)

	print "\tSpeed up..."
	for i in range(255):
		myMotor.setSpeed(i)
		time.sleep(0.01)

	print "\tSlow down..."
	for i in reversed(range(255)):
		myMotor.setSpeed(i)
		time.sleep(0.01)

	print "Backward! ", m
	myMotor.run(Adafruit_MotorHAT.BACKWARD)

	print "\tSpeed up..."
	for i in range(255):
		myMotor.setSpeed(i)
		time.sleep(0.01)

	print "\tSlow down..."
	for i in reversed(range(255)):
		myMotor.setSpeed(i)
		time.sleep(0.01)

	print "Release", m
	myMotor.run(Adafruit_MotorHAT.RELEASE)
	time.sleep(1.0)
