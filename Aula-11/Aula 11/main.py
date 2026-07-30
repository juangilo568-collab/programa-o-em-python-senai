try: 
    numero = int(input('inteiro:'))
except ValueError as erro:
    print(erro)

try:
    n1  =  int(input('nº: '))
    n2  =  int(input('nº: '))
    n1 / n2
    l = [1,2,3]
    print(l[n1])


except   ZeroDivisionError as erro:
    print(erro)


except IndexError as erro:
    print(erro)    


except ValueError as erro: 
    print(erro) 