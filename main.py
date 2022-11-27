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
        "UID" : "",
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
            [InlineKeyboardButton(text=done_reg, callback_data="done")]
    ]
    context.bot.sendMessage(chat_id=chat_id, text=mexc_register, reply_markup = InlineKeyboardMarkup(register_but))


def done(update: Update, context: CallbackQuery):
    query = update.callback_query
    data = query.data
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    if data == "done":
        text = " برای ادامه ثبت نام UID صرافی خود را وارد کنید."
        context.bot.editMessageText(text=text, chat_id=chat_id, message_id=message_id)

def check(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_data["UID"] = update.message.text
    ch_id = -1001508066765
    King_of_trade_id = -1001881041517
    UID = user_data["UID"]
    phone = user_data["user_phone"]
    user_text = "phone = {} \n UID = {} \n user_id = {}".format(phone, UID, chat_id)
    inviteLink = context.bot.create_chat_invite_link(chat_id=King_of_trade_id ,member_limit=3)
    greeting = " ثبت نام شما با موفقیت انجام شد. \n برای عضویت در کانال روی لینک زیر کلیک کنید."
    context.bot.sendMessage(chat_id=ch_id, text= user_text)
    context.bot.sendMessage(chat_id=chat_id, text= greeting)
    context.bot.sendMessage(chat_id=chat_id, text = inviteLink.invite_link)





start_handler = CommandHandler('start', start) 
mexc_handler = MessageHandler (Filters.contact,callback=mexc, pass_user_data=True)
done_handler = CallbackQueryHandler(done)
check_handler = MessageHandler(Filters.regex(r'^\d{8}$'), callback=check)


dispatcher.add_handler(check_handler)
dispatcher.add_handler(done_handler)
dispatcher.add_handler(mexc_handler)
dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()
