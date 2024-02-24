from calculadora import Calculadora

if __name__ == "__main__":
    calculdadora = Calculadora()
    calculdadora.set_num1(6)
    calculdadora.set__num2(4)

    resultado = calculdadora.adicao()
    print("Adição:" ,resultado)

    resultado = calculdadora.sub()
    print("Subtração:" ,resultado)

    resultado = calculdadora.mult()
    print("Multiplicação:" ,resultado)

    resultado = calculdadora.div()
    print("Divisão:" ,resultado)

    resultado = calculdadora.raiz()
    print("Raiz quadrada" ,resultado)