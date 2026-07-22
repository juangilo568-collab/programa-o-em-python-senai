# concatenação

# +
print('isso é um texto ' + ' ' + '10')
# print(10 + 10)

# ,
print('isso é um texto ',  '10')

# % 
print('isso é um texto  %d'%(10))

# .format()
print('isso é um texto  {}'.format(10))

# f-string
print(f'isso é um texto  {10} ')

#1
msg = 'Boas vindas'
print(msg)

#2
idade = int(input("Digite sua idade:"))
resultado  = idade >=18 
print(resultado)


#3
n1 = float(input("Digite o primeiro número de sua multiplicação:"))
n2 = float(input("Digite o segundo núemro de sua multiplicação:"))

print('O resulado de sua multiplicação é: ', n1 * n2)

#4
numero1 = int(input('Digite o primeiro número da sua divisão:'))
numero2 = int(input('Digite o segundo número da sua divisão:'))

print('O resultado de sua divisão é:', numero1 / numero2)

#5

num1 = int(input('Digite o primeiro número da sua subtração:'))
num2 = int(input('Digite o segundo número da sua subtração:'))

print('O resultado de sua subtração é:', num1 - num2)

#6

number1 = int(input('Digite o primeiro número da sua divisão inteira:'))
number2 = int(input('Digite o segundo número da sua divisão inteira:'))

print('O seu resultado é:', number1 // number2)

#7

decimal1 = 10.5
decimal2 = 20.5
decimal3 = 30.7
decimal4 = 40.8

print('O resultado da sua multiplicação decimal é =', decimal1 * decimal2 * decimal3 * decimal4)

#8

numero = int(input('Digite um número:'))
print("O dobro de seu número é=", numero * 2)

#9 Sistema de cadastro

nome = str(input('Digite seu nome:'))
email = str(input('Digite seu e-mail:'))
idade = int(input("Digite sua idade:"))
cidade = str(input('Qual sua cidade?'))
graduação = str(input('Informe sua graduação:'))
estado_civil = str(input('Informe seu estado civil:'))

print('Seus dados estão correto?:',
      nome,
      email,
      idade,
      cidade,
      graduação,
      estado_civil)
