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
برای ادامه ثبت روی ارسال شماره کلیک کنید.
"""

send_num = """
ارسال شماره
"""

mexc_url ='https://www.mexc.com/landings/englishirannewuser12?handleDefaultLocale=keep&inviteCode=mexc-1Wb9n'

mexc_register = 'برای ادامه ثبت نام میتوانید از طریق لینک زیر و یا کد mexc-1Wb9n  در صرافی مکسی ثبت نام کنید و سپس روی انجام شد کلیک کنید.'
mexc_reg = 'ثبت نام در مکسی'
done_reg = 'انجام شد'
user_data =  {

        "user_name" : "",
        "user_phone" : "",
    }
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    buttons = [
        [KeyboardButton(send_num, request_contact= True)]
    ]
    context.bot.sendMessage(chat_id=chat_id, text=register, reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard= True, one_time_keyboard=True))

def mexc(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_data["user_phone"] = update.message.contact.phone_number
    print(user_data['user_phone'])
    register_but = [
            [InlineKeyboardButton(text=mexc_reg, url=mexc_url)],
            [InlineKeyboardButton(text=done_reg, url=mexc_url)]
    ]
    context.bot.sendMessage(chat_id=chat_id, text=mexc_register, reply_markup = InlineKeyboardMarkup(register_but))

start_handler = CommandHandler('start', start) 
mexc_handler = MessageHandler (Filters.contact,callback=mexc, pass_user_data=True)
dispatcher.add_handler(mexc_handler)
dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()
