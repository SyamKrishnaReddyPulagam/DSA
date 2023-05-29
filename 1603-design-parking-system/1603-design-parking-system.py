class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.a=[big,medium,small]
    def addCar(self, carType):
        self.a[carType-1] -=1
        return self.a[carType-1]>=0
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
