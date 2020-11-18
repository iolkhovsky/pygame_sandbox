import math


class BoatModel:

    def __init__(self, init_x, init_y, init_angle):
        self.pos = (init_x, init_y)
        self.angle = init_angle
        self.power = 0.0
        self.K_fwd = 1.
        self.K_bck = 10.
        self.max_power_acceleration = 5.
        self.cur_v = 0
        self.cur_a = 0
        self.m = 2.

    def update(self, power, dt):
        k_res = self.K_fwd if self.cur_v >=0 else self.K_bck
        if power != 0:
            if power > 0:
                if self.cur_v >= 0:
                    self.cur_a = (power * self.max_power_acceleration - k_res * pow(self.cur_v, 2)) / self.m
                else:
                    self.cur_a = (power * self.max_power_acceleration + k_res * pow(self.cur_v, 2)) / self.m
            else:
                if self.cur_v >= 0:
                    self.cur_a = -1. * (abs(power) * self.max_power_acceleration + k_res * pow(self.cur_v, 2)) / self.m
                else:
                    self.cur_a = -1 * (abs(power) * self.max_power_acceleration - k_res * pow(self.cur_v, 2)) / self.m
        else:
            if self.cur_v != 0:
                if self.cur_v > 0:
                    self.cur_a = -1. * k_res * pow(self.cur_v, 2) / self.m
                else:
                    self.cur_a = k_res * pow(self.cur_v, 2) / self.m
            else:
                self.cur_a = 0.

        self.cur_v += self.cur_a * dt
        x, y = self.pos
        dx = self.cur_v * math.cos(math.radians(self.angle))
        dy = self.cur_v * math.sin(math.radians(self.angle))
        self.pos = x + dx, y + dy

