import telebot
from telebot import types
from PIL import Image
from main import bandage_maker, search_bandages


param = False
size = 'Steve'
token = '6204807010:AAGgP8MAjlTq0yclennyfPERXU-qUA2J1MQ'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    size_but_1 = types.KeyboardButton("Steve")
    size_but_2 = types.KeyboardButton("Alex")

    markup.add(size_but_1)
    markup.add(size_but_2)

    bot.send_message(message.chat.id, """Привет, если ты пришёл сюда, скорее всего ты хочешь получить повязку на 
свой скин, что ж тогда напиши размеры своего скина.""", reply_markup=markup)


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    size_but_1 = types.KeyboardButton("Steve")
    size_but_2 = types.KeyboardButton("Alex")

    markup.add(size_but_1)
    markup.add(size_but_2)

    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    global size
    if message.text == "Steve":
        size = message.text
    elif message.text == 'Alex':
        size = message.text

    if message.text == "Steve" or message.text == 'Alex':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        colour_but_1 = types.KeyboardButton("Жёлтый")
        colour_but_2 = types.KeyboardButton("Красный")
        colour_but_3 = types.KeyboardButton("Фиолетовый")
        colour_but_4 = types.KeyboardButton("Нуар")

        markup.add(colour_but_1)
        markup.add(colour_but_2)
        markup.add(colour_but_3)
        markup.add(colour_but_4)

        bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

    if message.text == "Жёлтый" or message.text == 'Красный' or message.text == 'Фиолетовый' or message.text == 'Нуар':
        color = message.text

        global param
        param = True

        bot.send_message(message.chat.id, 'Круто!')
        bot.send_message(message.chat.id, 'Теперь мне нужна развёртка твоего скина')

        search_bandages(size, color)


@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'photos/' + message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bandage_maker(src)

        # ans = Image.open('photos/you.png')
        with open('photos/you.png', 'rb') as ans:
            bot.send_document(message.chat.id, ans)

    except Exception as e:
        bot.reply_to(message, e)


bot.infinity_polling()
