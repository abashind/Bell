from Models.BaseVehicle import BaseVehicle


class EScooter(BaseVehicle):
    def __init__(self, weight, color):
        super().__init__(weight, color)

    @property
    def emotor_power(self):
        if self.__emotor_power is not None:
            return self.__emotor_power
        else:
            raise ValueError("Value for emotor_power wasn't assigned.")

    @emotor_power.setter
    def emotor_power(self, value):
        if value > 0:
            self.__emotor_power = value
        else:
            raise AttributeError("Power must be more than 0.")


    def print_info(self):
        super().print_info()
        print(f"    Emotor power(hp): {self.__emotor_power}")