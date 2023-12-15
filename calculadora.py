# -*- coding: utf-8 -*-
"""calculadora.ipynb
"""

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
resultado = 0
print("-"*50)
print("1. Soma 2. Subtração 3. Multiplicação 4. Divisão")
print("-"*50)
operacao = int(input("Escolha a operação desejada: "))
if operacao == 1:
    resultado = num1+num2
    print(f'{num1} + {num2} = {resultado}')
elif operacao == 2:
    resultado = num1-num2
    print(f'{num1} - {num2} = {resultado}')
elif operacao == 3:
    resultado = num1*num2
    print(f'{num1} * {num2} = {resultado}')
elif operacao == 4:
    resultado = num1/num2
    print(f'{num1} / {num2} = {resultado}')

else:
    print(resultado)
