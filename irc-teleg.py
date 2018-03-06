import sys
import irc
import telebot

token = 'token_name'

client_irc = irc.IRC()

nick = 'Pons_IRC_Telegram'
server = 'chat.freenode.net'
channel = sys.argv[1]
chat_id = 0 # some negative number

client_irc.connect(server, nick)
client_irc.join(channel)

client_teleg = telebot.TeleBot(token)

client_teleg.polling()

while True:
    # IRC -> telegram
    status, metha = client_irc.handle_event()
    if status == 'INPUT_MESSAGE':
        client_teleg.send_message(chat_id, "{}: {}".format(metha['author'], metha['message']))
