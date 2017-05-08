
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


Logins=[]


lb=Label(janela, text= "", bg= "blue")
lb.grid(row= 4, column= 2)

def salvaloginsenha():
    lo=username.get()

    clear()

    Tmenu = Tk()
    Tmenu.geometry("500x600+40+40")
    Tmenu.title("Rocket Chat")


    mensagem = Entry(Tmenu)
    mensagem.grid(row = 3, column = 0)

    botao1 = Button(Tmenu,text = "Send" ,relief=FLAT)
    botao1.pack(anchor = E,side = BOTTOM)
    
    

   

   

Entrar = Button(janela, text="Enter", bg="red",command=salvaloginsenha) 

Entrar.grid(row=3, column=2)
clear()



janela.mainloop()



## TELA DO APLICATIVO##
#tela do app
Ta = Tk()
Ta.geometry("500x600+40+40")
Ta.title("Inicio")
photo=PhotoImage(file="orange.png")
vida=Label(Ta, image=photo)
vida.pack()

Ta.mainloop()


 
