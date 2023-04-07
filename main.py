import telebot
from telebot.types import User

bot = telebot.TeleBot("5854004624:AAGeOVtXH_A2AY5dBrL2-5HS4Hx5AycYmv0")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Merhaba! Kullanıcı bilgilerini almak için /userinfo komutunu kullanın.")

@bot.message_handler(commands=['userinfo'])
def user_info(message):
    user: User = message.from_user
    first_name = user.first_name
    last_name = user.last_name or ""
    username = user.username or ""
    user_id = user.id
    
    try:
        phone_number = user.contact.phone_number
    except AttributeError:
        phone_number = "Numara bilgine erişemedim :X "

    message_text = f"Kullanıcı bilgileri:\n\nAdı: {first_name} {last_name}\nKullanıcı adı: @{username}\nID: {user_id}\nNumarası: {phone_number}"
    bot.reply_to(message, message_text)

@bot.inline_handler(func=lambda query: True)
def inline_handler(query):
    try:
        user: User = query.from_user
        first_name = user.first_name
        last_name = user.last_name or ""
        username = user.username or ""
        user_id = user.id

        try:
            phone_number = user.contact.phone_number
        except AttributeError:
            phone_number = "Numara bilgisi yok"

        message_text = f"Kullanıcı bilgileri:\n\nAdı: {first_name} {last_name}\nKullanıcı adı: {username}\nID: {user_id}\nNumarası: {phone_number}"

        r = telebot.types.InlineQueryResultArticle(
            id='1', title="Kullanıcı Bilgileri", input_message_content=telebot.types.InputTextMessageContent(message_text))
        bot.answer_inline_query(query.id, [r])
    except Exception as e:
        print(e)

bot.polling()
