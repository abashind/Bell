import random
from Properties.Colors import Colors
from Models.Motorcycle import Motorcycle
from Fabrics.BaseFabric import BaseFabric


class MotorcycleFabric(BaseFabric):

    type = 'Motorcycle'

    @staticmethod
    def get_one(weight: int, color: Colors, motor_pwr: int, accel: int):
        mbike = Motorcycle(weight, color)
        mbike.motor_power = motor_pwr
        mbike.acceleration = accel
        return mbike

    @staticmethod
    def get_rnd_one():
        weight = random.randint(70, 450)
        color = random.choice(list(Colors))
        motor_pwr = random.randint(5, 200)
        accel = random.randint(3, 30)
        return MotorcycleFabric.get_one(weight, color, motor_pwr, accel)
