# Exibe o cabeçalho da loja e o cardápio
print('****Bem-vindo à loja Gelados Edivaldo Carmo de Souza LTDA****')
print('-------------------------CARDÁPIO--------------------------')
print('--------| Tamanho | Cupuaçu (CP)  |   Açaí (AC)   |--------')
print('--------|    P    |    R$ 10,00   |     R$ 12,00  |--------')
print('--------|    M    |    R$ 15,00   |     R$ 17,00  |--------')
print('--------|    G    |    R$ 19,00         R$ 21,00  |--------')

# Inicializa a variável que irá acumular o valor total do pedido
acumulador = 0

# Loop principal que permite ao usuário fazer pedidos repetidamente
while (True):
    sabor = input('Entre com o sabor desejado (CP/AC): ') # Solicita usuário o sabor
    sabor = sabor.upper()

    if sabor != 'CP' and sabor != 'AC': # Verifica se o sabor é válido
      print('Opção INVÁLIDA!!! Por favor digite um sabor VÁLIDO.')
      continue

    # Solita ao usuário tamanho desejado
    tamanho = input('Entre com o tamanho desejado (P/M/G): ')
    tamanho = tamanho.upper()
    
    # Verifica se o tamanho é válido
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':  
      print('Opção INVÁLIDA!!! Por favor digite uma opção VÁLIDA.')
      continue 

    # Calcula o valor do pedido com base no sabor e tamanho escolhidos
    if sabor == 'CP' and tamanho == 'P':
      print('Você escolheu sabor Cupuaçu tamanho P.')
      acumulador += 10

    elif sabor == 'CP' and tamanho == 'M':
      print('Você escolheu sabor Cupuaçu tamanho M.')
      acumulador += 15

    elif sabor == 'CP' and tamanho == 'G':
      print('Você escolheu sabor Cupuaçu tamanho G.')
      acumulador += 19
    
    elif sabor == 'AC' and tamanho == 'P':
      print('Você escolheu sabor Açaí tamanho P.')
      acumulador += 12

    elif sabor == 'AC' and tamanho == 'M':
      print('Você escolheu sabor Açaí tamanho M.')
      acumulador += 17

    elif sabor == 'AC' and tamanho == 'G':
      print('Você escolheu sabor Açaí tamanho G.')
      acumulador += 21

    # Pergunta ao usuário se deseja fazer mais pedidos ou encerrar o pedido
    pedir_mais = input('Deseja fazer mais algum pedido (S/digite outra tecla)?: ')
    pedir_mais = pedir_mais.upper()

    # Se o usuário escolher continuar, o loop continuará, caso contrário, o valor total é exibido e o loop é encerrado
    if pedir_mais == 'S':
      continue
    else:
      print(f'O valor total a ser pago é R$: {acumulador:.2f}')
      break

   