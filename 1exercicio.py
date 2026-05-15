# **Exercício 1**:
# Faça um algoritmo usando o for para mostrar os números pares e impares de 0 a 100.


for i in range(1,101):
    if i % 2 == 0:
        print(f"{i} é par")
    else:
        print(f"{i} é ímpar")
