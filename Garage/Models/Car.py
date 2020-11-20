from Models.Motorcycle import Motorcycle
from Properties.SteeringWheelPositions import SteeringWheelPositions


class Car(Motorcycle):
    def __init__(self, weight, color):
        super().__init__(weight, color)

    @property
    def st_wheel_pos(self):
        if self.__st_wheel_pos is not None:
            return self.__st_wheel_pos
        else:
            raise AttributeError("Value for st_wheel_pos wasn't assigned.")

    @st_wheel_pos.setter
    def st_wheel_pos(self, value):
        if isinstance(value, SteeringWheelPositions):
            self.__st_wheel_pos = value
        else:
            raise TypeError("Unknown steering wheel position...")

    def print_info(self):
        super().print_info()
        print(f"    Steering wheel position is: {self.__st_wheel_pos.name}")
