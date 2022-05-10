#import math
from math import sqrt, pi

def hipotenusa(a,b):
    c = sqrt(a**2+b**2)
    return c

def areaCirculo(radio):
    area = pi * radio ** 2

def areaTrianguloHeron(a,b,c):
    s = (a+b+c)/2
    area = sqrt(s*(s-a)*(s-b)*(s-c))

def perimetroTrianguloRectangulo(a,b):
    perimetro = a + b + hipotenusa(a,b)
    return perimetro