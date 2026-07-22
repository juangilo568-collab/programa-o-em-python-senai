#calculadora

n1  =  float(input('Digite um número:'))
op =  input('Digite a operação: ')
n2  =  float(input('Digite um número'))
resultado =  (op == '+' and (n1 +  n2)) or (op == '-' and n1 - n2) or (op == '*' and n1 * n2) or (op == '/' and n1 /n2)


print(resultado)


#Constante
def dado():
    return 20

DADO = dado()

print(DADO)

#calculo de imc
altura = float(input('Altura:'))
peso = float(input('Peso:'))
imc = peso/(altura **2)

print(imc)

idade  =  int(input('Idade: '))
carta_motorista = input('Possui carta: ')


resultado = (idade >= 18 and carta_motorista == 'sim' and ('Pode dirigir...')) or ('Não pode ...')


print(resultado)