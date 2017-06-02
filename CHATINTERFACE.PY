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


##  CLASSE CRIAR CHAT  ##


class Chat(Rocket_Chat) :
    def __init__(self, Logins,assunto):
        self.assunto=assunto
        self.Chat = Tk()
        self.Chat.title("Rocket Chat")
        self.Chat.geometry("500x600+40+40")
        self.Chat['bg'] = 'gray'
        user = Rocket_Chat(Logins[0], Logins[1])
        user.post(assunto)
                ## Widgets ##
        self.opcoes = Frame(self.Chat, bg= "light blue")
        self.opcoes.pack(fill=BOTH)
        
        self.input_user = StringVar()
        self.input_field = Entry(self.Chat, text=self.input_user)
        self.input_field.focus()
        reading=receive(assunto)
        self.TextoInicio = Label(self.opcoes, text = "Bem vindo ao Rocket Chat", bg = "light blue")
        self.scroll=Scrollbar(self.Chat)
        self.label = Text(self.Chat,height=200,width=200, bg= "gray")
        self.exit = Button(self.opcoes, text = "Menu", command = self.sair, bg= "grey")
        self.edita = Button(self.opcoes, text='Editar texto e fundo', command=self.Edita)
        
        
        
        
        ## Coloca na tela ##
        
        self.exit.pack(side = RIGHT)
        self.TextoInicio.pack(side= LEFT)
        self.input_field.pack(side=BOTTOM, fill=X)
        self.label.pack()
        self.input_field.bind("<Return>", self.Envia)
        self.edita.pack()
        
        
        self.Chat.after(2000, lambda:self.atualiza(assunto))
    
    ##  TELA PARA EDIÇÃO DE TEXTO  ## 
    def Edita(self):
        
        def sel():
           size = str(var.get())
           font = str(vari.get())
           more = str(varia.get())
           self.label["font"]=font, size, more
           
        root = Tk()
        root["bg"]="gray"
        root.title("Editar")
        var = IntVar()
        vari = StringVar()
        varia= StringVar()
        
        scale = Scale( root, variable = var, cursor = "dot", from_=10, to= 100, orient=HORIZONTAL,bg = "gray")
        scale.pack(anchor=CENTER)
        button = Button(root, text="Atualizar",font= ('Verdana','12','italic','bold'), command=sel)
        button.pack(side=BOTTOM)
        
        
        f1=Frame(root, bg="gray")
        f2=Frame(root, bg="gray")
        f3=Frame(root, bg="gray")
        
        f1.pack(side=TOP)
        f2.pack(side=LEFT)
        f3.pack(side=RIGHT)
        
        Rmore = Radiobutton(f3, text="Negrito", variable=varia, value="bold",bg = "gray")
        Rmore.pack()
        
        Rmore1= Radiobutton(f3, text="Itálico", variable=varia, value="italic",bg = "gray")
        Rmore1.pack()
        
        Rmore2= Radiobutton(f3, text="Nenhum", variable=varia, value="",bg = "gray")
        Rmore2.pack()
        
        Rfont = Radiobutton(f2, text="Times", variable=vari, value="Times",bg = "gray")
        Rfont.pack( anchor = W )
        
        Rfont1= Radiobutton(f2, text="Verdana", variable=vari, value="Verdana",bg = "gray")
        Rfont1.pack( anchor = W )
        
        corfundo=Button(root, text= "Cor do fundo",bg = "gray", command=self.getColor)
        corfundo.pack(anchor=CENTER)
        root.mainloop()
        
        
        
        
        
    ##  MÉTODO DE MUDAR A COR DO FUNDO ##
    def getColor(self):
        color = askcolor()
        (y,x) = color
        self.label["bg"]=x
        self.Chat["bg"]= x
        
    
    ## MÉTODO DE ENVIAR MENSAGEM  ##
    def Envia(self,event):
        user= Rocket_Chat(Logins[0], Logins[1])
        self.label.delete('1.0', END) 
        reading=receive(self.assunto)
        
        for x in reading:
            mensagem=reading[x]["message"]
            pessoa=reading[x]["name"]
            t0t=("{0}: {1}\n".format(pessoa,mensagem))
            self.label.insert(END,t0t, 'bold_italics') 
        self.label.see("end")
        self.input_get = self.input_field.get()
        
        user.send(self.input_get,self.assunto)
        self.texto = "{0}: {1}  \n".format(user.nome, self.input_get)
        self.scroll.config(command=self.label.yview)
        self.label.configure(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=RIGHT, fill=Y)        
        self.input_user.set('')
        self.label.insert(END,self.texto) 
        self.label.pack(side=BOTTOM)
        self.input_field.delete('0', END)
    

        return "break"

    ## MÉTODO DE ATUALIZAR A PÁGINA AUTOMATICAMENTE ##
    def atualiza(self,assunto):
        self.label.delete('1.0', END) 
        reading=receive(assunto)
        
        for x in reading:
            mensagem=reading[x]["message"]
            pessoa=reading[x]["name"]
            t0t=("{0}: {1}\n".format(pessoa,mensagem))
            self.label.insert(END,t0t, 'bold_italics') 
        self.label.see("end")
        self.Chat.after(2000, lambda: self.atualiza(assunto))
        return 0

    
    
    def sair(self):
        menu=Menu()
        self.Chat.destroy()
        menu.inicia()
        
    
    
    
    
    def inicia(self):
        self.Chat.mainloop()
    
    
    def acaba(self):
        self.Chat.destroy()


