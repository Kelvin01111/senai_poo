

import math


class Triangulo:
    def __init__(self, base = None, altura = None):
        self.__base = base
        self.__altura = altura

    #Getters
    def get_base(self):
        return self.__base
    
    def get_altura(self):
        return self.__altura
    
    #Setters

    def set_base(self, base):
        self.__base = base

    def set_altura(self, altura):
        self.__altura = altura
    
    def calcular_area(self):
        area = (self.__base * self.__altura)/2

        return round(area,2)
    
    def calculo_perimetro(self):
        hipotenusa = math.sqrt(self.__base**2 + self.__altura**2)
        perimetro = self.__base + self.__altura + hipotenusa

        return round(perimetro, 2)
    