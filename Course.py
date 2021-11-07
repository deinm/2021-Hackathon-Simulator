from Wall import WallSprite, DynamicWallSprite, invisible_WallSprite
from Car import CarSprite
from Trophy import TrophySprite
from Parking import Parking
from Crosswalk import Crosswalk
from Schoolzone import Schoolzone
from TrafficSign import Right, Left

import random
import numpy as np, cv2



Map1 = (
    [
        WallSprite((500, 0), 1000, 4),  # Boundary box
        WallSprite((500, 800), 1000, 4),
        WallSprite((0, 400), 4, 800),
        WallSprite((1000, 400), 4, 800),
    

        WallSprite((170,210), 200, 4),
        WallSprite((370,710), 200, 4),
        WallSprite((570,210), 200, 4),
        WallSprite((770,710), 200, 4),
        WallSprite((70,460), 4, 500),   
        WallSprite((270,460), 4, 500),
        WallSprite((470,460), 4, 500),
        WallSprite((670,460), 4, 500),
        WallSprite((870,460), 4, 500),

        # WallSprite((750,225), 4, 250),
        # WallSprite((688,350), 125, 4),
        
        DynamicWallSprite((200, 150), (200, 65), 4, 125),

    ],
    [
        TrophySprite()
    ],
    [

    ],
    [
        
    ],
    [

    ],
    [

    ],
    [
        CarSprite('images/car.png', (50, 50), 180, player=1),
    ],
)