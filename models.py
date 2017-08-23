from random import randrange
import numpy

class Cell:
    x = 0
    y = 0
    z = 0
    type = ''
    destroyed = False

    def __init__(self):
        self.x = randrange(1,5000)
        self.y = randrange(1,5000)
        self.z = randrange(1,5000)


    def set_type(self,typ):
        self.type = typ

    def get_destroyed(self):
        self.destroyed = True

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_type(self):
        return self.type

class Virus(Cell):

    def do_nothing(self):
        pass
    def destroy(self):
        pass
    def move(self):
        pass

class Activity:
    pass
