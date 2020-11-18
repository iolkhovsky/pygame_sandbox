import math


"""
Equations of motion:
- vector form: 
    Fmotor + Fwat_res = m * a
- 1d projection: 
    Fmotor - sign(v) * Kres * v^2 = m * (dv/dt)
    dv = (Fmotor - sign(v) * Kres * v2^2) * dt / m
"""


class BoatModel:

    def __init__(self, init_position, init_azimuth, k_fwd=1., k_back=10., motor_power=20., mass=2., J=10.):
        self._x, self._y = init_position
        self._azimuth = init_azimuth
        self._k_res_forward = k_fwd
        self._k_res_back = k_back
        self._k_rudder = k_fwd
        self._k_rotation = 1000
        self._motor_power = motor_power
        self._m = mass
        self._inert_mom = J
        self._speed = 0
        self._acceleration = 0
        self._rotation_speed = 0
        self._motor_position_vector = 0.5

    def __str__(self):
        return f"Boat model, m={self._m}, motor power={self._motor_power}, water resistance={self._k_res_forward}"

    def update(self, relative_power, steering, dt):
        steering = max(min(90, steering), -90)
        relative_power = max(min(1.0, relative_power), -1.0)
        k_body = self._k_res_forward if self._speed >= 0 else self._k_res_back
        k_rudder = self._k_rudder * abs(math.sin(math.radians(steering)))
        k_res = k_body + k_rudder
        speed_sign = 1 if self._speed >= 0 else -1

        resistance_force = k_res * pow(self._speed, 2)
        self._acceleration = (relative_power * self._motor_power -
                              speed_sign * resistance_force) * dt / self._m
        self._speed += self._acceleration

        rudder_sign = 1 if steering >= 0 else -1
        rotation_sign = 1 if self._rotation_speed >= 0 else -1
        rudder_resistance = k_rudder * math.pow(self._speed, 2)
        rotation_force = rudder_resistance * abs(math.cos(math.radians(steering)))

        rotation_momentum = -1 * rudder_sign * rotation_force * self._motor_position_vector
        resistance_momentum = -1 * rotation_sign * self._k_rotation * math.pow(self._rotation_speed, 2)

        rotation_accel = (rotation_momentum + resistance_momentum) * dt / self._inert_mom
        self._rotation_speed += rotation_accel

        self._azimuth += math.degrees(self._rotation_speed)
        while self._azimuth > 180:
            self._azimuth -= 360.
        while self._azimuth < -180:
            self._azimuth += 360.

        dx = self._speed * math.cos(math.radians(self._azimuth))
        dy = self._speed * math.sin(math.radians(self._azimuth))
        self._x += dx
        self._y += dy
        return (self._x, self._y), self._speed, self._acceleration, self._azimuth
