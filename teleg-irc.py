import sys
import irc
import telebot

token = 'token_name'

client_irc = irc.IRC()

nick = 'Pons_IRC_Telegram'
server = 'chat.freenode.net'
channel = sys.argv[1]
chat_id = -270350582

client_irc.connect(server, nick)
client_irc.join(channel)

client_teleg = telebot.TeleBot(token)
@client_teleg.message_handler(content_types=["text"])
def send(message):
    client_irc.send(channel, message.text)

client_teleg.polling()
