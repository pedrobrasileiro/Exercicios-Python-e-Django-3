#!/usr/bin/env python3
# encoding: utf-8
"""

programa1.py

Created by Pedro Brasileiro Cardoso Junior on 2010-12-28.
Copyright (c) 2010 Particular. All rights reserved.

Importa o módulo random e sorteia um número inteiro
entre 1 e 100

"""

import random
numero = random.randint(1,100)
escolha = 0
tentativas = 0
while escolha != numero:
  escolha = int(input("Escolha um número entro 1 a 100: "))
  tentativas += 1
  if escolha < numero: 
    print("O número", escolha, "é menor que o sorteado")
  elif escolha > numero:
    print("O número", escolha, "é maior que o sorteado")

print("Parabéns, você acertou em", tentativas, "tentativas")