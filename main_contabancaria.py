from conta_bancaria import Contabancaria

if __name__ == "__main__":
    conta_bancaria = Contabancaria(2345, "Pedro", 852)
    
    conta_bancaria.saldo = 100

    conta_bancaria.deposito = 0
    conta_bancaria.sacar = 230


    conta_bancaria.exibir_informacao()

