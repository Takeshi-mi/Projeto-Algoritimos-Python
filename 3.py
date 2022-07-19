'''
3. Fibonacci
• O usuário informa um número e é impresso na tela qual é esse número na
série de Fibonacci (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...)
• Por exemplo: se o usuário digitar 7, deve retornar o 7º número da
sequência (13)
'''
print('FIBONACCI')
num = int(input('Digite a posição da sequência de Fibonacci que você deseja saber:  '))

for i in range(1,num):
  fibonacci = (i-1) + (i-2)
  print(fibonacci)

  