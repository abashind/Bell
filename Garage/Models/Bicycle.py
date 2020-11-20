from Models.BaseVehicle import BaseVehicle


class Bicycle(BaseVehicle):
    def __init__(self, weight, color):
        super().__init__(weight, color)

    @property
    def number_of_speeds(self):
        if self.__number_of_speeds is not None:
            return self.__number_of_speeds
        else:
            raise ValueError("Value for number_of_speeds wasn't assigned.")

    @number_of_speeds.setter
    def number_of_speeds(self, value):
        if value > 0:
            self.__number_of_speeds = value
        else:
            raise AttributeError("Number_of_speeds must be more than 0.")

    def print_info(self):
        super().print_info()
        print(f"    Number of speeds: {self.__number_of_speeds}")
