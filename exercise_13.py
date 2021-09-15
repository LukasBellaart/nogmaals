from RobotArm import RobotArm;robotArm = RobotArm(); robotArm.randomLevel(1,7)
counter = 2
while True:
    canGrab = robotArm.grab()
    if not canGrab:
        break
    for i in range(1,counter):
        robotArm.moveRight()
    robotArm.drop()
    counter += 1
    for i in range(1,10):
        robotArm.moveLeft()
    

robotArm.wait()