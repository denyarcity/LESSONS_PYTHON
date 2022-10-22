"""
Задание 2.
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Единственный класс этого проекта — одежда (класс Clothes).
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5), для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактный класс для единственного класса проекта, проверить на практике работу декоратора @property
Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57
Два класса: абстрактный и Clothes
"""

from abc import ABC, abstractmethod

class clothes(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_cloth_count(self):
        pass

class coat(clothes):

    def __init__(self, v):
        self.v = v

    @property
    def get_cloth_count(self):
        return self.v/6.5 + 0.5

class suit(clothes):

    def __init__(self, h):
        self.h = h

    @property
    def get_cloth_count(self):
        return self.h * 2 + 0.3


c1 = coat(52)
print(c1.get_cloth_count)

c2 = coat(56)
print(c2.get_cloth_count)


s1 = suit(164)
print(s1.get_cloth_count)

s2 = suit(172)
print(s2.get_cloth_count)