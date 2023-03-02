# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 3 - Problem 4
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
O valor inteiro da entrada deve estar N (0 < N < 46).
Exemplo:
Série de Fibonacci
=-=-=-=-=-=-=-=-=-

Digite o valor inteiro (0 < N < 46):

Processes:
A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

Output(s):
"A série de Fibonacci até 5 é: 0 1 1 2 3"
"""


def main():
  
  def quarto(a):
    fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i in range(len(fib)):
        x = i + 1
        if(sum(fib[i:x]) == a):
            del fib[i:]
    y = str(fib)
    chars = ["[", "]", ","]
    res = y.translate(str.maketrans({ord(x): '' for x in chars}))
    return print("A série de Fibonacci até " + str(a) + " é: " + res)

  print("Série de Fibonacci")
  print("=-=-=-=-=-=-=-=-=-\n")
  a = int(input("Digite o valor inteiro (0 < N < 46): "))
  quarto(a)

if __name__ == '__main__':
  main()
