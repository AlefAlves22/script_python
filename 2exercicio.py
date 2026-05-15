# **Exercício 2**:
# Escreva um script que leia três números e mostre o maior e o menor deles.
n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))
print("\n")
if n1 >= n2 and n1 >= n3:
  maior = n1
  if n2 >= n3:
    meio = n2
    menor = n3
  else:
    meio = n3
    menor = n2

elif n2 >= n1 and n2 >= n3:
  maior = n2
  if n1 >= n3:
   meio = n1
   menor = n3
  else:
   meio = n3
   menor = n1
else:
  maior = n3
  if n2 > n1:
    meio = n2
    menor = n1
  else:
    meio = n2
    menor = n1


print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")

