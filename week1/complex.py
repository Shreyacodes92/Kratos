import math

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real, imag)

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __str__(self):
        real = "{0:.2f}".format(self.real)
        imag = "{0:+.2f}".format(self.imag)
        return real + imag + "i"

if __name__ == '__main__':
    a_real, a_imag = map(float, input().split())
    b_real, b_imag = map(float, input().split())

    a = Complex(a_real, a_imag)
    b = Complex(b_real, b_imag)

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print("{0:.2f}+0.00i".format(abs(a)))
    print("{0:.2f}+0.00i".format(abs(b)))
