# -*- coding: Windows-1251 -*-
import telebot
import os

class ParseMode(object):
    """This object represents a Telegram Message Parse Modes."""

    MARKDOWN = 'Markdown'
    """:obj:`str`: 'Markdown'"""
    HTML = 'HTML'
    """:obj:`str`: 'HTML'"""

token = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(token)

char_icon = 'https://image.ibb.co/iUAyRG/placeholde2r.png'
char_icon2 = 'https://image.ibb.co/eHgdkm/2.png'

@bot.message_handler(commands=['start'])
def start(x):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Розклад', 'Центри', 'Самоврядування', 'Q&A', "Мапа", 'Legal misc', 'Кафедри']])
    bot.send_photo(x.chat.id, 'AgADAgADIagxG9HA0Ul7lOxon-ugp9cPSw0ABJj6Ht95jmqlvYUPAAEC', 'Ласкаво просимо! Будь ласка, Оберіть категорію',
    reply_markup=keyboard)



#Назад
#!
#!
#!
@bot.message_handler(func=lambda message:message.text=='Назад')
def start(x):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Розклад', 'Центри', 'Організації', 'Q&A', "Мапа", 'Кафедри', 'Legal misc']])
    bot.send_photo(x.chat.id, 'AgADAgADIKgxG9HA0UkEt24TAqJ7yxHGDw4ABBjCNec_JQt1sI8AAgI', 'Оберіть категорію',
    reply_markup=keyboard)
#!
#!
#!


