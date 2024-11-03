# Crie uma variável chamada saida e atribua a ela o valor ‘’;
# Crie uma função chamada adicao . Tal função deverá receber dois
# parâmetros e retornar a soma entre ambos;
# Crie uma função chamada subracao . Tal função deverá receber dois
# parâmetros e retornar a subtração entre ambos;
# Crie uma função chamada multiplicacao . Tal função deverá receber dois
# parâmetros e retornar a multiplicação entre ambos;
# Crie uma função chamada divisao. Tal função deverá receber dois
# parâmetros, verificar se um deles é igual a 0. Em caso positivo, deverá
# retornar a mensagem “Não foi possível realizar a divisão por 0”. Em caso
# negativo, deverá retornar a divisão entre ambos;
# Crie uma função chamada calculadora. Tal função deverá receber três
# parâmetros, sendo eles: os dois números que serão usados para os
# cálculos e a operação matemática que se deseja realizar. Sobre esse
# último parâmetro, você poderá utilizar tanto o sinal da operação quanto o
# seu nome;
# No corpo da função calculadora você deverá verificar qual a operação
# desejada pelo usuário, checando o valor do parâmetro correspondente.
# Utilize estruturas de condição para isso e, dependendo da operação
# desejada, você deverá chamar a função relativa a ela, passando as
# variáveis contendo os dois números para serem utilizados no cálculo.
# Armazene o resultado da chamada às funções de cálculo numa variável
# chamada resultado. Ao final da função calculadora você deverá retornar a
# variável resultado;
# Crie um laço while e, como condição do mesmo, verifique se o valor da
# variável saída é diferente de n. Lembre-se de que o usuário poderá inserir
# tanto N quanto n;
# No escopo do laço while peça ao usuário para digitar o primeiro número e
# armazene seu valor numa variável. Faça o mesmo para o segundo número
# e para a operação matemática. Passe essas três variáveis para o método
# calculadora, armazenando o retorno dessa chamada numa variável
# também chamada resultado. Imprima na tela o valor da variável resultado
# precedido pelo texto ‘Resultado da operação: ‘. Por fim, pergunte ao
# usuário se ele deseja continuar ou não executando o programa. Armazene
# tal input na variável saida;
# Tome cuidado com a condição de verificação do laço for em relação à
# entrada do usuário armazenada na variável saida. Em outras palavras,
# deixe claro para o usuário as respostas possíveis para a pergunta se ele
# deseja sair. Use, por exemplo, S/N. Com isso você poderá considerar um
# desses dois valores na verificação do laço para saber se deve continuar
# executando o programa ou se deve encerrá-lo.

saida = ""
def adicao(num1, num2):
  return num1 + num2

def subtracao(num1, num2):
  return num1 - num2

def multiplicacao(num1, num2):
  return num1 * num2

def divisao(num1, num2):
  if num2 == 0:
    return 'Não foi possível realizar a divisão por 0'
  else:
    return num1 / num2

def calculadora(num1, num2, operacao):
  if operacao == 'adicao' or operacao == '+':
    return adicao(num1, num2)
  elif operacao == 'subtracao' or operacao == '-':
    return subtracao(num1, num2)
  elif operacao == 'multiplicacao' or operacao == '*':
    return multiplicacao(num1, num2)
  elif operacao == 'divisao' or operacao == '/':
    return divisao(num1, num2)

while saida != 'n' and saida != 'N':
  num1 = int(input('Digite o primeiro número: '))
  num2 = int(input('Digite o segundo número: '))
  operacao = input('Digite a operação matemática: ')
  print('O resultado da operação: ' + str(calculadora(num1, num2, operacao)))
  saida = input('Deseja continuar? [S/N] ')

print('Programa encerrado.')
