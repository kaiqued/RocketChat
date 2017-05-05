from firebase import firebase
from multiprocessing import Process
from sseclient import SSEClient
import json
import time
import properties as prop


class Chat(object):

	def __init__(self):
		print ("\n\n\n--- Rocket Chat ---")


	def firebase_data(self):
		# Firebase URL
		fbase = firebase.FirebaseApplication(prop.https://rocket-messenger.firebaseio.com/, None)

		# Le o JSON
		result = fbase.get('', None)
		print (result)
		print ("\n\n\n")

		
		# Le o nome do grupo
		result_grupo = fbase.get('Grupo', None)
		print (result_grupo)
		print ("\n\n\n")


		# Le o JSON
		result = fbase.get('', None)
		print (result)
		print ("\n\n\n")



	def firebase_chat(self):
		
		server_sent = SSEClient(prop.https://rocket-messenger.firebaseio.com/ + "Messages.json")

		print("\n\nFirebase Server - %s" % (prop.https://rocket-messenger.firebaseio.com/ + "Messages.json"))


		for new_msg in server_sent:
			msg_data = json.loads(new_msg.data)
			# printa nova mensagem

			if msg_data is None:
				continue

			# Le mensagens ja existentes
			if msg_data["path"] == "/": 
				print("\nWhen you weren't there ... \n")
				for (nodeid, message) in msg_data["data"].items():
					try:
						print("%s says: %s\n" % (msg["name"], msg["message"]))
						
					except:
						pass

			# #New Message
			else: 
				try:
					print("%s says: %s\n" % (msg_data["data"]["name"], msg_data["data"]["message"]))
					# print "\n"
				except:
					pass

	

if __name__ == '__main__':
	rocket_firebase = FirebaseApp()

	# acompanhar mudanças
	chat_app = Process(target=rocket_firebase.firebase_chat)
	chat_app.start()

	time.sleep(1)
	username = input("Username: ")
	fb = firebase.FirebaseApplication(prop.https://rocket-messenger.firebaseio.com/, None)

	# Posta mensagem inicial
	fb.post('Messages',
			{"name": username,
			 "message": "Entrou na discussão",
			 ".priority": time.time() * 1000
			})

	# Posta mensagens novoas
	while (True):
		message = input(" ")
		print("\n")
		fb.post('Messages',
				{
					"name": username,
					"message": message,
					".priority": time.time() * 1000
				})