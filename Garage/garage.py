# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from Fabrics import *


def rnd_0_2():
    return random.randint(0, 2)


if __name__ == '__main__':

    garage = []
    garage.extend(ScooterFabric.get_number_of_rnd(rnd_0_2()))
    garage.extend(EScooterFabric.get_number_of_rnd(rnd_0_2()))
    garage.extend(BicycleFabric.get_number_of_rnd(rnd_0_2()))
    garage.extend(MotorcycleFabric.get_number_of_rnd(rnd_0_2()))
    cars = list(CarFabric.get_number_of_rnd(rnd_0_2()))
    garage.extend(cars)

    cars_in_garage = len(cars) if len(cars) != 0 else "no"
    print(f"You have {cars_in_garage} cars in garage. But furthermore...")

    pcs_in_garage = len(garage)
    if pcs_in_garage == 0:
        print("You have nothing else in your garage. Try again!")
    elif pcs_in_garage > 5:
        print(f"You are a very rich person and have {pcs_in_garage} vehicles in your garage! \n")
    else:
        print(f"You ain't a very rich person but you still have {pcs_in_garage} vehicles in your garage! \n")

    for item in garage:
        item.print_info()
        print('')
