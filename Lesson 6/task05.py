# 6. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:

    def __init__(self, title='Запуск отрисовки.'):
        self.title = title

    def draw(self):
        print(self.title)


class Pen(Stationery):

    def __init__(self):
        super().__init__('Ручка')

    def draw(self):
        print(f'Запуск отрисовки. Выбранный инструмент: {self.title}')


class Pencil(Stationery):

    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        print(f'Запуск отрисовки. Выбранный инструмент: {self.title}')


class Handle(Stationery):

    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        print(f'Запуск отрисовки. Выбранный инструмент: {self.title}')


stationery = Stationery()

pen = Pen()
pencil = Pencil()
handle = Handle()

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
