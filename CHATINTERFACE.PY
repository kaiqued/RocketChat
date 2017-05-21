from tkinter import *

import os

from chat_firebase import Rocket_Chat, receive

from firebase import firebase

clear=lambda:os.system('cls')
Logins = []
import PIL
FIREBASE_URL = "https://rocket-messenger.firebaseio.com/"
fb = firebase.FirebaseApplication(FIREBASE_URL,  None)

from tkinter.colorchooser import *


##  CLASSE CRIAR LOGIN  ##

class Criar:
    def __init__(self):
        self.inicial = Tk()
        self.inicial.title("Início")
        self.inicial.geometry("325x125+100+100")
        self.inicial['bg']='orange'
    
    
        self.log=StringVar()
        self.sen=StringVar()
        
        tusername = Label(self.inicial, text = "Username: ", fg= "black", bg= "orange")
        tpassword = Label(self.inicial, text = "Senha: ", fg= "black", bg= "orange")
        BoasVindas = Label(self.inicial, text="Escolha qual vai ser seu login e senha", bg="orange")
        self.Nome = Entry(self.inicial, width = 24)
        self.Senha = Entry(self.inicial, width = 24)
        Salvar = Button(self.inicial, text="Salvar", bg="red",command=self.salva, width=9)
        
        tusername.grid(row= 1, column= 0,sticky=E)
        tpassword.grid(row= 2, column= 0,sticky=E)
        BoasVindas.grid(row= 0, column= 1)
        self.Nome.grid(row= 1, column= 1)
        self.Senha.grid(row= 2, column= 1)
        Salvar.grid(row=3, column=1)
        nome = self.log.get()
        senha = self.sen.get()

        
    def salva(self):   
        nome = self.Nome.get()
        senha = self.Senha.get()
        Logins.append(nome)
        Logins.append(senha)
        user=Rocket_Chat(Logins[0],Logins[1])
        user.salva_data()
        lb["fg"]="green"
        lb["text"]="Login e senha salvos!"
        self.acaba()
    
        
    def clica(self):
        pass
        
        
    
    def inicia(self):
        self.inicial.mainloop()
    
    
    def acaba(self):
        self.inicial.destroy()
    



        
###   TELA INICIAL DE LOGIN   ###



#  CRIA A JANELA  #
Tinicio = Tk()

Tinicio.geometry("325x125+100+100")
Tinicio.title("Entrada")
Tinicio["bg"]= "light blue"

#  DEFINE AS FUNÇÕES  #
def salva_login_senha():   
    app = Criar()
    app.inicia()
    

def checa_login_senha():
    login = username.get()
    secret = password.get()
    saves = fb.get("https://rocket-messenger.firebaseio.com/","data")
    
    for lg in saves:
        name=saves[lg]["name"]
        senha=saves[lg]["password"]
        if name==login and secret==senha:
            Logins.append(login) 
            Logins.append(secret)
            try:
                Tinicio.destroy()
            except:
                print("erro 1")
        
        else:
            try:
                lb["fg"]="red"
                lb["text"]="Login ou Senha não existe!"
            except:
                print("erro    2")
#  DEFINE OS WIDGETS  #

lb = Label(Tinicio, text= "", bg= "light blue")
tusername = Label(Tinicio, text = "Username: ", fg= "black", bg= "light blue")
tpassword = Label(Tinicio, text = "Senha: ", fg= "black", bg= "light blue")
BoasVindas = Label(Tinicio, text="Seja bem-vindo ao Rocket Chat!", bg="light blue", width=24)
username = Entry(Tinicio, width = 24)
password = Entry(Tinicio, width = 24,show='*')
Criar = Button(Tinicio, text="Criar", bg="red",command=salva_login_senha, width=9)
Entrar = Button(Tinicio, text="Enter", bg="red",command=checa_login_senha,width=9)

#  POSICIONA OS WIDGETS  #

lb.grid(row= 5, column= 1)
tusername.grid(row= 1, column= 0,sticky=E)
tpassword.grid(row= 2, column= 0,sticky=E)
BoasVindas.grid(row= 0, column= 1)
username.grid(row= 1, column= 1)
password.grid(row= 2, column= 1)
Criar.grid(row=4, column=1,sticky=E)
Entrar.grid(row=4, column=1,sticky=W)

