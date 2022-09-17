"""bug_0_algo controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot


def move(robot):
    # get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6

    #Motors
    left_motor = robot.getDevice("left wheel motor")
    right_motor = robot.getDevice("right wheel motor")
    
    left_motor.setPosition(float("inf"))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float("inf"))
    right_motor.setVelocity(0.0)
    
    #Proximity
    p_sen = []
    for i in range(8):
        s = f"ps{str(i)}"
        p_sen.append(robot.getDistanceSensor(s))
        p_sen[i].enable(timestep) 

    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        # Read the sensors:
        for i in range(8):
            print(f"i: {i}, val: {p_sen[i].getValue()}")
    
        # Process sensor data here.
        left_wall = p_sen[5].getValue() > 80
        right_wall = p_sen[2].getValue() > 80
        front_wall = p_sen[7].getValue() > 80
        
        left_motor.setVelocity(max_speed)
        right_motor.setVelocity(max_speed)
        
    
    # Enter here exit cleanup code.

# create the Robot instance.
robot = Robot()
move(robot)


