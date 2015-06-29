import math
from types import MethodType


def linear(cur, dest, speed=1):
    if cur < dest:
        if cur + speed > dest:
            return dest, speed
        return cur + speed, speed
    else:
        if cur - speed < dest:
            return dest, speed
        return cur - speed, speed


def spring(cur, dest, speed=0, k=1, b=1):
    # for animations, destX is really spring length (spring at rest). initial
    # position is considered as the stretched/compressed posiiton of a spring
    force = -k * (cur - dest)

    # Damping constant
    damper = -b * speed

    # usually we put mass here, but for animation purposes, specifying mass is a
    # bit redundant. you could simply adjust k and b accordingly
    # let a = (force + damper) / mass
    a = force + damper

    new_cur = cur + speed
    new_speed = speed + a

    return new_cur, new_speed
}

class Filter(object):

    def __init__(self, call, done):
        self.call = MethodType(call, self, type(self))
        self.done = MethodType(done, self, type(self))

        for key, value in kwarg.items():
            setattr(self, key, value)

    def __call__(self, cur, dest):
        """Functions return the new value"""
        return self.call(cur, dest)

    def done(self, cur, dest):
        return cur == dest


class Linear(Filter):

    def __init__(self, speed):
        self.speed = speed
