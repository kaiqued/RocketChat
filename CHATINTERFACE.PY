from tkinter import *
import os
clear=lambda:os.system('cls')


#LOGIN E SENHA, ENTRADA
Logins = []


janela = Tk()
janela.geometry("250x150+100+100")
janela.title("Entrada")
janela["bg"]= "blue"



tusername = Label(janela, text = "Username: ", bg= "blue")
tusername.grid(row = 1, column= 1)



username = Entry(janela)
username.grid(row=1, column=2)






lb=Label(janela, text= "", bg= "blue")
lb.grid(row= 4, column= 2)



def salvaloginsenha():
    login=username.get()
    print(login)   
    janela.destroy()
    return 
   

        
   


Entrar = Button(janela, text="Enter", bg="red",command=salvaloginsenha) 
Entrar.grid(row=3, column=2)

janela.mainloop()


#aplicativo
Tmenu = Tk()
Tmenu.geometry("500x600+40+40")
Tmenu.title("Rocket Chat")
#criando painel
p = PanedWindow(orient=HORIZONTAL)
p.pack(anchor=CENTER, fill=X)
input_user = StringVar()
input_field = Entry(Tmenu, text=input_user)
p.add(input_field)

scroll=Scrollbar(Tmenu)
label = Text(Tmenu,height=500,width=500)

def Enter_pressed(event):
    input_get = input_field.get()
    scroll.config(command=label.yview)
    label.configure(yscrollcommand=scroll.set)
    scroll.pack(side=RIGHT, fill=Y)        
    input_user.set('\n')
    label.pack(side=TOP)
    label.insert(END,input_get)
   
    return "break"



input_field.bind("<Return>", Enter_pressed)

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
