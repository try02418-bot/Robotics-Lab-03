from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

import math as m

# robot is the instance of the robot that will allow us to call its methods and to define events with the @event decorator.
robot = Create3(Bluetooth("KIRITO-BOT"))  # Will connect to the first robot found.

HAS_COLLIDED = False
SENSOR2CHECK = 0
ARRIVAL_THRESHOLD = 5

# Implementation for fail-safe robots
# EITHER BUTTON
@event(robot.when_touched, [True, True])  # User buttons: [(.), (..)]
async def when_either_button_touched(robot):
    pass

# EITHER BUMPER
@event(robot.when_bumped, [True, True])  # [left, right]
async def when_either_bumped(robot):
    pass

# ==========================================================

# Helper Functions

# === FIND WHICH SIDE THE WALLS ARE COMING FROM
async def findWall():
    pass

# === MOVE UNTIL WE FIND A GAP, TRACK LARGEST
async def findGaps():
    pass

# === MOVE ALONG A FOUND GAP TO GET ITS START AND END
async def calculateGap():
    pass

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
