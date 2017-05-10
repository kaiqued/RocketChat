from tkinter import *
import os
clear=lambda:os.system('cls')


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



def salvaloginsenha():
    login=username.get()
    login=username.get()
    Logins.append(login)   
    Tinicio.destroy()
    return





Entrar = Button(Tinicio, text="Enter", bg="red",command=salvaloginsenha) 
Entrar.grid(row=3, column=2)

Tinicio.mainloop()


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

def Enter_pressed(event):
    input_get = input_field.get()
    
    texto = "{0}: {1}  \n".format(Logins[0], input_get)
    scroll.config(command=label.yview)
    label.configure(yscrollcommand=scroll.set)
    scroll.pack(side=RIGHT, fill=Y)        
    input_user.set('')
    
    label.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    label.tag_configure('big', font=('Verdana', 20, 'bold'))
    label.tag_configure('color', foreground='#476042', font=('tempus Sans ITC', 12, 'bold'))
    label.tag_bind('follow', '<1>', lambda e, t=label: t.insert(END, "Not now, maybe later!"))
    
    
    label.pack(side=TOP)
    label.insert(END,texto)
    
    return "break"



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










frame.pack()
Tmenu.mainloop()
