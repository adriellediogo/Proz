# -*- coding: utf-8 -*-
"""calculadora_2.ipynb"""

def calculadora (num1,num2, operacao):
  if operacao == 1:
    return num1+num2
  elif operacao == 2:
    return num1-num2
  elif operacao == 3:
    return num1*num2
  elif operacao == 4:
    return num1/num2
  else:
    return 0

calc = True

while(calc == True):
  print(60*"-")
  print("1. Soma 2. Subtração 3. Multiplicação 4. Divisão 0. Sair")
  print(60*"-")
  operacao = int(input("Escolha a operação desejada: "))
  if (operacao < 0) or (operacao > 4):
    print("Opção inexistente. Tente novamente.")
  elif (operacao == 0):
    break
  else:
    num1 = int(input("Insira o primeiro número: "))
    num2 = int(input("Insira o segundo número: "))
    resultado = calculadora (num1, num2, operacao)
    print(resultado)
