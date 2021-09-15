from RobotArm import RobotArm;robotArm = RobotArm('exercise 9')
for i in range(1,5):
    for i in range(1,5):
        robotArm.grab()
        for i in range(1,7):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(1,6):
            robotArm.moveLeft()
    for i in range(1,5):
        robotArm.moveLeft()
robotArm.wait()