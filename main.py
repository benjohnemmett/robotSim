
import world as w
import robot as r
import ai 
import matplotlib.pyplot as plt

newWorld = w.world(0,0)
newRobot = r.robot(newWorld,2,2,0)
newAI    = ai.ai(newRobot)

print newAI.map

plt.imshow(newRobot.whereAmI(),interpolation='nearest')
plt.figure(num=1)
pause(0.1)
raw_input("+")


print newRobot.sense()
print "Command: Drive 5.1, actual " + str(newRobot.drive(5.1))
print newRobot

print newRobot.sense()
print "Command: Drive 100.1, actual " + str(newRobot.drive(100.1))
print newRobot

plt.imshow(newRobot.whereAmI(),interpolation='nearest')
plt.show()
pause(0.1)
raw_input("+")

print newRobot.sense()
newRobot.turn(2)
print newRobot

plt.imshow(newRobot.whereAmI(),interpolation='nearest')
plt.show()
pause(0.1)
raw_input("+")

print newRobot.sense()
newRobot.drive(4.3)
print newRobot

plt.imshow(newRobot.whereAmI(),interpolation='nearest')
plt.show()
pause(0.1)
raw_input("+")

print newRobot.sense()

plt.close()