##  CLASSE JANELA DE CRIAR A CONTA  ##

class Criar(Rocket_Chat):
    def __init__(self):
        self.inicial = Tk()
        self.inicial.title("Início")
        self.inicial.geometry("325x125+100+100")
        self.inicial['bg']='orange'
        
        tusername = Label(self.inicial, text = "Username: ", fg= "black", bg= "orange")
        tpassword = Label(self.inicial, text = "Senha: ", fg= "black", bg= "orange")
        BoasVindas = Label(self.inicial, text="Escolha qual vai ser seu login e senha", bg="orange")
        self.Nome = Entry(self.inicial, width = 24)
        self.Senha = Entry(self.inicial, width = 24)
        Salvar = Button(self.inicial, text="Salvar", bg="red",command=self.salva, width=9)
        self.lbl = Label(self.inicial, text= "", bg= "orange")
        self.inicial.bind("<Return>", self.Enter)

        self.lbl.grid(row= 5, column= 1)
        tusername.grid(row= 1, column= 0,sticky=E)
        tpassword.grid(row= 2, column= 0,sticky=E)
        BoasVindas.grid(row= 0, column= 1)
        self.Nome.grid(row= 1, column= 1)
        self.Senha.grid(row= 2, column= 1)
        Salvar.grid(row=3, column=1)

    ## MÉTODO QUE CHECA SE O LOGIN EXIXTE  ##

    def salva(self):   
        n_nome = self.Nome.get()
        n_senha = self.Senha.get()
        saves = fb.get("https://rocket-messenger.firebaseio.com/","data")
        answer= False
        for lg in saves:
            teste_n=saves[lg]["name"]
            teste_s=saves[lg]["password"]
            if n_nome==teste_n or n_senha==teste_s:
                answer=True

        if answer==True:
            self.lbl["fg"]="red"
            self.lbl["text"]="Login ou Senha já existente!"
        elif answer==False:
            user=Rocket_Chat(n_nome,n_senha)
            user.salva_data()
            log.lb["fg"]="green"
            log.lb["text"]="Login e senha salvos!"
            self.acaba()
                    
    ## MESMA FUNÇÃO QUE O MÉTODO SALVA, PORÉM COM O ENTER ##             
    def Enter(self,event):
        n_nome = self.Nome.get()
        n_senha = self.Senha.get()
        saves = fb.get("https://rocket-messenger.firebaseio.com/","data")
        answer= False
        for lg in saves:
            teste_n=saves[lg]["name"]
            teste_s=saves[lg]["password"]
            if n_nome==teste_n or n_senha==teste_s:
                answer=True

        if answer==True:
            self.lbl["fg"]="red"
            self.lbl["text"]="Login ou Senha já existente!"
        elif answer==False:
            user=Rocket_Chat(n_nome,n_senha)
            user.salva_data()
            log.lb["fg"]="green"
            log.lb["text"]="Login e senha salvos!"
            self.acaba()
        
        
    
    def inicia(self):
        self.inicial.mainloop()
    
    
    def acaba(self):
        self.inicial.destroy()
    
    
