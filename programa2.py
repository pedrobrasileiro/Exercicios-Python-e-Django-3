#!/usr/bin/env python3
# encoding: utf-8
"""
programa2.py

Created by Pedro Brasileiro Cardoso Junior on 2010-12-28.
Copyright (c) 2010 Particular. All rights reserved.

Exemplo de endentação

"""

def main():
  x = 1
  
  while True:
    if x > 5:
      print(x, "fim.")
      break
    else:
      print(x, "menor")
    
    x += 1
    
  x = 0
  
def nao_implementado():
    pass
      
if __name__ == '__main__': main() # evite fazer isso