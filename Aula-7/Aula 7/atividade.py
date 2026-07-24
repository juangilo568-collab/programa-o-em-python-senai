#Exercício 0: Escreva um programa que use a função range() para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.
lista1 =  list(range(2,21, 2))
print(lista1)

#Exercício 1: Crie uma lista chamada numeros que contenha os números inteiros de 1 a 10 e imprima-a na tela.
numeros = list(range(1,10))
print(numeros)

#Exercício 2: Acesse e imprima o terceiro elemento da lista numeros.
lista = list(range(1,6))
print(lista[3])

#Exercício 3: Adicione o número 9 à lista numeros e imprima a lista atualizada.
lista.insert(5, 9)
print(lista)

#Exercício 4: Remova o número 5 da lista numeros e imprima a lista resultante.
lista.remove(5)
print(lista)

#Exercício 5: Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista numeros e imprima o resultado.
carros = ['Corsa','Palio','Uno']

print(carros, numeros)