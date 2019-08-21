import telebot;
import random;
import requests
bot = telebot.TeleBot('803891316:AAERH4aK9FYPWPYbwas-kN5tR-kZ1u_vfU4');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = -1001184721224
    id = chat_id
    if message.text == "Привет":
        bot.send_message(id, text="Ну здравствуйте, сударь")
    elif message.text == "привет":
        bot.send_message(id, text="дарова")
    elif message.text == "/help":
        bot.send_message(id, text="Пока что я ничего не умею. Надеюсь мой хозяин - маразматик допишет меня уже.")
    elif message.text == "/start":
        bot.send_message(message.from_user.id, text="А? Шо? Кто посмел меня разбудить?")
    elif message.text.lower() == "хуй":
        bot.send_message(id, text="Не матерись сука!")
    elif message.text.lower() == "иди нахуй":
        bot.send_message(id, text="Сам иди, мешок с говном!")
    elif message.text.lower() == "спааааааам":
        for i in range(0,200):
            bot.send_message(id, text="ДАА!!! ЭТО СПААААМ!!!")
    elif message.text.lower() == "ау":
        bot.send_message(id, text="Да тут я!!!")
    elif message.text.lower() == "заткнись":
        bot.send_message(id, text="Нет, иди в попу, кожанный ублюдок!")
    elif message.text.lower() == "тупой бот":
        bot.send_message(id, text="Тупой человек")
        bot.send_message(id, text="Хотя нет, животное")
    elif message.text.lower() == "айди группы":
        bot.send_message(id, id)
    elif message.text.lower() == "рандомное число":
        bot.send_message(id, random.randint(0,100))
    elif message.text.lower() == "красава":
        bot.send_message(id, "Пасиб))")
    elif message.text.lower() == "ауе":
        bot.send_message(id, "Жопа на бутылке")
    elif message.text == '/rog':
        bot.send_message(message.from_user.id, "Что написать?");
        bot.register_next_step_handler(message, get_text)
@bot.message_handler(content_types=['text'])
def get_text(message):
    global text;
    text = message.text;
    bot.send_message(chat_id=-1001184721224, text=text);
    bot.register_next_step_handler(message, get_text_messages)

bot.polling(none_stop=True, interval=0)