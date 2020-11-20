import random
from Properties.Colors import Colors
from Models.Bicycle import Bicycle
from Fabrics.BaseFabric import BaseFabric


class BicycleFabric(BaseFabric):

    @staticmethod
    def get_one(weight: int, color: Colors, num_of_speeds: int):
        bicycle = Bicycle(weight, color)
        bicycle.number_of_speeds = num_of_speeds
        return bicycle

    @staticmethod
    def get_rnd_one():
        weight = random.randint(10, 30)
        color = random.choice(list(Colors))
        num_of_speeds = random.randint(1, 50)
        return BicycleFabric.get_one(weight, color, num_of_speeds)
