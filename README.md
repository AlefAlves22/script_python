# Explicação dos códigos.

1.
<img width="305" height="121" alt="image" src="https://github.com/user-attachments/assets/2cfdb914-739a-4302-bdd3-98964d012001" />

- Para fazer esse exercício eu ultilizei o "for i in range", então eu atribuí o valor de 1 a 100 para o :"i".
 
 - Depois eu ultilizei o algumas atribuições como:
 
            # % para ter o resto da divisão
            # == para comparação
- Então o que eu disse na linha "if i % 2 == 0", foi que se(if) o resto da divisão do valor do "i" for 0 (ou seja não ter resto), o número é par.
Caso ao contrário (else), o número é ímpar.

2. 
<img width="446" height="796" alt="image" src="https://github.com/user-attachments/assets/0d22c38c-285a-440c-bce8-98898e5d2bfe" />

- Primeiro eu coloquei um float(input) para as variáveis (n1, n2, n3), onde eles cria caixas para o clinte digitar e a partir do que é digitado pelo cliente avaríavel é atribuída e o float ajuda os números que não são inteiros serem digitados também.
- Depois eu usei uma estrutura de repetição (if, elif e else), e dentro deles eu coloquei a mesma estrutura de decisão, para que eles pudessem fazer isso 3 vezes comparando qual era o maior, meio e menor númeroentre os digitados epelo cliente.
- No final eu coloquei dois prints, para ele exibir somente o menor e o mair número.

3. 
 <img width="386" height="201" alt="image" src="https://github.com/user-attachments/assets/29a92a5f-4e3b-4237-8bbf-4a4245212985" />

- Primeiro eu uso input, para que a pessoa possa digitar seu nome, e conforme o que a pessoa digita o .upper() transforma tudo em caixa alta.
- Então eu coloco o "for" para criar uma estrutura de repetição, e depois um range para colocar o que o for vai repetir por várias veze.
- E no final eu coloco um print (:i) para que ele possa criar um efeito de escada no nome cortando ele por letra.

4.
<img width="610" height="692" alt="image" src="https://github.com/user-attachments/assets/39a34cb1-ebd5-4114-9a3c-1622f706b5cc" />

- Primeiro eu fiz um input para a pessoa digitar qual termo da série de fibonacci ele queria descobrir.
- Depois eu fiz um if e else para que eu pergunta para a pessoa se ele sabe o que é série de fibonacci ou não.
- Então eu pego o int(input), para receber o termo da sequência que a pessoa quer descobrir.
- for i in range(numero - 2): Essa parte do código ele cria um laço de repetição para a quantidade de termo necessária para o print.
- Dentro do laço, eu somo os dois números anteriores (resto), mostro o resultado e depois atualizo as variáveis para que o cálculo continue avançando para o próximo número.

5.
<img width="564" height="898" alt="image" src="https://github.com/user-attachments/assets/8be0f4b2-aeb6-4afd-92ac-cb1b8159475d" />

- Primeiro eu coloquei um import time, para carregar o módulo de tempo.
- Depois eu coloquei um while len(), para ele atribuir alguma restrições que tinha na atividade para cada varíavel, onde ele trava a próxima pergunta até a pessoa digitar a resposta correta.
- No final eu coloquei vários prints no final para colocar as informações de formas mais organizadas.

6.
<img width="600" height="373" alt="image" src="https://github.com/user-attachments/assets/24426325-b751-45d7-89b1-1f9eabcf3e32" />

- int(input) Ele funciona para você digitar um número, para que possa saber se ele é primo ou não.
- np = true, ele funciona para que o número é primo até que se prove ao contrário.
- for i in range(2, num), ele cria um laço para que ele divida todos os números de 2 até o número que foi digitado.
- if num % i == 0, ele vai texteando as divisões para ver se tem alguma divisão exta entre os números.
- np = False, se ele encontrar alguma divisão que dê exata o número ele não é primo.
- no final tem um print para mostrar se ele é primo ou não.
