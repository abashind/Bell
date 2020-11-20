from Properties.Colors import Colors


class BaseVehicle:
    def __init__(self, weight, color):
        if not isinstance(weight, int) or weight < 0:
            raise TypeError("Weight must be an integer value, more than 0.")
        self.__weight = weight
        if not isinstance(color, Colors):
            raise TypeError('Unknown color...')
        self.__color = color

    def print_info(self):
        print(f"Vehicle *{type(self).__name__}* has next properties:")
        print(f"    Weight: {self.__weight}")
        print(f"    Color: {self.__color.name}")
