class Vehicle:
    def __init__(self, speed):
        if speed > 2 or speed <= 0:
            raise ValueError('Speed can be only in (0,2]')
        self.speed = speed

    def get_speed(self):
        return self.speed

