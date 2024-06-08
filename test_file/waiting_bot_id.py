import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import random
import time

token = "7202581976:AAETgo3coDHml353GRtLgLWMMJq0Iz41a5Y"
id = "6891680238"

bot = telegram.Bot(token)
info_message = '''대기번호 및 시간을 안내해주는 <대기인원 알리미> 봇입니다. 원하시는 정보가 있다면 아래와 같이 입력해주세요.

- 대기번호 확인 : "번호" or "대기번호"
- 예상 대기시간 확인 : "시간" or "대기시간"
- 남은 인원 수 확인 : "인원" or "대기인원"'''
bot.sendMessage(chat_id=id, text=info_message)

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()


user_dic={}

def waiting_time(user_number, number_wait_time):
    per_people_time = 0.5 
    people_front = user_number - 1
    total_waiting_time = people_front * per_people_time

    current_time = int(time.time()/60) 
    passed_time = current_time - number_wait_time

    waiting_time = total_waiting_time - passed_time
    return int(waiting_time)
 
def handler(update, context):
    user_id = update.message.from_user.id
    user_text = update.message.text 
    user_name = f"{update.message.from_user.last_name}{update.message.from_user.first_name}"

    current_time = int(time.time()/60)

    if (user_text == "번호") or (user_text == "대기번호"): 
        if user_id not in user_dic:
            user_number = random.randint(1, 50)
            user_dic[user_id] = {
                'user_number': user_number,
                'number_wait_time': current_time
            }
        user_number = user_dic[user_id]['user_number']
        bot.send_message(chat_id=id, text=f"{user_name} 님의 대기번호는 {user_number}번 입니다.") 

    elif (user_text == "시간") or (user_text == "대기시간"):  
        if user_id in user_dic:
            user_number = user_dic[user_id]['user_number']
            number_wait_time = user_dic[user_id]['number_wait_time']
            bot.send_message(chat_id=id, text=f"예상되는 남은 대기시간은 {waiting_time(user_number, number_wait_time)}분 입니다.")
        else:
            bot.send_message(chat_id=id, text=f"먼저 대기번호를 확인해주세요.")
                             
    elif (user_text == "인원") or (user_text == "대기인원"):  
        if user_id in user_dic:
            user_number = user_dic[user_id]['user_number']
            number_wait_time = user_dic[user_id]['number_wait_time']
            people_front = user_number - 1
            passed_time = current_time - number_wait_time
            if passed_time >= 1:
                people_front = user_number - (passed_time//0.5) - 1
            bot.send_message(chat_id=id, text=f"남은 대기인원은 {int(people_front)}명 입니다.")
        else:
            bot.send_message(chat_id=id, text=f"먼저 대기번호를 확인해주세요.")

    else: 
        bot.send_message(chat_id=id, text="올바른 단어를 입력해주세요.")  
 
echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)