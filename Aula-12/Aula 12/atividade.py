# CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.
def par_ou_impar():
    numero = int(input("Digite um numero..."))
    if numero % 2 == 0:
        return  "Par"
    else:
        return "impar"

print(par_ou_impar())

# CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.

def multiplicacao():
    n1 = int(input("Digite o primeiro numero:"))
    n2 = int(input("Digite o segundo numero:"))
    n3 = int(input("Digite o terceiro numero:"))

    resultado = n1 * n2 * n3
    print("A multiplicacao de seus numeros são:", resultado)

multiplicacao()

# CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.

def elevado():