# Exercício 3
# Faça um algoritmo que imprima o nome digitado pelo usuário na vertical em escada.


nome = input("Digite seu nome: ")

nome = nome.upper()


for i in range(1, len(nome) + 1):
    print(nome[:i])