"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex_number:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        if not isinstance(other, Complex_number):
            if not isinstance(other, (int, float)):
                raise TypeError("Допустимо сложение только комплексных или действительных чисел")
            else:
                return Complex_number(self.real + other, self.imaginary)
        return Complex_number(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        if not isinstance(other, Complex_number):
            if not isinstance(other, (int, float)):
                raise TypeError("Допустимо умножение только комплексных или действительных чисел")
            else:
                return Complex_number(self.real * other, self.imaginary * other)
        return Complex_number(self.real * other.real - self.imaginary * other.imaginary, self.imaginary * other.real +
                              self.real * other.imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

    def __eq__(self, other):
        if self.real == other.real and self.imaginary == other.imaginary:
            return True
        else:
            return False


if __name__ == '__main__':
    A = Complex_number(2, 5)
    B = Complex_number(3, 2)
    assert A + B == Complex_number(5, 7)
    assert A * B == Complex_number(-4, 19)
    assert A + 3.1 == Complex_number(5.1, 5)
    assert A * 3 == Complex_number(6, 15)
