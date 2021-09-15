from RobotArm import RobotArm;robotArm = RobotArm('exercise 12')
counter = 0
while True:
    if counter == 10:
        break  
    canGrab = robotArm.grab()
    if not canGrab:
        counter += 1
    color = robotArm.scan()
    if color == "red":
        for i in range(1,10):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(1,10):
            robotArm.moveLeft()
        counter = 0
    else:
        counter += 1
        robotArm.drop()
    robotArm.moveRight()

robotArm.wait()