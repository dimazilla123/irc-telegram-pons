import socket
import sys

class IRC:

    irc = socket.socket()
    encoding = 'utf-8'

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        print(":test PRIVMSG " + chan + ":" + msg + "\r\n")
        self.irc.send(bytes(":test PRIVMSG " + chan + " :" + msg + "\r\n", self.encoding))

    def join(self, channel):
        self.irc.send(bytes("JOIN " + channel + "\r\n", self.encoding))

    def connect(self, server, botnick):
        #defines the socket
        print("connecting to: " + server)
        self.irc.connect((server, 6667))                                                         #connects to the server
        self.irc.send(bytes("USER " + botnick + " " + botnick +" " + botnick + " :Scribator logī\r\n", self.encoding)) #user authentication
        self.irc.send(bytes("NICK " + botnick + "\r\n", self.encoding))

    def handle_event(self):
        text = self.irc.recv(2040).decode(self.encoding)
        status, metha = None, None
        if text.find('PING') != -1:
            self.irc.send(bytes('PONG ' + text.split()[1] + '\r\n', self.encoding))
            status = 'PING'
        elif text.find('PRIVMSG') != -1:
            author = text[1:text.find('!'):]
            message = text[text.rfind(' :') + 2::]
            reciver = text[text.find('PRIVMSG') + len('PRIVMSG') + 1:text.rfind(' :'):]
            metha = {'author' : author, 'message' : message, 'reciver' : reciver}
            status = 'INPUT_MESSAGE'

        return (status, metha)
