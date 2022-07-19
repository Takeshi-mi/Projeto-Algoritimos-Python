'''
2. Retornar o maior, menor e média
• Usuário informa a 3 números e depois mostre o maior, o menor e a média
de todos os números.
'''
def comparar():
  print('=-'*10+' COMPARANDO NÚMEROS '+'-='*10)
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
    print(f"O MENOR número digitado foi {menor}.")
    print(f"O MAIOR número digitado foi {maior}.")