Tinicio.mainloop()



### MENU ###
Tassunto = Tk()
Tassunto.geometry("+40+40")
Tassunto.title("Menu de Assuntos")
Tassunto["bg"] = "light green"
TextoInicio = Label (Tassunto, text = "Selecione o assunto desejado:", bg = "light blue").pack(anchor=NW)
def assunto():
    Tassunto.destroy()
    
#TextoInicio = Text(Tassunto, text = "Escolha a sala que deseje entrar,seu cuzão",bg = "black")
Button(Tassunto, text='Futebol', command=assunto,width=9).pack(anchor="center")
Button(Tassunto, text='Politica', command=assunto,width=9).pack(anchor="center")
Button(Tassunto, text='Celebridades', command=assunto,width=9).pack(anchor="center")
Button(Tassunto, text='Vôlei', command=assunto,width=9).pack(anchor="center")
Button(Tassunto, text='Tecnologia', command=assunto,width=9).pack(anchor="center")
Button(Tassunto, text='Culinária', command=assunto,width=9).pack(anchor="center")
Tassunto.mainloop()








###  TELA DO CHAT  ###


#  CRIA A TELA  #

class Chat(Rocket_Chat) :
    def __init__(self, Logins):
        self.Chat = Tk()
        self.Chat.title("Rocket Chat")
        self.Chat.geometry("500x600+40+40")
        self.Chat['bg'] = 'gray'
        user.post()
        
        
        ## Widgets ##
        self.opcoes = Frame(self.Chat, bg= "light blue")
        self.opcoes.pack(fill=BOTH)
        
        self.input_user = StringVar()
        self.input_field = Entry(self.Chat, text=self.input_user)
        reading=receive()
        self.TextoInicio = Label(self.opcoes, text = "Bem vindo ao Rocket Chat", bg = "light blue")
        self.scroll=Scrollbar(self.Chat)
        self.label = Text(self.Chat,height=200,width=200, bg= "gray")
        self.exit = Button(self.opcoes, text = "Fugir", command = self.sair, bg= "grey")
        self.cor = Button(self.opcoes, text='Select Color', command=self.getColor)
        
        
        
        
        ## Coloca na tela ##
        
        self.exit.pack(side = RIGHT)
        self.TextoInicio.pack(side= LEFT)
        self.input_field.pack(side=BOTTOM, fill=X)
        self.label.pack()
        self.input_field.bind("<Return>", self.Envia)
        self.cor.pack()
        
        
        self.Chat.after(2000, self.atualiza)
    
    
    def getColor(self):
        color = askcolor()
        (y,x) = color
        self.label["bg"]=x
        self.Chat["bg"]= x
        
    
    
    
    
    
    
    def Envia(self,event):

        self.label.delete('1.0', END) 
        reading=receive()
        
        for x in reading:
            mensagem=reading[x]["message"]
            pessoa=reading[x]["name"]
            t0t=("{0}: {1}\n".format(pessoa,mensagem))
            self.label.insert(END,t0t, 'bold_italics') 
        self.label.see("end")
        self.input_get = self.input_field.get()
        
        user.send(self.input_get)
        self.texto = "{0}: {1}  \n".format(user.nome, self.input_get)
        self.scroll.config(command=self.label.yview)
        self.label.configure(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=RIGHT, fill=Y)        
        self.input_user.set('')
        self.label.insert(END,self.texto, 'bold_italics') 
        self.label.pack(side=BOTTOM)
    
    

        return "break"

    def atualiza(self):
        self.label.delete('1.0', END) 
        reading=receive()
        
        for x in reading:
            mensagem=reading[x]["message"]
            pessoa=reading[x]["name"]
            t0t=("{0}: {1}\n".format(pessoa,mensagem))
            self.label.insert(END,t0t, 'bold_italics') 
        self.label.see("end")
        self.Chat.after(20, self.atualiza)
        return 0

    
    
    def sair(self):
        self.acaba()
    
    
    
    
    def inicia(self):
        self.Chat.mainloop()
    
    
    def acaba(self):
        self.Chat.destroy()
        
