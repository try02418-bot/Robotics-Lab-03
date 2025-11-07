from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

import math as m

# robot is the instance of the robot that will allow us to call its methods and to define events with the @event decorator.
robot = Create3(Bluetooth("KIRITO-BOT"))  # Will connect to the first robot found.

HAS_COLLIDED = False
SENSOR2CHECK = 0
ARRIVAL_THRESHOLD = 5
STOP = False 
SIDEWALL_FOUND = False 

IR_ANGLES = [-65.3, -38.0, -20.0, -3.0, 14.25, 34.0, 65.3]


# Implementation for fail-safe robots
# EITHER BUTTON
@event(robot.when_touched, [True, True])  # User buttons: [(.), (..)]
async def when_either_button_touched(robot):
    global STOP
    STOP = True
    print("STOPPED")
    await robot.set_wheel_speeds(0, 0)
    await robot.set_lights_rgb(255, 0, 0)

# EITHER BUMPER
@event(robot.when_bumped, [True, True])  # [left, right]
async def when_either_bumped(robot):
    global STOP
    STOP = True
    print("STOPPED")
    await robot.set_wheel_speeds(0, 0)
    await robot.set_lights_rgb(255, 0, 0)

# ==========================================================

# Helper Functions

# === FIND WHICH SIDE THE WALLS ARE COMING FROM
async def findWall():
    pass

# === MOVE UNTIL WE FIND A GAP, TRACK LARGEST
async def findGaps(robot):
    #frontDist == 
    
    return largest_gap # ((x1, y1), (x2, y2))

# === MOVE ALONG A FOUND GAP TO GET ITS START AND END
async def calculateGap(robot):

    return gapPositions

# === ADJUST COURSE TO ENSURE MOVING IN A STRAIGHT LINE
async def courseCorrect():
    pass

# === MOVE FROM THE END OF THE COURSE TO THE LARGEST GAP
async def park():
    pass

# ==========================================================

# Main function

@event(robot.when_play)
async def selfParking(robot):
    pass


# start the robot
robot.play()
