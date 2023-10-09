
print('****Bem-vindo à Pizzaria Edivaldo Carmo de Souza LTDA****')
print('------------------------CARDÁPIO-------------------------')
print('|CÓDIGO | DESCIÇÃO   | PIZZA MÉDIA (M)| PIZZA GRANDE (G) |')
print('|    21 | Napolitana |       R$ 20,00 |        R$ 26,00  |')
print('|    22 | Margherita |       R$ 20,00 |        R$ 26,00  |')
print('|    23 | Calabresa  |       R$ 25,00 |        R$ 32,50  |')
print('|    24 | Toscana    |       R$ 30,00 |        R$ 39,00  |')
print('|    25 | Portuguesa |       R$ 30,00 |        R$ 39,00  |')
print('---------------------------------------------------------')

acumulador = 0
while (True):
   tamanho = input('Entre com o tamanho de pizza desejada (M/G): ')
   tamanho = tamanho.upper()
   if tamanho != 'M' and tamanho != 'G':
      print('Opção INVÁLIDA!!! Por favor digite uma opção VÁLIDA.')
      continue # se o usuário digitar algo inválido o laço de repetição se inicia novamente
   
   codigo = float(input('Entre com o código da pizza desejada (21/22/23/24/25): '))
   if codigo != 21 and codigo != 22 and codigo != 23 and codigo != 24 and codigo != 25:
      print('Opção INVÁLIDA!!! Por favor digite um código VÁLIDO.')
      continue # se o usuário digitar algo inválido o laço de repetição se inicia novamente
   
   if codigo == 21 and tamanho == 'M':
      print('Você escolheu a pizza sabor Napolitana tamanho M.')
      acumulador += 20
   
   elif codigo == 21 and tamanho == 'G':
      print('Você escolheu a pizza sabor Napolitana tamanho G.')
      acumulador += 26

   elif codigo == 22 and tamanho == 'M':
      print('Você escolheu a pizza sabor Margherita tamanho M.')
      acumulador += 20

   elif codigo == 22 and tamanho == 'G':
      print('Você escolheu a pizza sabor Margherita tamanho G.')
      acumulador += 26

   elif codigo == 23 and tamanho == 'M':
      print('Você escolheu a pizza sabor Calabresa tamanho M.')
      acumulador += 25

   elif codigo == 23 and tamanho == 'G':
      print('Você escolheu a pizza sabor Calabresa tamanho G.')
      acumulador += 32.50

   elif codigo == 24 and tamanho == 'M':
      print('Você escolheu a pizza sabor Toscana tamanho M.')
      acumulador += 30

   elif codigo == 24 and tamanho == 'G':
      print('Você escolheu a pizza sabor Toscana tamanho G.')
      acumulador += 39

   elif codigo == 25 and tamanho == 'M':
      print('Você escolheu a pizza sabor Portuguesa tamanho M.')
      acumulador += 30

   elif codigo == 25 and tamanho == 'G':
      print('Você escolheu a pizza sabor Portuguesa tamanho G.')
      acumulador += 39
        
   pedir_mais = input('Deseja pedir mais alguma pizza (S/digite outra tecla)?: ')
   pedir_mais = pedir_mais.upper()

   if pedir_mais == 'S':
      continue
   else:
      print(f'O valor total a ser pago é R$: {acumulador:.2f}')
      break

   