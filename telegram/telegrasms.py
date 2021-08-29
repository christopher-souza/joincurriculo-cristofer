import requests
import datetime


class Telegram(object):

	def bot_sendtextinfo(self, nome, titulo, email, id_user, mensagem):
  
		
		bot_message = """Olá, eu me chamo, {}\n Quero falar sobre:{}\n 

						Meu Id ou número para contato é:{}\n 
						Meu email{}\n 
						E a minha mensagem é:{}\n """.format(nome, titulo, id_user, email, mensagem)
		
		bot_token = '1976162613:AAEsfCF3SNqE4MWA_IXBTmOt-DVkziYEkoM'
		bot_chatID = '-542421050'
		send = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=html&text=' + str(bot_message)
		#response = requests.get(send_text)
		r = requests.get(send)
	    
		print(r)

		
