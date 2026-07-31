def saque(saldo, sq):
    return saldo -  sq

def deposito(saldo , dp):
    return saldo +  dp

def extrato(saldo):
    return saldo

def banco():

    while True:
        print('acesse seu banco ...')
        ac = input('Deseja acessar o banco? ')
        while ac  == 'sim':
              senha =  input('SENHA >>>')
              saldo =  [5000]
              for i in range(3):
                  if senha == '123':
                      print('conta XXX')
                     
                      print('saldo', saldo)
                      op = input('Escolha  a operação: ')
                      if op == 'saque':
                          valor_saque =  float(input('Valor saque>>>'))
                          s  =  sum(saldo)
                          if valor_saque > s:
                              print('Sem saldo ...')
                          else:
                             
                              s =  sum(saldo)
                              print('Saque: R$', valor_saque)
                              print('Em conta', saque(s, valor_saque))
                              saldo.append(-valor_saque)
                              ac = input('Deseja acessar o banco? ')
                      elif op == 'deposito':
                          valor_deposito =  float(input('Valor deposito>>>'))
                          if valor_deposito:
                              s =  sum(saldo)
                              print('deposito: R$', valor_deposito)
                              print('Em conta', deposito(s, valor_deposito))
                              saldo.append(valor_deposito)
                              ac = input('Deseja continuar? ')
                      elif op == 'extrato':
                           print('extrato', saldo)                                            

banco()
