import sqlite3 # banco de dados
import tkinter as tk # interface 
from tkinter import messagebox # caixas de mensagens
from tkinter import ttk # interface grafica tb
import customtkinter as ctk

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('dark-blue')


def conectar():
    return sqlite3.connect('Cadastro2.db')


def criar_tabela():
    conn = conectar()
    c= conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        endereco TEXT NOT NULL             
        )       
    ''')
    conn.commit()
    conn.close()
  


# CREATE
def inserir_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()

    if nome and email:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO usuarios(nome, email, telefone, endereco) VALUES(?,?,?,?)',(nome, email,telefone,endereco))
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'DADOS INSERIDOS COM SUCESSO!') 
        mostrar_usuario()
    else:
        messagebox.showerror('ERRO', 'ALGO DEU ERRADO!') 


# READ
def mostrar_usuario():
    for row in tree.get_children():   
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()    
    c.execute('SELECT * FROM usuarios')
    usuarios = c.fetchall()
    for usuario in usuarios:
        tree.insert("", "end", values=(usuario[0], usuario[1],usuario[2],usuario[3], usuario[4]))
    conn.close()    


# DELETE
def delete_usuario():
    dado_del = tree.selection()
    if dado_del:
       user_id = tree.item(dado_del)['values'][0]
       conn = conectar()
       c = conn.cursor()    
       c.execute('DELETE FROM usuarios WHERE id = ? ',(user_id,))
       conn.commit()
       conn.close()
       messagebox.showinfo('', 'DADO DELETADO')
       mostrar_usuario()

    else:
       messagebox.showerror('', 'OCORREU UM ERRO')  


# UPDATE 
       
def editar():
     selecao = tree.selection()
     if selecao:
         user_id = tree.item(selecao)['values'][0]
         novo_nome = entry_nome.get()
         novo_email = entry_email.get()
         novo_telefone = entry_telefone.get()
         novo_endereco = entry_endereco.get()

         if novo_nome and novo_email:
            conn = conectar()
            c = conn.cursor()    
            c.execute('UPDATE usuarios SET nome = ? , email = ? , telefone = ? , endereco = ? WHERE id = ? ', (novo_nome,novo_email,novo_telefone,novo_endereco, user_id))
            conn.commit()
            conn.close()  
            messagebox.showinfo('', 'DADOS ATUALIZADOS')
            mostrar_usuario()

         else:
             messagebox.showwarning('', 'PREENCHA TODOS OS CAMPOS')

     else:
            messagebox.showerror('','ALGO DEU ERRADO!')


# ==========================================================
# INTERFACE
# ==========================================================

janela = ctk.CTk()
janela.title('CRUD')
janela.geometry('900x700')


# TÍTULO

titulo = ctk.CTkLabel(
    janela,
    text='CADASTRO DE USUÁRIOS',
    font=('Arial', 24, 'bold')
)
titulo.pack(pady=20)


# CAMPO NOME

entry_nome = ctk.CTkEntry(
    janela,
    placeholder_text='Nome',
    width=400
)
entry_nome.pack(pady=5)


# CAMPO EMAIL

entry_email = ctk.CTkEntry(
    janela,
    placeholder_text='E-mail',
    width=400
)
entry_email.pack(pady=5)


# CAMPO TELEFONE

entry_telefone = ctk.CTkEntry(
    janela,
    placeholder_text='Telefone',
    width=400
)
entry_telefone.pack(pady=5)


# CAMPO ENDEREÇO

entry_endereco = ctk.CTkEntry(
    janela,
    placeholder_text='Endereço',
    width=400
)
entry_endereco.pack(pady=5)


# BOTÕES

frame_botoes = ctk.CTkFrame(
    janela,
    fg_color='transparent'
)
frame_botoes.pack(pady=10)


btn_salvar = ctk.CTkButton(
    frame_botoes,
    text='Salvar',
    command=inserir_usuario
)
btn_salvar.grid(
    row=0,
    column=0,
    padx=5
)


btn_deletar = ctk.CTkButton(
    frame_botoes,
    text='Deletar',
    command=delete_usuario
)
btn_deletar.grid(
    row=0,
    column=1,
    padx=5
)


btn_atualizar = ctk.CTkButton(
    frame_botoes,
    text='Atualizar',
    command=editar
)
btn_atualizar.grid(
    row=0,
    column=2,
    padx=5
)


# TABELA

columns = ('ID', 'NOME', 'E-MAIL','TELEFONE', 'ENDEREÇO')

tree = ttk.Treeview(
    janela,
    columns=columns,
    show='headings'
)

tree.pack(
    padx=20,
    pady=15,
    fill='both',
    expand=True
)


for col in columns:
    tree.heading(col, text=col)


# CRIA TABELA

criar_tabela()

mostrar_usuario()


janela.mainloop()