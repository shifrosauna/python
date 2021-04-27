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
    def __init__(self):
        self.storage = []
        self.dict_departments = {}

    def add_equipment(self, item: "OfficeEquipment", amount: int):
        self.storage.append([item, amount])

    def transfer_to_department(self, id: int, department_name: str):
        self.dict_departments.update({department_name: self.storage[id][0]})
        self.storage[id][1] -= 1

    @staticmethod
    def ValidateAmount(amount):
        try:
            int(amount)
        except ValueError:
            print('Количество оргтехники может быть только целое число!')
            exit(1)


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

    def __init__(self, *args, print_speed: int):
        super().__init__('Принтер', *args)
        self.print_speed = print_speed

    @property
    def info(self):
        return f"{self.type_equipment} {self.vendor} {self.model} {self.color} {self.price} {self.print_speed}"


class Scanner(OfficeEquipment):

    def __init__(self, *args, scan_resolution: int):
        super().__init__('Сканер', *args)
        self.scan_resolution = scan_resolution

    @property
    def info(self):
        return f"{self.type_equipment} {self.vendor} {self.model} {self.color} {self.price} {self.scan_resolution}"


class Xerox(OfficeEquipment):

    def __init__(self, *args, copy_speed: int):
        super().__init__('Ксерокс', *args)
        self.copy_speed = copy_speed

    @property
    def info(self):
        return f"{self.type_equipment} {self.vendor} {self.model} {self.color} {self.price} {self.copy_speed}"


printer = Printer("HP", "TR-500", "Белый", 2000, print_speed=500)
scanner = Scanner("Samsung", "T-200", "Черный", 5000, scan_resolution=900)
xerox = Xerox("Cannon", "HDJ-64", "Серый", 8000, copy_speed=1200)

my_storage = Storage()
# printer_amount = 'dscds'
printer_amount = 2
Storage.ValidateAmount(printer_amount)
my_storage.add_equipment(printer, printer_amount)

scanner_amount = 3
Storage.ValidateAmount(scanner_amount)
my_storage.add_equipment(scanner, scanner_amount)

xerox_amount = 5
Storage.ValidateAmount(xerox_amount)
my_storage.add_equipment(xerox, xerox_amount)

print(my_storage.storage)
my_storage.transfer_to_department(2, "АХО")
print(my_storage.storage)
print(my_storage.dict_departments)
