# Exercício 11 Escreva um programa que peça um número de 1 a 10, e mostre a tabuada desse número.

num = int(input("Digite um número 1 a 10, para descobrir a tabuada dele: "))
for i in range(1, 11):
  print(num, "x", i, "=", num * i)