#CHAMO A BIBLIOTECA
import sqlite3
import tkinter as tk




#CRIO O ARQUIVO
c =  sqlite3.connect('nome.db')

#CRIO UM CURSOS PARA DECLARAR SQL NO PYTHON
cs = c.cursor()


cs.execute('''CREATE TABLE IF NOT EXISTS dados(
           
           nome TEXT,
           idade INTEGER      
           
           )''')

#ATUALIZO O BANCO
c.commit()


nome = input('Nome: ')
idade =  int(input('Idade:  '))


cs.execute('INSERT INTO dados values(?,?)', (nome, idade))


nome = input('Nome: ')
idade =  int(input('Idade:  '))


cs.execute('INSERT INTO dados values(?,?)', (nome, idade))


nome = input('Nome: ')
idade =  int(input('Idade:  '))


cs.execute('INSERT INTO dados values(?,?)', (nome, idade))
c.commit()



cs.execute('SELECT * FROM dados')
dados =  cs.fetchall()






for d in dados:
    print('nome:', d[0], 'idade:', d[1])


