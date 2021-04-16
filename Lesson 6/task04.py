# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# 5. Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    direction = 'едит прямо!'

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала.'

    def stop(self):
        self.speed = 0
        return f'{self.name} остановилась.'

    def turn(self):
        if self.direction == 'едит прямо!':
            return f'{self.name} {self.direction}'
        else:
            return f'{self.name} повернула на {self.direction}'

    def show_speed(self):
        return f'Скорость автомобиля: {self.name} : {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Скорость автомобиля {self.name} {self.speed} км/ч (превышает 60 км/ч)!'
        else:
            return f'Скорость автомобиля {self.name} : {self.speed} км/ч'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Скорость автомобиля {self.name} {self.speed} км/ч (превышает 40 км/ч)!'
        else:
            return f'Скорость автомобиля  {self.name} : {self.speed} км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car1 = TownCar(25, 'Синий', 'Kia Carens', False)
car2 = SportCar(150, 'Черная', 'Bugatti', False)
car3 = WorkCar(80, 'Белая', 'Honda Pilot', False)
car4 = PoliceCar(110, 'Бело-Голубая', 'Mersedes-Benz E200', True)

# Kia Carens поехала
print(car1.go())
# Kia Carens повернула на лево
car1.direction = 'лево'
print(car1.turn())
# Kia Carens текущая скорость
print(car1.show_speed())
# Kia Carens остановилась
print(car1.stop())
# Kia Carens скорость должна быть = 0 км/ч
print(car1.show_speed())

# Bugatti поехала
print(car2.go())
# Bugatti повернула на лево
car2.direction = 'право'
print(car2.turn())
# Bugatti текущая скорость
print(car2.show_speed())

#  Текущая скорость Honda Pilot
print(car3.show_speed())
#  Цвет Honda Pilot
print(f'Цвет {car3.name} - {car3.color}')

if car4.is_police:
    print(f'{car4.name} - полицейский автомобиль! ')

print(f'{car4.turn()}')
print(f'{car4.show_speed()}')
