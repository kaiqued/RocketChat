from multiprocessing import Process
from firebase import firebase
from sseclient import SSEClient
import json
import time

FIREBASE_URL = "https://rocket-messenger.firebaseio.com/"



if __name__ == "__main__":
    print(__name__)
    time.sleep(1)
    username = input("Input your username: ")
    fb = firebase.FirebaseApplication(FIREBASE_URL,  None)

    # Avisa que o usuário logou
    fb.post("rocket-messenger",
            {"name": username,
             "message": "Joined the chat",
             ".priority": time.time() * 1000
            })

    # Posta mensagem do usuário
    while (True):
        message = input("")
        print("\n")
        fb.post("rocket-messenger",
                {
                    "name": username,
                    "message": message,
                    ".priority": time.time() * 1000
                })

