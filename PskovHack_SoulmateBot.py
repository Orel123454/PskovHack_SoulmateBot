import telebot
import feedparser
import random
from telebot import types

python_wiki_rss_url= "https://news.yandex.ru/koronavirus.rss"   # Ссылка на rss новости, возможны любые новости в формате rss

feed = feedparser.parse( python_wiki_rss_url )

bot = telebot.TeleBot('токен украли коспирологи(') # Авторизируемся через токин бота
summ = 0
ft = []
for post in feed.entries:
    ft.append(post.title + "\n" + post.description + "\n" + post.link) # Разбиваем ленту на новости

@bot.message_handler(content_types=['text']) # Включаем прослушивание текстовых сообщений
def start(message):
    keyboard = types.InlineKeyboardMarkup()  # Создаём клавиатуру
    key_yes = types.InlineKeyboardButton(text='Новости', callback_data='yes') 
    keyboard.add(key_yes); 
    key_no= types.InlineKeyboardButton(text='Тест', callback_data='no')
    keyboard.add(key_no)
    question = "Что Вы хотите от такого милого бота?" + "\n" + "Вы можете:" + "\n" + "1. Узнать последние новости про COVID-19." + "\n" + "2. Пройти тест на симптоматику COVID-19 и получить рекомендации."
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard) 
    

