import config
import telebot
from telebot import types
import logging

bot = telebot.TeleBot(config.token)

#logger
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log'
)

@bot.message_handler(commands = ['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    btn1 = types.KeyboardButton('/links-design')
    btn2 = types.KeyboardButton('/links-darkIT')
    btn3 = types.KeyboardButton('/links-IT')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Добро пожаловать, " + str(message.from_user.username) + '🤘', reply_markup = markup)

@bot.message_handler(commands = ['links-design'])
def links(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Подборка сервисов для дизайнера', url="https://telegra.ph/Podborka-servisov-dlya-dizajnera-10-31"))
    bot.send_message(message.chat.id, 'Полезные ссылки для Вас в сфере Web-Дизайна 🖌', reply_markup=markup)

@bot.message_handler(commands = ['links-darkIT'])
def links(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Автоматический взлом WI-FI', url="https://telegra.ph/Kak-organizovat-poluavtomaticheskij-vzlom-Wi-Fi-11-06"))
    markup.add(types.InlineKeyboardButton('Эффективный СМС Бомбер', url="https://telegra.ph/Delaem-ehffektivnyj-SMS-Bomber-besplatno-10-06"))
    markup.add(types.InlineKeyboardButton('Ставим скрытый майнер на свой сайт', url="https://telegra.ph/Stavim-skrytyj-majner-na-svoj-sajt-10-29"))
    bot.send_message(message.chat.id, 'Полезные ссылки для Вас в сфере Тёмной стороны IT 😈', reply_markup=markup)

@bot.message_handler(commands = ['links-IT'])
def links(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Приватные Уроки IT', url="https://telegra.ph/Sliv-platnyh-kursov-11-03"))
    markup.add(types.InlineKeyboardButton('Бесплатный домен .com .net .org на 1 год', url="https://telegra.ph/Besplatnyj-domen-com-net-org-na-1-god-09-02"))
    bot.send_message(message.chat.id, 'Полезные ссылки для Вас в сфере IT 👨‍💻', reply_markup=markup)

if __name__ == '__main__':
     bot.polling(none_stop=True)