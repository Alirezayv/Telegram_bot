from email.mime import image
import logging
from time import CLOCK_THREAD_CPUTIME_ID
from telegram import *
from telegram.ext import *
from requests import *


updater = Updater( token ='5030895573:AAH63KvuN-Td40DCcVjGhLP9sZqs97V19yM', use_context=True)
dispatcher = updater.dispatcher



def createLink(phone_number):
    phone = phone_number.replace("+","")
    link = f"http://t.me/Cwealth_info_bot?start={phone}"
    return link

my_bot = Bot(token ='5030895573:AAH63KvuN-Td40DCcVjGhLP9sZqs97V19yM')
textChannel_ID = "-1001168876759"

register = """
برای ثبت نام، نام و نام خانوادگی خود را وارد کنید.
"""

sendingPhone = "ارسال شماره تلفن"

registerd = """
شما عضو شدید
"""

user_data =  {

        "user_name" : "",
        "user_phone" : "",
    }
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.sendMessage(chat_id, "What is your name?")

def get_phone(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_data["user_name"] = update.message.text
    context.bot.sendMessage(chat_id, user_data['user_name'])


start_handler = CommandHandler('start', start) 

txt_handler = MessageHandler(Filters.chat_type.private, get_phone)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(txt_handler)

updater.start_polling()
updater.idle()
