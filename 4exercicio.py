# **Exercício 4:**
# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... (o próximo termo, a partir do terceiro (número 2), é sempre gerado a partir do somatório dos últimos dois). Faça um programa capaz de gerar a série até o n−ésimo termo (onde o valor n deve ser inserido pelo usuário).

import time 

question = (input("Você sabe o que é a série de Fibonaci? "))
print("\n")
if question.lower() == "sim":
  print("Então vamos descobrir algum termo da série!!!")

elif question.lower() == "não":
  print("A sequência de Fibonacci é a soma dos dois termos anteriores, começada pelo número 1. Usada principalmente para explicar padrões na de crescimento na natureza.")
  time.sleep(5)
  print("\n")
  print("Sabendo disso vamos descobrir algum termo dessa série !!")
numero = int(input("Digite qual termo da série de fibonaci você quer descobrir:"))
primeiro = 1
segundo = 2
print(primeiro)
print(segundo)
for i in range(numero - 2):
  resto =primeiro + segundo
  print(resto)
  primeiro = segundo
  segundo = resto