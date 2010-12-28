#!/usr/bin/env python
# encoding: utf-8
"""
programa1.py

Created by Pedro Brasileiro Cardoso Junior on 2010-12-28.
Copyright (c) 2010 Particular. All rights reserved.

Primeiro Programa

"""

import random
numero = random.randint(1,100)
escolha = 0
tentativas = 0
while escolha != numero: 
  escolha = input("Escolha um numero entre 1 e 100: ")
  if escolha < 1:
    print "O numero", escolha, "eh menor que 1."
  elif escolha > 100:
    print "O numero", escolha, "eh maior que 100."
  elif escolha < numero:
    tentativas += 1
    print "O numero", escolha, "eh menor que o sorteado."
  elif escolha > numero:
    tentativas += 1
    print "O numero", escolha, "eh maior que o sorteado."

print "Parabens! Voce acertou com", tentativas, "tentativas."
    
