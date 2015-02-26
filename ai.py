# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 22:17:58 2015

@author: Ben
"""
import robot
import numpy as np

class ai(object):
    
    def __init__(self,robot):
        
        self.robot = robot #This is the simulated robot that this ai algorithm lives inside
        self.map = np.array([[4]])
        
# Robot control functions
    def sense(self):
        return self.robot.sense()
        
    def move(self,distance):
        return self.robot.move(distance)
        
    def turn(self,o):
        return self.robot.turn(o)
        
# Robot AI functions
#   def navigateToGoal(self, goal): # Plan and follow a route to reach the goal
#   def createAreaMap(self):        # Drive around the area to create a map of the environment
