class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.car = {
            1 : big,
            2 : medium,
            3 : small
        }

    def addCar(self, carType):
        if self.car[carType] > 0:
            self.car[carType] -= 1
            return True
        else:
            return False