# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 22:17:58 2015

@author: Ben
"""
import robot
import numpy as np
import math
import map

class ai(object):
    
    def __init__(self,robot):
        
        self.robot = robot #This is the simulated robot that this ai algorithm lives inside
        self.map = map.map(5,5,2.5,2.5)
        self.x = 0.0
        self.y = 0.0
        self.o = 0.0
        
# Robot control functions
    def sense(self):
        return self.robot.sense()
        
    def move(self,distance):
        return self.robot.move(distance)
        
    def turn(self,o):
        return self.robot.turn(o)
    
    def senseAndUpdateMap(self):
        d = self.sense();
        
        #Break down into X and Y components
        dx = d*math.cos(self.o)
        dy = d*math.sin(self.o)
        
        
        
        
        
# Robot AI functions
#   def navigateToGoal(self, goal): # Plan and follow a route to reach the goal
#   def createAreaMap(self):        # Drive around the area to create a map of the environment
