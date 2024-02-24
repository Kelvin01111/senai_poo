

class Contabancaria:
    def __init__(self, conta = None, titular = None, saldo = None):
        self.__conta = conta
        self.__titular = titular
        self.__saldo = saldo

    #Getters
    
    @property
    def conta(self):
        return self.__conta
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    

    #Setters

    @conta.setter
    def conta(self, conta):
        self.__conta = conta

    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    #Metodo Depósito
    def deposito(self, valor):
        if (valor > 0):
            self.__saldo = self.__saldo + valor
            print(f"Depósito de R${valor} realizado")
            print(f"Saldo Atual R${self.__saldo}")
        else:
            print("Valor de depósito inválido")

    #Metodo Saque
            
    def sacar(self, valor):
        if (valor > 0) and (valor <= self.__saldo):
            self.__saldo = self.__saldo - valor
            print(f"Saque de R${valor}")
            print(f"Saldo Atual R${self.__saldo}")
        else:
            print(f"Valor de saque inválido ou insuficiente")

    def exibir_informacao(self):
        print(f"Numero da Conta: {self.__conta}")
        print(f"Titular da Conta:{self.__titular}")
        print(f"Saldo da conta: {self.__saldo}")


            

