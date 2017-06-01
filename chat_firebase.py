from firebase import firebase
import json
import requests

#coleta informações do firebase
FIREBASE_URL = "https://rocket-messenger.firebaseio.com/"
fb = firebase.FirebaseApplication(FIREBASE_URL,  None)

class Rocket_Chat():
    #método para iniciar o usuário
    def __init__(self,login,password):
        self.nome=login
        self.senha=password

    #método para salvar um usuário novo no dic data
    def salva_data(self):    
        fb.post("data",
                {"name": self.nome,
                 "password": self.senha
                })
    
    #método para postar a entrada numa conversa     
    def post(self,assunto):
        # Avisa que o usuário logou
        fb.post(assunto,
                {"name": self.nome,
                 "message": "Joined the chat"
                })
    #método para postar mensagem no assunto
    def send(self,mensagem,assunto):
        self.mes=mensagem
        fb.post(assunto,
                {
                    "name": self.nome,
                    "message": self.mes
                })


#função que recebe o dic de qualquer conversa
def receive(assunto):
    reading = fb.get("https://rocket-messenger.firebaseio.com/", assunto)
    return reading



#teste de inteligencia artificial
'''
def ia(mensagem):

	r = requests.get("https://www.wolframcloud.com/objects/8bdd110e-181c-48d1-a95f-f376f00e3f12?inputMsg="+ mensagem)
	listar=r.text.split(",")
	
	listar[2]=listar[2].replace(" ","")
	listar[2]=int(listar[2])
	listar[3]=listar[3].replace("}","")
	
	return listar
'''

