# Exercicio 8: Dada a lista L = [5, 7, 2, 9, 4, 1, 3] Escreva um programa que imprima as seguintes informações: a) tamanho da lista. b) maior valor da lista. c) menor valor da lista. d) soma de todos os elementos da lista. e) lista em ordem crescente. f) lista em ordem decrescente.

L = [5,7,9,4,1,3]
# a) tamanho da lista.
tamanho = len(L)
print(f"O tamanho da lista é: {tamanho}")

# 2)maior valor da lista
maior = max(L)
print(f"O maior número da lista é: {maior}")

# 3) Menos valor da lista
menor = min(L)
print(f"O menor número da lista é: {menor}")

# 4) soma de todos elementos da lista
soma = sum(L)
print(f"A soma de todos os núeros da lista é: {soma}")

# 5) ordem crescente
crescente = L.sort()
print(f"A ordem crescente dos termos é: {crescente}")

# 6) ordem decescente
decrescente = sorted(L, reverse=True)
print(f"A decrescente dos termos é: {decrescente}")

