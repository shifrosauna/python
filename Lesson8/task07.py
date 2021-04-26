# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и
# умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class ComplexNumber:
    real: float
    imaginary: float

    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other: 'ComplexNumber'):
        return ComplexNumber(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def __mul__(self, other: 'ComplexNumber'):
        r1 = self.real * other.real
        r2 = self.imaginary * other.imaginary * -1

        i1 = self.real * other.imaginary
        i2 = self.imaginary * other.real

        real = r1 + r2
        indeterminate = i1 + i2

        return ComplexNumber(real, indeterminate)

    def __str__(self):
        return f"{self.real}{'+' if self.imaginary > 0 else ''}{self.imaginary}i"


a = ComplexNumber(7, 22)
b = ComplexNumber(3, 45)

# Суммой двух комплексных чисел z1=a1+b1i и z2=a2+b2i называется комплексное число z, которое равно
# z=(a1+a2)+(b1+b2)
# (7+22i) + (3+45i) = (7 + 3) + (22 + 45)i = (10+67i)
print(f"({a.real} +{a.imaginary}i) + ({b.real}+{b.imaginary}i) = {a + b}")

# Произведением двух комплексных чисел z1=a1+b1i и z2=a2+b2i называется комплексное число z, равное
# z=z1⋅z2=(a1a2−b1b2)+(a1b2+b1a2)i

# (7+22i) * (3+45i) = (3*7-22*45)+(7*45+22*3)i = -969+381i
print(f"({a.real} +{a.imaginary}i) * ({b.real}+{b.imaginary}i) = {a * b}")
