# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 3 - Problem 2
# Description:
"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
A entrada contém um valor inteiro N (2 < N < 1000).

Processes:
Leia 1 valor inteiro N (2 < N < 1000).

A seguir, mostre a tabuada de N:
1 x N = N 
2 x N = 2N
...
10 x N = 10N

Output(s):
Imprima a tabuada de N, conforme o exemplo fornecido.

"""


def main():

  def segundo(a):
    return print(str(a) + " x 1 = " + str(a * 1)), print(
      str(a) + " x 2 = " +
      str(a * 2)), print(str(a) + " x 3 = " + str(a * 3)), print(
        str(a) + " x 4 = " +
        str(a * 4)), print(str(a) + " x 5 = " + str(a * 5)), print(
          str(a) + " x 6 = " +
          str(a * 6)), print(str(a) + " x 7 = " + str(a * 7)), print(
            str(a) + " x 8 = " +
            str(a * 8)), print(str(a) + " x 9 = " + str(a * 9)), print(
              str(a) + " x 10 = " + str(a * 10))

  a = int(input("Digite um número inteiro entre 2 e 1000: "))

  segundo(a)


if __name__ == '__main__':
  main()
