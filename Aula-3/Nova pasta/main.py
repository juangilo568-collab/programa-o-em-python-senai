#crtl + f5
#shift + enter
print('Hello, word!')

#dados primitivos
print('strings == textos')
print(10+2) #int inteiro
print(5.5 - 1.2) #float real
print(True + True) #boleanos
print(False) #boleanos
print(type(10))

#type - verificar o tipo de dado

# + sinais aritméticos

# print(10 +  2) soma
# print(10 -  2) subtração
# print(10 *  2) multiplicação
# print(10.0 /  2) divisão
# print(10 //  2) divisão  c/ 2 barras
# print(10 % 2) módulo 
# print(16 ** 2) potencia elevado

#sinais lógicos 

print(10 > 2) #maior
print(10 < 2) #menor
print(10 >= 2) #maior ou igual
print(10 <= 2) #menor ou igual
print(10 == 2) #igual
print(10 != 2)#diferente

nota_1 = 10
nota_2 = 6
nota_3 = 9


media = (nota_1 + nota_2 + nota_3)/3
print('NOTA:')
print(round(media, 2))


aprovado = media >= 7
recuperacao =  media >= 5 and media < 7
reprovado = media < 5


resultado =  (media >=7 and print('Aprovado')) or  (media >=5 and media < 7 and print('Recuperação')) or (media <5 and print('reprovado'))  


# print('situação do aluno: ')
# print('Aprovado:')
# print(aprovado)
# print('Recuperação:')
# print(recuperacao)
# print('Reprovado:')
# print(reprovado)


#Calculadora


valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
print(valor1 + valor2)

