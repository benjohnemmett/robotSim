# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:25:09 2015

@author: ben
"""

import world as w
import robot as r
import ai
import numpy as np

print 'Unit Test 1'
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

newAI.printMap()
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