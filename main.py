import logging
from telegram import *
from telegram.ext import *
from requests import *


updater = Updater( token ='Token', use_context=True)
dispatcher = updater.dispatcher


register = "رفیق از طریق گزینه ارسال شماره، شماره تلفنت رو باهمون به اشتراک بزار ❤️"

send_num = """
ارسال شماره
"""

mexc_url ='https://www.mexc.com/landings/englishirannewuser12?handleDefaultLocale=keep&inviteCode=mexc-1Wb9n'

mexc_register = 'برای شرکت تو مسابقه با لینک زیر ثبت نام کن👇🏻 \n \n پولاتو بریز تو این صرافی تا مسابقه برات شروع بشه \n \n حواست باشه رو لینک میخوای بزنی با یه فیلترشکن بزن مهم نیست ثابت باشه یا نه با فیلترشکن معمولی هم اوکیه \n \n بعد از این که ثبت نامت تموم شد \n \n روی انجام شد کلیک کن ❤️'
mexc_reg = 'ثبت نام در مکسی'
done_reg = 'انجام شد'
user_data =  {

        "user_name" : "",
        "user_phone" : "",
        "UID" : "",
    }
def start(update: Update, context: CallbackContext):
    bot_users_id = -1001648692269 
    chat_id = update.effective_chat.id
    context.bot.sendMessage(chat_id=bot_users_id,text=chat_id)
    buttons = [
        [KeyboardButton(send_num, request_contact= True)]
    ]
    context.bot.sendMessage(chat_id=chat_id, text=register, reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard= True, one_time_keyboard=True))

def mexc(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_data["user_phone"] = update.message.contact.phone_number
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
    uid_text = 'آموزش ارسال UID'
    uid_but = [
            [InlineKeyboardButton(text=uid_text, callback_data="uid")]
        ]
    if data == "done":
        text = "حالا UID صرافی رو برای ربات بفرست تا لینک کانال مسابقه برات ارسال بشه."
        context.bot.editMessageText(text=text, chat_id=chat_id, message_id=message_id, reply_markup = InlineKeyboardMarkup(uid_but))
    elif data == "uid":
        uid_help = 'طبق عکسای بالا برو جلو و UID یا همون عدد هشت رقمی رو برای ربات بفرست'
        photo1 = open('src/UID1.PNG', 'rb')
        photo2 = open('src/UID2.PNG', 'rb')
        context.bot.sendPhoto(chat_id=chat_id, photo=photo1)
        context.bot.sendPhoto(chat_id=chat_id, photo=photo2)
        context.bot.sendMessage(chat_id=chat_id, text= uid_help)



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
