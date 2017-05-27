from firebase import firebase
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
    
         
    def post(self,assunto):
        # Avisa que o usuário logou
        fb.post(assunto,
                {"name": self.nome,
                 "message": "Joined the chat"
                })

    def send(self,mensagem,assunto):
        self.mes=mensagem
        fb.post(assunto,
                {
                    "name": self.nome,
                    "message": self.mes
                })



def receive(assunto):
    reading = fb.get("https://rocket-messenger.firebaseio.com/", assunto)
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


reading = fb.get("https://rocket-messenger.firebaseio.com/",None)

lista = []
for i in range (len(reading)):
	lista.append(reading[i])

print(len(reading))
'''

