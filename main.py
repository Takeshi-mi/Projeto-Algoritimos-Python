
# Importando bibliotecas
import os
from time import sleep
# Atalhos para cores
r = '\033[31m'; g = '\033[32m'; b = '\033[34m';y = '\033[33m'; rs = '\033[0;0m'

def menu():
  print(f'''
        
             ________________________________________________
            /                                                \\
        
           |    _________________________________________     |
           |   |                                         |    |  
           |   |  {g}C:\> _ BEM VINDO!{rs}                      |    |
           |   |      {g}Selecione uma opção:{rs}               |    |
           |   |  {g}[1] - Faixa etária{rs}                     |    |     
           |   |  {g}[2] - Retornar maior, menor e média{rs}    |    |
           |   |  {g}[3] - Série Fibonacci{rs}                  |    |      
           |   |  {g}[4] - Criptografar palavra{rs}             |    | 
           |   |  {g}[5] - Descriptografar palavra{rs}          |    |
           |   |  {g}[6] - Tabuada{rs}                          |    |  
           |   |  {g}[7] - Sair{rs}                             |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
                      
        {rs}
        ''')
  while True:
      try:
        return int(input('Digite a sua opção: '  ))
      except:
        print(r+'Opção inválida.'+rs)



# DEFININDO FAIXA ETARIA E SEXO (opção 1)
        
def FaixaEtaria():
  homem = 0
  mulher = 0
  idades_geral = 0
  idades_homem = 0
  idades_mulher = 0
  while True:
    try:
      qtd = int(input('Digite a quantidade de pessoas: '))
      break
    except:
      print(f'{r}Opção inválida, digite um número inteiro.{rs}')

  for pessoa in range(qtd):
    print('=='*20)
    print('\033[1;7;33m'+f'\t\t\tPESSOA {pessoa+1}{rs}')
    sexo = input(f"\tInforme o sexo da pessoa {pessoa+1}.\n [M] masculino\n [F] feminino\n Sexo: ")
    while sexo not in 'FfMm':
      sexo = input('\t\tDigite uma opção válida (F, f, M, m): ')
    if sexo == 'M' or sexo == 'm':
      homem = homem + 1
    if sexo == 'F' or sexo == 'f':
      mulher = mulher + 1
    # Pedindo e validando idade como número inteiro
    while True:
      try:
        idade = int(input(f'\tDigite a idade da pessoa {pessoa+1}: '))
        break
      except:
        print(f'{r}Opção inválida. Digite um número inteiro{rs}')
    # Validando como número positivo.
    while idade < 0 or idade >= 130:
      idade = int(input(f'{r}\t\tDigite uma idade válida, entre 0 e 130 anos: {rs}'))
    idades_geral = idades_geral + idade
    if sexo in 'mM': # Outro jeito de fazer o if(não é bom ficar variando,eu sei. Mas vou deixar dos dois jeitos para eu lembrar que existe.)
      idades_homem = idades_homem + idade
    if sexo in 'Ff':
      idades_mulher += idade

 # Evitando a mensagem de erro "ZeroDivisionError"
  if homem == 0:
    media_homem = 0
  else:
    media_homem = idades_homem/homem
  if mulher == 0:
    media_mulher = 0
  else:
    media_mulher = idades_mulher/mulher
  print(f'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        Pessoas pesquisadas: {qtd}
        Homens: {homem}
        Mulheres: {mulher}
        Média das idades: {idades_geral/qtd:.2f}
        Média das idades dos homens: {media_homem:.2f}
        Média das idades das mulheres: {media_mulher:.2f}''')
  # Adicionando a saída no arquivo
  arquivo = open("output.txt","a") # Tem que ser append,senão sobrescreve.
  arquivo.write(f'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
          Pessoas pesquisadas: {qtd}
          Homens: {homem}
          Mulheres: {mulher}
          Média das idades: {idades_geral/qtd}
          Média das idades dos homens: {media_homem}
          Média das idades das mulheres: {media_mulher}\n''')
  arquivo.close()  

# DEFININDO COMPARADOR (opção 2)
def comparar():
  print('=-'*10+f' {b}COMPARANDO NÚMEROS{rs} '+'-='*10)
  n1 = int(input('Digite o primeiro número: '))
  n2 = int(input('Digite o segundo número: '))
  n3 = int(input('Digite o terceiro número: '))
  
  maior = n1
  if n2 > n1 and n2 > n3:
      maior = n2
  if n3 > n1 and n3 > n2:
      maior = n3
  menor = n1
  if n2 < n3 and n2 < n1:
      menor = n2
  if n3 < n2 and n3 < n1:
      menor = n3
  # Caso forem iguais
  if n1 == n2 and n2 == n3:
    print('Os números são iguais')
  else:
    print(f"\tO {r}MENOR{rs} número digitado foi {r}{menor}{rs}.")
    print(f"\tO {b}MAIOR{rs} número digitado foi {b}{maior}{rs}.")
  # salvando no arquivo
  arquivo = open('output.txt','a')
  if n1 == n2 and n2 == n3:
    arquivo.write('=='*28+'\nOs números são iguais\n')
  else:
    arquivo.write('=='*28+f'''\n\tO MENOR número digitado foi {menor}.
  O MAIOR número digitado foi {maior}.\n''')
  arquivo.close()

