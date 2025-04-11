number1 = int(input("Informe o primeiro número: "))
number2 = int(input("Informe o segundo número: "))
number3 = int(input("Informe o terceiro número: "))

if number1 < number2 and number1 < number3 and number2 < number3: #1,2,3
    print({number3},{number2},{number1})
    
elif number1 < number2 and number1 < number3 and number3 < number2: #1,3,2
    print({number2},{number3},{number1})

elif number2 < number1 and number2 < number3 and number1 < number3: #2,3,1
    print({number3},{number1},{number2})

elif number2 < number1 and number2 < number3 and number3 < number1: #2,1,3
    print({number3},{number1},{number2})

elif number3 < number1 and number3 < number2 and number1 < number2: #3,1,2
    print(number3,number2,number1)

elif number3 < number1 and number3 < number2 and number2 < number1: #3,2,1
    print(number1,number2,number3)