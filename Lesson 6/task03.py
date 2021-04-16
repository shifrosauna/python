# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'ФИO: {self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())


director = Position('Владимир Владимирович', 'Путин', 'Директор', 20000, 7000)
technick = Position('Иван Петрович', 'Иванов', 'Техник', 17000, 2000)

print(director.get_full_name())
print(f'Общий доход: {director.get_total_income()}')
print(technick.get_full_name())
print(f'Общий доход: {technick.get_total_income()}')
print(technick.position)
