'''
3. Fibonacci
• O usuário informa um número e é impresso na tela qual é esse número na
série de Fibonacci (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...)
• Por exemplo: se o usuário digitar 7, deve retornar o 7º número da
sequência (13)
'''
# print('FIBONACCI')
# num = int(input('Digite a posição da sequência de Fibonacci que você deseja saber:  '))

# f1 = 0
# f2 = 1 
# seq = 3
# while seq < num:
#   f3 = f1 + f2
#   print(f3)
#   f1 = f2
#   f2 = f3
#   seq += 1
#   print(f1)

num = int(input('Digite o termo da sequência que você deseja saber: '))
f1 = 0
f2 = 1
for i in range(num):
  f3 = f1 + f2
  f1 = f2
  f2 = f3
print(f'O {num}º termo da sequência de Fibonacci é {f1}')
