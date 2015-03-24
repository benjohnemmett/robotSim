# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 22:17:58 2015

@author: Ben
"""
import numpy as np
import math
import statMap

class ai(object):
    
    traceStepSize = 0.25
    
    def __init__(self,robot):
        
        self.robot = robot #This is the simulated robot that this ai algorithm lives inside
        self.map = statMap.statMap(5,5,2,2)
        self.x = 0.0
        self.y = 0.0
        self.o = 0.0
        
# Robot control functions
    def sense(self):
        return self.robot.sense()
        
    def drive(self,distance):
        # Command Robot to drive requested distance
        d = self.robot.drive(distance)

        # Update estimated position
        self.x += d*math.cos(self.o)
        self.y += d*math.sin(self.o)        
        
        return d
        
    def turn(self,o):
        # Command Robot to turn requested anglular amount
        o = self.robot.turn(o)
        
        # Update orientation estimate
        self.o = (self.o + o) % (2*math.pi)
        
        return o
    
    def senseAndUpdateMap(self):
        traceStepSize = 0.33
        
        # Command Robot to sense distance to nearest echo source
        E = self.sense();
        
        # Break distance down into X and Y components
        dx = math.cos(self.o)
        dy = math.sin(self.o)
        
        # Calculate predicted location of echo source
        Ex = self.x + dx*E
        Ey = self.y + dy*E
        
        # Find Row & Column on map of estimated echo source location
        ERow = round(Ey)
        ECol = round(Ex)
        # Increase probability of echo source at location estimate
        self.map.bumpUp(ERow,ECol)
        
        tx = self.x + traceStepSize*dx
        ty = self.y + traceStepSize*dy
        
        # Decriment probability of echo source between Robot and estimated echo source location
        while (round(ty) != ERow) | (round(tx) != ECol): # Stop decrimenting when you get to the Echo Source location
            
            tRow = round(ty)
            tCol = round(tx)

            self.map.knockDown(tRow,tCol)            
            
            tx += traceStepSize*dx
            ty += traceStepSize*dy
            
        return E

    def senseAndUpdateMap360(self):
        # Take measurements while incrementally spinning in place to map out local area.
        oTotal = 0       
        
        while(oTotal < 2*math.pi):
            distance = self.senseAndUpdateMap()        
            nextTurn = 0.3/distance
            self.turn(nextTurn)
            oTotal += nextTurn
            
    def getMap(self):
        return self.map.mapWithMarker(self.y,self.x,4)

    def printMap(self):
        tmp = self.map.mapWithMarker(self.y,self.x,4)
        print tmp
        
    def navigateToGoal(self,x,y):
        grad = self.map.gradientMapToGoal(y,x)
        print grad.astype(int)
        waypoints = self.map.planRouteToGoal(self.y,self.x,y,x)
        print waypoints
        
    def goToWayPoint(self,wp):
        o = math.atan2((wp[0]-self.y),(wp[1]-self.x)) 
        print 'Turn to ' + str(o * 180/math.pi) + ' deg'
        self.turnToHeading(o)
        
    def turnToHeading(self,o):
        theta_ = o - self.o
        theta_pi = theta_ + math.pi
        theta = (theta_pi %(2*math.pi)) - math.pi
        
        return self.turn(theta)
        
        
# Robot AI functions
#   def navigateToGoal(self, goal): # Plan and follow a route to reach the goal
#   def createAreaMap(self):        # Drive around the area to create a map of the environment
