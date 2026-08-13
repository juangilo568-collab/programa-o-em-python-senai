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
root.configure(bg = 'lightblue')
#root.iconbitmap('i.ico')


tk.Label(root, text =  'CADASTRO DE USUÁRIOS:', font = ('system','15') , bg='lightblue').grid(row=0, column=1)


tk.Label(root, text =  'nome:', bg='lightblue', font = ('system','10')).grid(row=3, column=1)
nome_input = tk.Entry(root)
nome_input.grid(row=3, column=2)  


tk.Label(root, text =  'e- mail:', bg='lightblue', font = ('system','10')).grid(row=5, column=1)
email_input = tk.Entry(root)
email_input.grid(row=5, column=2)  


btn =  tk.Button(root, text= 'Inserir', command=criar_cliente, width=15, font = ('system','10'))
btn.grid(row=7, column=1, pady=10)





root.mainloop()




