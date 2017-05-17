from multiprocessing import Process
from firebase import firebase
from sseclient import SSEClient
import json


FIREBASE_URL = "https://rocket-messenger.firebaseio.com/"
fb = firebase.FirebaseApplication(FIREBASE_URL,  None)

class Rocket_Chat():

    def __init__(self,login,password):
        self.nome=login
        self.senha=password


    def salva_data(self):    
        fb.post("data",
                {"name": self.nome,
                 "password": self.senha
                })
    
         
    def post(self):
        # Avisa que o usuário logou
        fb.post("rocket-messenger",
                {"name": self.nome,
                 "message": "Joined the chat"
                })

    def send(self,mensagem):
        self.mes=mensagem
        fb.post("rocket-messenger",
                {
                    "name": self.nome,
                    "message": self.mes
                })



def receive():
    reading = fb.get("https://rocket-messenger.firebaseio.com/","rocket-messenger")
    return reading





'''
#testes
username = input("Input your username: ")

user=Rocket_Chat(username)

user.post()

user.send()

#resgata a conversa
reading=receive()
for x in reading:
    mensagem=reading[x]["message"]
    pessoa=reading[x]["name"]
    txt=("{0}: {1}\n".format(pessoa,mensagem))
    label.insert(END,txt, 'bold_italics') 
    
'''

