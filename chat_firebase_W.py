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
                 "message": "Joined the chat"
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




def ia(mensagem):

	r = requests.get("https://www.wolframcloud.com/objects/8bdd110e-181c-48d1-a95f-f376f00e3f12?inputMsg="+ mensagem)
	listar=r.text.split(",")
	
	listar[2]=listar[2].replace(" ","")
	listar[2]=int(listar[2])
	listar[3]=listar[3].replace("}","")
	
	return listar

'''
kaique="bosta cú"
jao=ia(kaique)
print(jao)
'''





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




    def salva(self):   
        login = self.Nome.get()
        secret = self.Senha.get()
        saves = fb.get("https://rocket-messenger.firebaseio.com/","data")
        answer= False
        for lg in saves:
            name=saves[lg]["name"]
            senha=saves[lg]["password"]
            if login==name or secret==senha:
                answer=True

        if answer==True:
            self.lbl["fg"]="red"
            self.lbl["text"]="Login ou Senha já existente!"
        if answer==False:
            user=Rocket_Chat(login,secret)
            user.salva_data()
            log.lb["fg"]="green"
            log.lb["text"]="Login e senha salvos!"
            self.acaba()   
'''

