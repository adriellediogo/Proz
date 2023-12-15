# -*- coding: utf-8 -*-
"""hotel.ipynb
Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.
"""

cont = 0
while (cont<20):
    cont+=1
    if cont == 13:
      continue
    print(cont, "º Andar")

"""
Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

"""

for cont in range(20, 0, -1):
  if cont == 13:
    continue
  print(cont, "º Andar")
