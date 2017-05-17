from tkinter import *
import os
from chat_firebase import Rocket_Chat, receive
from firebase import firebase

clear=lambda:os.system('cls')
Logins = []
import PIL
y=0
FIREBASE_URL = "https://rocket-messenger.firebaseio.com/"
fb = firebase.FirebaseApplication(FIREBASE_URL,  None)

class inicio:
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
    app = inicio()
    
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
            Tinicio.destroy()

    #erro da quando ele acha o login, pq ai a janela fecha e o codigo roda isso aqui, so q a janlea nao ta mais aberta->pensar num else   
    lb["fg"]="red"
    lb["text"]="Login não existe!"

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






###  TELA DO CHAT  ###

#  CRIA A TELA  #
Tmenu = Tk()
Tmenu.geometry("500x600+40+40")
Tmenu.title("Rocket Chat")
Tmenu["bg"] = "gray"
label = Text(Tmenu,height=500,width=500, bg= "gray")
'''
reading=receive()
for x in reading:
    mensagem=reading[x]["message"]
    pessoa=reading[x]["name"]
    t0t=("{0}: {1}\n".format(pessoa,mensagem))
    label.insert(END,t0t, 'bold_italics') 
'''

#  CONFIGURA AS FUNÇÕES  #

def batata(event):

    label.delete('1.0', END)
    reading=receive()
    for x in reading:
        mensagem=reading[x]["message"]
        pessoa=reading[x]["name"]
        t0t=("{0}: {1}\n".format(pessoa,mensagem))
        label.insert(END,t0t, 'bold_italics') 
    input_get = input_field.get()
    user.send(input_get)
    texto = "{0}: {1}  \n".format(user.nome, input_get)
    scroll.config(command=label.yview)
    label.configure(yscrollcommand=scroll.set)
    scroll.pack(side=RIGHT, fill=Y)        
    input_user.set('')
    label.insert(END,texto, 'bold_italics') 
    label.pack(side=BOTTOM)
    
    

    return "break"

#  CRIA OS WIDGETS  #
user=Rocket_Chat(Logins[0],Logins[1])
user.post()
p = PanedWindow(orient=HORIZONTAL)
input_user = StringVar()
input_field = Entry(Tmenu, text=input_user)

reading=receive()

TextoInicio = Label(Tmenu, text = "Bem vindo ao Rocket Chat", bg = "light blue")
scroll=Scrollbar(Tmenu)
frame = Frame(Tmenu, width=1, height=1)




    
#  POSICIONA OS WIDGETS  #

p.pack(anchor=CENTER, fill=X)
input_field.bind("<Return>", batata)
input_field.pack( side=BOTTOM, fill=X)
print(y)
y+=1
TextoInicio.pack(side = TOP, fill= X)
frame.pack()
#  CONFIGURA O TEXTO QUE ENTRA NO CHAT  #

label.tag_configure('bold_italics', font=('Arial', 15, 'italic'))
label.tag_configure('big', font=('Verdana', 20, 'bold'))
label.tag_configure('color', foreground='gray', font=('tempus Sans ITC', 12, 'bold'))







Tmenu.mainloop()

