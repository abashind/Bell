import abc


class BaseFabric(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def get_one():
        pass

    @staticmethod
    @abc.abstractmethod
    def get_rnd_one():
        pass

    @classmethod
    def get_number_of_rnd(cls, number: int):
        for _ in range(number):
            yield cls.get_rnd_one()
