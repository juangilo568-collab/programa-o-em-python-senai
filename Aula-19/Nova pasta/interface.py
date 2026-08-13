import sqlite3
import tkinter as tk
from tkinter import messagebox


con = sqlite3.connect('cadastro.db')
cursor = con.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,            
        nome TEXT NOT NULL,
        email TEXT NOT NULL 
   )
''')


# crud




def criar_cliente():
    nome  =  nome_input.get()
    email = email_input.get()
    cursor.execute('INSERT INTO clientes (nome, email) values(?,?)', (nome, email))
    con.commit()
    messagebox.showinfo('', 'DADOS INSERIDOS COM SUCESSO')



def listar_clentes():
    cursor.execute('SELECT * FROM clientes')
    return cursor.fetchall()


def atualizar_mail(id_cliente, novo_email):
    cursor.execute('UPDATE clientes SET email=? WHERE id = ?', (novo_email, id_cliente))
    con.commit()


def deletar_cliente(id_cliente):
    cursor.execute('DELETE FROM clientes WHERE id = ?', (id_cliente,))
    con.commit()





root  =  tk.Tk()
root.geometry('500x350')


tk.Label(root, text =  'CADASTRO DE USUÁRIOS:').grid(row=0, column=0)


tk.Label(root, text =  'nome:').grid(row=1, column=1)
nome_input = tk.Entry(root)
nome_input.grid(row=2, column=1)  


tk.Label(root, text =  'e- mail:').grid(row=4, column=1)
email_input = tk.Entry(root)
email_input.grid(row=5, column=1)  


btn =  tk.Button(root, text= 'Inserir', command=criar_cliente)
btn.grid(row=6, column=1)





root.mainloop()