##  CLASSE JANELA DE ESCOLHER O ASSUNTO  ## 
class Menu():
    def __init__(self):
        try:
            log.acaba()
        except:
            print("Entrou no menu")
        self.Tassunto= Tk()
        self.Tassunto.geometry("400x100+40+40")
        self.Tassunto.title("Menu de Assuntos")
        self.Tassunto["bg"] = "light green"
        self.TextoInicio = Label (self.Tassunto, text = "Selecione o assunto desejado:", bg = "light blue").pack(fill=X,anchor=NW)
        self.entra= Button(self.Tassunto,bd=10, text='Entre no Chat', command=self.Tema,width=9).pack(side=BOTTOM)
        self.ass= Entry(self.Tassunto)
        self.ass.focus()
        self.ass.pack()
        self.Tassunto.bind("<Return>", self.Enter)
        
    def Tema(self):
        assunto= self.ass.get()
        
        user = Rocket_Chat(Logins[0],Logins[1])
        
        chat = Chat(Logins,assunto)
        self.acaba()
        chat.inicia()
    
    def Enter(self, event):
        assunto= self.ass.get()
        
        user = Rocket_Chat(Logins[0],Logins[1])
        
        chat = Chat(Logins,assunto)
        self.acaba()
        chat.inicia()
          
    def inicia(self):
        self.Tassunto.mainloop()
    
    
    def acaba(self):
        self.Tassunto.destroy()
    
## CLASSE JANELA DE LOGIN  ##

class Tlogin(Criar, Chat):
    def __init__(self):
        self.Tlogin = Tk()
        self.Tlogin.title("Início")
        self.Tlogin.geometry("325x125+100+100")
        self.Tlogin['bg']='light blue'
    
    
        self.tusername = Label(self.Tlogin, text = "Username: ", fg= "black", bg= "light blue")
        self.tpassword = Label(self.Tlogin, text = "Senha: ", fg= "black", bg= "light blue")
        self.BoasVindas = Label(self.Tlogin, text="Seja bem-vindo ao Rocket Chat!", bg="light blue", width=24)
        self.username = Entry(self.Tlogin, width = 24)
        self.username.focus()
        self.password = Entry(self.Tlogin, width = 24, show= "*")
        self.Criar = Button(self.Tlogin, text="Criar", bg="light green",command=self.salva_login_senha, width=9)
        self.Entrar = Button(self.Tlogin, text="Enter", bg="light green",command=self.checa_login_senha,width=9)
        self.lb = Label(self.Tlogin, text= "", bg= "light blue")
        self.Tlogin.bind("<Return>", self.Enter)
        
        self.lb.grid(row= 5, column= 1)
        self.tusername.grid(row= 1, column= 0,sticky=E)
        self.tpassword.grid(row= 2, column= 0,sticky=E)
        self.BoasVindas.grid(row= 0, column= 1)
        self.username.grid(row= 1, column= 1)
        self.password.grid(row= 2, column= 1)
        self.Criar.grid(row=4, column=1,sticky=E)
        self.Entrar.grid(row=4, column=1,sticky=W)        
        

    def salva_login_senha(self):   
        app = Criar()
        app.inicia()
        
    ## MÉTODO QUE CHECA SE O LOGIN E A SENHA ESTÃO CORRETOS ## 
    def checa_login_senha(self):
        uname = self.username.get()
        secret = self.password.get()
        saves = fb.get("https://rocket-messenger.firebaseio.com/","data")

        login=False
        for lg in saves:
            name=saves[lg]["name"]
            senha=saves[lg]["password"]
            if uname==name and secret==senha:
                login=True
        if login==True:
            Logins.append(uname) 
            Logins.append(secret)
            user = Rocket_Chat(Logins[0],Logins[1])
            menu = Menu()
            menu.inicia()

        if login==False:
            self.lb["fg"]="red"
            self.lb["text"]="Login ou Senha não existe!"
    
    ## MESMO MÉTODO QUE O ANTERIOR, PORÉM COM O ENTER ##
    def Enter(self, event):
        uname = self.username.get()
        secret = self.password.get()
        saves = fb.get("https://rocket-messenger.firebaseio.com/","data")

        login=False
        for lg in saves:
            name=saves[lg]["name"]
            senha=saves[lg]["password"]
            if uname==name and secret==senha:
                login=True
        if login==True:
            Logins.append(uname) 
            Logins.append(secret)
            user = Rocket_Chat(Logins[0],Logins[1])
            menu = Menu()
            menu.inicia()
            self.acaba()
        elif login==False:
            self.lb["fg"]="red"
            self.lb["text"]="Login ou Senha não existe!"
                        
        

    def inicia(self):
        self.Tlogin.mainloop()
    
    
    def acaba(self):
        self.Tlogin.destroy()



## INICIA O CHAT ##
log= Tlogin()
log.inicia()