@bot.callback_query_handler(func=lambda call: True) # Прослушивание данных с клавиатуры
def callback_worker(call):
    global summ
    if call.data == "yes": 
        bot.send_message(call.message.chat.id, ft[random.randint(0, 5)]) # Вывод новостей. 5 указывается для избежения нехватки новостей
    elif call.data == "no":  # Сам тест
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_1_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_1_no')
        keyboard.add(key_no)
        summ = 0
        question = "Превышала ли температура Вашего тела отметку в 37,0 °C в последнее время?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_1_yes":
        summ+=12
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_2_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_2_no')
        keyboard.add(key_no)
        question = "Беспокоит ли Вас затрудненное дыхание?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_1_no":
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_2_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_2_no')
        keyboard.add(key_no)
        question = "Беспокоит ли Вас затрудненное дыхание?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_2_yes":
        summ+=12
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_3_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_3_no')
        keyboard.add(key_no)
        question = "Чихание?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_2_no":
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_3_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_3_no')
        keyboard.add(key_no)
        question = "Чихание?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_3_yes":
        summ+=5
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_4_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_4_no')
        keyboard.add(key_no)
        question = "Кашель?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_3_no":
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_4_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_4_no')
        keyboard.add(key_no)
        question = "Кашель?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_4_yes":
        summ+=11
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_5_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_5_no')
        keyboard.add(key_no)
        question = "Беспокоит ли Вас заложенность носа?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_4_no":
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_5_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_5_no')
        keyboard.add(key_no)
        question = "Беспокоит ли Вас заложенность носа?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_5_yes":
        summ+=5
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_6_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_6_no')
        keyboard.add(key_no)
        question = "Боли в мышцах?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_5_no":
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_6_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_6_no')
        keyboard.add(key_no)
        question = "Боли в мышцах?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_6_yes":
        summ+=6
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_7_yes')
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_7_no')
        keyboard.add(key_no)
        question = "Боли в груди?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_6_no":
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_7_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_7_no')
        keyboard.add(key_no)
        question = "Боли в груди?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_7_yes":
        summ+=8
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_8_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_8_no')
        keyboard.add(key_no)
        question = "Беспокоит ли Вас головная боль?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_7_no":
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_8_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_8_no')
        keyboard.add(key_no)
        question = "Беспокоит ли Вас головная боль?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_8_yes":
        summ+=11
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_9_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_9_no')
        keyboard.add(key_no)
        question = "Слабость?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_8_no":
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_9_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_9_no')
        keyboard.add(key_no)
        question = "Слабость?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_9_yes":
        summ+=8
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_10_yes')
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_10_no')
        keyboard.add(key_no)
        question = "Расстройства пищеварительной системы?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_9_no":
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_10_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_10_no')
        keyboard.add(key_no)
        question = "Расстройства пищеварительной системы?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_10_yes":
        summ+=4
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_11_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_11_no')
        keyboard.add(key_no)
        question = "Контактировали ли Вы с официально заразившимся COVID-19 за последние 14 дней?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_10_no":
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_11_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_11_no')
        keyboard.add(key_no)
        question = "Контактировали ли Вы с официально заразившимся COVID-19 за последние 14 дней?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_11_yes":
        summ+=12
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_12_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_12_no')
        keyboard.add(key_no)
        question = "Контактировали ли Вы с потенциально заразившимся COVID-19 за последние 14 дней?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_11_no":
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='test_12_yes') 
        keyboard.add(key_yes); 
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='test_12_no')
        keyboard.add(key_no)
        question = "Контактировали ли Вы с потенциально заразившимся COVID-19 за последние 14 дней?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "test_12_yes": 
        summ+=12
        if(summ<4):
            question = "Скорее всего, с Вами всё в порядке. Нет повода для беспокойства, но советую всё же соблюдать рекомендации Минздрава [https://covid19.rosminzdrav.ru/]."
            bot.send_message(call.message.chat.id, text=question)
        elif(summ<12):
            question = "У Вас есть первые признаки болезни и (или) Вы недавно контактировали с возможно заразившимися. Советую уделять больше внимания своему здоровью и соблюдать рекомендации Минздрава [https://covid19.rosminzdrav.ru/]."
            bot.send_message(call.message.chat.id, text=question)
        elif(summ<23):
            question = "Несколько признаков болезни беспокоят Вас. Советую обратиться к терапевту и соблюдать рекомендации Минздрава [https://covid19.rosminzdrav.ru/]."
            bot.send_message(call.message.chat.id, text=question)
        elif(summ<46):
            question = "Вам свойственны симптомы болезни. Советую обратиться к терапевту и соблюдать рекомендации Минздрава [https://covid19.rosminzdrav.ru/]."
            bot.send_message(call.message.chat.id, text=question)
        else:
            question = "Большинство симптомов болезни беспокоят Вас. Настоятельно рекомендую обратиться к терапевту и соблюдать рекомендации Минздрава [https://covid19.rosminzdrav.ru/]"
            bot.send_message(call.message.chat.id, text=question)
    elif call.data == "test_12_no":
        if(summ<4):
            question = "Скорее всего, с Вами всё в порядке. Нет повода для беспокойства, но советую всё же соблюдать рекомендации Минздрава [https://covid19.rosminzdrav.ru/]."
            bot.send_message(call.message.chat.id, text=question)
        elif(summ<12):
            question = "У Вас есть первые признаки болезни и (или) Вы недавно контактировали с возможно заразившимися. Советую уделять больше внимания своему здоровью и соблюдать рекомендации Минздрава [https://covid19.rosminzdrav.ru/]."
            bot.send_message(call.message.chat.id, text=question)
        elif(summ<23):
            question = "Несколько признаков болезни беспокоят Вас. Советую обратиться к терапевту и соблюдать рекомендации Минздрава [https://covid19.rosminzdrav.ru/]."
            bot.send_message(call.message.chat.id, text=question)
        elif(summ<46):
            question = "Вам свойственны симптомы болезни. Советую обратиться к терапевту и соблюдать рекомендации Минздрава [https://covid19.rosminzdrav.ru/]."
            bot.send_message(call.message.chat.id, text=question)
        else:
            question = "Большинство симптомов болезни беспокоят Вас. Настоятельно рекомендую обратиться к терапевту и соблюдать рекомендации Минздрава [https://covid19.rosminzdrav.ru/]"
            bot.send_message(call.message.chat.id, text=question)



bot.polling(none_stop=True, interval=0) # Пуллинг 