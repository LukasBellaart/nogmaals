from RobotArm import RobotArm;robotArm = RobotArm('exercise 11')
for i in range(1,10): 
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.moveRight()
    robotArm.drop()

    robotArm.moveRight()

robotArm.wait()