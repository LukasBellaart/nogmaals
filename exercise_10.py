from RobotArm import RobotArm;robotArm = RobotArm('exercise 10')
counter = 10
for i in range(1,6):
    robotArm.grab()
    for i in range(1,counter):
        robotArm.moveRight()
    robotArm.drop()
    counter = counter - 1
    for i in range(1,counter):
        robotArm.moveLeft()
    counter = counter - 1
robotArm.wait()