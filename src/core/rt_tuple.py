import numpy as np

class RtTuple(object):
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def is_vector(self):
        if self.w != 1.0:
            return False
        return True