@bot.inline_handler(lambda query: query.query == 'Марцеляк')
def query_text(inline_query):
    hint = 'Будь ласка, введіть прізвище викладача'
    try:
        r = types.InlineQueryResultArticle('1.', 'Марцеляк Олег Володимирович', types.InputTextMessageContent(
                'Зав. кафедри конституційного права (248 аудиторія), Марцеляк Олег Володимирович'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'Майданик')
def query_text(inline_query):
    hint = 'Будь ласка, введіть прізвище викладача'
    try:
        r = types.InlineQueryResultArticle('1.', 'Майданик Роман Андрійович', types.InputTextMessageContent(
                'Зав. кафедри цивільного права (249 аудиторія), Майданик Роман Андрійович'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'Пришва')
def query_text(inline_query):
    hint = 'Будь ласка, введіть прізвище викладача'
    try:
        r = types.InlineQueryResultArticle('1.', 'Пришва Надія Юріївна', types.InputTextMessageContent(
                'Зав. кафедри фінансового права (245 аудиторія), Пришва Надія Юріївна'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'Іншин')
def query_text(inline_query):
    hint = 'Будь ласка, введіть прізвище викладача'
    try:
        r = types.InlineQueryResultArticle('1.', 'Іншин Микола Іванович', types.InputTextMessageContent(
                'Зав. кафедри трудового права та права соціального забезпечення (241 аудиторія), Іншин Микола Іванович'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'Бобровник')
def query_text(inline_query):
    hint = 'Будь ласка, введіть прізвище викладача'
    try:
        r = types.InlineQueryResultArticle('1.', 'Бобровник Світлана Василівна', types.InputTextMessageContent(
                'Зав. кафедри теорії права та держави (260 аудиторія), Бобровник Світлана Василівна'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'Погорецький')
def query_text(inline_query):
    hint = 'Будь ласка, введіть прізвище викладача'
    try:
        r = types.InlineQueryResultArticle('1.', 'Погорецький Микола Анатолійович', types.InputTextMessageContent(
                'Зав. кафедри правосуддя (250 аудиторія), Погорецький Микола Анатолійович'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'Фурса')
def query_text(inline_query):
    hint = 'Будь ласка, введіть прізвище викладача'
    try:
        r = types.InlineQueryResultArticle('1.', 'Фурса Світлана Ярославівна', types.InputTextMessageContent(
                'Зав. кафедри нотаріального та виконавчого процесу і адвокатури (265 аудиторія), Фурса Світлана Ярославівна'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'Андрушко')
def query_text(inline_query):
    hint = 'Будь ласка, введіть прізвище викладача'
    try:
        r = types.InlineQueryResultArticle('1.', 'Андрушко Петро Петрович', types.InputTextMessageContent(
                'Зав. кафедри кримінального права та кримінології (251 аудиторія), Андрушко Петро Петрович'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'Мірошниченко')
def query_text(inline_query):
    hint = 'Будь ласка, введіть прізвище викладача'
    try:
        r = types.InlineQueryResultArticle('1.', 'Мірошниченко Марія Іванівна', types.InputTextMessageContent(
                'Зав. кафедри історії права та держави (аудиторія 344), Мірошниченко Марія Іванівна'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'Орлюк')
def query_text(inline_query):
    hint = 'Будь ласка, введіть прізвище викладача'
    try:
        r = types.InlineQueryResultArticle('1.', 'Орлюк Олена Павлівна', types.InputTextMessageContent(
                'Зав. кафедри інтелектуальної власності (263 аудиторія), Орлюк Олена Павлівна'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'Трубчанінова')
def query_text(inline_query):
    hint = 'Будь ласка, введіть прізвище викладача'
    try:
        r = types.InlineQueryResultArticle('1.', 'Трубчанінова Тетяна Анатоліївна', types.InputTextMessageContent(
                'Зав. кафедри іноземних мов (257 аудиторія), Трубчанінова Тетяна Анатоліївна'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'Коваленко')
def query_text(inline_query):
    hint = 'Будь ласка, введіть прізвище викладача'
    try:
        r = types.InlineQueryResultArticle('1.', 'Коваленко Тетяна Олександрівна', types.InputTextMessageContent(
                'Зав. кафедри земельного та аграрного права(242 аудиторія), Коваленко Тетяна Олександрівна'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'Краснова')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1.', 'Краснова Марія Василівна', types.InputTextMessageContent(
                'Зав. кафедри екологічного права (244 аудиторія), Краснова Марія Василівна'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'Бевзенко')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', 'Бевзенко Володимир Михайлович', types.InputTextMessageContent(
                'Зав. кафедри адміністративного права (324 аудиторія), Бевзенко Володимир Михайлович'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == 'Щербина')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', 'Щербина Валентин Степанович', types.InputTextMessageContent(
                    'Зав. кафедри господарського права (256 аудиторія), Щербина Валентин Степанович'), thumb_url=char_icon,
                                                   thumb_width=48, thumb_height=48)
       bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
       print(e)

#-----------------------------------------Inline

@bot.inline_handler(lambda query: query.query == 'Кафедра адміністративного права' or 'Адмінка' or 'Адм' or 'Адміністративне' or 'Адміні')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', 'Бевзенко Володимир Михайлович', types.InputTextMessageContent(
                'Зав. кафедри адміністративного права <b>(324 аудиторія)</b>, Бевзенко Володимир Михайлович', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', 'Гриценко Іван Сергійович', types.InputTextMessageContent(
                'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Гриценко Іван Сергійович', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', 'Берлач Анатолій Іванович', types.InputTextMessageContent(
           'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Берлач Анатолій Іванович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', 'Діхтієвський Петро Васильович', types.InputTextMessageContent(
           'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Діхтієвський Петро Васильович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', 'Мельник Роман Сергійович', types.InputTextMessageContent(
           'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Мельник Роман Сергійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', 'Смокович Михайло Іванович', types.InputTextMessageContent(
           'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Смокович Михайло Іванович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', 'Ващенко Юлія Вячеславівна', types.InputTextMessageContent(
           'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Ващенко Юлія Вячеславівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', 'Вільгушинський Михайло Йосипович', types.InputTextMessageContent(
           'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Вільгушинський Михайло Йосипович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', 'Пасенюк Олександр Михайлович', types.InputTextMessageContent(
           'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Пасенюк Олександр Михайлович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', 'Цуркан Михайло Іванович', types.InputTextMessageContent(
           'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Цуркан Михайло Іванович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', 'Герасименко Євген Станіславович', types.InputTextMessageContent(
           'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Герасименко Євген Станіславович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', 'Задирака Наталія Юріївна', types.InputTextMessageContent(
           'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Задирака Наталія Юріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', 'Пухтецька Алла Альбертівна', types.InputTextMessageContent(
           'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Пухтецька Алла Альбертівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', 'Куйбіда Роман Олексійович', types.InputTextMessageContent(
           'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Куйбіда Роман Олексійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', 'Заярний Олег Анатолійович', types.InputTextMessageContent(
           'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Заярний Олег Анатолійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', 'Радишевська Олеся Ростиславівна', types.InputTextMessageContent(
           'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Радишевська Олеся Ростиславівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', 'Соломаха Артем Григорович', types.InputTextMessageContent(
           'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Соломаха Артем Григорович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', 'Гревцова Радмила Юріївна', types.InputTextMessageContent(
           'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Гревцова Радмила Юріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r19 = types.InlineQueryResultArticle('19.', 'Міхровська Марина Станіславівна', types.InputTextMessageContent(
           'Викладач кафедри адміністративного права <b>(324 аудиторія)</b>, Міхровська Марина Станіславівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r20 = types.InlineQueryResultArticle('20.', 'Про кафедру', types.InputTextMessageContent(
           'Аудиторія: <b> 324 </b > \nЗавідувач кафедри: <b> д.ю.н., проф.Бевзенко Володимир Михайлович </b> \n <a href = "https://law.knu.ua/ua/library/9-literatura-kafedry-administratyvnoho-prava"> Література кафедри </a>\n <a href = "https://law.knu.ua/ua/administrative-law"> Детальніше прокафедру </a>', parse_mode='html'), thumb_url=char_icon2, thumb_width=48, thumb_height=48)


       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20])
    except Exception as e:
       print(e)
#-----------------------------------------Inline



#@bot.message_handler(func=lambda message: message.text == 'Марцеляк')
#def start(m):
    #   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #keyboard.add(*[types.KeyboardButton(name) for name in ['Конституційне', 'Назад']])

@bot.inline_handler(lambda query: query.query == 'Кафедра цивільного права' or 'Цивільне' or 'Цив' or 'Цивільного')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', 'Майданик Роман Андрійович', types.InputTextMessageContent(
                'Зав. кафедри цивільного права <b>(249 аудиторія)</b>, Майданик Роман Андрійович', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', 'Безклубий Ігор Анатолійович', types.InputTextMessageContent(
                'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Безклубий Ігор Анатолійович', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', 'Боднар Тетяна Валеріївна', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Боднар Тетяна Валеріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', 'Дзера Олександр Васильович', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Дзера Олександр Васильович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', 'Кохановська Олена Велеонінівна', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Кохановська Олена Велеонінівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', 'Діковська Ірина Андріївна', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Діковська Ірина Андріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', 'Кузнєцова Наталія Семенівна', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Кузнєцова Наталія Семенівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', 'Отраднова Олеся Олександрівна', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Отраднова Олеся Олександрівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', 'Грамацький Ернест Мірчевич', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Грамацький Ернест Мірчевич',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', 'Макода Володимир Євгенович', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Макода Володимир Євгенович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', 'Михальнюк Оксана Василівна', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Михальнюк Оксана Василівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', 'Панова Людмила Вячеславівна', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Панова Людмила Вячеславівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', 'Первомайський Олег Олексійович', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Первомайський Олег Олексійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', 'Радченко Лілія Іванівна', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Радченко Лілія Іванівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', 'Рябоконь Євген Олександрович', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Рябоконь Євген Олександрович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', 'Харченко Георгій Георгійович', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Харченко Георгій Георгійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', 'Цюра Вадим Васильович', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Цюра Вадим Васильович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', 'Сабодаш Роман Богданович', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Сабодаш Роман Богданович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r19 = types.InlineQueryResultArticle('19.', 'Єфіменко Леонід Васильович', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Єфіменко Леонід Васильович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r20 = types.InlineQueryResultArticle('20.', 'Бажанов Валентин Олександрович', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Бажанов Валентин Олександрович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r21 = types.InlineQueryResultArticle('21.', 'Воєводін Богдан Володимирович', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Воєводін Богдан Володимирович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r22 = types.InlineQueryResultArticle('22.', 'Москаленко Катерина Вікторівна', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Москаленко Катерина Вікторівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r23 = types.InlineQueryResultArticle('23.', 'Ромащенко Іван Олегович', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Ромащенко Іван Олегович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r24 = types.InlineQueryResultArticle('24.', 'Хоменко Михайло Михайлович', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Хоменко Михайло Михайлович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r25 = types.InlineQueryResultArticle('25.', 'Базова Тетяна Павлівна', types.InputTextMessageContent(
           'Викладач кафедри цивільного права <b>(249 аудиторія)</b>, Базова Тетяна Павлівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r26 = types.InlineQueryResultArticle('26.', 'Про кафедру', types.InputTextMessageContent(
           'Аудиторія: <b>249</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Майданик Роман Андрійович</b> \n<a href="https://law.knu.ua/ua/library/11-literatura-kafedry-tsyvilnoho-prava">Література кафедри</a>\n<a href="https://law.knu.ua/ua/civil-law">Детальніше про кафедру</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)


       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == 'Кафедра фінансового права' or 'Фін' or 'Фінанс' or 'Фінансове')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', 'Пришва Надія Юріївна', types.InputTextMessageContent(
                'Зав. кафедри фінансового права <b>(245 аудиторія)</b>, Пришва Надія Юріївна', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', 'Гетманцев Данило Олександрович', types.InputTextMessageContent(
                'Викладач кафедри фінансового права <b>(245 аудиторія)</b>, Гетманцев Данило Олександрович', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', 'Якимчук Наталія Яківна', types.InputTextMessageContent(
           'Викладач кафедри фінансового права <b>(245 аудиторія)</b>, Якимчук Наталія Яківна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', 'Перощук Зорина Іванівна', types.InputTextMessageContent(
           'Викладач кафедри фінансового права <b>(245 аудиторія)</b>, Перощук Зорина Іванівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', 'Губерська Наталія Леонідівна', types.InputTextMessageContent(
           'Викладач кафедри фінансового права <b>(245 аудиторія)</b>, Губерська Наталія Леонідівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', 'Кадькаленко Сергій Тимофійович', types.InputTextMessageContent(
           'Викладач кафедри фінансового права <b>(245 аудиторія)</b>, Кадькаленко Сергій Тимофійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', 'Чуприна Людмила Миколаївна', types.InputTextMessageContent(
           'Викладач кафедри фінансового права <b>(245 аудиторія)</b>, Чуприна Людмила Миколаївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', 'Ковалко Наталія Миколаївна', types.InputTextMessageContent(
           'Викладач кафедри фінансового права <b>(245 аудиторія)</b>, Ковалко Наталія Миколаївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', 'Лещенко Роман Миколайович', types.InputTextMessageContent(
           'Викладач кафедри фінансового права <b>(245 аудиторія)</b>, Лещенко Роман Миколайович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', 'Гедзюк Олена Вікторівна', types.InputTextMessageContent(
           'Викладач кафедри фінансового права <b>(245 аудиторія)</b>, Гедзюк Олена Вікторівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', 'Про кафедру', types.InputTextMessageContent(
           'Аудиторія: <b>245</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Пришва Надія Юріївна</b> \n<a href="https://law.knu.ua/ua/library/21-literatura-kafedry-finansovogo-prava">Література кафедри</a>\n<a href="https://law.knu.ua/ua/financial-law">Детальніше про кафедру</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)



       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == 'Кафедра трудового права та права соціального забезпечення' or 'Трудове' or 'Псз' or 'Соціальн' or 'Труд' or 'Трудового')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', 'Іншин Микола Іванович', types.InputTextMessageContent(
                'Зав. кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Іншин Микола Іванович', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', 'Щербина Віктор Іванович', types.InputTextMessageContent(
                'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Щербина Віктор Іванович', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', 'Андріїв Василь Михайлович', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Андріїв Василь Михайлович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', 'Мельничук Наталія Олексіївна', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Мельничук Наталія Олексіївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', 'Гришина Юлія Миколаївна', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Гришина Юлія Миколаївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', 'Занфірова Тетяня Анатоліївна', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Занфірова Тетяня Анатоліївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', 'Венедиктов Сергій Валентинович', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Венедиктов Сергій Валентинович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', 'Вавженчук Сергій Ярославович', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Вавженчук Сергій Ярославович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', 'Тищенко Олена Володимирівна', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Тищенко Олена Володимирівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', 'Волинець Владислав Володимирович', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Волинець Владислав Володимирович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', 'Кучма Ольга Леонідівна', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Кучма Ольга Леонідівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', 'Панасюк Олег Терентійович', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Панасюк Олег Терентійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', 'Черноус Світлана Миколаївна', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Черноус Світлана Миколаївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', 'Саленко Ірина Володимирівна', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Саленко Ірина Володимирівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', 'Вахонєва Тетяна Миколаївна', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Вахонєва Тетяна Миколаївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', 'Малюга Леся Юріївна', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Малюга Леся Юріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', 'Богдан Ірина Анатоліївна', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Богдан Ірина Анатоліївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', 'Погорєлова Олександра Сергіївна', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Погорєлова Олександра Сергіївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r19 = types.InlineQueryResultArticle('19.', 'Сахарук Ірина Сергіївна', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Сахарук Ірина Сергіївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r20 = types.InlineQueryResultArticle('20.', 'Сіроха Дмитро Ігорович', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Сіроха Дмитро Ігорович',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r21 = types.InlineQueryResultArticle('21.', 'Сіньова Людмила Миколаївна', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Сіньова Людмила Миколаївна',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r22 = types.InlineQueryResultArticle('22.', 'Кузьменко Галина Валентинівна', types.InputTextMessageContent(
           'Викладач кафедри трудового права та права соціального забезпечення <b>(241 аудиторія)</b>, Кузьменко Галина Валентинівна',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r23 = types.InlineQueryResultArticle('23.', 'Про кафедру', types.InputTextMessageContent(
           'Аудиторія: <b>241</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Іншин Микола Іванович</b> \n<a href="https://law.knu.ua/ua/library/20-literatura-kafedry-trudovogo-prava-ta-prava-socialnogo-zabezpechennja">Література кафедри</a>\n<a href="https://law.knu.ua/ua/labor-law-and-law-of-social-security">Детальніше про кафедру</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                            thumb_width=48, thumb_height=48)



       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == 'Кафедра теорії права та держави' or 'Тдп' or 'Теорії')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', 'Бобровник Світлана Василівна', types.InputTextMessageContent(
                'Зав. кафедри теорії права та держави <b>(260 аудиторія)</b>, Бобровник Світлана Василівна', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', 'Дзейко Жанна Олександрівна', types.InputTextMessageContent(
                'Викладач кафедри теорії права та держави <b>(260 аудиторія)</b>, Дзейко Жанна Олександрівна', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', 'Костицький Василь Васильович', types.InputTextMessageContent(
           'Викладач кафедри теорії права та держави <b>(260 аудиторія)</b>, Костицький Василь Васильович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', 'Котюк Іван Ілліч', types.InputTextMessageContent(
           'Викладач кафедри теорії права та держави <b>(260 аудиторія)</b>, Котюк Іван Ілліч',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', 'Малишев Борис Володимирович', types.InputTextMessageContent(
           'Викладач кафедри теорії права та держави <b>(260 аудиторія)</b>, Малишев Борис Володимирович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', 'Костицький Василь Васильович', types.InputTextMessageContent(
           'Викладач кафедри теорії права та держави <b>(260 аудиторія)</b>, Костицький Василь Васильович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', 'Самохвалов Віктор Панасович', types.InputTextMessageContent(
           'Викладач кафедри теорії права та держави <b>(260 аудиторія)</b>, Самохвалов Віктор Панасович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', 'Котюк Володимир Олександрович', types.InputTextMessageContent(
           'Викладач кафедри теорії права та держави <b>(260 аудиторія)</b>, Котюк Володимир Олександрович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', 'Дудар Світлана Костянтинівна', types.InputTextMessageContent(
           'Викладач кафедри теорії права та держави <b>(260 аудиторія)</b>, Дудар Світлана Костянтинівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', 'Кабанець Наталія Іванівна', types.InputTextMessageContent(
           'Викладач кафедри теорії права та держави <b>(260 аудиторія)</b>, Кабанець Наталія Іванівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', 'Ковальчук Олександр Михайлович', types.InputTextMessageContent(
           'Викладач кафедри теорії права та держави <b>(260 аудиторія)</b>, Ковальчук Олександр Михайлович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', 'Котенко Тетяна Вікторівна', types.InputTextMessageContent(
           'Викладач кафедри теорії права та держави <b>(260 аудиторія)</b>, Котенко Тетяна Вікторівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', 'Николина Катерина Валеріївна', types.InputTextMessageContent(
           'Викладач кафедри теорії права та держави <b>(260 аудиторія)</b>, Николина Катерина Валеріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', 'Теремцова Ніна Володимирівна', types.InputTextMessageContent(
           'Викладач кафедри теорії права та держави <b>(260 аудиторія)</b>, Теремцова Ніна Володимирівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', 'Середюк Вікторія Володимирівна', types.InputTextMessageContent(
           'Викладач кафедри теорії права та держави <b>(260 аудиторія)</b>, Середюк Вікторія Володимирівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', ' Дубов Геннадій Олексійович', types.InputTextMessageContent(
           'Викладач кафедри теорії права та держави <b>(260 аудиторія)</b>,  Дубов Геннадій Олексійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', 'Кобан Ольга Геннадіївна', types.InputTextMessageContent(
           'Викладач кафедри теорії права та держави <b>(260 аудиторія)</b>, Кобан Ольга Геннадіївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', 'Богдан Ольга Василівна', types.InputTextMessageContent(
           'Викладач кафедри теорії права та держави <b>(260 аудиторія)</b>, Богдан Ольга Василівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r19 = types.InlineQueryResultArticle('19.', 'Про кафедру', types.InputTextMessageContent(
           'Аудиторія: <b>260</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Бобровник Світлана Василівна</b> \n<a href="https://law.knu.ua/ua/library/22-literatura-kafedry-teorii-prava-ta-derzhavy">Література кафедри</a>\n<a href="https://law.knu.ua/ua/theory-of-law-and-state">Детальніше про кафедру</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)


       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == 'Кафедра правосуддя' or 'правосуддя')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', 'Погорецький Микола Анатолійович', types.InputTextMessageContent(
                'Зав. кафедри правосуддя <b>(250 аудиторія)</b>, Погорецький Микола Анатолійович', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', 'Кучинська Оксана Петрівна', types.InputTextMessageContent(
                'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Кучинська Оксана Петрівна', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', 'Прилуцький Сергій Валентинович', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Прилуцький Сергій Валентинович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', 'Притика Юрій Дмитрович', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Притика Юрій Дмитрович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', 'Шумило Микола Єгорович', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Шумило Микола Єгорович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', 'Яновська Олександра Григорівна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Яновська Олександра Григорівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', 'Сергєєва Діана Борисівна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Сергєєва Діана Борисівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', 'Дунаєвська Людмила Григорівна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Дунаєвська Людмила Григорівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', 'Шибіко Василь Петрович', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Шибіко Василь Петрович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', 'Ахтирська Наталія Миколаївна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Ахтирська Наталія Миколаївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', 'Бишевець Олена Володимирівна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Бишевець Олена Володимирівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', 'Василина Наталія Володимирівна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Василина Наталія Володимирівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', 'Васильєва-Шаламова Жанна Віталіївна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Васильєва-Шаламова Жанна Віталіївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', 'Грабовська Оксана Олександрівна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Грабовська Оксана Олександрівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', 'Гринюк Володимир Олексійович', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Гринюк Володимир Олексійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', 'Захарова Олена Семенівна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Захарова Олена Семенівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', 'Кіреєва Наталія Олександрівна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Кіреєва Наталія Олександрівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', 'Ізарова Ірина Олександрівна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Ізарова Ірина Олександрівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r19 = types.InlineQueryResultArticle('19.', 'Костюченко Олена Юріївна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Костюченко Олена Юріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r20 = types.InlineQueryResultArticle('20.', 'Крижанівський Віктор В’ячеславович', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Крижанівський Віктор В’ячеславович',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r21 = types.InlineQueryResultArticle('21.', 'Лисенко Анатолій Миколайович', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Лисенко Анатолій Миколайович',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r22 = types.InlineQueryResultArticle('22.', 'Малюга Віктор Іванович', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Малюга Віктор Іванович',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r23 = types.InlineQueryResultArticle('23.', 'Плахотнік Олег Віталійович', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Плахотнік Олег Віталійович',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r24 = types.InlineQueryResultArticle('24.', 'Сиза Наталія Петрівна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Сиза Наталія Петрівна',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r25 = types.InlineQueryResultArticle('25.', 'Скригонюк Микола Іванович', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Скригонюк Микола Іванович',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r26 = types.InlineQueryResultArticle('26.', 'Нестор Наталія Володимирівна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Нестор Наталія Володимирівна',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r27 = types.InlineQueryResultArticle('27.', 'Саленко Ольга Василівна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Саленко Ольга Василівна',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r28 = types.InlineQueryResultArticle('28.', 'Виноградова Анна Ігорівна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Виноградова Анна Ігорівна',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r29 = types.InlineQueryResultArticle('29.', 'Задоєнко Олексій Володимирович', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Задоєнко Олексій Володимирович',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r30 = types.InlineQueryResultArticle('30.', 'Набруско Марія Степанівна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Набруско Марія Степанівна',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r31 = types.InlineQueryResultArticle('31.', 'Котюк Олександр Іванович', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Котюк Олександр Іванович',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r32 = types.InlineQueryResultArticle('32.', 'Топорецька Зоряна Миколаївна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Топорецька Зоряна Миколаївна',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r33 = types.InlineQueryResultArticle('33.', 'Зеленська Марина Ігорівна', types.InputTextMessageContent(
           'Викладач кафедри правосуддя <b>(250 аудиторія)</b>, Зеленська Марина Ігорівна',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r34 = types.InlineQueryResultArticle('34.', 'Про кафедру', types.InputTextMessageContent(
           'Аудиторія: <b>250</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Погорецький Микола Анатолійович</b> \n<a href="https://law.knu.ua/ua/library/10-literatura-kafedry-pravosuddia">Література кафедри</a>\n<a href="https://law.knu.ua/ua/justice">Детальніше про кафедру</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                            thumb_width=48, thumb_height=48)

       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, r27, r28, r29, r30, r31, r32, r33, r34])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == 'Кафедра нотаріального та виконавчого процесу і адвокатури' or 'Нотар' or 'Нотаріального' or 'Кафедра нотаріального' or 'Адвокатури'or 'Кафедра адвокатури')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', 'Фурса Світлана Ярославівна', types.InputTextMessageContent(
                'Зав. кафедри нотаріального та виконавчого процесу і адвокатури <b>(265 аудиторія)</b>, Фурса Світлана Ярославівна', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', 'Бондарєва Марія Володимирівна', types.InputTextMessageContent(
                'Викладач кафедри нотаріального та виконавчого процесу і адвокатури <b>(265 аудиторія)</b>, Бондарєва Марія Володимирівна', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', ' Бондар Ірина Вадимівна', types.InputTextMessageContent(
           'Викладач кафедри нотаріального та виконавчого процесу і адвокатури <b>(265 аудиторія)</b>,  Бондар Ірина Вадимівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', 'Рабовська Світлана Янівна', types.InputTextMessageContent(
           'Викладач кафедри нотаріального та виконавчого процесу і адвокатури <b>(265 аудиторія)</b>, Рабовська Світлана Янівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', 'Снідевич Олександр Станіславович', types.InputTextMessageContent(
           'Викладач кафедри нотаріального та виконавчого процесу і адвокатури <b>(265 аудиторія)</b>, Снідевич Олександр Станіславович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', 'Кухнюк Дмитро Володимирович', types.InputTextMessageContent(
           'Викладач кафедри нотаріального та виконавчого процесу і адвокатури <b>(265 аудиторія)</b>, Кухнюк Дмитро Володимирович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', 'Мельник Ірина Степанівна', types.InputTextMessageContent(
           'Викладач кафедри нотаріального та виконавчого процесу і адвокатури <b>(265 аудиторія)</b>, Мельник Ірина Степанівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', 'Кучер Тетяна Миколаївна', types.InputTextMessageContent(
           'Викладач кафедри нотаріального та виконавчого процесу і адвокатури <b>(265 аудиторія)</b>, Кучер Тетяна Миколаївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', 'Малярчук (Лисенко) Любов Сергіївна', types.InputTextMessageContent(
           'Викладач кафедри нотаріального та виконавчого процесу і адвокатури <b>(265 аудиторія)</b>, Малярчук (Лисенко) Любов Сергіївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', 'Дерій Олена Олександрівна', types.InputTextMessageContent(
           'Викладач кафедри нотаріального та виконавчого процесу і адвокатури <b>(265 аудиторія)</b>, Дерій Олена Олександрівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', 'Горбань Наталія Сергіївна', types.InputTextMessageContent(
           'Викладач кафедри нотаріального та виконавчого процесу і адвокатури <b>(265 аудиторія)</b>, Горбань Наталія Сергіївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', 'Про кафедру', types.InputTextMessageContent(
           'Аудиторія: <b>265</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Фурса Світлана Ярославівна</b> \n<a href="https://law.knu.ua/ua/library/23-literatura-kafedry-notarialnogo-ta-vykonavchogo-procesu-i-advokatury">Література кафедри</a>\n<a href="https://law.knu.ua/ua/notarial-and-executive-process-and-advocacy">Детальніше про кафедру</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)

       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == 'Кафедра кримінального права та кримінології' or 'Крим' or 'Кримінального' or 'Кримінальне')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', 'Андрушко Петро Петрович', types.InputTextMessageContent(
                'Зав. кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Андрушко Петро Петрович', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', 'Берзін Павло Сергійович', types.InputTextMessageContent(
                'Викладач кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Берзін Павло Сергійович', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', 'Хавронюк Микола Іванович', types.InputTextMessageContent(
           'Викладач кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Хавронюк Микола Іванович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', 'Шапченко Сергій Дмитрович', types.InputTextMessageContent(
           'Викладач кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Шапченко Сергій Дмитрович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', 'Бахуринська Олена Олександрівна', types.InputTextMessageContent(
           'Викладач кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Бахуринська Олена Олександрівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', 'Волинець Руслан Анатолійович', types.InputTextMessageContent(
           'Викладач кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Волинець Руслан Анатолійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', 'Давидович Ірина Ігорівна', types.InputTextMessageContent(
           'Викладач кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Давидович Ірина Ігорівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', 'Дзюба Володимир Трохимович', types.InputTextMessageContent(
           'Викладач кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Дзюба Володимир Трохимович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', 'Єфремов Сергій Олександрович', types.InputTextMessageContent(
           'Викладач кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Єфремов Сергій Олександрович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', 'Задоя Костянтин Петрович', types.InputTextMessageContent(
           'Викладач кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Задоя Костянтин Петрович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', 'Ільїна Оксана Валеріївна', types.InputTextMessageContent(
           'Викладач кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Ільїна Оксана Валеріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', 'Кікалішвилі Марія Вікторівна', types.InputTextMessageContent(
           'Викладач кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Кікалішвилі Марія Вікторівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', 'Усатий Григорій Олександрович', types.InputTextMessageContent(
           'Викладач кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Усатий Григорій Олександрович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', 'Куцевич Максим Петрович', types.InputTextMessageContent(
           'Викладач кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Куцевич Максим Петрович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', 'Беньківський Володимир Олександрович', types.InputTextMessageContent(
           'Викладач кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Беньківський Володимир Олександрович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', 'Демченко Ірина Михайлівна', types.InputTextMessageContent(
           'Викладач кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Демченко Ірина Михайлівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', 'Птащенко Дмитро Сергійович', types.InputTextMessageContent(
           'Викладач кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Птащенко Дмитро Сергійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', 'Ткаченко Валентина Василівна', types.InputTextMessageContent(
           'Викладач кафедри кримінального права та кримінології <b>(251 аудиторія)</b>, Ткаченко Валентина Василівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r19 = types.InlineQueryResultArticle('19.', 'Про кафедру', types.InputTextMessageContent(
           'Аудиторія: <b>251</b> \nЗавідувач кафедри: <b>к.ю.н., проф. Андрушко Петро Петрович</b> \n<a href="https://law.knu.ua/ua/library/19-literatura-kafedry-kryminalnoho-prava-ta-kryminolohii">Література кафедри</a>\n<a href="https://law.knu.ua/ua/criminal-law-and-criminology">Детальніше про кафедру</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)


       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == 'Кафедра конституційного права' or 'Конституційне' or 'Конст' or 'Конституційного' or 'Кафедра конституційного')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', 'Марцеляк Олег Володимирович', types.InputTextMessageContent(
                'Зав. кафедри конституційного права <b>(248 аудиторія)</b>, Марцеляк Олег Володимирович', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', 'Мяловицька Ніна Анатоліївна', types.InputTextMessageContent(
                'Викладач кафедри конституційного права <b>(248 аудиторія)</b>, Мяловицька Ніна Анатоліївна', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', 'Совгиря Ольга Володимирівна', types.InputTextMessageContent(
           'Викладач кафедри конституційного права <b>(248 аудиторія)</b>, Совгиря Ольга Володимирівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', 'Лотюк Ольга Степанівна', types.InputTextMessageContent(
           'Викладач кафедри конституційного права <b>(248 аудиторія)</b>, Лотюк Ольга Степанівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', 'Васильченко Оксана Петрівна', types.InputTextMessageContent(
           'Викладач кафедри конституційного права <b>(248 аудиторія)</b>, Васильченко Оксана Петрівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', 'Стецюк Петро Богданович', types.InputTextMessageContent(
           'Викладач кафедри конституційного права <b>(248 аудиторія)</b>, Стецюк Петро Богданович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', 'Волошин Юрій Олексійович', types.InputTextMessageContent(
           'Викладач кафедри конституційного права <b>(248 аудиторія)</b>, Волошин Юрій Олексійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', 'Колодій Анатолій Миколайович', types.InputTextMessageContent(
           'Викладач кафедри конституційного права <b>(248 аудиторія)</b>, Колодій Анатолій Миколайович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', 'Городецький Олександр Васильович', types.InputTextMessageContent(
           'Викладач кафедри конституційного права <b>(248 аудиторія)</b>, Городецький Олександр Васильович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', 'Москалюк Олександр Володимирович', types.InputTextMessageContent(
           'Викладач кафедри конституційного права <b>(248 аудиторія)</b>, Москалюк Олександр Володимирович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', 'Ключковський Юрій Богданович', types.InputTextMessageContent(
           'Викладач кафедри конституційного права <b>(248 аудиторія)</b>, Ключковський Юрій Богданович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', 'Сінькевич Олена Василівна', types.InputTextMessageContent(
           'Викладач кафедри конституційного права <b>(248 аудиторія)</b>, Сінькевич Олена Василівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', 'Черняк Євгенія Валеріївна', types.InputTextMessageContent(
           'Викладач кафедри конституційного права <b>(248 аудиторія)</b>, Черняк Євгенія Валеріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', 'Слюсаренко Юрій Анатолійович', types.InputTextMessageContent(
           'Викладач кафедри конституційного права <b>(248 аудиторія)</b>, Слюсаренко Юрій Анатолійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', 'Чехович Тетяна Валеріївна', types.InputTextMessageContent(
           'Викладач кафедри конституційного права <b>(248 аудиторія)</b>, Чехович Тетяна Валеріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', 'Шамрай В’ячеслав Вікторович', types.InputTextMessageContent(
           'Викладач кафедри конституційного права <b>(248 аудиторія)</b>, Шамрай В’ячеслав Вікторович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', 'Кудрявцева Олена Миколаївна', types.InputTextMessageContent(
           'Викладач кафедри конституційного права <b>(248 аудиторія)</b>, Кудрявцева Олена Миколаївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', 'Кравцова Зоріна Сергіївна', types.InputTextMessageContent(
           'Викладач кафедри конституційного права <b>(248 аудиторія)</b>, Гревцова Радмила Юріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r19 = types.InlineQueryResultArticle('19.', 'Про кафедру', types.InputTextMessageContent(
           'Аудиторія: <b>248</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Марцеляк Олег Володимирович</b> \n<a href="https://law.knu.ua/ua/library/13-literatura-kafedry-konstytutsiinoho-prava">Література кафедри</a>\n<a href="https://law.knu.ua/ua/constitutional-law">Детальніше про кафедру</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)


       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == 'Кафедра історії права та держави' or 'ІДПЗК' or 'ІПД' or 'Історії' or 'Кафедра істроії')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', 'Захарченко Петро Павлович', types.InputTextMessageContent(
                'В.о. зав. кафедри історії права та держави <b>(344 аудиторія)</b>, Захарченко Петро Павлович', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', 'Захарченко Петро Павлович', types.InputTextMessageContent(
                'Викладач кафедри історії права та держави <b>(344 аудиторія)</b>, Захарченко Петро Павлович', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', 'Вовк Олександр Йосипович', types.InputTextMessageContent(
                'Викладач кафедри історії права та держави <b>(344 аудиторія)</b>, Вовк Олександр Йосипович', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', 'Цвєткова Юліанна Володимирівна', types.InputTextMessageContent(
           'Викладач кафедри історії права та держави <b>(344 аудиторія)</b>, Цвєткова Юліанна Володимирівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', 'Левчук Марія В’ячеславівна', types.InputTextMessageContent(
           'Викладач кафедри історії права та держави <b>(344 аудиторія)</b>, Левчук Марія В’ячеславівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', 'Дячук Леонтій Володимирович', types.InputTextMessageContent(
           'Викладач кафедри історії права та держави <b>(344 аудиторія)</b>, Дячук Леонтій Володимирович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', 'Калиновський Валерій Степанович', types.InputTextMessageContent(
           'Викладач кафедри історії права та держави <b>(344 аудиторія)</b>, Калиновський Валерій Степанович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', 'Мацелюх Іванна Андріївна', types.InputTextMessageContent(
           'Викладач кафедри історії права та держави <b>(344 аудиторія)</b>, Мацелюх Іванна Андріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', 'Чубата Марина Валеріївна', types.InputTextMessageContent(
           'Викладач кафедри історії права та держави <b>(344 аудиторія)</b>, Чубата Марина Валеріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', 'Карпічков Віталій Олександрович', types.InputTextMessageContent(
           'Викладач кафедри історії права та держави <b>(344 аудиторія)</b>, Карпічков Віталій Олександрович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', 'Крижевський Антон Васильович', types.InputTextMessageContent(
           'Викладач кафедри історії права та держави <b>(344 аудиторія)</b>, Крижевський Антон Васильович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', 'Про кафедру', types.InputTextMessageContent(
           'Аудиторія: <b>344</b> \nВ.О. Завідувача кафедри: <b>к.і.н., д.ю.н., проф. Мірошниченко Марія Іванівна</b> \n<a href="https://law.knu.ua/ua/library/15-literatura-kafedry-istorii-prava-ta-derzhavy">Література кафедри</a>\n<a href="https://law.knu.ua/ua/history-of-law-and-state">Детальніше про кафедру</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)

       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == 'Кафедра інтелектуальної власності' or 'Кафедра інтелектуальної' or 'Інтелектуальної')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', 'Орлюк Олена Павлівна', types.InputTextMessageContent(
                'В. о. зав. кафедри інтелектуальної власності <b>(257 аудиторія)</b>, Орлюк Олена Павлівна', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', 'Мироненко Наталія Михайлівна', types.InputTextMessageContent(
                'Викладач кафедри інтелектуальної власності <b>(257 аудиторія)</b>, Мироненко Наталія Михайлівна', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', 'Кодинець Анатолій Олександрович', types.InputTextMessageContent(
           'Викладач кафедри інтелектуальної власності <b>(257 аудиторія)</b>, Кодинець Анатолій Олександрович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', 'Комзюк Леонід Трохимович', types.InputTextMessageContent(
           'Викладач кафедри інтелектуальної власності <b>(257 аудиторія)</b>, Комзюк Леонід Трохимович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', 'Блажівська Оксана Євгеніївна', types.InputTextMessageContent(
           'Викладач кафедри інтелектуальної власності <b>(257 аудиторія)</b>, Блажівська Оксана Євгеніївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', 'Петренко Сергій Анатолійович', types.InputTextMessageContent(
           'Викладач кафедри інтелектуальної власності <b>(257 аудиторія)</b>, Петренко Сергій Анатолійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', 'Харченко Олеся Степанівна', types.InputTextMessageContent(
           'Викладач кафедри інтелектуальної власності <b>(257 аудиторія)</b>, Харченко Олеся Степанівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', 'Кашинцева Оксана Юріївна', types.InputTextMessageContent(
           'Викладач кафедри інтелектуальної власності <b>(257 аудиторія)</b>, Кашинцева Оксана Юріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', 'Носік Юрій Володимирович', types.InputTextMessageContent(
           'Викладач кафедри інтелектуальної власності <b>(257 аудиторія)</b>, Носік Юрій Володимирович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', 'Кривошеїна Інга Валеріївна', types.InputTextMessageContent(
           'Викладач кафедри інтелектуальної власності <b>(257 аудиторія)</b>, Кривошеїна Інга Валеріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', 'Котенко Микола Віталійович', types.InputTextMessageContent(
           'Викладач кафедри інтелектуальної власності <b>(257 аудиторія)</b>, Котенко Микола Віталійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', 'Кронда Ольга Юріївна', types.InputTextMessageContent(
           'Викладач кафедри інтелектуальної власності <b>(257 аудиторія)</b>, Кронда Ольга Юріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', 'Каращук Оксана Олександрівна', types.InputTextMessageContent(
           'Викладач кафедри інтелектуальної власності <b>(257 аудиторія)</b>, Каращук Оксана Олександрівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', 'Майданик Любов Романівна', types.InputTextMessageContent(
           'Викладач кафедри інтелектуальної власності <b>(257 аудиторія)</b>, Майданик Любов Романівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', 'Огнев’юк Ганна Зіновіївна', types.InputTextMessageContent(
           'Викладач кафедри інтелектуальної власності <b>(257 аудиторія)</b>, Огнев’юк Ганна Зіновіївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', 'Зеров Костянтин Олександрович', types.InputTextMessageContent(
           'Викладач кафедри інтелектуальної власності <b>(257 аудиторія)</b>, Зеров Костянтин Олександрович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', 'Про кафедру', types.InputTextMessageContent(
           'Аудиторія: <b>263</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Орлюк Олена Павлівна</b> \n<a href="https://law.knu.ua/ua/library/40-literatura-kafedry-intelektualnoi-vlasnosti">Література кафедри</a>\n<a href="https://law.knu.ua/ua/intellectual-property">Детальніше про кафедру</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)

       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == 'Кафедра іноземних мов' or 'Іноземних' or 'Англійської' or 'Кафедра іноземних' or 'Кафедра англійської')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', 'Трубчанінова Тетяна Анатоліївна', types.InputTextMessageContent(
                'Зав. кафедри іноземних мов <b>(257  аудиторія)</b>, Трубчанінова Тетяна Анатоліївна', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', 'Шаблій Олена Анатоліївна', types.InputTextMessageContent(
                'Викладач кафедри іноземних мов <b>(257  аудиторія)</b>, Шаблій Олена Анатоліївна', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', 'Клавдіч Вікторія Олександрівна', types.InputTextMessageContent(
           'Викладач кафедри іноземних мов <b>(257  аудиторія)</b>, Клавдіч Вікторія Олександрівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', 'Самочорнова Ольга Анатоліївна', types.InputTextMessageContent(
           'Викладач кафедри іноземних мов <b>(257  аудиторія)</b>, Самочорнова Ольга Анатоліївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', 'Жигадло Олена Юріївна', types.InputTextMessageContent(
           'Викладач кафедри іноземних мов <b>(257  аудиторія)</b>, Жигадло Олена Юріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', 'Саєнко Лідія Миколаївна', types.InputTextMessageContent(
           'Викладач кафедри іноземних мов <b>(257  аудиторія)</b>, Саєнко Лідія Миколаївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', 'Волгіна Світлана Анатоліївна', types.InputTextMessageContent(
           'Викладач кафедри іноземних мов <b>(257  аудиторія)</b>, Волгіна Світлана Анатоліївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', 'Альшева Анна Олексіївна', types.InputTextMessageContent(
           'Викладач кафедри іноземних мов <b>(257  аудиторія)</b>, Альшева Анна Олексіївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', 'Законов Сергій Петрович', types.InputTextMessageContent(
           'Викладач кафедри іноземних мов <b>(257  аудиторія)</b>, Законов Сергій Петрович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', 'Шабатько Катерина Василівна', types.InputTextMessageContent(
           'Викладач кафедри іноземних мов права <b>(257  аудиторія)</b>, Шабатько Катерина Василівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', 'Заярна Інна Сергіївна', types.InputTextMessageContent(
           'Викладач кафедри іноземних мов <b>(257  аудиторія)</b>, Заярна Інна Сергіївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', 'Юзефович Катерина Анатоліївна', types.InputTextMessageContent(
           'Викладач кафедри іноземних мов <b>(257  аудиторія)</b>, Юзефович Катерина Анатоліївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', 'Полякова Ганна Володимирівна', types.InputTextMessageContent(
           'Викладач кафедри іноземних мов <b>(257  аудиторія)</b>, Полякова Ганна Володимирівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', 'Ступенко Марія Юріївна', types.InputTextMessageContent(
           'Викладач кафедри іноземних мов <b>(257  аудиторія)</b>, Ступенко Марія Юріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', 'Кравець Катерина Юріївна', types.InputTextMessageContent(
           'Викладач кафедри іноземних мов <b>(257  аудиторія)</b>, Кравець Катерина Юріївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', 'Кузьмінська Любов Степанівна', types.InputTextMessageContent(
           'Викладач кафедри іноземних мов <b>(257  аудиторія)</b>, Кузьмінська Любов Степанівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', 'Найдьонова Алла Володимирівна', types.InputTextMessageContent(
           'Викладач кафедри іноземних мов <b>(257  аудиторія)</b>, Найдьонова Алла Володимирівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', 'Про кафедру', types.InputTextMessageContent(
           'Аудиторія: <b>257</b> \nЗавідувач кафедри: <b>к.філол.н., доц. Трубчанінова Тетяна Анатоліївна</b> \n<a href="https://law.univ.kiev.ua/ua/library/16-literatura-kafedry-inozemnykh-mov">Література кафедри</a>\n<a href="https://law.univ.kiev.ua/ua/foreign-languages">Детальніше про кафедру</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)

       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18])
    except Exception as e:
       print(e)


@bot.inline_handler(lambda query: query.query == 'Кафедра земельного та аграрного права' or 'Кафедра земельного' or 'Кафедра аграрного' or 'Земельного' or 'Аграрного' or 'Зем')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', 'Коваленко Тетяна Олександрівна', types.InputTextMessageContent(
                'В.о. зав. кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Коваленко Тетяна Олександрівна', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', 'Марк Поллінс', types.InputTextMessageContent(
                'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Марк Поллінс', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', 'Крістофер Келлі', types.InputTextMessageContent(
           'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Крістофер Келлі',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', 'Мірошниченко Анатолій Миколайович', types.InputTextMessageContent(
           'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Мірошниченко Анатолій Миколайович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', 'Носік Володимир Васильович', types.InputTextMessageContent(
           'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Носік Володимир Васильович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', 'Калашник Наталія Григорівна', types.InputTextMessageContent(
           'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Калашник Наталія Григорівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', 'Бусуйок Діана Вікторівна', types.InputTextMessageContent(
           'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Бусуйок Діана Вікторівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', ' Третяк Тарас Олексійович', types.InputTextMessageContent(
           'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>,  Третяк Тарас Олексійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', 'Марченко Світлана Іванівна', types.InputTextMessageContent(
           'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Марченко Світлана Іванівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', 'Марусенко Роман Ігоревич', types.InputTextMessageContent(
           'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Марусенко Роман Ігоревич',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', 'Бахуринська Марія Михайлівна', types.InputTextMessageContent(
           'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Бахуринська Марія Михайлівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', 'Заєць Олена Іванівна', types.InputTextMessageContent(
           'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Заєць Олена Іванівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', 'Правдюк Віталій Михайлович', types.InputTextMessageContent(
           'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Правдюк Віталій Михайлович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', 'Саркісова Тамара Борисівна', types.InputTextMessageContent(
           'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Куйбіда Роман Олексійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', 'Коломійцева Діана Миколаївна', types.InputTextMessageContent(
           'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Коломійцева Діана Миколаївна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', 'Кононов Владислав Віталійовична', types.InputTextMessageContent(
           'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Кононов Владислав Віталійович',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', ' Семенець Ольга Семенівна', types.InputTextMessageContent(
           'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Семенець Ольга Семенівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', 'Куцевич Ольга Петрівна', types.InputTextMessageContent(
           'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Куцевич Ольга Петрівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r19 = types.InlineQueryResultArticle('19.', 'Федотова Олександра Семенівна', types.InputTextMessageContent(
           'Викладач кафедри земельного та аграрного права <b>(242 аудиторія)</b>, Федотова Олександра Семенівна',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r20 = types.InlineQueryResultArticle('20.', 'Про кафедру', types.InputTextMessageContent(
           'Аудиторія: <b>242</b> \nЗавідувач кафедри: <b>д.ю.н., доц. Коваленко Тетяна Олександрівна</b> \n<a href="https://law.univ.kiev.ua/ua/library/18-literatura-kafedry-zemelnoho-ta-ahrarnoho-prava">Література кафедри</a>\n<a href="https://law.univ.kiev.ua/ua/land-and-agricultural-law">Детальніше про кафедру</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)
       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == 'Кафедра господарського права' or 'Госп' or 'Кафедра господарського' or 'Господарського')
def query_text(inline_query):
        try:
            r = types.InlineQueryResultArticle('1.', 'Щербина Валентин Степанович', types.InputTextMessageContent(
                'Зав. кафедри господарського права <b>(256 аудиторія)</b>, Щербина Валентин Степанович',
                parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
            r2 = types.InlineQueryResultArticle('2.', 'Радзивілюк Валерія Вікторівн', types.InputTextMessageContent(
                'Викладач кафедри господарського права <b>(256 аудиторія)</b>, Радзивілюк Валерія Вікторівн',
                parse_mode='html'), thumb_url=char_icon,
                                                thumb_width=48, thumb_height=48)
            r3 = types.InlineQueryResultArticle('3.', 'Рєзнікова Вікторія Вікторівна', types.InputTextMessageContent(
                'Викладач кафедри господарського права <b>(256 аудиторія)</b>, Рєзнікова Вікторія Вікторівна',
                parse_mode='html'), thumb_url=char_icon,
                                                thumb_width=48, thumb_height=48)
            r4 = types.InlineQueryResultArticle('4.', 'Пацурія Ніно Бондовна', types.InputTextMessageContent(
                'Викладач кафедри господарського права <b>(256 аудиторія)</b>, Пацурія Ніно Бондовна',
                parse_mode='html'), thumb_url=char_icon,
                                                thumb_width=48, thumb_height=48)
            r5 = types.InlineQueryResultArticle('5.', 'Поєдинок Валерія Вікторівна', types.InputTextMessageContent(
                'Викладач кафедри господарського права <b>(256 аудиторія)</b>, Поєдинок Валерія Вікторівна',
                parse_mode='html'), thumb_url=char_icon,
                                                thumb_width=48, thumb_height=48)
            r6 = types.InlineQueryResultArticle('6.', 'Кологойда Олександра В’ячеславівна', types.InputTextMessageContent(
                'Викладач кафедри господарського права <b>(256 аудиторія)</b>, Кологойда Олександра В’ячеславівна',
                parse_mode='html'), thumb_url=char_icon,
                                                thumb_width=48, thumb_height=48)
            r7 = types.InlineQueryResultArticle('7.', 'Лукач Ірина Володимирівна', types.InputTextMessageContent(
                'Викладач кафедри господарського права <b>(256 аудиторія)</b>, Лукач Ірина Володимирівна',
                parse_mode='html'), thumb_url=char_icon,
                                                thumb_width=48, thumb_height=48)
            r8 = types.InlineQueryResultArticle('8.', 'Вільгушинський Михайло Йосипович', types.InputTextMessageContent(
                'Викладач кафедри господарського права <b>(256 аудиторія)</b>, Вільгушинський Михайло Йосипович',
                parse_mode='html'), thumb_url=char_icon,
                                                thumb_width=48, thumb_height=48)
            r9 = types.InlineQueryResultArticle('9.', 'Клепікова Ольга Вікторівна', types.InputTextMessageContent(
                'Викладач кафедри господарського права <b>(256 аудиторія)</b>, Клепікова Ольга Вікторівна',
                parse_mode='html'), thumb_url=char_icon,
                                                thumb_width=48, thumb_height=48)
            r10 = types.InlineQueryResultArticle('10.', 'Повар Павло Олександрович', types.InputTextMessageContent(
                'Викладач кафедри господарського права <b>(256 аудиторія)</b>, Повар Павло Олександрович',
                parse_mode='html'), thumb_url=char_icon,
                                                 thumb_width=48, thumb_height=48)
            r11 = types.InlineQueryResultArticle('11.', 'Попова Анастасія Володимирівна',
                                                 types.InputTextMessageContent(
                                                     'Викладач кафедри господарського права <b>(256 аудиторія)</b>, Попова Анастасія Володимирівна',
                                                     parse_mode='html'), thumb_url=char_icon,
                                                 thumb_width=48, thumb_height=48)
            r12 = types.InlineQueryResultArticle('12.', 'Кравець Ірина Мирославівна', types.InputTextMessageContent(
                'Викладач кафедри господарського права <b>(256 аудиторія)</b>, Кравець Ірина Мирославівна',
                parse_mode='html'), thumb_url=char_icon,
                                                 thumb_width=48, thumb_height=48)
            r13 = types.InlineQueryResultArticle('13.', 'Горяєва Олександра Сергіївна', types.InputTextMessageContent(
                'Викладач кафедри господарського права <b>(256 аудиторія)</b>, Горяєва Олександра Сергіївна',
                parse_mode='html'), thumb_url=char_icon,
                                                 thumb_width=48, thumb_height=48)
            r14 = types.InlineQueryResultArticle('14.', 'Паракуда Ірина Вікторівна', types.InputTextMessageContent(
                'Викладач кафедри господарського права <b>(256 аудиторія)</b>, Паракуда Ірина Вікторівна',
                parse_mode='html'), thumb_url=char_icon,
                                                 thumb_width=48, thumb_height=48)
            r15 = types.InlineQueryResultArticle('15.', 'Пожоджук Тетяна Богданівна', types.InputTextMessageContent(
                'Викладач кафедри господарського права <b>(256 аудиторія)</b>, Пожоджук Тетяна Богданівна',
                parse_mode='html'), thumb_url=char_icon,
                                                 thumb_width=48, thumb_height=48)
            r16 = types.InlineQueryResultArticle('16.', 'Россильна Ольга Василівна',
                                                 types.InputTextMessageContent(
                                                     'Викладач кафедри господарського права <b>(256 аудиторія)</b>, Россильна Ольга Василівна',
                                                     parse_mode='html'), thumb_url=char_icon,
                                                 thumb_width=48, thumb_height=48)
            r17 = types.InlineQueryResultArticle('17.', 'Науменко Оксана Миколаївна', types.InputTextMessageContent(
                'Викладач кафедри господарського права <b>(256 аудиторія)</b>, Науменко Оксана Миколаївна',
                parse_mode='html'), thumb_url=char_icon,
                                                 thumb_width=48, thumb_height=48)
            r18 = types.InlineQueryResultArticle('18.', 'Про кафедру', types.InputTextMessageContent(
                'Аудиторія: <b>256</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Щербина Валентин Степанович</b> \n<a href="https://law.knu.ua/ua/library/8-literatura-kafedry-hospodarskoho-prava">Література кафедри</a> \n<a href="https://law.knu.ua/ua/commercial-law">Детальніше про кафедру</a>',
                parse_mode='html'), thumb_url=char_icon2,
                                                 thumb_width=48, thumb_height=48)
            bot.answer_inline_query(inline_query.id,
                                    [r, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18])
        except Exception as e:
            print(e)

@bot.inline_handler(lambda query: query.query == 'Кафедра екологічного права' or 'екологічного' or 'Кафедра екологічного' or 'Еко' or 'Еколог')
def query_text(inline_query):
            try:
                r = types.InlineQueryResultArticle('1.', 'Краснова Марія Василівна', types.InputTextMessageContent(
                    'Зав. кафедри екологічного права <b>(244 аудиторія)</b>, Краснова Марія Василівна',
                    parse_mode='html'), thumb_url=char_icon,
                                                   thumb_width=48, thumb_height=48)
                r2 = types.InlineQueryResultArticle('2.', 'Балюк Галина Іванівна', types.InputTextMessageContent(
                    'Викладач екологічного права <b>(244 аудиторія)</b>, Балюк Галина Іванівна',
                    parse_mode='html'), thumb_url=char_icon,
                                                    thumb_width=48, thumb_height=48)
                r3 = types.InlineQueryResultArticle('3.', 'Ковальчук Тетяна Григорівна', types.InputTextMessageContent(
                    'Викладач екологічного права <b>(244 аудиторія)</b>, Ковальчук Тетяна Григорівна',
                    parse_mode='html'), thumb_url=char_icon,
                                                    thumb_width=48, thumb_height=48)
                r4 = types.InlineQueryResultArticle('4.', 'Позняк Еліна Владиславівна',
                                                    types.InputTextMessageContent(
                                                        'Викладач кафедри адміністративного права <b>(244 аудиторія)</b>, Позняк Еліна Владиславівна',
                                                        parse_mode='html'), thumb_url=char_icon,
                                                    thumb_width=48, thumb_height=48)
                r5 = types.InlineQueryResultArticle('5.', 'Євстігнєєв Андрій Сергійович', types.InputTextMessageContent(
                    'Викладач екологічного права <b>(244 аудиторія)</b>, Євстігнєєв Андрій Сергійович',
                    parse_mode='html'), thumb_url=char_icon,
                                                    thumb_width=48, thumb_height=48)
                r6 = types.InlineQueryResultArticle('6.', 'Власенко Юлія Леонідівна', types.InputTextMessageContent(
                    'Викладач екологічного права <b>(244 аудиторія)</b>, Власенко Юлія Леонідівна',
                    parse_mode='html'), thumb_url=char_icon,
                                                    thumb_width=48, thumb_height=48)
                r7 = types.InlineQueryResultArticle('7.', 'Сушик Ольга Володимирівна', types.InputTextMessageContent(
                    'Викладач екологічного права <b>(244 аудиторія)</b>, Сушик Ольга Володимирівна',
                    parse_mode='html'), thumb_url=char_icon,
                                                    thumb_width=48, thumb_height=48)
                r8 = types.InlineQueryResultArticle('8.', 'Бевз Олена Володимирівна',
                                                    types.InputTextMessageContent(
                                                        'Викладач екологічного права <b>(244 аудиторія)</b>, Бевз Олена Володимирівна',
                                                        parse_mode='html'), thumb_url=char_icon,
                                                    thumb_width=48, thumb_height=48)
                r9 = types.InlineQueryResultArticle('9.', 'Слепченко Анжела Анатоліївна', types.InputTextMessageContent(
                    'Викладач екологічного права <b>(244 аудиторія)</b>, Слепченко Анжела Анатоліївна',
                    parse_mode='html'), thumb_url=char_icon,
                                                    thumb_width=48, thumb_height=48)
                r10 = types.InlineQueryResultArticle('10.', 'Шараєвська Тетяна Анатоліївна', types.InputTextMessageContent(
                    'Викладач кафедри екологічного права <b>(244 аудиторія)</b>, Шараєвська Тетяна Анатоліївна',
                    parse_mode='html'), thumb_url=char_icon,
                                                     thumb_width=48, thumb_height=48)
                r11 = types.InlineQueryResultArticle('11.', 'Шомпол Олена Анатоліївна',
                                                     types.InputTextMessageContent(
                                                         'Викладач кафедри екологічного права <b>(244 аудиторія)</b>, Шомпол Олена Анатоліївна',
                                                         parse_mode='html'), thumb_url=char_icon,
                                                     thumb_width=48, thumb_height=48)
                r12 = types.InlineQueryResultArticle('12.', 'Шоха Тетяна Петрівна', types.InputTextMessageContent(
                    'Викладач кафедри екологічного права <b>(244 аудиторія)</b>, Шоха Тетяна Петрівна',
                    parse_mode='html'), thumb_url=char_icon,
                                                     thumb_width=48, thumb_height=48)
                r13 = types.InlineQueryResultArticle('13.', 'Про кафедру', types.InputTextMessageContent(
                    'Аудиторія: <b>244</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Краснова Марія Василівна</b> \n<a href="https://law.knu.ua/ua/library/17-literatura-kafedry-ekolohichnoho-prava">Література кафедри</a> \n<a href="https://law.knu.ua/ua/environmental-law">Детальніше про кафедру</a>',
                    parse_mode='html'), thumb_url=char_icon2,
                                                     thumb_width=48, thumb_height=48)
                bot.answer_inline_query(inline_query.id,
                                        [r, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13])
            except Exception as e:
                print(e)

#bot.send_message(m.chat.id, 'Зав. кафедри конституційного права, проф. Марцеляк Олег Володимирович', reply_markup=keyboard)



@bot.message_handler(func=lambda message:message.text=='Розклад')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['1 курс', '2 курс', '3 курс', '4 курс', 'Назад']])
    bot.send_message(m.chat.id, 'Будь ласка, оберіть курс',
        reply_markup=keyboard)

@bot.message_handler(func=lambda message:message.text=='1 курс')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['I потік (1к)', 'II потік (1к)', 'III потік (1к)', 'IV потік (1к)', 'Назад']])
    bot.send_message(m.chat.id, 'Будь ласка, оберіть потік',
        reply_markup=keyboard)

@bot.message_handler(func=lambda message:message.text=='2 курс')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['I потік (2к)', 'II потік (2к)', 'III потік (2к)', 'Назад']])
    bot.send_message(m.chat.id, 'Будь ласка, оберіть потік',
        reply_markup=keyboard)

@bot.message_handler(func=lambda message:message.text=='3 курс')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['I потік (3к)', 'II потік (3к)', 'III потік (3к)', 'Назад']])
    bot.send_message(m.chat.id, 'Будь ласка, оберіть потік',
        reply_markup=keyboard)

@bot.message_handler(func=lambda message:message.text=='4 курс')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['I потік (4к)', 'II потік (4к)', 'III потік (4к)', 'Назад']])
    bot.send_message(m.chat.id, 'Будь ласка, оберіть потік',
        reply_markup=keyboard)





#Legal misc
@bot.message_handler(func=lambda message:message.text=='Legal misc')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['LegalWizardBot', 'Legal.random', 'Назад']])
    bot.send_message(m.chat.id, 'Розділ, присвячений цікавинкам зі світу юриспруденції.',
        reply_markup=keyboard)


#Club
@bot.message_handler(func=lambda message:message.text=='Центри')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Німецького права', 'Американського права', 'Медичного права', 'Польського права', 'Адаптації законодавства', 'Назад']])
    bot.send_message(m.chat.id, 'Будь ласка, оберіть центр',
        reply_markup=keyboard)

#Misc
@bot.message_handler(func=lambda message:message.text=='Організації')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Асоціація випускників', 'Debate Society', 'Назад']])
    bot.send_message(m.chat.id, 'Будь ласка, оберіть цікавлячу вас категорію',
        reply_markup=keyboard)


#Q&A
@bot.message_handler(func=lambda message:message.text=='Q&A')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Верхній\нижній тижні', 'Інше питання', 'Назад']])
    bot.send_message(m.chat.id, 'Будь ласка, оберіть питання',
        reply_markup=keyboard)

#----------------------П Р И К О Л Ы =))))))))))))))))))))))
@bot.message_handler(content_types=['sticker'])
def sticker(message):
    bot.send_sticker (message.chat.id, 'CAADAgADCAADHjyUFm82G8zkqvIUAg')

@bot.message_handler(content_types=['voice'])
def sticker(message):
    bot.send_voice (message.chat.id, 'AwADBAADL70AAiIZZAd2IfXkFUsbYgI')


#                К                    А                       Ф                    Е__________________Д_________________Р________________И
#--------------------------------------------------------------------------------------------

@bot.message_handler(func=lambda message:message.text=='Кафедри')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['А\Г\Е\З', 'І\К', 'Н\П\Т', 'Ф\Ц', 'Назад']])
    bot.send_photo(m.chat.id, 'AgADAgADiagxG5c38UlgI0rrVHnod_PWDw4ABNqjUjELwBfeJawAAgI', 'Будь ласка, оберіть першу літеру назви цікавлячої Вас кафедри',
        reply_markup=keyboard)

@bot.message_handler(func=lambda message:message.text=='А\Г\Е\З')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Адміністративне', 'Господарське', 'Екологічне', 'Земельне&Аграрне', 'Назад']])
    bot.send_message(m.chat.id, 'Будь ласка, оберіть кафедру',
        reply_markup=keyboard)

@bot.message_handler(func=lambda message:message.text=='І\К')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Іноземних мов', 'Інтелектуальної власності', 'Історія права&держави', 'Конституційне', 'Кримінальне&Кримінологія', 'Назад']])
    bot.send_message(m.chat.id, 'Будь ласка, оберіть кафедру',
        reply_markup=keyboard)

@bot.message_handler(func=lambda message:message.text=='Н\П\Т')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Нотаріат, адвокатура, виконавче', 'Правосуддя', 'Теорія права&держави', 'Трудового&ПСЗ', 'Назад']])
    bot.send_message(m.chat.id, 'Будь ласка, оберіть кафедру',
        reply_markup=keyboard)

@bot.message_handler(func=lambda message:message.text=='Ф\Ц')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Фінансове', 'Цивільне', 'Назад']])
    bot.send_message(m.chat.id, 'Будь ласка, оберіть кафедру',
        reply_markup=keyboard)
#-------------------------------------------------------------------------------------------

#main

#ROZKLAD

@bot.message_handler(content_types=['text'])
def potik(message):
    if message.text == 'I потік (1к)':
       bot.send_photo(message.chat.id, 'AgADAgADEagxGxkDCUuIt6aNXaH7Bj4ySw0ABIOBwIm7GqVfaNkQAAEC')
    elif message.text == 'II потік (1к)':
       bot.send_photo(message.chat.id, 'AgADAgADo6gxGyalAUufdoM2wxidYdvlDw4ABCNL8G4wutyhZsoBAAEC')
    elif message.text == 'III потік (1к)':
       bot.send_photo(message.chat.id, 'AgADAgADpagxGyalAUtoMVQLgTfAUCjTDw4ABEdKq9pyEkUm6sMBAAEC')
    elif message.text == 'IV потік (1к)':
       bot.send_photo(message.chat.id, 'AgADAgADp6gxGyalAUu3mozNHJK2ceoOSw0ABAwgLHMgBs10QdMQAAEC')

    elif message.text == 'I потік (2к)':
        bot.send_photo(message.chat.id, 'AgADAgADDqkxGyalCUtw98ZoqvG67U89Sw0ABE1cVkJe4x9IOd0QAAEC')
    elif message.text == 'II потік (2к)':
        bot.send_photo(message.chat.id, 'AgADAgADEKkxGyalCUs6cgTj3rvRn0bsDw4ABEX9d5yJ0tn2lskBAAEC')
    elif message.text == 'III потік (2к)':
        bot.send_photo(message.chat.id, 'AgADAgADEakxGyalCUtWTUMsCtYLFR8xSw0ABOZ89VDsigQ_Qt4QAAEC')

    elif message.text == 'I потік (3к)':
        bot.send_photo(message.chat.id, 'AgADAgADEqkxGyalCUsg2sPu7oiAuxbRDw4ABPAc7LjJp8Do9MoBAAEC')
    elif message.text == 'II потік (3к)':
        bot.send_photo(message.chat.id, 'AgADAgADE6kxGyalCUu6i9UKuKGDQ7vuDw4ABM1SQz7noKveZc4BAAEC')
    elif message.text == 'III потік (3к)':
        bot.send_photo(message.chat.id, 'AgADAgADFKkxGyalCUvXLD8DTcU-0o85Sw0ABIrgMEgt1tPE2uUQAAEC')

    elif message.text == 'I потік (4к)':
        bot.send_photo(message.chat.id, 'AgADAgADF6kxGyalCUt3Yom2hlXTaug8Sw0ABDE-oDGNVXslDekQAAEC')
    elif message.text == 'II потік (4к)':
        bot.send_photo(message.chat.id, 'AgADAgADGKkxGyalCUtfucVBWZEWAAFi3A8OAATqsRjUwvfEUPHMAQABAg')
    elif message.text == 'III потік (4к)':
        bot.send_photo(message.chat.id, 'AgADAgADGakxGyalCUtMJBXqC9azFJLVDw4ABHPFO0xHNH5b98kBAAEC')

    #Club
    elif message.text == 'Німецького права':
       bot.send_message(message.chat.id, 'Метою діяльності Центру є налагодження постійних академічних зв’язків та сприяння здійсненню спільних дослідницьких та навчальних проектів між юридичним факультетом та вищими юридичними навчальними закладами Німеччини, включаючи програми обмінів студентами та викладачами та створення можливості '
                                         'для викладання правових дисциплін, пов’язаних з правовою системою Німеччини, студентам юридичного факультету. http://zdr.knu.ua/ua/')
    elif message.text == 'Американського права':
       bot.send_message(message.chat.id,'Метою діяльності ACLC є створення постійних академічних зв’язків та сприяння здійсненню спільних дослідницьких, навчальних проектів між студентами та лекторами. http://aclc.knu.ua/index.php')
    elif message.text == 'Медичного права':
       bot.send_message(message.chat.id,'http://health.law.knu.ua')
    elif message.text == 'Адаптації законодавства':
       bot.send_message(message.chat.id, 'Мета діяльності Центру полягає у системному дослідженні фундаментальних і прикладних проблем адаптації законодавства України до законодавства Європейського Союзу (актів acquis communautaire). https://law.knu.ua/ua/center-for-the-study-of-problems-of-adaptation-of-the-ukrainian-laws-to-the-eu-laws')
    elif message.text == 'Польського права':
       bot.send_message(message.chat.id, 'https://www.facebook.com/centrumprawapolskiego/?rc=p')

    #Misc
    elif message.text == 'Асоціація випускників':
       bot.send_message(message.chat.id, 'Не дивлячись на назву, асоціація ставить собі за мету не тільки сприяти подальшому розвитку випускників, але і впроваджувати цікаві ідеї у студентське життя. '
                                         'Серед безлічі проектів можна згадати про стипендію імені почесного випускника, школу правничої майстерності, організацію стажування студентів та випускників. Дізнатися про інші проекти, а також долучитися до діяльності можна за посиланням https://alumni.law.knu.ua/')
    elif message.text == 'Debate Society':
       bot.send_message(message.chat.id, 'Дебати - престижне інтелектуальне змагання, яким займайються студенти провідних навчальних закладів по всьому світу (від Гарварду у США до Сіднею в Австралії, від Оксфорду в Британії до Кейптаунського університету в ПАР). Це регламентована дискусія, учасники якої переконують слухачів/суддів в тому, що їх позиція стосовно теми обговорення є вірною/правильною/істинною. https://www.facebook.com/debateclubknu/')

    #M A P
    elif message.text == 'Мапа':
       bot.send_photo(message.chat.id, 'AgADAgADI6gxG9HA0UkBzN_OjzvQvDwySw0ABAcvN4qqBQPevagPAAEC', 'Пропонуємо скористатися інтерактивною мапою! Перейдіть за посиланням, оберіть необхідну аудиторію та швидко знайдіть її, не засмучуючи викладача своїм запізненням! http://mapknulaw.org.ua/view/ver1-01/')



    #Кафедри
    # ---------------------------------------------------------------------------
    # ---------------------------------------------------------------------------
    # ---------------------------------------------------------------------------
    elif message.text == 'Адміністративне':
       bot.send_message(message.chat.id, 'Аудиторія: <b>324</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Бевзенко Володимир Михайлович</b> \n<a href="https://law.knu.ua/ua/library/9-literatura-kafedry-administratyvnoho-prava">Література кафедри</a>\n<a href="https://law.knu.ua/ua/administrative-law">Детальніше про кафедру</a>', parse_mode="HTML")

    elif message.text == 'Господарське':
       bot.send_message(message.chat.id, 'Аудиторія: <b>256</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Щербина Валентин Степанович</b> \n<a href="https://law.knu.ua/ua/library/8-literatura-kafedry-hospodarskoho-prava">Література кафедри</a> \n<a href="https://law.knu.ua/ua/commercial-law">Детальніше про кафедру</a>', parse_mode="HTML")

    elif message.text == 'Екологічне':
       bot.send_message(message.chat.id, 'Аудиторія: <b>244</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Краснова Марія Василівна</b> \n<a href="https://law.knu.ua/ua/library/17-literatura-kafedry-ekolohichnoho-prava">Література кафедри</a> \n<a href="https://law.knu.ua/ua/environmental-law">Детальніше про кафедру</a>', parse_mode="HTML")

    elif message.text == 'Земельне&Аграрне':
       bot.send_message(message.chat.id,
                         'Аудиторія: <b>242</b> \nЗавідувач кафедри: <b>д.ю.н., доц. Коваленко Тетяна Олександрівна</b> \n<a href="https://law.univ.kiev.ua/ua/library/18-literatura-kafedry-zemelnoho-ta-ahrarnoho-prava">Література кафедри</a>\n<a href="https://law.univ.kiev.ua/ua/land-and-agricultural-law">Детальніше про кафедру</a>',
                         parse_mode="HTML")

#-------------------------------------------------------------------------
    elif message.text == 'Іноземних мов':
       bot.send_message(message.chat.id,
                         'Аудиторія: <b>257</b> \nЗавідувач кафедри: <b>к.філол.н., доц. Трубчанінова Тетяна Анатоліївна</b> \n<a href="https://law.univ.kiev.ua/ua/library/16-literatura-kafedry-inozemnykh-mov">Література кафедри</a>\n<a href="https://law.univ.kiev.ua/ua/foreign-languages">Детальніше про кафедру</a>',
                         parse_mode="HTML")

    elif message.text == 'Інтелектуальної власності':
       bot.send_message(message.chat.id,
                         'Аудиторія: <b>263</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Орлюк Олена Павлівна</b> \n<a href="https://law.knu.ua/ua/library/40-literatura-kafedry-intelektualnoi-vlasnosti">Література кафедри</a>\n<a href="https://law.knu.ua/ua/intellectual-property">Детальніше про кафедру</a>',
                         parse_mode="HTML")

    elif message.text == 'Історія права&держави':
       bot.send_message(message.chat.id,
                         'Аудиторія: <b>344</b> \nВ.О. Завідувача кафедри: <b>к.і.н., д.ю.н., проф. Мірошниченко Марія Іванівна</b> \n<a href="https://law.knu.ua/ua/library/15-literatura-kafedry-istorii-prava-ta-derzhavy">Література кафедри</a>\n<a href="https://law.knu.ua/ua/history-of-law-and-state">Детальніше про кафедру</a>',
                         parse_mode="HTML")

    elif message.text == 'Конституційне':
       bot.send_message(message.chat.id,
                         'Аудиторія: <b>248</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Марцеляк Олег Володимирович</b> \n<a href="https://law.knu.ua/ua/library/13-literatura-kafedry-konstytutsiinoho-prava">Література кафедри</a>\n<a href="https://law.knu.ua/ua/constitutional-law">Детальніше про кафедру</a>',
                         parse_mode="HTML")

    elif message.text == 'Кримінальне&Кримінологія':
       bot.send_message(message.chat.id,
                         'Аудиторія: <b>251</b> \nЗавідувач кафедри: <b>к.ю.н., проф. Андрушко Петро Петрович</b> \n<a href="https://law.knu.ua/ua/library/19-literatura-kafedry-kryminalnoho-prava-ta-kryminolohii">Література кафедри</a>\n<a href="https://law.knu.ua/ua/criminal-law-and-criminology">Детальніше про кафедру</a>',
                         parse_mode="HTML")

    elif message.text == 'Нотаріат, адвокатура, виконавче':
       bot.send_message(message.chat.id,
                         'Аудиторія: <b>265</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Фурса Світлана Ярославівна</b> \n<a href="https://law.knu.ua/ua/library/23-literatura-kafedry-notarialnogo-ta-vykonavchogo-procesu-i-advokatury">Література кафедри</a>\n<a href="https://law.knu.ua/ua/notarial-and-executive-process-and-advocacy">Детальніше про кафедру</a>',
                         parse_mode="HTML")

    elif message.text == 'Правосуддя':
       bot.send_message(message.chat.id,
                         'Аудиторія: <b>250</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Погорецький Микола Анатолійович</b> \n<a href="https://law.knu.ua/ua/library/10-literatura-kafedry-pravosuddia">Література кафедри</a>\n<a href="https://law.knu.ua/ua/justice">Детальніше про кафедру</a>',
                         parse_mode="HTML")

    elif message.text == 'Теорія права&держави':
        bot.send_message(message.chat.id,
                         'Аудиторія: <b>260</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Бобровник Світлана Василівна</b> \n<a href="https://law.knu.ua/ua/library/22-literatura-kafedry-teorii-prava-ta-derzhavy">Література кафедри</a>\n<a href="https://law.knu.ua/ua/theory-of-law-and-state">Детальніше про кафедру</a>',
                         parse_mode="HTML")

    elif message.text == 'Трудового&ПСЗ':
        bot.send_message(message.chat.id,
                         'Аудиторія: <b>241</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Іншин Микола Іванович</b> \n<a href="https://law.knu.ua/ua/library/20-literatura-kafedry-trudovogo-prava-ta-prava-socialnogo-zabezpechennja">Література кафедри</a>\n<a href="https://law.knu.ua/ua/labor-law-and-law-of-social-security">Детальніше про кафедру</a>',
                         parse_mode="HTML")

    elif message.text == 'Фінансове':
        bot.send_message(message.chat.id,
                         'Аудиторія: <b>245</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Пришва Надія Юріївна</b> \n<a href="https://law.knu.ua/ua/library/21-literatura-kafedry-finansovogo-prava">Література кафедри</a>\n<a href="https://law.knu.ua/ua/financial-law">Детальніше про кафедру</a>',
                         parse_mode="HTML")

    elif message.text == 'Цивільне':
        bot.send_message(message.chat.id,
                         'Аудиторія: <b>249</b> \nЗавідувач кафедри: <b>д.ю.н., проф. Майданик Роман Андрійович</b> \n<a href="https://law.knu.ua/ua/library/11-literatura-kafedry-tsyvilnoho-prava">Література кафедри</a>\n<a href="https://law.knu.ua/ua/civil-law">Детальніше про кафедру</a>',
                         parse_mode="HTML")

bot.polling(none_stop=True)