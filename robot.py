'''
Truth Model for a simple crawling robot
'''

import numpy as np
import math

class robot(object):
    
    
    
    def __init__(self,world,sx,sy,sO):
        
        self.world = world
        (eowx, eowy) = world.map.shape
        
        x = round(sx)
        y = round(sy)
        o = sO % (2*math.pi)
            
        self.o = o
        if((sx >= 0) & (sx <= eowx) & (sy >= 0) & (sy <= eowy)):
            if(world.map[y][x] == 0):
                self.x = sx
                self.y = sy
            else:
                o = np.where(world.map == 0)
                self.x = o[0][0]
                self.y = o[0][1]
                print "Invalid Robot location: Starting Robot at " + str(self.x) + "," + str(self.y)
        else:
            o = np.where(world.map == 0)
            self.x = o[0][0]
            self.y = o[0][1]
            print "Invalid Robot location: Starting Robot at " + str(self.x) + "," + str(self.y)
            
    def __str__(self):
        m = np.copy(self.world.map)
        m[round(self.y)][round(self.x)] = 4
        return str(m) + " radians"
#    
#    def show(self):
#        m = np.copy(self.world.map)
#        m[round(self.y)][round(self.x)] = 4
#        print m
#        print str(self.o) + " radians"
        
    def whereAmI(self):
        m = np.copy(self.world.map)
        m[round(self.y)][round(self.x)] = 4
        return m
        
# Commands which will be given to the Arduino Controller

    def drive(self,distance):
        #Assuming small increments of motion (<=1)
        # To Do
        #   - Break down into loop of small motion steps 
        #   - Add noise to measurement
        #   - Add process noise as well
        xOrig = self.x
        yOrig = self.y
        
        stepSize = 0.1
        (eowx, eowy) = self.world.map.shape
        
        dx = math.cos(self.o)
        dy = math.sin(self.o)
        
        numSteps = int(math.floor(distance/stepSize))
        residualStepSize = distance % stepSize        
        
        for i in range(numSteps):
                        
            tx = self.x + dx*stepSize
            ty = self.y + dy*stepSize
            if((tx >= 0) & (tx <= eowx) & (ty >= 0) & (ty <= eowy)): #Check if sim robot went off the sim map
                if(self.world.map[round(ty)][round(tx)] == 0):      #Check if sim robot hit something
                    self.x = tx
                    self.y = ty
                #else:
                    #print "Bonk! You hit something."
            #else:
                #print "Oops! You tried to go off the map!"

        tx = self.x + dx*residualStepSize
        ty = self.y + dy*residualStepSize
        if((tx >= 0) & (tx <= eowx) & (ty >= 0) & (ty <= eowy)): #Check if sim robot went off the sim map
            if(self.world.map[round(ty)][round(tx)] == 0):      #Check if sim robot hit something
                self.x = tx
                self.y = ty
            #else:
                #print "Bonk! You hit something."
        #else:
           # print "Oops! You tried to go off the map!"
                
        return math.sqrt((self.x-xOrig)**2 + (self.y-yOrig)**2)
            
    def turn(self,do):
        if(do > 2*math.pi):
            print "Warning turn angle greater than 2pi given!"
        o = self.o      # Get original orientation
        to = o + do     # Add new turn command offset
        self.o = to % (2*math.pi) # Set new Orientation 
        measured = do   # Get meaurement from IMU which will be sent to AI
        #print "Turn start: "+ str(o) + " end: " + str(self.o) + " do: " + str(do) + " measured: " + str(measured)
        return measured
        
    def sense(self):
        #To Do
        #   - Add measurement noise
        stepSize = 0.2
        tx = self.x
        ty = self.y 
        
        m = self.world.map
        
        while((m[round(ty)][round(tx)] == 0) | (m[round(ty)][round(tx)] == 4)):
            tx += stepSize*math.cos(self.o)
            ty += stepSize*math.sin(self.o)
            
        d = math.sqrt((tx - self.x)**2 + (ty-self.y)**2)
        return d
        