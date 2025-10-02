class cauculadora:
    pass
    def calcular(self,opcao,num1,num2):
        if opcao == "+":
            return self.__adicionar(num1,num2)
        elif opcao == "-":
            return self.__subtrair(num1,num2)
        else:
            print("Opção invalída!")

    def __adicionar(self,num1,num2):
        return num1+num2

    def __subtrair(self,num1,num2):
        return num1-num2

calc = cauculadora()
 
resultado = calc.calcular("+",100,40)
print(resultado)