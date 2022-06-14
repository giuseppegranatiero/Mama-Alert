import socket
import threading
from gtts import gTTS
from playsound import playsound
import os

# Choosing Nickname
nickname = "Static"

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def alert(name):
    myText = name + " is coming!"

    language='en'

    output=gTTS(text=myText, lang=language, slow=False)

    output.save("result.mp3")
    playsound("result.mp3")
    os.remove("result.mp3")

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname - Face Recognition Alert
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
                if 'Giuseppe' in message:
                    alert("Giuseppe")

        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()
