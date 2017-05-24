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


class Chat(Rocket_Chat) :
    def __init__(self, Logins):
        
        self.Chat = Tk()
        self.Chat.title("Rocket Chat")
        self.Chat.geometry("500x600+40+40")
        self.Chat['bg'] = 'gray'
        user = Rocket_Chat(Logins[0], Logins[1])
        try:
            user.post()
        except:
            print("123")
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
        self.cor = Button(self.opcoes, text='Editar texto e fundo', command=self.Edita)
        
        
        
        
        ## Coloca na tela ##
        
        self.exit.pack(side = RIGHT)
        self.TextoInicio.pack(side= LEFT)
        self.input_field.pack(side=BOTTOM, fill=X)
        self.label.pack()
        self.input_field.bind("<Return>", self.Envia)
        self.cor.pack()
        
        
        self.Chat.after(2000, self.atualiza)
    
    
    def Edita(self):
        
        def sel():
           size = str(var.get())
           font = str(vari.get())
           more = str(varia.get())
           self.label["font"]=font, size, more
           
        root = Tk()
        root["bg"]="gray"
        
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
        
        R1 = Radiobutton(f3, text="Negrito", variable=varia, value="bold",bg = "gray")
        R1.pack()
        
        R2 = Radiobutton(f3, text="Itálico", variable=varia, value="italic",bg = "gray")
        R2.pack()
        
        
        
        R1 = Radiobutton(f2, text="Times", variable=vari, value="Times",bg = "gray")
        R1.pack( anchor = W )
        
        R2 = Radiobutton(f2, text="Verdana", variable=vari, value="Verdana",bg = "gray")
        R2.pack( anchor = W )
        
        corfundo=Button(root, text= "Cor do fundo",bg = "gray", command=self.getColor)
        corfundo.pack(anchor=CENTER)
                    
        
        
        
        
        
        
    def getColor(self):
        color = askcolor()
        (y,x) = color
        self.label["bg"]=x
        self.Chat["bg"]= x
        
    
    
    def Envia(self,event):
        user= Rocket_Chat(Logins[0], Logins[1])
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
        self.Chat.after(2000, self.atualiza)
        return 0

    
    
    def sair(self):
        self.acaba()
    
    
    
    
    def inicia(self):
        self.Chat.mainloop()
    
    
    def acaba(self):
        self.Chat.destroy()




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
        self.inicial.bind("<Return>", self.Enter)
        
        tusername.grid(row= 1, column= 0,sticky=E)
        tpassword.grid(row= 2, column= 0,sticky=E)
        BoasVindas.grid(row= 0, column= 1)
        self.Nome.grid(row= 1, column= 1)
        self.Senha.grid(row= 2, column= 1)
        Salvar.grid(row=3, column=1)
        nome = self.Nome.get()
        senha = self.Senha.get()

        
    def salva(self):   
        nome = self.Nome.get()
        senha = self.Senha.get()
        Logins.append(nome)
        Logins.append(senha)
        user=Rocket_Chat(Logins[0],Logins[1])
        user.salva_data()
        log.lb["fg"]="green"
        log.lb["text"]="Login e senha salvos!"
        self.acaba()
    
        
    def Enter(self,event):
        nome = self.Nome.get()
        senha = self.Senha.get()
        Logins.append(nome)
        Logins.append(senha)
        user=Rocket_Chat(Logins[0],Logins[1])
        user.salva_data()
        log.lb["fg"]="green"
        log.lb["text"]="Login e senha salvos!"
        self.acaba()
        
        
    
    def inicia(self):
        self.inicial.mainloop()
    
    
    def acaba(self):
        self.inicial.destroy()
    
    
    
class Menu():
    def __init__(self):
        log.acaba()
        self.Tassunto= Tk()
        self.Tassunto.geometry("+40+40")
        self.Tassunto.title("Menu de Assuntos")
        self.Tassunto["bg"] = "light green"
        self.TextoInicio = Label (self.Tassunto, text = "Selecione o assunto desejado:", bg = "light blue").pack(anchor=NW)
        self.Futebol= Button(self.Tassunto,bd=10, text='Entre no Chat', command=self.Tema,width=9).pack(side=BOTTOM)
        self.fut= Entry(self.Tassunto)
        self.fut.pack()
        
        
    def Tema(self):
        assunto= self.fut.get()
        print(assunto)
        user = Rocket_Chat(Logins[0],Logins[1])
        jooj = Chat(Logins)
        jooj.inicia()
        
          
    def inicia(self):
        self.Tassunto.mainloop()
    
    
    def acaba(self):
        self.Tassunto.destroy()
    
    

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
        self.password = Entry(self.Tlogin, width = 24)
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
        
    
    def Enter(self, event):
        login = self.username.get()
        secret = self.password.get()
        saves = fb.get("https://rocket-messenger.firebaseio.com/","data")
        
        for lg in saves:
            name=saves[lg]["name"]
            senha=saves[lg]["password"]
            if name==login and secret==senha:
                Logins.append(login) 
                Logins.append(secret)
                user = Rocket_Chat(Logins[0],Logins[1])
                menu = Menu()
                menu.inicia()
               
            else:
                try:
                    self.lb["fg"]="red"
                    self.lb["text"]="Login ou Senha não existe!"
                except:
                    print("erro    2")
                    
    def checa_login_senha(self):
        login = self.username.get()
        secret = self.password.get()
        saves = fb.get("https://rocket-messenger.firebaseio.com/","data")
        
        for lg in saves:
            name=saves[lg]["name"]
            senha=saves[lg]["password"]
            if name==login and secret==senha:
                Logins.append(login) 
                Logins.append(secret)
                user = Rocket_Chat(Logins[0],Logins[1])
                menu = Menu()
                menu.inicia()
                break
            else:
                try:
                    self.lb["fg"]="red"
                    self.lb["text"]="Login ou Senha não existe!"
                except:
                    print("erro    2")
                    break
    def inicia(self):
        self.Tlogin.mainloop()
    
    
    def acaba(self):
        self.Tlogin.destroy()




log= Tlogin()
log.inicia()

        
### MENU ###











###  TELA DO CHAT  ###


#  CRIA A TELA  #
