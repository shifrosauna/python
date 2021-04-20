# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import abstractmethod


class Clothes:

    def __init__(self, size=0):
        self.size = size

    @abstractmethod
    def tissue_consumption(self):
        pass

    def full_tissue_consumption(Coat, Costume):
        return round(Coat.tissue_consumption + Costume.tissue_consumption, 2)


# Пальто
class Coat(Clothes):

    def __init__(self, V):
        super(Coat, self).__init__(V)

    @property
    def tissue_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


# Костюм
class Costume(Clothes):

    def __init__(self, H):
        super(Costume, self).__init__(H)

    @property
    def tissue_consumption(self):
        return round(self.size * 2 + 0.3, 2)


coat = Coat(15)
print(f'Расход ткани на пальто: {coat.tissue_consumption}')
costume = Costume(25)
print(f'Расход ткани на костюм:{costume.tissue_consumption}')
print(f'Общий расход ткани на костюм и пальто:{Clothes.full_tissue_consumption(coat, costume)}')
