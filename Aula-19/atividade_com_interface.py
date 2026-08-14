#importo as bibliotecas
import sqlite3
import customtkinter as ctk

# definição de cores
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')


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

#salva o processo que acabei de fazer
con.commit()


select_id = None


# FUNÇÕES

def atualizar_lista():

#espaço onde será colocado a lista do cadastro
    for widget in scroll.winfo_children():

#apago os resultados pois o próximo cadastro entrara na frente, atualizado
        widget.destroy()

#executo todos os dados (*) da tabela em ordem
    cursor.execute('SELECT * FROM clientes ORDER BY id DESC')


    for cliente in cursor.fetchall():

        nome = cliente[1]

        btn = ctk.CTkButton(
            scroll,
            text=nome,
            anchor='w',
            fg_color=('gray85', 'gray20'),
            text_color=('black', 'white'),
            hover_color=('gray', 'gray30'),
            command=lambda c=cliente: selecionar(c)
        )

        btn.pack(fill='x', padx=2, pady=2)


def selecionar(cliente):

    global select_id

    select_id = cliente[0]

    entry_nome.delete(0, 'end')
    entry_nome.insert(0, cliente[1])

    entry_idade.delete(0, 'end')
    entry_idade.insert(0, cliente[2])

    entry_email.delete(0, 'end')
    entry_email.insert(0, cliente[3])

    entry_endereco.delete(0, 'end')
    entry_endereco.insert(0, cliente[4])

    entry_trabalho.delete(0, 'end')
    entry_trabalho.insert(0, cliente[5])

    entry_graduacao.delete(0, 'end')
    entry_graduacao.insert(0, cliente[6])

    btn_save.configure(text='Atualizar')


def limpar():

    global select_id

    select_id = None

    entry_nome.delete(0, 'end')
    entry_idade.delete(0, 'end')
    entry_email.delete(0, 'end')
    entry_endereco.delete(0, 'end')
    entry_trabalho.delete(0, 'end')
    entry_graduacao.delete(0, 'end')

    btn_save.configure(text='Salvar')


def salvar():

    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    endereco = entry_endereco.get()
    trabalho = entry_trabalho.get()
    graduacao = entry_graduacao.get()

    if not nome:
        return

    if select_id:

        cursor.execute('''
            UPDATE clientes
            SET nome = ?,
                idade = ?,
                email = ?,
                endereco = ?,
                trabalho = ?,
                graduacao = ?
            WHERE id = ?
        ''', (
            nome,
            idade,
            email,
            endereco,
            trabalho,
            graduacao,
            select_id
        ))

    else:

        cursor.execute('''
            INSERT INTO clientes
            (nome, idade, email, endereco, trabalho, graduacao)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            nome,
            idade,
            email,
            endereco,
            trabalho,
            graduacao
        ))

    con.commit()

    limpar()
    atualizar_lista()


def excluir():

    if select_id:

        cursor.execute(
            'DELETE FROM clientes WHERE id = ?',
            (select_id,)
        )

        con.commit()

        limpar()
        atualizar_lista()


# INTERFACE

app = ctk.CTk()
app.title('Banco de dados')
app.geometry('500x600')


# INPUTS

entry_nome = ctk.CTkEntry(
    app,
    placeholder_text='Nome'
)
entry_nome.pack(
    padx=20,
    pady=(20, 5),
    fill='x'
)


entry_idade = ctk.CTkEntry(
    app,
    placeholder_text='Idade'
)
entry_idade.pack(
    padx=20,
    pady=5,
    fill='x'
)


entry_email = ctk.CTkEntry(
    app,
    placeholder_text='Email'
)
entry_email.pack(
    padx=20,
    pady=5,
    fill='x'
)


entry_endereco = ctk.CTkEntry(
    app,
    placeholder_text='Endereço'
)
entry_endereco.pack(
    padx=20,
    pady=5,
    fill='x'
)


entry_trabalho = ctk.CTkEntry(
    app,
    placeholder_text='Trabalho'
)
entry_trabalho.pack(
    padx=20,
    pady=5,
    fill='x'
)


entry_graduacao = ctk.CTkEntry(
    app,
    placeholder_text='Graduação'
)
entry_graduacao.pack(
    padx=20,
    pady=5,
    fill='x'
)


# SESSÃO DOS BOTÕES

btn_frame = ctk.CTkFrame(
    app,
    fg_color='transparent'
)

btn_frame.pack(
    padx=20,
    pady=10,
    fill='x'
)


btn_save = ctk.CTkButton(
    btn_frame,
    text='Salvar',
    width=100,
    command=salvar
)

btn_save.pack(
    side='left',
    expand=True,
    padx=2
)


btn_delete = ctk.CTkButton(
    btn_frame,
    text='Deletar',
    fg_color='red',
    hover_color='darkred',
    width=100,
    command=excluir)

btn_delete.pack(
    side='left',
    expand=True,
    padx=2)


btn_clear = ctk.CTkButton(
    btn_frame,
    text='Limpar',
    fg_color='green',
    hover_color='darkgreen',
    width=100,
    command=limpar)

btn_clear.pack(
    side='left',
    expand=True,
    padx=2)


# LISTA

scroll = ctk.CTkScrollableFrame(app)

scroll.pack(
    padx=20,
    pady=10,
    fill='both',
    expand=True
)


# ATUALIZA A LISTA

atualizar_lista()


# INICIA A INTERFACE

app.mainloop()


# FECHA A CONEXÃO

con.close()
