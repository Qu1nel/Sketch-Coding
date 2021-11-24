from math import sin, cos
from typing import Tuple

import pygame as pg
from numba import njit

from map import world_map
from settings import *


@njit(fastmath=True, nopython=True)
def one(cur_angle):
    sin_a = sin(cur_angle)
    cos_a = cos(cur_angle)
    return sin_a, cos_a


@njit(fastmath=True, nopython=True)
def two(xO, yO, depth, cos_a, sin_a):
    return xO + depth * cos_a, yO + depth * sin_a


@njit(fastmath=True, nopython=True)
def three(depth, angle, cur_angle, PROJ_RATIO):
    depth = depth * cos(angle - cur_angle)
    proj_height = PROJ_RATIO / depth
    c = 255 / (1 + depth * depth * 0.0002)
    return depth, proj_height, c


def ray_casting(surface, pos: Tuple, angle: float):
    cur_angle = angle - HALF_FOV
    xO, yO = pos
    for ray in range(NUM_RAY):
        sin_a, cos_a = one(cur_angle)
        for depth in range(MAX_DEPTH):
            x, y = two(xO, yO, depth, cos_a, sin_a)
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                depth, proj_height, c = three(depth, angle, cur_angle, PROJ_RATIO)
                color = (c, c, c)
                pg.draw.rect(surface, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                break
        cur_angle += DELTA_ANGLE
