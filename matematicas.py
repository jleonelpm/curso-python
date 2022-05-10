from math import sqrt, pi

def hipotenusa(a, b):
    c = sqrt(a**2 + b**2)
    return c

def areaCirculo(radio):
    area = pi * radio ** 2
    return area

def areaTrianguloHeron(a, b, c):
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def perimetroTrianguloRectangunlo(base, altura):
    perimetro = base + altura + hipotenusa(base,altura)
    return perimetro