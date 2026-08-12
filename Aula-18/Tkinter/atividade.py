
# atividade a partir desse código


#biblioteca importada e apelidada de "as"
import tkinter as tk




#criação de janela, largura e texto
janela  =  tk.Tk()
janela.geometry('1700x750')
janela.title('FORMULÁRIO')



# TITULO DO FORM


titulo  =  tk.Label(janela, text='FORMULARIO DE CADASTRO')
titulo.pack()


# TÍTULO  DO NOME |  INPUT DO NOME

nome_texto = tk.Label(janela, text  =  'Nome')
nome_texto.pack()


nome_input =  tk.Entry(janela)
nome_input.pack()

#Idade

idade = tk.Label(janela, text = "Informe sua idade")
idade.pack()

idade = tk.Entry(janela)
idade.pack()
 
#Email

Email = tk.Label(janela, text = "Informe seu e-mail")
Email.pack()

Email = tk.Entry(janela)
Email.pack()


#Endereco

Endereco = tk.Label(janela, text = "Informe seu endereco")
Endereco.pack()

Endereco = tk.Entry(janela)
Endereco.pack()



#Celular
Celular = tk.Label(janela, text = "Informe seu celular")
Celular.pack()

Celular = tk.Entry(janela)
Celular.pack()


#Cep
Cep = tk.Label(janela, text = "Informe seu cep")
Cep.pack()

Cep = tk.Entry(janela)
Cep.pack()

#Cidade
Cidade = tk.Label(janela, text = "Informe seu cidade")
Cidade.pack()

Cidade = tk.Entry(janela)
Cidade.pack()

#Cursos
Cursos = tk.Label(janela, text = "Informe seus cursos")
Cursos.pack()

Cursos = tk.Entry(janela)
Cursos.pack()

def enviar():
    print("CADASTRO DO CLIENTE")
    print("Nome:", nome_input.get())
    print("Idade:", idade.get())
    print("E-mail:", Email.get())
    print("Endereço:", Endereco.get())
    print("Celular:", Celular.get())
    print("CEP:", Cep.get())
    print("Cidade:", Cidade.get())
    print("Cursos:", Cursos.get())

btn = tk.Button(janela, text="Enviar", command=enviar)
btn.pack()

janela.mainloop()


# subir para o github 