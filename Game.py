import copy
import math
import time
import random
import numpy as np
import pygame
from pygame.locals import (K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP,
                           KEYDOWN, USEREVENT, K_w, K_a, K_s, K_d)
from typing import Iterable

from Car import CarSprite
from Trophy import TrophySprite
from Wall import WallSprite
from Dynamic import Dynamic


class Game:
    WIN_SCORE = 10
    TIME_LIMIT = 480 # seconds

    def __init__(self, walls, trophies, parkings,
                 crosswalks, traffic_signs, schoolzone, cars: Iterable[CarSprite], databases):
        self.init_args = \
            [
                copy.copy(walls),
                copy.copy(trophies),
                copy.copy(parkings),
                copy.copy(crosswalks),
                copy.copy(cars),
                copy.copy(databases)
            ]
        pygame.init()
        self.cars = cars
        self.screen = pygame.display.set_mode((1200, 800))
        self.traffic_signs = traffic_signs
        self.school_zones = schoolzone
        self.clock = pygame.time.Clock()
        font = pygame.font.Font(None, 75)
        self.font = pygame.font.SysFont("notosansmonocjkkrregular", 50, True, False)
        self.score_font = pygame.font.SysFont("notosansmonocjkkrregular", 100, True, False)
        self.win_font = pygame.font.Font(None, 50)
        self.win_condition = None
        self.win_text = font.render('', True, (0, 255, 0))
        self.loss_text = font.render('', True, (255, 0, 0))
        self.wall_group = pygame.sprite.RenderPlain(*walls)
        self.trophy_group = pygame.sprite.RenderPlain(*trophies)
        self.crosswalk_group = pygame.sprite.RenderPlain(*crosswalks)
        self.car_group = pygame.sprite.RenderPlain(*cars)
        self.parkings = parkings
        self.rect = self.screen.get_rect()
        self.stop = False
        self.car_update = True
        self.databases = databases
        self.dynamic_flag = False
        self.dynamic = Dynamic('images/bird.png', (-100, 0))
        self.dynamic_group = pygame.sprite.RenderPlain(self.dynamic)

        self.event_keys = [K_RIGHT, K_LEFT, K_UP, K_DOWN]
        if len(cars) == 2:
            self.event_keys.extend([K_d, K_a, K_w, K_s])

        self.trophy_count = [0, 0]
        self.timeout_flag = False
        self.initial_time = None
        self.seconds = 0
        self.trophy_respawn_time = 0

    def run(self, auto=False):
        # seconds = 0
        record = False
        temp_v2x_data = []
        crashed_cars = []
        self.initial_time = time.time()
        while True:
            deltat = self.clock.tick(30)
            self.seconds = time.time() - self.initial_time

            if self.seconds >= Game.TIME_LIMIT:
                self.timeout_flag = True

            if self.win_condition is not None and not record:
                record = True
                result = self.seconds
                print("Total time:", result)

            if self.timeout_flag:
                print("Timeout!")
                print(f"Player 1 : {self.trophy_count[0]}\nPlayer 2 : {self.trophy_count[1]}")
                if self.trophy_count[0] > self.trophy_count[1]:
                    print("Player 1 wins!")
                elif self.trophy_count[0] < self.trophy_count[1]:
                    print("Player 2 wins!")
                else:
                    print("draw!")
                break

            # Car control
            events = pygame.event.get()

            if auto:
                for user_car in self.cars:
                    user_car.k_right = user_car.k_left = user_car.k_up = user_car.k_down = 0

            for event in events:
                if not hasattr(event, 'key') or \
                        (auto and
                         event.type != USEREVENT and
                         event.key in self.event_keys):
                    continue

                if auto:
                    if self.win_condition is None and event.key in self.event_keys:
                        car_idx = event.key in self.event_keys[4:]  # if 0~3(True): 1st car, 4~7, 2nd car(False)
                        key_idx = self.event_keys.index(event.key)
                        if key_idx % 4 == 0:
                            if self.cars[car_idx].k_right > -8:
                                self.cars[car_idx].k_right += -1
                        elif key_idx % 4 == 1:
                            if self.cars[car_idx].k_left < 8:
                                self.cars[car_idx].k_left += 1
                        elif key_idx % 4 == 2:
                            if self.cars[car_idx].k_up < 5:
                                self.cars[car_idx].k_up += 1
                        elif key_idx % 4 == 3:
                            if self.cars[car_idx].k_down > -5:
                                self.cars[car_idx].k_down += -1
                        elif event.key == K_ESCAPE:
                            self.databases[car_idx].stop = True
                else:
                    down = event.type == KEYDOWN
                    if self.win_condition is None and event.key in self.event_keys:
                        car_idx = event.key in self.event_keys[4:]  # if 0~3(True): 1st car, 4~7, 2nd car(False)
                        key_idx = self.event_keys.index(event.key)
                        if key_idx % 4 == 0:
                            self.cars[car_idx].k_right = down * -5
                        elif key_idx % 4 == 1:
                            self.cars[car_idx].k_left = down * 5
                        elif key_idx % 4 == 2:
                            self.cars[car_idx].k_up = down * 2
                        elif key_idx % 4 == 3:
                            self.cars[car_idx].k_down = down * -2
                        elif event.key == K_ESCAPE:
                            self.databases[car_idx].stop = True

                if self.win_condition is not None and \
                        (event.key == K_ESCAPE and event.key == K_SPACE):
                    print(result)
                    time.sleep(0.1)
                    for database in self.databases:
                        database.stop = True

            if True in [database.stop for database in self.databases]:
                break

            for crashed_car_idx in crashed_cars:
                user_car = self.cars[crashed_car_idx - 1]
                if user_car.last_collision + 2 <= self.seconds:
                    user_car.respawn()
                    user_car.MAX_FORWARD_SPEED = 15
                    user_car.MAX_REVERSE_SPEED = 15

            # RENDERING
            self.screen.fill((0, 0, 0))
            if self.car_update:
                self.car_group.update(deltat)

            collisions = pygame.sprite.groupcollide(
                self.car_group, self.wall_group, False, False, collided=pygame.sprite.collide_rect_ratio(0.95))
            self.score_board()
            # 벽과 충돌했을 때
            if collisions != {}:
                # self.car_update = False
                # self.win_condition = False
                crashed_cars = [user_car.player for user_car in list(collisions.keys())]
                for crashed_car_idx in crashed_cars:
                    user_car = self.cars[crashed_car_idx - 1]

                    if user_car.last_collision < 999:
                        continue
                    user_car.MAX_FORWARD_SPEED = 0
                    user_car.MAX_REVERSE_SPEED = 0
                    user_car.k_right = 0
                    user_car.k_left = 0
                    user_car.crash(self.seconds, pygame.image.load('images/collision.png'))

                collisions = {}

            crosswalk_collisions = pygame.sprite.groupcollide(
                self.car_group,
                self.crosswalk_group,
                False,
                False,
                collided=None
            )

            trophy_collision = pygame.sprite.groupcollide(
                self.car_group,
                self.trophy_group,
                False,
                False
            )

            for user_car, colled_crosswalk in crosswalk_collisions.items():
                if colled_crosswalk[0].color == "red":
                    crashed_cars = [user_car.player for user_car in list(crosswalk_collisions.keys())]
                    for crashed_car_idx in crashed_cars:
                        user_car = self.cars[crashed_car_idx - 1]

                        if user_car.last_collision < 999:
                            continue
                        user_car.MAX_FORWARD_SPEED = 0
                        user_car.MAX_REVERSE_SPEED = 0
                        user_car.k_right = 0
                        user_car.k_left = 0
                        user_car.crash(self.seconds, pygame.image.load('images/collision.png'))

                    crosswalk_collisions = {}

            # trophy 먹었을 때
            if trophy_collision != {}:
                trophy_collision_car_idx = list(trophy_collision.keys())[0].player
                self.trophy_count[trophy_collision_car_idx - 1] += 1
                print(f"Player {trophy_collision_car_idx} won the trophy")
                print(self.trophy_count)

                if self.WIN_SCORE in self.trophy_count:
                    score_max = max(self.trophy_count)
                    win_player = [player for player, score in enumerate(self.trophy_count) if score == score_max][0] + 1
                    print(f"Player {win_player} wins!")
                    break

                # trophy respawn
                self.trophy_group.sprites()[0].trophy_respawn()
                self.trophy_respawn_time = time.time()

            # 1분 동안 trophy 아무도 못먹으면 trophy respawn
            if time.time() - self.trophy_respawn_time > 120:
                self.trophy_group.sprites()[0].trophy_respawn()
                self.trophy_respawn_time = time.time()

            # print(temp_v2x_data)
            temp_v2x_data.clear()
            temp_v2x_data.append((self.trophy_group.sprites()[0].data))

            for parking in self.parkings:
                for user_car in self.cars:
                    parking.update(user_car)
                    parking.draw(self.screen)
                    if parking.is_in_range(user_car):
                        temp_v2x_data.append((id(parking), parking.data))

            self.wall_group.update()
            self.crosswalk_group.update()
            self.crosswalk_group.draw(self.screen)

            for crosswalk in self.crosswalk_group:
                for user_car in self.cars:
                    if crosswalk.is_in_range(user_car):
                        temp_v2x_data.append((id(crosswalk), crosswalk.data))
            new_dict = dict()

            for traffic_sign in self.traffic_signs:
                traffic_sign.draw(self.screen)
                temp_v2x_data.append((id(traffic_sign), traffic_sign.data))

            for school_zone in self.school_zones:
                for user_car in self.cars:
                    check_speed = school_zone.update(user_car)
                    if check_speed is False:
                        self.car_update = False
                        self.win_condition = False

                        user_car.image = pygame.image.load('images/collision.png')
                        user_car.MAX_FORWARD_SPEED = 0
                        user_car.MAX_REVERSE_SPEED = 0
                        user_car.k_right = 0
                        user_car.k_left = 0

                    school_zone.draw(self.screen)
                    temp_v2x_data.append((id(school_zone), school_zone.data))

            for v2x_data in temp_v2x_data:
                key, value = v2x_data
                new_dict[key] = value
            for database in self.databases:
                database.v2x_data = new_dict
            # print(self.database.v2x_data)
            self.wall_group.draw(self.screen)
            self.car_group.draw(self.screen)
            self.trophy_group.draw(self.screen)

            # Dynamic Obstacle
            dynamic_collisions = pygame.sprite.groupcollide(
                self.car_group, self.dynamic_group, False, False, collided=pygame.sprite.collide_rect_ratio(1))
            self.dynamic_group.update(dynamic_collisions)
            if dynamic_collisions != {}:
                self.car_update = False
                self.win_condition = False

                crashed_cars = [user_car.player for user_car in list(collisions.keys())]
                for crashed_car_idx in crashed_cars:
                    user_car = self.cars[crashed_car_idx - 1]
                    user_car.image = pygame.image.load('images/collision.png')
                    user_car.MAX_FORWARD_SPEED = 0
                    user_car.MAX_REVERSE_SPEED = 0
                    user_car.k_right = 0
                    user_car.k_left = 0

            if self.school_zones != []:
                for user_car in self.cars:
                    if (250 <= user_car.position[0] < 250 + 550) and (350 <= user_car.position[1] < 350 + 100) & (
                            self.dynamic_flag == False):
                        if self.dynamic.x == -100:
                            self.dynamic.x = random.randint(250, 600)
                        if 0 <= user_car.position[0] - self.dynamic.x <= 100:
                            if self.dynamic.time == 0:
                                self.dynamic.time = time.time()
                            if time.time() - self.dynamic.time < 5:
                                self.dynamic.draw(self.screen)
                            else:
                                self.dynamic.x = -100

            # Counter Render
            pygame.display.flip()

            self.make_lidar_data()

    # Score Board
    def score_board(self, x=1030, y=140):
        PURPLE = (123, 88, 254)
        GREEN = (30, 180, 0)

        player1 = self.font.render("Player 1", True, GREEN)
        self.screen.blit(player1, [x, y])

        score1 = self.score_font.render(str(self.trophy_count[0]), True, GREEN)
        self.screen.blit(score1, [1080, y + 100])
        score2 = self.score_font.render(str(self.trophy_count[1]), True, PURPLE)
        self.screen.blit(score2, [1080, y + 220])

        player2 = self.font.render("Player 2", True, PURPLE)
        self.screen.blit(player2, [x, y + 340])

        time_format = self.time_format()
        time = self.font.render(time_format, True, (255, 255, 255))
        self.screen.blit(time, [x, 700])

    def time_format(self):
        seconds = self.seconds
        second = 0
        millisecond = 0
        minute = int(seconds//60)
        second = str(int(seconds-60*minute))
        temp = round(seconds-60*minute, 3)*1000
        millisecond = str(int(temp%1000))
        time_format = f"{minute}:{second}:{millisecond}"
        return time_format

    def again(self, auto):
        self.__init__(*self.init_args)
        self.run(auto=auto)

    def make_lidar_data(self):
        for idx, database in enumerate(self.databases):
            # lidar_data = np.zeros((360))
            lidar_data = []
            L = 100
            array = pygame.surfarray.array3d(self.screen)

            user_car = database.car
            x, y = user_car.position

            car_direction = user_car.direction % 360

            lidar_x = int(x - 20 * math.sin(math.pi * car_direction / 180))
            lidar_y = int(y - 20 * math.cos(math.pi * car_direction / 180))

            for direction in range(-90 + car_direction, 270 + car_direction):
                direction = direction % 360

                x, y = lidar_x, lidar_y
                m = math.tan(math.pi * direction / 180)
                if direction == 0:
                    while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                        x = x
                        y -= 1
                        try:
                            if (array[int(x)][int(y)] == 255).all():
                                break
                        except IndexError:
                            break
                elif (0 < direction < 45) or (315 <= direction < 360):
                    while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                        y -= 1
                        x = (m) * (y - lidar_y) + lidar_x
                        try:
                            if (array[int(x)][int(y)] == 255).all():
                                break
                        except IndexError:
                            break
                elif (45 <= direction < 90) or (90 < direction < 135):
                    while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                        x -= 1
                        y = (1 / m) * (x - lidar_x) + lidar_y
                        try:
                            if (array[int(x)][int(y)] == 255).all():
                                break
                        except IndexError:
                            break
                elif direction == 90:
                    while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                        x -= 1
                        y = y
                        try:
                            if (array[int(x)][int(y)] == 255).all():
                                break
                        except IndexError:
                            break
                elif (135 <= direction < 180) or (180 < direction < 225):
                    while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                        y += 1
                        x = (m) * (y - lidar_y) + lidar_x
                        try:
                            if (array[int(x)][int(y)] == 255).all():
                                break
                        except IndexError:
                            break
                elif direction == 180:
                    while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                        x = x
                        y += 1
                        try:
                            if (array[int(x)][int(y)] == 255).all():
                                break
                        except IndexError:
                            break
                elif (225 <= direction < 270) or (270 < direction < 315):
                    while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                        x += 1
                        y = (1 / m) * (x - lidar_x) + lidar_y
                        try:
                            if (array[int(x)][int(y)] == 255).all():
                                break
                        except IndexError:
                            break
                elif direction == 270:
                    while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                        x += 1
                        y = y
                        try:
                            if (array[int(x)][int(y)] == 255).all():
                                break
                        except IndexError:
                            break
                else:
                    print(f"Uncatched Case: {direction}")

                length = math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2)
                if length > L:
                    length = L

                # lidar_data[direction] = length
                lidar_data.append(length)

            # lidar_data = np.concatenate(
            #     (lidar_data[-90:], lidar_data[:270]), axis=None
            # )
            # lidar_data = np.concatenate(
            #     (lidar_data, lidar_data), axis=None
            # )
            # lidar_data = \
            #     lidar_data[user_car.direction % 360:
            #                user_car.direction % 360 + 360]
            database.lidar.data = lidar_data


if __name__ == "__main__":
    walls = [
        WallSprite((512, 2.5), 1024, 5),
        WallSprite((512, 765.5), 1024, 5),
        WallSprite((2.5, 384), 5, 768),
        WallSprite((1021.5, 384), 5, 768)
    ]
    trophies = [
        TrophySprite((300, 50))
    ]
    car = CarSprite('images/car.png', (50, 700))
    g = Game(walls, trophies, car)
    g.run()
