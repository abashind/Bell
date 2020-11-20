from Models.BaseVehicle import BaseVehicle


class Scooter(BaseVehicle):
    def __init__(self, weight, color):
        super().__init__(weight, color)
