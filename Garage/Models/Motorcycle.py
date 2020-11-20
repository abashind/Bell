from Models.BaseVehicle import BaseVehicle


class Motorcycle(BaseVehicle):
    def __init__(self, weight, color):
        super().__init__(weight, color)

    @property
    def motor_power(self):
        if self.__motor_power is not None:
            return self.__motor_power
        else:
            raise AttributeError("Value for motor_power wasn't assigned.")

    @motor_power.setter
    def motor_power(self, value):
        if value > 0:
            self.__motor_power = value
        else:
            raise AttributeError("Power must be more than 0.")

    @property
    def acceleration(self):
        if self.__acceleration is not None:
            return self.__acceleration
        else:
            raise AttributeError("Value for acceleration wasn't assigned.")

    @acceleration.setter
    def acceleration(self, value):
        if value > 0:
            self.__acceleration = value
        else:
            raise AttributeError("Acceleration must be more than 0.")

    def print_info(self):
        super().print_info()
        print(f"    Motor power(hp): {self.__motor_power}")
        print(f"    Acceleration 0-100km/h, sec : {self.__acceleration}")
