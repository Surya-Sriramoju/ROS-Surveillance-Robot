#!/usr/bin/env python

from gpiozero import PWMOutputDevice
from time import sleep
import rospy
from geometry_msgs.msg import Twist

PWM_FORWARD_LEFT_PIN = 5
PWM_REVERSE_LEFT_PIN = 6
PWM_FORWARD_RIGHT_PIN = 17
PWM_REVERSE_RIGHT_PIN = 27

forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)

forwardRight = PWMOutputDevice(PWM_aFORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)

def allStop():
        forwardLeft.value = 0
        reverseLeft.value = 0
        forwardRight.value = 0
        reverseRight.value = 0
def forwardDrive(l,r):
        forwardLeft.value = l
        reverseLeft.value = 0
        forwardRight.value = r
        reverseRight.value = 0
def reverseDrive(l,r):
        forwardLeft.value = 0
        reverseLeft.value = l
        forwardRight.value = 0
        reverseRight.value = r
def spinLeft(l,r):
        forwardLeft.value = 0
        reverseLeft.value = l
        forwardRight.value = r
        reverseRight.value = 0
def spinRight(l,r):
        forwardLeft.value = l
        reverseLeft.value = 0
        forwardRight.value = 0
        reverseRight.value = r

def message(command):
    x = command
    linear = x.linear.x
    angular = x.angular.z
    l = linear - (angular/2)
    r = linear + (angular/2)
    l = abs(l)
    r = abs(r)
    if linear>0:
	forwardDrive(l,r)
    elif linear<0:
	reverseDrive(l,r)
    elif angular > 0:
	spinLeft(l,r)
    elif angular < 0:
	spinRight(l,r)
    elif(linear == 0 and angular == 0):
	allStop()


def main():
    rospy.init_node('test1')
    rospy.Subscriber('/cmd_vel',Twist,message)
    rospy.spin()
if __name__ == '__main__':
    main()
