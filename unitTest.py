# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:25:09 2015

@author: ben
"""

import world as w
import robot as r
import ai
import numpy as np
import math

print '\nBegin Unit Test 1\n'
# This is a noiseless test to show that the senseAndUpdateMap() function is working properly
# First, the robot senses the distance to the wall directly right of himself twice to get a good confidence,
# Then an obstical is placed between the robot and the wall, two more readings are taken.
# Finally, the obastacle is removed and two more readings are taken. 
#
# Expect the aiMap to show the wall, then the obstacle without effecting the wall confidence, then the obstacle confidence should fall and the wall confidence should continue to rise

printFlag = 0

expectedMap = np.array([[ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                 [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                 [ 0.0, 0.0, 0.0, 0.0, 0.39858075,  0.0, 0.9375],
                 [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                 [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])
                 
newWorld = w.world(0,0,1)
newRobot = r.robot(newWorld,3,4,0,noise=0)
newAI    = ai.ai(newRobot)

for i in range(2):
    newAI.senseAndUpdateMap()
    if(printFlag):
        print newAI.map

newWorld.map[4][5] = 1   
    
for i in range(2):
    newAI.senseAndUpdateMap()
    if(printFlag):
        print newAI.map

newWorld.map[4][5] = 0   
    
for i in range(2):
    newAI.senseAndUpdateMap()
    if(printFlag):
        print newAI.map

print ' - AI map'
newAI.printMap()
print ' - Truth Map'
print newRobot.whereAmI()

actualMap = newAI.map.mapArray

if(np.allclose(actualMap,expectedMap)): #(actualMap == expectedMap).all()):
    print 'Unit Test 1 Passed'
else:
    print 'Unit Test 1 Failed'
    print 'Expected Map'
    print expectedMap
    print 'Actual Map'
    print newAI.map.mapArray
    
# Test Navigate to Goal x only
print '\nBegin Unit Test 2a\n'
newAI.navigateToGoal(0,1.0)

print ' - AI map'
newAI.printMap()
print ' - Truth Map'
print newRobot.whereAmI()
    
# Test Navigate to Goal y only
print '\nBegin Unit Test 2b\n'
newAI.navigateToGoal(2.5,1.0)

print ' - AI map'
newAI.printMap()
print ' - Truth Map'
print newRobot.whereAmI()
    
    
# Test Navigate to Goal x & y both
print '\nBegin Unit Test 2c\n'
newAI.navigateToGoal(-1,-1)

print ' - AI map'
newAI.printMap()
print ' - Truth Map'
print newRobot.whereAmI()
    
    
# Test Navigate to Goal off map
print '\nBegin Unit Test 2d\n'
newAI.navigateToGoal(2,4)

print ' - AI map'
newAI.printMap()
print ' - Truth Map'
print newRobot.whereAmI()


# Test Navigate to Goal around obstacle
newWorld.map[7][5] = 1 
print '\nBegin Unit Test 2e\n'
newAI.turnToHeading(math.pi*(3.0/2.0))
newAI.senseAndUpdateMap()
print ' - AI map'
newAI.printMap()
print ' - Truth Map'
print newRobot.whereAmI()

newAI.navigateToGoal(2,0)

print ' - AI map'
newAI.printMap()
print ' - Truth Map'
print newRobot.whereAmI()