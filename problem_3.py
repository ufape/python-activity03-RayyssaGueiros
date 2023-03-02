# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 3 - Problem 3
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
A primeira linha de entrada contém um valor inteiro N que indica os
vários casos de teste que vem a seguir. Cada caso de teste contém um
inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de
amostras utilizadas e um caractere Tipo ('S', 'R' ou 'C'),
indicando o tipo de amostra (S:Salmão, R:Rabanete e C:Cenoura).
Exemplo:
Quantas amostras: 10
Tipo: C
Quantidade: 10
Tipo: R
Quantidade: 6
Tipo: S
Quantidade: 15
Tipo: C
Quantidade: 5
Tipo: R
Quantidade: 14
Tipo: C
Quantidade: 9
Tipo: R
Quantidade: 6
Tipo: S
Quantidade: 8
Tipo: C
Quantidade: 5
Tipo: R
Quantidade: 14

Processes:
Maria acabou de iniciar seu curso de Engenharia de Alimentos e precisa
de sua ajuda para organizar os experimentos de um laboratório o qual
ela é responsável. Ela quer saber no final do ano, quantas amostras
foram utilizadas no laboratório e o percentual de cada tipo de amostra
utilizada.

Este laboratório em especial utiliza três tipos de amostras: salmão,
rabanete e cenoura. Para obter estas informações, ela sabe exatamente
o número de experimentos que foram realizados, o tipo de amostra
utilizada e a quantidade de amostras utilizadas em cada experimento.

Output(s):
Apresente o total de amostras utilizadas, o total de cada tipo de
amostra utilizada e o percentual de cada uma em relação ao total
de amostras utilizadas, sendo que o percentual deve ser apresentado
com dois dígitos após o ponto.
Exemplo:
Total: 92 amostras
Total de cenoura: 29
Total de rabanete: 40
Total de salmão: 23
Percentual de cenoura: 31.52%
Percentual de rabanete: 43.48%
Percentual de salmão: 25.00%
"""


def main():

  def terceiro(a):
    c = []
    s = []
    r = []
    for i in range(a):
      t = input("Tipo: ")
      b = int(input("Quantidade: "))
      if(t == "C"):
        c.append(b)
      elif(t == "S"):
        s.append(b)
      elif(t == "R"):
        r.append(b)
    soma_total = sum(c) + sum(r) + sum(s)
    pc = (sum(c)*100)/soma_total
    pr = (sum(r)*100)/soma_total
    ps = (sum(s)*100)/soma_total
    r1 = "{:.2f}".format(pc)
    r2 = "{:.2f}".format(pr)
    r3 = "{:.2f}".format(ps)
    return print("Total: " + str(soma_total) + " amostras."), print("Total de cenouras: " + str(sum(c)) + "."), print("Total de rabanetes: " + str(sum(r)) + "."), print("Total de salmões: " + str(sum(s)) + "."), print("Percentual de cenouras: " + str(r1) + "%"), print("Percentual de rabanetes: " + str(r2) + "%"), print("Percentual de salmões: " + str(r3) + "%")
    
  a = int(input("Quantas amostras: "))

  terceiro(a)    
  
if __name__ == '__main__':
    main()
