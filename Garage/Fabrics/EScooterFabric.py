import random
from Properties.Colors import Colors
from Models.EScooter import EScooter
from Fabrics.BaseFabric import BaseFabric


class EScooterFabric(BaseFabric):

    @staticmethod
    def get_one(weight: int, color: Colors, emotor_pow: int):
        escooter = EScooter(weight, color)
        escooter.emotor_power = emotor_pow
        return escooter

    @staticmethod
    def get_rnd_one():
        weight = random.randint(10, 30)
        color = random.choice(list(Colors))
        emotor_pow = random.randint(1, 50)
        return EScooterFabric.get_one(weight, color, emotor_pow)
