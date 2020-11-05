"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self, result):
        return result


class Coat(Clothes):
    def __init__(self, size):
        self.V = float(size)

    @property
    def consumption(self):
        return super().consumption(self.V / 6.5 + 0.5)


class Suit(Clothes):

    def __init__(self, height):
        self.H = float(height)

    @property
    def consumption(self):
        return super().consumption(2 * self.H + 0.3)


if __name__ == '__main__':
    coat1 = Coat(40)
    coat2 = Coat(42)
    suit1 = Suit(1.5)
    suit2 = Suit(1.8)
    clothes_list = [coat1, coat2, suit1, suit2]
    all_consumption = 0
    for el in clothes_list:
        all_consumption += el.consumption
    print(all_consumption)
