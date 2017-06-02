from firebase import firebase
import json
import requests


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
                 "message": "Joined the chat",
                 "humor": "Neutro"
                })

    def send(self,mensagem,assunto,humor):
        self.mes=mensagem
        self.humor=humor
        fb.post(assunto,
                {
                    "name": self.nome,
                    "message": self.mes,
                    "humor": self.humor
                })



def receive(assunto):
    reading = fb.get("https://rocket-messenger.firebaseio.com/", assunto)
    return reading



#função de inteligencia artificial
def ia(mensagem):

	r = requests.get("https://www.wolframcloud.com/objects/9201a182-54d4-4368-b350-72d32059ebe7?inputMsg="+ mensagem)
	listar=r.text.split(",")
	
	listar[2]=listar[2].replace(" ","")
	listar[2]=int(listar[2])
	listar[3]=listar[3].replace("}","")
	listar[3]=listar[3].replace(" ","")
	return listar


#teste
'''
chatbot=ia("que merda tio babaca do caralho")

print(chatbot[3])
'''