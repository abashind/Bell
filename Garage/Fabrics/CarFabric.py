import random
from Properties.Colors import Colors
from Properties.SteeringWheelPositions import SteeringWheelPositions
from Models.Car import Car
from Fabrics.BaseFabric import BaseFabric


class CarFabric(BaseFabric):

    type = 'Motorcycle'

    @staticmethod
    def get_one(weight: int, color: Colors, motor_pwr: int, accel: int, st_wheel_pos: SteeringWheelPositions):
        car = Car(weight, color)
        car.motor_power = motor_pwr
        car.acceleration = accel
        car.st_wheel_pos = st_wheel_pos
        return car

    @staticmethod
    def get_rnd_one():
        weight = random.randint(600, 4000)
        color = random.choice(list(Colors))
        motor_pwr = random.randint(50, 1000)
        accel = random.randint(3, 30)
        st_wheel_pos = random.choice(list(SteeringWheelPositions))
        return CarFabric.get_one(weight, color, motor_pwr, accel, st_wheel_pos)
