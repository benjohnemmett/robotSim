# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 22:17:58 2015

@author: Ben
"""
import numpy as np
import math
import aiMap

class ai(object):
    
    def __init__(self,robot):
        
        self.robot = robot #This is the simulated robot that this ai algorithm lives inside
        self.map = aiMap.aiMap(5,5,2.5,2.5)
        self.x = 0.0
        self.y = 0.0
        self.o = 0.0
        
# Robot control functions
    def sense(self):
        return self.robot.sense()
        
    def drive(self,distance):
        d = self.robot.drive(distance)

        self.x += d*math.cos(self.o)
        self.y += d*math.sin(self.o)        
        
        return d
        
    def turn(self,o):
        o = self.robot.turn(o)
        self.o = (self.o + o) % (2*math.pi)
        return o
    
    def senseAndUpdateMap(self):
        d = self.sense();
        #print "Sensed echo " + str(d) + " away."
        
        # Break down into X and Y components
        dx = d*math.cos(self.o)
        dy = d*math.sin(self.o)
                
        # Calculate predicted location of echo
        sx = self.x + dx
        sy = self.y + dy        
        
        #print "Sensed echo " + str(d) +" away (" + str(sx) + "," + str(sy)
        #print "\tEstimated location " + str(sy) + "," + str(sx) 
        
        
        #To Do: Account for sensor noise by creating a map of probabilities of echo sources
        #       Let there be a probabilistic distribution around the estimated echo source location
        #       which becomes negative as it approaches the Robot.
        #       
        #       This may be a 2 part algorithm. First convolve the prior probabilities with those of the new measurement, then penalize probabilities closer to the robot. 
        #
        #
        #       p=0.80                          __   
        #                                      /  \
        # Robot p=0.0                        /     \__________________
        #                                  /         
        #       p=-0.1  _________________/     
        #  ^
        #  | probablity of echo source : distance from Robot -> 
        #
        
        self.map.setValue(sy,sx,1)
        
    def printMap(self):
        tmp = self.map.mapWithMarker(self.y,self.x,4)
        print tmp
        
        
        
# Robot AI functions
#   def navigateToGoal(self, goal): # Plan and follow a route to reach the goal
#   def createAreaMap(self):        # Drive around the area to create a map of the environment
