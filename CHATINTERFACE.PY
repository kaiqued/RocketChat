
from tkinter import *
import os
from chat_firebase import Rocket_Chat , receive

clear=lambda:os.system('cls')



def close_window():   
    login=username.get()
    Logins.append(login)
    Tinicio.destroy()




def Enter_pressed(event):
    input_get = input_field.get()
    user.send(input_get)
    texto = "{0}: {1}  \n".format(user.nome, input_get)
    scroll.config(command=label.yview)
    label.configure(yscrollcommand=scroll.set)
    scroll.pack(side=RIGHT, fill=Y)        
    input_user.set('')
    
    label.tag_configure('bold_italics', font=('Arial', 20, 'bold', 'italic'))
    label.tag_configure('big', font=('Verdana', 20, 'bold'))
    label.tag_configure('color', foreground='gray', font=('tempus Sans ITC', 12, 'bold'))
    label.insert(END,texto, 'bold_italics') 
    
    label.pack(side=BOTTOM)
    
    
    return "break"




#LOGIN E SENHA, ENTRADA
Logins = []


Tinicio = Tk()
Tinicio.geometry("300x100+100+100")
Tinicio.title("Entrada")
Tinicio["bg"]= "blue"


tusername = Label(Tinicio, text = "Username: ", bg= "blue")
tusername.grid(row = 1, column= 1)


username = Entry(Tinicio)
username.grid(row=1, column=2)



lb=Label(Tinicio, text= "", bg= "blue")
lb.grid(row= 4, column= 2)



Entrar = Button(Tinicio, text="Enter", bg="red",command=close_window)
Entrar.grid(row=3, column=2)

Tinicio.mainloop()

user=Rocket_Chat(Logins[0])
user.post()

#aplicativo
Tmenu = Tk()
Tmenu.geometry("500x600+40+40")
Tmenu.title("Rocket Chat")
Tmenu["bg"] = "gray"
#criando painel
p = PanedWindow(orient=HORIZONTAL)
p.pack(anchor=CENTER, fill=X)
input_user = StringVar()
input_field = Entry(Tmenu, text=input_user)
input_field.pack( side=BOTTOM, fill=X)
scroll=Scrollbar(Tmenu)
label = Text(Tmenu,height=500,width=500, bg= "gray")


input_field.bind("<Return>", Enter_pressed)


TextoInicio = Label(Tmenu, text = "Bem vindo ao Rocket Chat", bg = "blue")
TextoInicio.pack(side = TOP, fill= X)

#criando o painélel
"""p1 = PanedWindow(orient=VERTICAL)
p1.pack(side=RIGHT, fill=Y)
scrollbar = Scrollbar(Tmenu)
scrollbar=.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=Text.yview)
scrollbar.pack(side=RIGHT, fill=Y)
p1.add(scrollbar)"""


frame = Frame(Tmenu, width=1, height=1)


""""
NOTA PARA GABRIEL:
--> Logins[0] é o nome do usuario;
--> texto é a mensagem enviada
"""


frame.pack()
Tmenu.mainloop()