# DEFININDO FIBONACCI (opção 3)
def fibo():
  print(b+'=='*12+' Sequência Fibonacci '+'=='*12+rs)
  while True:
    try:
      num = int(input('Digite o termo da sequência que você deseja saber: '))
      break
    except:
      print(f'{r}Opção inválida, digite um número inteiro.{rs}')
  f1 = 0
  f2 = 1
  for i in range(num):
    f3 = f1 + f2
    f1 = f2
    f2 = f3
  print(f'\tO {num}º termo da sequência de Fibonacci é {f1}')
  # Salvando no txt
  arquivo = open('output.txt','a') 
  arquivo.write('=='*28+'\n'+f'O {num}º termo da sequência de Fibonacci é {f1}'+'\n')
  arquivo.close()


# DEFININDO CRIPTOGRAFIA (opção 4)
chave = 0
palavra = ''
crypt = ''
def criptografar():
  global chave,palavra,crypt
  alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  while True:
    try:
      chave = int(input('Digite um número para definir a chave da criptografia: '))
      break
    except:
      print(f'{r}Opção inválida, digite um número inteiro.{rs}')
  palavra = input('Digite a palavra a ser criptografada: ').lower().strip() # Não sei como fazer pra não bugar se o usuário colocar espaços. Estou sem tempo pra pensar, vou usar .strip() pra prevenir isso.   
      
  crypt = ''
  for i in palavra:
    indice = alfabeto.index(i)
    nova_letra = alfabeto[(indice+chave)%26] # Tira o módulo de 26 que é a quantidade de letras do alfabeto
    crypt += nova_letra
  print(f'\t{g}Palavra:      {rs}',palavra)
  print(f'\t{g}Criptografia: {rs}', crypt)
  # Salvando no arquivo
  arquivo = open('output.txt','a')
  arquivo.write('=='*28+f'\n\tPalavra:  {palavra}\n\tCriptografia: {crypt}\n')
  arquivo.close()

# DEFININDO DESCRIPTOGRAFIA (opção 5)
def descriptografar():
  global palavra,chave,crypt
  alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  # Reaproveito as variáveis da função anterior,pois usei global
  descrypt = ''
  for i in crypt:
    indice = alfabeto.index(i)
    nova_letra = alfabeto[(indice-chave)%26] # Tira o módulo de 26 que é a quantidade de letras do alfabeto
    descrypt += nova_letra
  if palavra == '':
    print('Você tem que criptografar usando a função 4 primeiro.')
  else:
    print(f'\t{g}Criptografia:{rs}    ', crypt)
    print(f'\t{g}Descriptografia: {rs}', descrypt)
  #escrevendo no arquivo
  arquivo = open('output.txt','a')
  arquivo.write('=='*28+f'\n\tCriptografia:  {crypt}\n\tDescriptografia: {descrypt}\n')
  arquivo.close()
  


# DEFININDO CALCULADORA (opção 6)
def tabuada():
  print(''' 
   _____________________
  |  _________________  |
  | | TABUADA         | |
  | |_________________| |
  |  ___ ___ ___   ___  |
  | | 7 | 8 | 9 | | + | |
  | |___|___|___| |___| |
  | | 4 | 5 | 6 | | - | |
  | |___|___|___| |___| |
  | | 1 | 2 | 3 | | x | |
  | |___|___|___| |___| |
  | | . | 0 | = | | / | |
  | |___|___|___| |___| |
  |_____________________|
  ''')
  while True:
    try:
      num = int(input('Digite um numero para calcular a tabuada: '))
      break
    except:
      print(f'{r}Opção inválida, digite um número inteiro.{rs}')
     
  print(f'\033[1;45m\n\tTABUADA DO {num}\t\033[0;0m\n')
  print('=='*12)
  output = ' '
  for i in range(1,11):
    print(f'| {num}   x {i:4} = {num*i:4}    |')
    output += f'| {num}   x {i:4} = {num*i:4}    |\n'
  print('=='*12)
  
  # Salvando no txt
  arquivo = open('output.txt','a') 
  arquivo.write('=='*28+'\n'+output+'\n')
  arquivo.close()
  

    
#main
op = -1
while op!= 7:
  os.system('clear')
  op = menu()
  if op < 0 or op > 7:
    print(f"{r}Opção inválida{rs}")
  elif op == 1:
    FaixaEtaria()
  elif op == 2:
    comparar()
  elif op == 3:
    fibo()
  elif op == 4:
    criptografar()
  elif op == 5:
    descriptografar()
  elif op == 6:
    tabuada()
  elif op == 7:
    print('Saindo...')
    sleep(1)
    print('\tObrigado,volte sempre!')
    
  input('\n\t Tecle ENTER para continuar')


