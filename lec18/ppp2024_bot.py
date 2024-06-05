import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
 
token = "7229073917:AAEPk6Q2y0z0b6oUdlkrImRZqw8W6MYm7SQ"
id = "6891680238"

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="테스트 중입니다.")

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()
 

def handler(update, context):
    user_text = update.message.text 
    if user_text == "안녕": 
        bot.send_message(chat_id=id, text="안녕하세요.") 
    elif user_text == "뭐해": 
        bot.send_message(chat_id=id, text="메시지를 보내는 중입니다.")  
    elif user_text == "잘했어": 
        bot.send_message(chat_id=id, text="감사합니다:)") 
    else: 
        bot.send_message(chat_id=id, text="잘 모르겠어요.")  
 
echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
