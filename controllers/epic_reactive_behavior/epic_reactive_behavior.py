from controller import Robot, Motor, DistanceSensor

robot = Robot()

TIME_STEP = 32
MAX_SPEED = 6.28

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

left_motor.setPosition(float('inf'))
left_motor.setVelocity(0.38 * MAX_SPEED)
right_motor.setPosition(float('inf'))
right_motor.setVelocity(0.38 * MAX_SPEED)

ds = []
for i in range(8):
    ds.append(robot.getDevice('ps'+str(i)))
    ds[-1].enable(TIME_STEP)

state = 'FORWARD1'

counter = 0

while robot.step(TIME_STEP) != -1:
    d = []
    for sensor in ds:
        d.append(sensor.getValue())
        
    if state == 'FORWARD1':
        right_motor.setVelocity(0.38 * MAX_SPEED)
        if d[0] > 90:
            state = 'TURN180'
    elif state == 'TURN180':
        right_motor.setVelocity(-0.38 * MAX_SPEED)
        counter += 1
        if counter == 59:
            state = 'FORWARD2'
            counter = 0
    elif state == 'FORWARD2':
        right_motor.setVelocity(0.38 * MAX_SPEED)
        if d[0] > 90:
            state = 'ALIGN'
    elif state == 'ALIGN':
        right_motor.setVelocity(-0.38 * MAX_SPEED)
        counter += 1
        if counter == 28:
            state = 'WFOLLOW'
            counter = 0
    elif state == 'WFOLLOW':
        right_motor.setVelocity(0.38 * MAX_SPEED)
        if d[5] < 90:
            state = 'STOP'
    elif state == 'STOP':
        left_motor.setVelocity(0)
        right_motor.setVelocity(0)
 
       
    
