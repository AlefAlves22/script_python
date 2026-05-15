# Exercício 10 Utilizando o laço While faça um programa que peça uma senha ao usuário, e que imprima "Acesso liberado" apenas se o usuário digitar a senha corretamente. A senha devera ser a seguinte senha númerica : "676767".

senha_certa = "676767"

senha = input("Digite a senha: ")

while senha != senha_certa:
  print("Senha errada")
  senha = input("Digite a senha novamente: ")

print("Senha correta! Acesso Liberado!")