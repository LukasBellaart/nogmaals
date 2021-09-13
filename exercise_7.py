from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
i,x = 1,1
while i <= 5:
    x = 1
    while x <= 7:
        robotArm.moveRight()
        if x == 7:
            robotArm.moveRight()
            break
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        x += 1
    i += 1
robotArm.wait()
