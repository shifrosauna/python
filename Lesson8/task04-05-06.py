# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
class Storage:
    pass


class OfficeEquipment:

    def __init__(
            self,
            type_equipment: str,
            vendor: str,
            model: str,
            color: str,
            price: float,
    ):
        self.type_equipment = type_equipment
        self.vendor = vendor
        self.model = model
        self.color = color
        self.price = price


class Printer(OfficeEquipment):
    print_speed: int

    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Scanner(OfficeEquipment):
    scan_resolution: int

    def __init__(self, *args):
        super().__init__('Сканер', *args)


class Xerox(OfficeEquipment):
    copy_speed: int

    def __init__(self, *args):
        super().__init__('Ксерокс', *args)


printer = Printer("HP", "TR-500", "Белый", 2000)
printer.print_speed = 500
print(printer.type_equipment, printer.print_speed)

scanner = Scanner("Samsung", "T-200", "Черный", 5000)
scanner.scan_resolution = 900
print(scanner.type_equipment, scanner.scan_resolution)

xerox = Xerox("Cannon", "HDJ-64", "Серый", 8000)
scanner.scan_resolution = 900
print(scanner.type_equipment, scanner.scan_resolution)
