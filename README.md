# robotSim
This project is a Python simulation for an intelligent robot. It is broken into two main portions: simulation and tactical. The simulation code is for development and debugging purposes. The tactical code is meant to drive an actual robot. 

Simulation
  A simulated world is represented my a binary map (world.py class). Navigable space (open ground) is represented by a 0 and non-navigable space (wall or other obstacle) is represented by a 1. 
  
  The robot itself is also simulated (robot.py). The simulated robot is able to turn in place, drive in a straight line, sense it's own motion, and sense the distance to the nearest object directly in front of it by way of ultrasonic rangefinder.
  
Tactical
  The tactical code (ai.py) is what actually drives the robot and attempts to map the world around it (statMap.py) by using the robot's rangefinder.
___________________________________________________________________________________________________________________________

Coordinate System

World Map Axis
  Row/Column are discrete integers which are used for truth Map and AI Environment Map. 

  X/Y are continuous scalars which are used for Truth Robot location and AI Robot location estimation.

        -col <----------------------------> +col
          -X <----------------------------> +X
          
-row -Y 
  ^   ^
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  v   v
+row  Y

Orientation is defined as radians off of the X axis clockwise.

    ---------------> X
    \    theta
     \  
      \
