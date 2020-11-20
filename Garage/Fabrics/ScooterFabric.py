import random
from Properties.Colors import Colors
from Models.Scooter import Scooter
from Fabrics.BaseFabric import BaseFabric


class ScooterFabric(BaseFabric):

    @staticmethod
    def get_one(weight: int, color: Colors):
        scooter = Scooter(weight, color)
        return scooter

    @staticmethod
    def get_rnd_one():
        weight = random.randint(10, 30)
        color = random.choice(list(Colors))
        return ScooterFabric.get_one(weight, color)
