
import world as w
import robot as r
import ai 
import matplotlib.pyplot as plt
import time
import math

newWorld = w.world(0,0,1)
newRobot = r.robot(newWorld,3,4,0)
newAI    = ai.ai(newRobot)

newAI.senseAndUpdateMap360()

plt.imshow(newAI.map.mapArray,interpolation='nearest')
plt.colorbar()
plt.show()

newAI.printMap()
print newRobot.whereAmI()

newAI.navigateToGoal(2,6)


"""
plt.imshow(newRobot.whereAmI(),interpolation='nearest')
plt.figure(num=1)
time.sleep(0.1)
raw_input("+")


print newRobot.sense()
print "Command: Drive 5.1, actual " + str(newRobot.drive(5.1))
print newRobot

print newRobot.sense()
print "Command: Drive 100.1, actual " + str(newRobot.drive(100.1))
print newRobot

plt.imshow(newRobot.whereAmI(),interpolation='nearest')
plt.show()
time.sleep(0.1)
raw_input("+")

print newRobot.sense()
newRobot.turn(2)
print newRobot

plt.imshow(newRobot.whereAmI(),interpolation='nearest')
plt.show()
time.sleep(0.1)
raw_input("+")

print newRobot.sense()
newRobot.drive(4.3)
print newRobot

plt.imshow(newRobot.whereAmI(),interpolation='nearest')
plt.show()
time.sleep(0.1)
raw_input("+")

print newRobot.sense()

plt.close()
"""
