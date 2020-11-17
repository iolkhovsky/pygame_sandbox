import math


class BoatModel:

    def __init__(self, init_x, init_y, init_angle):
        self.pos = (init_x, init_y)
        self.angle = init_angle
        self.power = 0.0
        self.K_fwd = 0.000001
        self.K_bck = 0.0000001
        self.max_power_acceleration = 0.5
        self.cur_v = 0
        self.m = 1.

    def update(self, power):
        a = 0.
        if self.cur_v * power > 0:
            a = (power * self.max_power_acceleration - self.K_fwd * pow(self.cur_v, 2)) / self.m
        else:
            a = (power * self.max_power_acceleration - self.K_fwd * pow(self.cur_v, 2)) / self.m
        self.cur_v += a
        x, y = self.pos
        dx = self.cur_v * math.cos(math.radians(self.angle))
        dy = self.cur_v * math.sin(math.radians(self.angle))
        self.pos = x + dx, y + dy

