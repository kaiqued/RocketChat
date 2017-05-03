import tkinter as tk
from tkinter import *




class application():
    #def message(self):
        #self.message=Entry(self.botao2)
        #self.message.pack(self.botao3)
        #pass
        
    def __init__(self):
        self.window=tk.Tk()
        self.frame1=Frame(self.window)
        self.frame1.pack()

        self.botao1=Button(self.frame1,text="send",background="white")
        self.botao1['font']=('Verdana','12','italic','bold')

        self.botao1['width']=10
        self.botao1['height']=2
        
        self.botao1.pack(side=BOTTOM)
        self.botao1.pack()
    
        #self.botao1.configure(command=self.message)
       

        self.botao2=tk.Button(self.frame1,background="green")
        self.botao2['width']=25
        self.botao2['height']=1
        self.botao2.pack(side=BOTTOM)

        self.botao3=tk.Button(self.frame1,background="red")
        self.botao3['width']=35
        self.botao3['height']=5
        self.botao3.pack(side=TOP)
        

        


    

    
        


    def iniciar(self):
        self.window.mainloop()

#app=application()
#app.iniciar()

#LOGIN E SENHA, ENTRADA
Logins=[]
Senhas=[]

janela = Tk()
janela.geometry("250x100+100+100")
janela.title("JANELA TOP")
janela["bg"]= "blue" 



tlogin = Label(janela, text = "Login: ", bg= "blue")
tlogin.grid(row = 1, column= 1)

tsenha = Label(janela, text = "Senha: ", bg = "blue")
tsenha.grid(row=2, column= 1)

login = Entry(janela)
login.grid(row=1, column=2)

senha = Entry (janela)
senha.grid(row= 2, column =2)
Logins=[]
Senhas=[]
def salvaloginsenha():
    lo=login.get()
    se=senha.get()
    Logins.append(lo)
    Senhas.append(se)

Entrar = Button(janela, text="Enter", bg="red",command = salvaloginsenha) 
Entrar.grid(row=3, column=2)


janela.mainloop()
