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


def main(auto, num_player):
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500, 30)
    # _ = (Map1, Map2, Map3)
    walls, trophies, parkings, crosswalks, traffic_signs, schoolzone, cars = Map1

    if len(cars) != num_player:
        cars = cars[:num_player]

    # Get LiDAR data, Set Control data
    brains = []
    databases = []
    # Get Control data Set LiDAR data
    for idx, car in enumerate(cars):
        control = Control(player=car.player)
        database = Database(LiDAR(), control, car)
        databases.append(database)

        if car.player == 1:
            brains.append(Brain1(database))
        elif car.player == 2:
            brains.append(Brain2(database))

    game = Game(walls, trophies, parkings,
                crosswalks, traffic_signs, schoolzone, cars, databases)

    if auto:
        for brain in brains:
            brain_thread = threading.Thread(target=brain.run)
            brain_thread.start()
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
    parser.add_argument(
            "--num_player",
            help="Define the number of players. "
                 "The max # of player is 2.",
            action="store_true", default=2
        )
    args = parser.parse_args()
    main(args.auto, args.num_player)
