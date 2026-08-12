import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter




def display():
    n1 = float(entrada1.get())
    n2 = float(entrada2.get())
    soma  =  n1  +  n2
    texto_.config(text = soma)
    mes  =  combo_box.get()
    texto_2.config(text= mes)
    
    




janela = tk.Tk()
janela.title('Testando tkinter')
janela.geometry('600x300')
janela.minsize(200, 200)  # width, height
janela.maxsize(500, 500)
janela.iconbitmap('i.ico')


# tk.Label(janela, text  =  'isso é um texto',font=('System', 30), fg= 'blue' ).pack()


sessao_1 =  tk.Frame(janela)
sessao_1.pack(pady=5)



entrada1  =  tk.Entry(sessao_1,width= 2,  font=('System', 15), fg= 'red')
entrada1.pack(side='left', padx=20)


entrada2  =  customtkinter.CTkEntry(sessao_1, font=('System', 15))
entrada2.pack(side='left')



sessao_2 =  tk.Frame(janela)
sessao_2.pack(pady=5)



btn  =  customtkinter.CTkButton(sessao_2, text = '+', command=display, font=('System', 15))
btn.pack(pady=15)



sessao_3 =  tk.Frame(janela)
sessao_3.pack(pady=5) 


texto_  =  tk.Label(sessao_3, text  =  'Resultado = ',font=('System', 15), fg= 'blue' )
texto_.pack()



combo_box = ttk.Combobox(
    janela,
    values=["Janeiro", "Fevereiro", "Março"],
    state="readonly"
)


combo_box.pack()



texto_2  =  tk.Label(sessao_3, text  =  '',font=('System', 15), fg= 'blue' )
texto_2.pack()



janela.mainloop()




















