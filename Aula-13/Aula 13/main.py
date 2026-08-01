# ***DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***  
# ***1 - Função -  cumprimentar o cliente***
# ***2 - Função - restaurante***
# ***3 - Sugestão utilize listas  e loops***




def cumprimentar(nome):
    return f'SEJA BEM VINDO! {nome}'


def restaurante():
    lista_compras = {'meus_produtos':[],'valores_produtos':[]} 
    cumprimentar('Ana')
    p =  input('Deseja comprar? ')
    
    while p  == 'sim':
        
        produ = {
        'lista_prod' :['','1 - SALADA', '2 -  MACARRONADA', '3 - SANDUICHE', '4  - SORVETE'],
        'valores' : [0,25.55,30.60,80.0,35.70]
        }


          
        print(produ)
        


        try:
            produto = int(input('Digite o id do produto: '))
            if produto:
                m_prod = produ['lista_prod'][produto]
                lista_compras['meus_produtos'].append(m_prod)
                lista_compras['valores_produtos'].append(produ['valores'][produto])
                print(lista_compras)
                p =  input('Deseja continuar? ')
        except ValueError:
            print(f'escolha um produto através do indice 1 - 2  -3 - 4')    
    else:
        total =  sum(lista_compras['valores_produtos'])
        print('R$', round(total, 2))
        print('obrigada volte sempre')    


restaurante()       