from triangulo import Triangulo


if __name__ == "__main__":
    triangulo = Triangulo()
    triangulo.set_base(2)
    triangulo.set_altura(4)

    print(triangulo.calcular_area())
    print(triangulo.calculo_perimetro())