
from tkinter import *
import os
from chat_firebase import Rocket_Chat, receive
from firebase import firebase

clear=lambda:os.system('cls')

FIREBASE_URL = "https://rocket-messenger.firebaseio.com/"
fb = firebase.FirebaseApplication(FIREBASE_URL,  None)


###   TELA INICIAL DE LOGIN   ###

Logins = []
#  CRIA A JANELA  #
Tinicio = Tk()
Tinicio.geometry("325x125+100+100")
Tinicio.title("Entrada")
Tinicio["bg"]= "light blue"

#  DEFINE AS FUNÇÕES  #

"""CRIEI DUAS FUNÇÕES, A PRIMEIRA CRIA A JANELA E A SEGUNDA SALVA E FECHA A JANELA"""





def tela_criar_login_senha():   
    Tcriar = Tk()
    Tcriar.geometry("350x125+100+100")
    Tcriar.title("Criar login e senha")
    Tcriar["bg"]= "orange"
    
    
    def salva_login_senha():   
        nome = username.get()
        senha = password.get()
        Logins.append(nome)
        Logins.append(senha)
        lb["fg"]="green"
        lb["text"]="Login e senha salvos!"
        Tcriar.destroy()
        
        
        
    tusername = Label(Tcriar, text = "Username: ", fg= "black", bg= "orange")
    tpassword = Label(Tcriar, text = "Senha: ", fg= "black", bg= "orange")
    BoasVindas = Label(Tcriar, text="Escolha qual vai ser seu login e senha", bg="orange")
    username = Entry(Tcriar, width = 24)
    password = Entry(Tcriar, width = 24)
    Salvar = Button(Tcriar, text="Salvar", bg="red",command=salva_login_senha, width=9)
    
    tusername.grid(row= 1, column= 0,sticky=E)
    tpassword.grid(row= 2, column= 0,sticky=E)
    BoasVindas.grid(row= 0, column= 1)
    username.grid(row= 1, column= 1)
    password.grid(row= 2, column= 1)
    Salvar.grid(row=3, column=1)
    Tcriar.mainloop()
    
    
def checa_login_senha():
    login = username.get()
    secret = password.get()
    saves = fb.get("https://rocket-messenger.firebaseio.com/","data")
    
    for lg in saves:
        name=saves[lg]["name"]
        senha=saves[lg]["password"]
        if name==login and secret==senha:
            Tinicio.destroy()
        
    lb["fg"]="red"
    lb["text"]="Login não existe!"

## TELA INICIO ##

#  DEFINE OS WIDGETS  #

lb = Label(Tinicio, text= "", bg= "light blue")
tusername = Label(Tinicio, text = "Username: ", fg= "black", bg= "light blue")
tpassword = Label(Tinicio, text = "Senha: ", fg= "black", bg= "light blue")
BoasVindas = Label(Tinicio, text="Seja bem-vindo ao Rocket Chat!", bg="light blue", width=24)
username = Entry(Tinicio, width = 24)
password = Entry(Tinicio, width = 24)
Criar = Button(Tinicio, text="Criar", bg="red",command=tela_criar_login_senha, width=9)
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

#user=Rocket_Chat(Logins[0],Logins[1])
#user.post()


## TELA CRIAR CONTA ##



###  TELA DO CHAT  ###

#  CRIA A TELA  #
Tmenu = Tk()
Tmenu.geometry("500x600+40+40")
Tmenu.title("Rocket Chat")
Tmenu["bg"] = "gray"

#  CONFIGURA AS FUNÇÕES  #

def Enter_pressed(event):
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
p = PanedWindow(orient=HORIZONTAL)
input_user = StringVar()
input_field = Entry(Tmenu, text=input_user)
label = Text(Tmenu,height=500,width=500, bg= "gray")
TextoInicio = Label(Tmenu, text = "Bem vindo ao Rocket Chat", bg = "light blue")
scroll=Scrollbar(Tmenu)
frame = Frame(Tmenu, width=1, height=1)

#  POSICIONA OS WIDGETS  #

p.pack(anchor=CENTER, fill=X)
input_field.bind("<Return>", Enter_pressed)
input_field.pack( side=BOTTOM, fill=X)
TextoInicio.pack(side = TOP, fill= X)
frame.pack()
#  CONFIGURA O TEXTO QUE ENTRA NO CHAT  #

label.tag_configure('bold_italics', font=('Arial', 15, 'italic'))
label.tag_configure('big', font=('Verdana', 20, 'bold'))
label.tag_configure('color', foreground='gray', font=('tempus Sans ITC', 12, 'bold'))







Tmenu.mainloop()
