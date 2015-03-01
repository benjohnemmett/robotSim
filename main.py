
import world as w
import robot as r
import ai 
import matplotlib.pyplot as plt
import time

newWorld = w.world(0,0)
newRobot = r.robot(newWorld,10,10,0)
newAI    = ai.ai(newRobot)

print newAI.map
newAI.senseAndUpdateMap()

print newAI.map

step = 100

for i in range(100):
    newAI.turn((2*pi)/100)
    newAI.senseAndUpdateMap()

newAI.printMap()
print newRobot.whereAmI()

print "Turning " + str(newAI.turn(0.75))
print "Moving " + str(newAI.drive(4.5))

newAI.printMap()
print newRobot.whereAmI()

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
