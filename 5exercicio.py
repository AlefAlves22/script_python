
# Exercício 5
# Faça um programa que leia e valide as seguintes informações:
# - Nome: maior que 3 caracteres;
# - Idade: entre 0 e 150;
# - Salário: maior que zero;
# - Sexo: 'f' ou 'm';
# - Estado Civil: 's', 'c', 'v', 'd';

import time

nome = (input("Digite seu nome: "))
while len(nome) < 3:
  nome = (input("Tente novamente o seu nome: "))

idade = float(input("Digite tua idade: "))
while idade > 150:
  idade = (input("Tente novamente a sua idade: "))

salario = float(input("Digite seu salário: "))
while salario < 0:
  salario = (input("Tente novamente o sua seu salário: "))

sexo = (input("Digite seu sexo (F/M): "))
while sexo != "f" and sexo != "m":
    print("Entrada inválida!")
    sexo = input("Digite seu sexo novamente (F/M): ").lower()

estadoc = (input("Digite seu estdo civil (s/c/v/d): ")).lower()
while estadoc != "s" and estadoc != "c" and estadoc != "v" and estadoc != "d":
    print("Estado civil não identificado")
print("\n")
print("********" *10)
print("\n")
print("Olá seja bem-vindo:")
print("Suas informções é:")
print("\n")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estadoc}")
