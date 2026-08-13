import sqlite3


# CRIO O BANCO DE DADOS
con = sqlite3.connect('Atividade.db')

# CRIO O CURSOR
cursor = con.cursor()


# CRIO A TABELA
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        email TEXT NOT NULL,
        endereco TEXT NOT NULL,
        trabalho TEXT NOT NULL,
        graduacao TEXT NOT NULL
    )
''')


# PEÇO OS DADOS
nome = input('Nome: ')
idade = int(input('Idade: '))
email = input('Email: ')
endereco = input('Endereço: ')
trabalho = input('Trabalho: ')
graduacao = input('Graduação: ')


# INSERO OS DADOS NA TABELA
cursor.execute('''
    INSERT INTO clientes
    (nome, idade, email, endereco, trabalho, graduacao)
    VALUES (?, ?, ?, ?, ?, ?)
''', (nome, idade, email, endereco, trabalho, graduacao))


# SALVO OS DADOS
con.commit()


# BUSCO OS DADOS DA TABELA
cursor.execute('SELECT * FROM clientes')

dados = cursor.fetchall()


# MOSTRO OS DADOS
for d in dados:
    print('ID:', d[0])
    print('Nome:', d[1])
    print('Idade:', d[2])
    print('Email:', d[3])
    print('Endereço:', d[4])
    print('Trabalho:', d[5])
    print('Graduação:', d[6])
    print('------------------------')


# FECHO A CONEXÃO
con.close()

