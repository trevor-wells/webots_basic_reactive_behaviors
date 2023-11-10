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

state = 'FORWARD'

counter = 0
obstacles = 0

while robot.step(TIME_STEP) != -1:
    d = []
    for sensor in ds:
        d.append(sensor.getValue())
        
    if state == 'FORWARD':
        right_motor.setVelocity(0.38 * MAX_SPEED)
        if d[0] > 90:
            state = 'CLOCKWISE'
            obstacles += 1
        elif obstacles == 2 and d[5] < 90:
            state = 'STOP'
    elif state == 'CLOCKWISE':
        right_motor.setVelocity(-0.38 * MAX_SPEED)
        counter += 1
        if (obstacles == 1 and counter == 59) or (obstacles == 2 and counter == 28):
            state = 'FORWARD'
            counter = 0 
    elif state == 'STOP':
        left_motor.setVelocity(0)
        right_motor.setVelocity(0)
 
       
    
