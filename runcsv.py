#!/usr/bin/python
import csv
import sys
import time
import atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
	print "All motors disabled"
atexit.register(turnOffMotors)


if len(sys.argv)!=2:
	sys.exit("Usage: runcsv.py commands.csv")


COMMANDS = {'FORWARD': Adafruit_MotorHAT.FORWARD,
            'BACKWARD': Adafruit_MotorHAT.BACKWARD,
            'RELEASE': Adafruit_MotorHAT.RELEASE}


def process_step(line, delay, motor, command, speed):
	delay = float(delay)
	if delay < 0.:
		sys.exit("line:%s Delay must be positive" % line)
	motor = int(motor)
	if (motor < 1) or (motor > 4):
		sys.exit("line:%s Motor number must be between 1 and 4." % line)
	command = command.strip()	
	if command not in COMMANDS:
		sys.exit("line:%s Command must be one of FORWARD, REVERSE and RELEASE." % line)
	speed = int(speed)
	if (speed < 0) or (speed > 255):
		sys.exit("line:%s Speed must be between 0 and 255." % line)
	return delay, motor, command, speed


steps = []
with open(sys.argv[1]) as csvfile:
	reader = csv.reader(csvfile)
	for line, row in enumerate(reader, start=1):
		if len(row)!=4:
			sys.exit("line:%s Step needs 4 entries: delay, motor, command, speed" % line)
		steps.append(process_step(line, *row))


print "Running", len(steps), "steps"
for delay, motor, command, speed in steps:
        print delay, motor, command, speed
	time.sleep(delay)
	m = mh.getMotor(motor)
	m.run(COMMANDS[command])
	m.setSpeed(speed)
print "Finished", len(steps), "steps"
