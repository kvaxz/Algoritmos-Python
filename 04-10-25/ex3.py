number1 = int(input("Informe o primeiro número: "))
number2 = int(input("Informe o segundo número: "))
number3 = int(input("Informe o terceiro número: "))

if number1 > number2 and number1 > number3: 
    print("O maior é o número: ",number1)

elif number2 > number3 and number2 > number1: 
    print("O maior é o número: ",number2)

elif number3 > number2 and number3 > number1: 
    print("O maior é o número: ",number3)

if number1 < number2 and number1 < number3:
    print("O menor é o número:",number1)

elif number2 < number1 and number2 < number3:
    print("O menor número é", number2)

elif number3 < number1 and number3 < number2:
    print("O menor número é",number3)
