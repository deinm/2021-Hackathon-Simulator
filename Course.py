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

        WallSprite((100, 62), 4, 124),
        WallSprite((100, 738), 4, 124),

        WallSprite((100, 210), 200, 4),
        
        
        

        WallSprite((813,100), 124, 4),
        WallSprite((875,450), 4, 500),
        WallSprite((750,225), 4, 250),
        WallSprite((813,500), 125, 100),
        WallSprite((752,725), 4, 150),
        WallSprite((688,350), 125, 4),
        WallSprite((650,625), 4, 150),


        WallSprite((100, 590), 200, 4),
        WallSprite((202, 325), 204, 50),
        WallSprite((202, 475), 204, 50),
        WallSprite((302, 200), 4, 200),
        WallSprite((302, 600), 4, 200),
        WallSprite((350, 98), 100, 4),
        WallSprite((402, 625), 4, 350),
        WallSprite((525, 450), 250, 4),
        WallSprite((450, 275), 100, 150),
        WallSprite((498, 100), 4, 200),

        WallSprite((550, 675), 4, 250),
        WallSprite((625, 125), 4, 250),

        DynamicWallSprite((200, 150), (200, 65), 4, 125),
        DynamicWallSprite((200, 650), (200, 738), 4, 125),
        DynamicWallSprite((650, 500), (650, 600), 4, 100),
    ],
    [
        TrophySprite()
    ],
    [

    ],
    [
        Crosswalk((350, 450), 100, 4, interval=random.randint(20, 40), phase=0),
        Crosswalk((100, 400), 4, 100, interval=random.randint(20, 40), phase=8),
        Crosswalk((685, 180), 125, 4, interval=random.randint(20, 40), phase=24),
        Crosswalk((940, 600), 125, 4, interval=random.randint(20, 40), phase=24),
    ],
    [

    ],
    [

    ],
    [
        CarSprite('images/car.png', (50, 50), 180, player=1),
    ],
)