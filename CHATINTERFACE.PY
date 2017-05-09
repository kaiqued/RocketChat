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
    return lo
    
   
def close_window(): 
    janela.destroy()

     

   

   

Entrar = Button(janela, text="Enter", bg="red",command=salvaloginsenha) 
Entrar = Button(janela, text="Enter", bg="red",command=close_window)
Entrar.grid(row=3, column=2)

janela.mainloop()


#aplicativo
Tmenu = Tk()
Tmenu.geometry("500x600+40+40")
Tmenu.title("Rocket Chat")

input_user = StringVar()
input_field = Entry(Tmenu, text=input_user)
input_field.pack(side=BOTTOM,fill=X)
def Enter_pressed(event):
    input_get = input_field.get()
    print(input_get)
    label = Label(Tmenu, text=input_get)
    input_user.set('')
    label.pack()
    return "break"





frame = Frame(Tmenu, width=300, height=300)
input_field.bind("<Return>", Enter_pressed)
frame.pack()

Tmenu.mainloop()


 
