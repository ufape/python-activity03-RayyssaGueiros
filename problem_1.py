# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 3 - Problem 1
# Description:
"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
A entrada contém dois valores inteiros.
Exemplo:
Digite um valor inteiro para X: 15
Digite um valor inteiro para Y: 12

Processes:
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos
números impares entre eles.

Output(s):
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores
ímpares que estão entre os valores fornecidos na entrada que deverá caber
em um inteiro.
Exemplo:
A soma dos números ímpares entre 15 e 12 é: 13

"""


def main():

  def primeiro(a, b):
    lista = []
    if (a > b):
      d = a
      a = b
      b = d
    c = a + 1
    lista.extend([c])
    while (c < b - 1):
      lista.extend([c + 1])
      c = c + 1
    for i in range(len(lista)):
      if (lista[i] % 2 == 0):
        lista[i] = 0
    return print("A soma dos números ímpares entre " + str(a) + " e " +
                 str(b) + " é: " + str(sum(lista)))

  x = int(input("Digite um valor inteiro para X: "))
  y = int(input("Digite um valor inteiro para Y: "))

  primeiro(x, y)


if __name__ == '__main__':
  main()
