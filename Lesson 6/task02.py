# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т
class Road:
    # Возьмем за вес одного кв.м асфальта толщиной 1см = 25кг
    __massa_asfalta = 25

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def get_massa_asphalt(self, thickness: float):
        return (self._length * self._width * self.__massa_asfalta * thickness) / 1000


road = Road(5000, 20)
print('Масса асфальта:', road.get_massa_asphalt(5), 'тонн')
