#definiton - incapsulamento e organização

def sistema_notas():
    n1 = float(input('nota 1'))
    n2 = float(input('nota 2'))

    if n1 and n2:
        media = (n1 + n2) / 2
        print(media)
    

sistema_notas()

def cadastro(quantidade, nomes, idades):
    for x in range(quantidade):
        nome = input('nome: ')
        idade  = input('idade: ')
        nomes.append(nome)
        idades.append(idade)
    return nomes, idades,
   


def reservas():
    lista_quartos = ['', "Simples", "Duplo" , "Luxo"]
    valores  =  [0,100.0,150.0,250.0]
    print(lista_quartos)
    print(valores)
    escolha  =  int(input('Escolha quarto >>>'))
    quantidade_dias = int(input('Quantidade de dias:  '))
    print(escolha)
    c =  quantidade_dias * valores[escolha]
    print('R$', c)
    l =  ['','pix','cc','cd']
    print(l)
    formapag =  int(input('digite a forma de pagamento: '))
   
    print(l[formapag])
    print('Obrigada volte sempre!')
   


def hotel_main():    

    nomes = []
    idades = []
    q =  int(input('Digite a quantidade de pessoas: '))
    dados_nomes, dados_idade = cadastro(q,nomes, idades)
    quantidade_pessoas = len(dados_nomes)
    print('quantidade de pessoas:', quantidade_pessoas)
    for n in range(quantidade_pessoas):
        print(f'Reserva do cliente {dados_nomes[n]}')
        reservas()


hotel_main() 
