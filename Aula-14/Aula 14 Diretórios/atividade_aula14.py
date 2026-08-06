#Criar e ler um arquivo

import os 

#arquivo criado e escrito
with open('arquivo.txt', 'w', encoding = "utf-8") as conteudo:
    conteudo.write("Meu nome é Juan")
    pass

#arquivo lido
with open("arquivo.txt", "r", encoding = 'utf-8') as arquivo:
    a = arquivo.read()
    print(a)

#Diretório
#os.mkdir('Pasta nova')

#Diretório renomeado
import os
#os.rename("Nova pasta", "Nova pasta2")

#Listar arquivos no diretório
import os
with os.scandir('Nova pasta2') as entrada:
    for arquivo in entrada:
        if arquivo.is_file():
            print(f'Arquivo encontrado: {arquivo.name}')


#Copiar o diretório todo 
import shutil
#shutil.copytree('Nova pasta2', "Nova pasta3")

#Remover um Diretório
import shutil
shutil.rmtree('C:/Users/Aluno/Downloads/Nova pasta/Nova pasta2')