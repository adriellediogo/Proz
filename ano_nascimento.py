# -*- coding: utf-8 -*-
"""ano_nascimento.ipynb
"""

nome = input("Digite o seu nome: ")

executar = True
while (executar == True):
  try:
    ano_nascimento =int(input("Informe o ano do seu nascimento: "))
    if (ano_nascimento < 1922) or (ano_nascimento > 2021):
      print("Insira um ano de nascimento que seja entre 1922 e 2021.")
    else:
      idade = 2022 - ano_nascimento
      print(f'{nome}, você tem {idade} anos.')
      executar = False
  except:
    print("Insira apenas números")
