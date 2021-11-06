import argparse
import os
import threading

import pygame

from Brain1 import Brain1
from Brain2 import Brain2
from Control import Control
from Course import Map1, Map2, Map3
from Database import Database
from Game import Game
from LiDAR import LiDAR


def main(auto):
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500, 30)
    # _ = (Map1, Map2, Map3)
    walls, trophies, parkings, crosswalks, traffic_signs, schoolzone, cars = Map1
    lidar = LiDAR()

    # Get LiDAR data, Set Control data
    brains = []
    databases = []
    # Get Control data Set LiDAR data
    for idx, car in enumerate(cars):
        control = Control(player=idx+1)
        database = Database(lidar, control, car)
        databases.append(database)

    brains.append(Brain1(databases[0]))
    brains.append(Brain2(databases[1]))

    game = Game(walls, trophies, parkings,
                crosswalks, traffic_signs, schoolzone, cars, databases)


    if auto:
        brain_thread1 = threading.Thread(target=brains[0].run,)
        brain_thread2 = threading.Thread(target=brains[1].run,)
        brain_thread1.start()
        brain_thread2.start()
    game.run(auto=auto)
    pygame.quit()

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "--auto",
            help="Do not use your keyboard command,\
                 but use pre-defined brain's command.",
            action="store_true", default=False
        )
    args = parser.parse_args()
    main(args.auto)
