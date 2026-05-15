#**Exercício** 6: Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

import time

num = int(input("Digite um número para saber se ele é primo ou não: "))

np = True
for i in range(2, num):
  if np % i == 0:
    np = False

if num == True:
  print("Número primo.")
else:
  print("Número não primo")