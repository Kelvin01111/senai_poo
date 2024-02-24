import math

class Calculadora:
    def __init__(self, num1 = None, num2 = None):
      self.__num1 = num1
      self.__num2 = num2

    #Getters
      
    def get_num1(self):
      return self.__num1
   
    def get_num2(self):
      return self.__num2
    
    #Setter

    def set_num1(self, num1):
       self.__num1 = num1

    def set__num2(self, num2):
       self.__num2 = num2

    
    def adicao(self):
       return self.__num1 + self.__num2
    
    def sub(self):
       return self.__num1 - self.__num2
    
    def mult(self):
       return self.__num1 * self.__num2
    
    def div(self):
       if self.__num2 != 0:
        return self.__num1 / self.__num2
       else:
            mensagem = "Não posso dividir por 0"
            return mensagem
       
    def raiz(self):
       if self.__num1 > 0:
          raiz = math.sqrt(self.__num1)
          return raiz
       else:
          mensagem = "Não posso calcular a raiz de números negativos"
          return mensagem