# -*- coding: Windows-1251 -*-
import telebot
import os
from pytelegrambotapi import types

class ParseMode(object):
    """This object represents a Telegram Message Parse Modes."""

    MARKDOWN = 'Markdown'
    """:obj:`str`: 'Markdown'"""
    HTML = 'HTML'
    """:obj:`str`: 'HTML'"""

types = telebot.types #
token = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(token)

char_icon = 'https://image.ibb.co/iUAyRG/placeholde2r.png'
char_icon2 = 'https://image.ibb.co/eHgdkm/2.png'

@bot.message_handler(commands=['start'])
def start(x):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['�������', '������', '��������������', 'Q&A', "����", 'Legal misc', '�������']])
    bot.send_photo(x.chat.id, 'AgADAgADIagxG9HA0Ul7lOxon-ugp9cPSw0ABJj6Ht95jmqlvYUPAAEC', '������� �������! ���� �����, ������ ��������',
    reply_markup=keyboard)



#�����
#!
#!
#!
@bot.message_handler(func=lambda message:message.text=='�����')
def start(x):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['�������', '������', '����������', 'Q&A', "����", '�������', 'Legal misc']])
    bot.send_photo(x.chat.id, 'AgADAgADIKgxG9HA0UkEt24TAqJ7yxHGDw4ABBjCNec_JQt1sI8AAgI', '������ ��������',
    reply_markup=keyboard)
#!
#!
#!


@bot.inline_handler(lambda query: query.query == '��������')
def query_text(inline_query):
    hint = '���� �����, ������ ������� ���������'
    try:
        r = types.InlineQueryResultArticle('1.', '�������� ���� �������������', types.InputTextMessageContent(
                '���. ������� ��������������� ����� (248 ��������), �������� ���� �������������'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == '��������')
def query_text(inline_query):
    hint = '���� �����, ������ ������� ���������'
    try:
        r = types.InlineQueryResultArticle('1.', '�������� ����� ���������', types.InputTextMessageContent(
                '���. ������� ��������� ����� (249 ��������), �������� ����� ���������'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == '������')
def query_text(inline_query):
    hint = '���� �����, ������ ������� ���������'
    try:
        r = types.InlineQueryResultArticle('1.', '������ ���� �����', types.InputTextMessageContent(
                '���. ������� ����������� ����� (245 ��������), ������ ���� �����'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == '�����')
def query_text(inline_query):
    hint = '���� �����, ������ ������� ���������'
    try:
        r = types.InlineQueryResultArticle('1.', '����� ������ ��������', types.InputTextMessageContent(
                '���. ������� ��������� ����� �� ����� ����������� ������������ (241 ��������), ����� ������ ��������'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == '���������')
def query_text(inline_query):
    hint = '���� �����, ������ ������� ���������'
    try:
        r = types.InlineQueryResultArticle('1.', '��������� ������� ��������', types.InputTextMessageContent(
                '���. ������� ���� ����� �� ������� (260 ��������), ��������� ������� ��������'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == '�����������')
def query_text(inline_query):
    hint = '���� �����, ������ ������� ���������'
    try:
        r = types.InlineQueryResultArticle('1.', '����������� ������ �����������', types.InputTextMessageContent(
                '���. ������� ���������� (250 ��������), ����������� ������ �����������'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == '�����')
def query_text(inline_query):
    hint = '���� �����, ������ ������� ���������'
    try:
        r = types.InlineQueryResultArticle('1.', '����� ������� ����������', types.InputTextMessageContent(
                '���. ������� ������������ �� ����������� ������� � ���������� (265 ��������), ����� ������� ����������'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == '��������')
def query_text(inline_query):
    hint = '���� �����, ������ ������� ���������'
    try:
        r = types.InlineQueryResultArticle('1.', '�������� ����� ��������', types.InputTextMessageContent(
                '���. ������� ������������ ����� �� ��������㳿 (251 ��������), �������� ����� ��������'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == '̳����������')
def query_text(inline_query):
    hint = '���� �����, ������ ������� ���������'
    try:
        r = types.InlineQueryResultArticle('1.', '̳���������� ���� �������', types.InputTextMessageContent(
                '���. ������� ����� ����� �� ������� (�������� 344), ̳���������� ���� �������'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == '�����')
def query_text(inline_query):
    hint = '���� �����, ������ ������� ���������'
    try:
        r = types.InlineQueryResultArticle('1.', '����� ����� �������', types.InputTextMessageContent(
                '���. ������� �������������� �������� (263 ��������), ����� ����� �������'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == '�����������')
def query_text(inline_query):
    hint = '���� �����, ������ ������� ���������'
    try:
        r = types.InlineQueryResultArticle('1.', '����������� ������ �����볿���', types.InputTextMessageContent(
                '���. ������� ��������� ��� (257 ��������), ����������� ������ �����볿���'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == '���������')
def query_text(inline_query):
    hint = '���� �����, ������ ������� ���������'
    try:
        r = types.InlineQueryResultArticle('1.', '��������� ������ ������������', types.InputTextMessageContent(
                '���. ������� ���������� �� ��������� �����(242 ��������), ��������� ������ ������������'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == '��������')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1.', '�������� ���� ��������', types.InputTextMessageContent(
                '���. ������� ����������� ����� (244 ��������), �������� ���� ��������'), thumb_url=char_icon, thumb_width=48, thumb_height=48)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == '��������')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', '�������� ��������� ����������', types.InputTextMessageContent(
                '���. ������� ��������������� ����� (324 ��������), �������� ��������� ����������'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == '�������')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', '������� �������� ����������', types.InputTextMessageContent(
                    '���. ������� �������������� ����� (256 ��������), ������� �������� ����������'), thumb_url=char_icon,
                                                   thumb_width=48, thumb_height=48)
       bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
       print(e)

#-----------------------------------------Inline

@bot.inline_handler(lambda query: query.query == '������� ��������������� �����' or '������' or '���' or '�������������' or '����')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', '�������� ��������� ����������', types.InputTextMessageContent(
                '���. ������� ��������������� ����� <b>(324 ��������)</b>, �������� ��������� ����������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', '�������� ���� ���������', types.InputTextMessageContent(
                '�������� ������� ��������������� ����� <b>(324 ��������)</b>, �������� ���� ���������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', '������ ������� ��������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(324 ��������)</b>, ������ ������� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', 'ĳ�������� ����� ����������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(324 ��������)</b>, ĳ�������� ����� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', '������� ����� ���������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(324 ��������)</b>, ������� ����� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', '�������� ������� ��������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(324 ��������)</b>, �������� ������� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', '������� ��� �����������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(324 ��������)</b>, ������� ��� �����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', '³������������ ������� ���������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(324 ��������)</b>, ³������������ ������� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', '������� ��������� ����������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(324 ��������)</b>, ������� ��������� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', '������ ������� ��������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(324 ��������)</b>, ������ ������� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', '����������� ����� ������������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(324 ��������)</b>, ����������� ����� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', '�������� ������ �����', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(324 ��������)</b>, �������� ������ �����',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', '��������� ���� ����������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(324 ��������)</b>, ��������� ���� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', '������ ����� ����������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(324 ��������)</b>, ������ ����� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', '������� ���� �����������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(324 ��������)</b>, ������� ���� �����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', '����������� ����� ������������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(324 ��������)</b>, ����������� ����� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', '�������� ����� ����������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(324 ��������)</b>, �������� ����� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', '�������� ������� �����', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(324 ��������)</b>, �������� ������� �����',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r19 = types.InlineQueryResultArticle('19.', '̳�������� ������ �����������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(324 ��������)</b>, ̳�������� ������ �����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r20 = types.InlineQueryResultArticle('20.', '��� �������', types.InputTextMessageContent(
           '��������: <b> 324 </b > \n�������� �������: <b> �.�.�., ����.�������� ��������� ���������� </b> \n <a href = "https://law.knu.ua/ua/library/9-literatura-kafedry-administratyvnoho-prava"> ˳�������� ������� </a>\n <a href = "https://law.knu.ua/ua/administrative-law"> ��������� ���������� </a>', parse_mode='html'), thumb_url=char_icon2, thumb_width=48, thumb_height=48)


       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20])
    except Exception as e:
       print(e)
#-----------------------------------------Inline



#@bot.message_handler(func=lambda message: message.text == '��������')
#def start(m):
    #   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #keyboard.add(*[types.KeyboardButton(name) for name in ['�������������', '�����']])

@bot.inline_handler(lambda query: query.query == '������� ��������� �����' or '�������' or '���' or '���������')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', '�������� ����� ���������', types.InputTextMessageContent(
                '���. ������� ��������� ����� <b>(249 ��������)</b>, �������� ����� ���������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', '��������� ���� �����������', types.InputTextMessageContent(
                '�������� ������� ��������� ����� <b>(249 ��������)</b>, ��������� ���� �����������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', '������ ������ ��������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ������ ������ ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', '����� ��������� ����������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ����� ��������� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', '����������� ����� ����������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ����������� ����� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', 'ĳ������� ����� �������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ĳ������� ����� �������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', '�������� ������ ��������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, �������� ������ ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', '��������� ����� ������������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ��������� ����� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', '���������� ������ ̳������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ���������� ������ ̳������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', '������ ��������� ���������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ������ ��������� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', '��������� ������ ��������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ��������� ������ ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', '������ ������� �����������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ������ ������� �����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', '������������� ���� ����������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ������������� ���� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', '�������� ˳�� �������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, �������� ˳�� �������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', '�������� ����� �������������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, �������� ����� �������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', '�������� ������ ����������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, �������� ������ ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', '���� ����� ����������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ���� ����� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', '������� ����� ����������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ������� ����� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r19 = types.InlineQueryResultArticle('19.', '�������� ����� ����������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, �������� ����� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r20 = types.InlineQueryResultArticle('20.', '������� �������� �������������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ������� �������� �������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r21 = types.InlineQueryResultArticle('21.', '������ ������ �������������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ������ ������ �������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r22 = types.InlineQueryResultArticle('22.', '���������� �������� ³�������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ���������� �������� ³�������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r23 = types.InlineQueryResultArticle('23.', '��������� ���� ��������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ��������� ���� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r24 = types.InlineQueryResultArticle('24.', '������� ������� ����������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ������� ������� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r25 = types.InlineQueryResultArticle('25.', '������ ������ �������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� <b>(249 ��������)</b>, ������ ������ �������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r26 = types.InlineQueryResultArticle('26.', '��� �������', types.InputTextMessageContent(
           '��������: <b>249</b> \n�������� �������: <b>�.�.�., ����. �������� ����� ���������</b> \n<a href="https://law.knu.ua/ua/library/11-literatura-kafedry-tsyvilnoho-prava">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/civil-law">��������� ��� �������</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)


       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == '������� ����������� �����' or 'Գ�' or 'Գ����' or 'Գ�������')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', '������ ���� �����', types.InputTextMessageContent(
                '���. ������� ����������� ����� <b>(245 ��������)</b>, ������ ���� �����', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', '��������� ������ �������������', types.InputTextMessageContent(
                '�������� ������� ����������� ����� <b>(245 ��������)</b>, ��������� ������ �������������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', '������� ������ �����', types.InputTextMessageContent(
           '�������� ������� ����������� ����� <b>(245 ��������)</b>, ������� ������ �����',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', '������� ������ �������', types.InputTextMessageContent(
           '�������� ������� ����������� ����� <b>(245 ��������)</b>, ������� ������ �������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', '��������� ������ ��������', types.InputTextMessageContent(
           '�������� ������� ����������� ����� <b>(245 ��������)</b>, ��������� ������ ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', '����������� ����� �����������', types.InputTextMessageContent(
           '�������� ������� ����������� ����� <b>(245 ��������)</b>, ����������� ����� �����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', '������� ������� ���������', types.InputTextMessageContent(
           '�������� ������� ����������� ����� <b>(245 ��������)</b>, ������� ������� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', '������� ������ ���������', types.InputTextMessageContent(
           '�������� ������� ����������� ����� <b>(245 ��������)</b>, ������� ������ ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', '������� ����� �����������', types.InputTextMessageContent(
           '�������� ������� ����������� ����� <b>(245 ��������)</b>, ������� ����� �����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', '������ ����� ³�������', types.InputTextMessageContent(
           '�������� ������� ����������� ����� <b>(245 ��������)</b>, ������ ����� ³�������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', '��� �������', types.InputTextMessageContent(
           '��������: <b>245</b> \n�������� �������: <b>�.�.�., ����. ������ ���� �����</b> \n<a href="https://law.knu.ua/ua/library/21-literatura-kafedry-finansovogo-prava">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/financial-law">��������� ��� �������</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)



       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == '������� ��������� ����� �� ����� ����������� ������������' or '�������' or '���' or '��������' or '����' or '���������')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', '����� ������ ��������', types.InputTextMessageContent(
                '���. ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ����� ������ ��������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', '������� ³���� ��������', types.InputTextMessageContent(
                '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ������� ³���� ��������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', '����� ������ ����������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ����� ������ ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', '��������� ������ ��������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ��������� ������ ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', '������� ��� ���������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ������� ��� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', '��������� ������ �����볿���', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ��������� ������ �����볿���',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', '���������� ����� ������������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ���������� ����� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', '��������� ����� �����������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ��������� ����� �����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', '������� ����� ������������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ������� ����� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', '�������� ��������� �������������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, �������� ��������� �������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', '����� ����� ��������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ����� ����� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', '������� ���� �����������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ������� ���� �����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', '������� ������� ���������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ������� ������� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', '������� ����� ������������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ������� ����� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', '������� ������ ���������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ������� ������ ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', '������ ���� �����', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ������ ���� �����',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', '������ ����� �����볿���', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ������ ����� �����볿���',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', '��������� ���������� ���㳿���', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ��������� ���������� ���㳿���',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r19 = types.InlineQueryResultArticle('19.', '������� ����� ���㳿���', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ������� ����� ���㳿���',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r20 = types.InlineQueryResultArticle('20.', 'ѳ���� ������ ��������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ѳ���� ������ ��������',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r21 = types.InlineQueryResultArticle('21.', 'ѳ����� ������� ���������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ѳ����� ������� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r22 = types.InlineQueryResultArticle('22.', '��������� ������ �����������', types.InputTextMessageContent(
           '�������� ������� ��������� ����� �� ����� ����������� ������������ <b>(241 ��������)</b>, ��������� ������ �����������',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r23 = types.InlineQueryResultArticle('23.', '��� �������', types.InputTextMessageContent(
           '��������: <b>241</b> \n�������� �������: <b>�.�.�., ����. ����� ������ ��������</b> \n<a href="https://law.knu.ua/ua/library/20-literatura-kafedry-trudovogo-prava-ta-prava-socialnogo-zabezpechennja">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/labor-law-and-law-of-social-security">��������� ��� �������</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                            thumb_width=48, thumb_height=48)



       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == '������� ���� ����� �� �������' or '���' or '����')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', '��������� ������� ��������', types.InputTextMessageContent(
                '���. ������� ���� ����� �� ������� <b>(260 ��������)</b>, ��������� ������� ��������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', '������ ����� ������������', types.InputTextMessageContent(
                '�������� ������� ���� ����� �� ������� <b>(260 ��������)</b>, ������ ����� ������������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', '���������� ������ ����������', types.InputTextMessageContent(
           '�������� ������� ���� ����� �� ������� <b>(260 ��������)</b>, ���������� ������ ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', '����� ���� ����', types.InputTextMessageContent(
           '�������� ������� ���� ����� �� ������� <b>(260 ��������)</b>, ����� ���� ����',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', '������� ����� �������������', types.InputTextMessageContent(
           '�������� ������� ���� ����� �� ������� <b>(260 ��������)</b>, ������� ����� �������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', '���������� ������ ����������', types.InputTextMessageContent(
           '�������� ������� ���� ����� �� ������� <b>(260 ��������)</b>, ���������� ������ ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', '���������� ³���� ���������', types.InputTextMessageContent(
           '�������� ������� ���� ����� �� ������� <b>(260 ��������)</b>, ���������� ³���� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', '����� ��������� �������������', types.InputTextMessageContent(
           '�������� ������� ���� ����� �� ������� <b>(260 ��������)</b>, ����� ��������� �������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', '����� ������� ������������', types.InputTextMessageContent(
           '�������� ������� ���� ����� �� ������� <b>(260 ��������)</b>, ����� ������� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', '�������� ������ �������', types.InputTextMessageContent(
           '�������� ������� ���� ����� �� ������� <b>(260 ��������)</b>, �������� ������ �������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', '��������� ��������� ����������', types.InputTextMessageContent(
           '�������� ������� ���� ����� �� ������� <b>(260 ��������)</b>, ��������� ��������� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', '������� ������ ³�������', types.InputTextMessageContent(
           '�������� ������� ���� ����� �� ������� <b>(260 ��������)</b>, ������� ������ ³�������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', '�������� �������� ��������', types.InputTextMessageContent(
           '�������� ������� ���� ����� �� ������� <b>(260 ��������)</b>, �������� �������� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', '��������� ͳ�� ������������', types.InputTextMessageContent(
           '�������� ������� ���� ����� �� ������� <b>(260 ��������)</b>, ��������� ͳ�� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', '������� ³����� ������������', types.InputTextMessageContent(
           '�������� ������� ���� ����� �� ������� <b>(260 ��������)</b>, ������� ³����� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', ' ����� ������� ����������', types.InputTextMessageContent(
           '�������� ������� ���� ����� �� ������� <b>(260 ��������)</b>,  ����� ������� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', '����� ����� �����䳿���', types.InputTextMessageContent(
           '�������� ������� ���� ����� �� ������� <b>(260 ��������)</b>, ����� ����� �����䳿���',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', '������ ����� ��������', types.InputTextMessageContent(
           '�������� ������� ���� ����� �� ������� <b>(260 ��������)</b>, ������ ����� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r19 = types.InlineQueryResultArticle('19.', '��� �������', types.InputTextMessageContent(
           '��������: <b>260</b> \n�������� �������: <b>�.�.�., ����. ��������� ������� ��������</b> \n<a href="https://law.knu.ua/ua/library/22-literatura-kafedry-teorii-prava-ta-derzhavy">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/theory-of-law-and-state">��������� ��� �������</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)


       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == '������� ����������' or '����������')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', '����������� ������ �����������', types.InputTextMessageContent(
                '���. ������� ���������� <b>(250 ��������)</b>, ����������� ������ �����������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', '��������� ������ �������', types.InputTextMessageContent(
                '�������� ������� ���������� <b>(250 ��������)</b>, ��������� ������ �������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', '���������� ����� ������������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ���������� ����� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', '������� ��� ���������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ������� ��� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', '������ ������ ��������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ������ ������ ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', '�������� ���������� ���������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, �������� ���������� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', '���㺺�� ĳ��� ��������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ���㺺�� ĳ��� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', '��������� ������� ���������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ��������� ������� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', '����� ������ ��������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ����� ������ ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', '��������� ������ ���������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ��������� ������ ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', '�������� ����� ������������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, �������� ����� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', '�������� ������ ������������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, �������� ������ ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', '���������-�������� ����� ³��볿���', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ���������-�������� ����� ³��볿���',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', '���������� ������ ������������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ���������� ������ ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', '������ ��������� ����������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ������ ��������� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', '�������� ����� ��������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, �������� ����� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', 'ʳ���� ������ ������������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ʳ���� ������ ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', '������� ����� ������������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ������� ����� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r19 = types.InlineQueryResultArticle('19.', '���������� ����� �����', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ���������� ����� �����',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r20 = types.InlineQueryResultArticle('20.', '������������ ³���� �����������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ������������ ³���� �����������',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r21 = types.InlineQueryResultArticle('21.', '������� ������� �����������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ������� ������� �����������',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r22 = types.InlineQueryResultArticle('22.', '������ ³���� ��������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ������ ³���� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r23 = types.InlineQueryResultArticle('23.', '�������� ���� ³��������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, �������� ���� ³��������',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r24 = types.InlineQueryResultArticle('24.', '���� ������ �������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ���� ������ �������',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r25 = types.InlineQueryResultArticle('25.', '��������� ������ ��������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ��������� ������ ��������',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r26 = types.InlineQueryResultArticle('26.', '������ ������ ������������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ������ ������ ������������',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r27 = types.InlineQueryResultArticle('27.', '������� ����� ��������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ������� ����� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r28 = types.InlineQueryResultArticle('28.', '����������� ���� �������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ����������� ���� �������',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r29 = types.InlineQueryResultArticle('29.', '������� ������ �������������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ������� ������ �������������',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r30 = types.InlineQueryResultArticle('30.', '�������� ���� ���������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, �������� ���� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r31 = types.InlineQueryResultArticle('31.', '����� ��������� ��������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ����� ��������� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r32 = types.InlineQueryResultArticle('32.', '���������� ������ ���������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ���������� ������ ���������',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r33 = types.InlineQueryResultArticle('33.', '��������� ������ �������', types.InputTextMessageContent(
           '�������� ������� ���������� <b>(250 ��������)</b>, ��������� ������ �������',
           parse_mode='html'), thumb_url=char_icon,
                                            thumb_width=48, thumb_height=48)
       r34 = types.InlineQueryResultArticle('34.', '��� �������', types.InputTextMessageContent(
           '��������: <b>250</b> \n�������� �������: <b>�.�.�., ����. ����������� ������ �����������</b> \n<a href="https://law.knu.ua/ua/library/10-literatura-kafedry-pravosuddia">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/justice">��������� ��� �������</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                            thumb_width=48, thumb_height=48)

       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, r27, r28, r29, r30, r31, r32, r33, r34])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == '������� ������������ �� ����������� ������� � ����������' or '�����' or '������������' or '������� ������������' or '����������'or '������� ����������')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', '����� ������� ����������', types.InputTextMessageContent(
                '���. ������� ������������ �� ����������� ������� � ���������� <b>(265 ��������)</b>, ����� ������� ����������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', '�������� ���� ������������', types.InputTextMessageContent(
                '�������� ������� ������������ �� ����������� ������� � ���������� <b>(265 ��������)</b>, �������� ���� ������������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', ' ������ ����� ��������', types.InputTextMessageContent(
           '�������� ������� ������������ �� ����������� ������� � ���������� <b>(265 ��������)</b>,  ������ ����� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', '��������� ������� �����', types.InputTextMessageContent(
           '�������� ������� ������������ �� ����������� ������� � ���������� <b>(265 ��������)</b>, ��������� ������� �����',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', '������� ��������� ������������', types.InputTextMessageContent(
           '�������� ������� ������������ �� ����������� ������� � ���������� <b>(265 ��������)</b>, ������� ��������� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', '������ ������ �������������', types.InputTextMessageContent(
           '�������� ������� ������������ �� ����������� ������� � ���������� <b>(265 ��������)</b>, ������ ������ �������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', '������� ����� ���������', types.InputTextMessageContent(
           '�������� ������� ������������ �� ����������� ������� � ���������� <b>(265 ��������)</b>, ������� ����� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', '����� ������ ���������', types.InputTextMessageContent(
           '�������� ������� ������������ �� ����������� ������� � ���������� <b>(265 ��������)</b>, ����� ������ ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', '�������� (�������) ����� ���㳿���', types.InputTextMessageContent(
           '�������� ������� ������������ �� ����������� ������� � ���������� <b>(265 ��������)</b>, �������� (�������) ����� ���㳿���',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', '���� ����� ������������', types.InputTextMessageContent(
           '�������� ������� ������������ �� ����������� ������� � ���������� <b>(265 ��������)</b>, ���� ����� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', '������� ������ ���㳿���', types.InputTextMessageContent(
           '�������� ������� ������������ �� ����������� ������� � ���������� <b>(265 ��������)</b>, ������� ������ ���㳿���',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', '��� �������', types.InputTextMessageContent(
           '��������: <b>265</b> \n�������� �������: <b>�.�.�., ����. ����� ������� ����������</b> \n<a href="https://law.knu.ua/ua/library/23-literatura-kafedry-notarialnogo-ta-vykonavchogo-procesu-i-advokatury">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/notarial-and-executive-process-and-advocacy">��������� ��� �������</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)

       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == '������� ������������ ����� �� ��������㳿' or '����' or '������������' or '����������')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', '�������� ����� ��������', types.InputTextMessageContent(
                '���. ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, �������� ����� ��������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', '����� ����� ���������', types.InputTextMessageContent(
                '�������� ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, ����� ����� ���������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', '�������� ������ ��������', types.InputTextMessageContent(
           '�������� ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, �������� ������ ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', '�������� ����� ���������', types.InputTextMessageContent(
           '�������� ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, �������� ����� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', '����������� ����� ������������', types.InputTextMessageContent(
           '�������� ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, ����������� ����� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', '�������� ������ �����������', types.InputTextMessageContent(
           '�������� ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, �������� ������ �����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', '��������� ����� �������', types.InputTextMessageContent(
           '�������� ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, ��������� ����� �������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', '����� ��������� ����������', types.InputTextMessageContent(
           '�������� ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, ����� ��������� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', '������� ����� �������������', types.InputTextMessageContent(
           '�������� ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, ������� ����� �������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', '����� ��������� ��������', types.InputTextMessageContent(
           '�������� ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, ����� ��������� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', '������ ������ ��������', types.InputTextMessageContent(
           '�������� ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, ������ ������ ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', 'ʳ������� ���� ³�������', types.InputTextMessageContent(
           '�������� ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, ʳ������� ���� ³�������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', '������ ������� �������������', types.InputTextMessageContent(
           '�������� ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, ������ ������� �������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', '������� ������ ��������', types.InputTextMessageContent(
           '�������� ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, ������� ������ ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', '����������� ��������� �������������', types.InputTextMessageContent(
           '�������� ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, ����������� ��������� �������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', '�������� ����� ���������', types.InputTextMessageContent(
           '�������� ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, �������� ����� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', '�������� ������ ���������', types.InputTextMessageContent(
           '�������� ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, �������� ������ ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', '�������� ��������� ��������', types.InputTextMessageContent(
           '�������� ������� ������������ ����� �� ��������㳿 <b>(251 ��������)</b>, �������� ��������� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r19 = types.InlineQueryResultArticle('19.', '��� �������', types.InputTextMessageContent(
           '��������: <b>251</b> \n�������� �������: <b>�.�.�., ����. �������� ����� ��������</b> \n<a href="https://law.knu.ua/ua/library/19-literatura-kafedry-kryminalnoho-prava-ta-kryminolohii">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/criminal-law-and-criminology">��������� ��� �������</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)


       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == '������� ��������������� �����' or '�������������' or '�����' or '���������������' or '������� ���������������')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', '�������� ���� �������������', types.InputTextMessageContent(
                '���. ������� ��������������� ����� <b>(248 ��������)</b>, �������� ���� �������������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', '���������� ͳ�� �����볿���', types.InputTextMessageContent(
                '�������� ������� ��������������� ����� <b>(248 ��������)</b>, ���������� ͳ�� �����볿���', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', '������� ����� ������������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(248 ��������)</b>, ������� ����� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', '����� ����� ���������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(248 ��������)</b>, ����� ����� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', '����������� ������ �������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(248 ��������)</b>, ����������� ������ �������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', '������ ����� ����������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(248 ��������)</b>, ������ ����� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', '������� ��� ����������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(248 ��������)</b>, ������� ��� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', '������ ������� �����������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(248 ��������)</b>, ������ ������� �����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', '����������� ��������� ����������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(248 ��������)</b>, ����������� ��������� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', '�������� ��������� �������������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(248 ��������)</b>, �������� ��������� �������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', '������������ ��� ����������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(248 ��������)</b>, ������������ ��� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', 'ѳ������� ����� ��������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(248 ��������)</b>, ѳ������� ����� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', '������ ������ ��������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(248 ��������)</b>, ������ ������ ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', '���������� ��� �����������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(248 ��������)</b>, ���������� ��� �����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', '������� ������ ��������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(248 ��������)</b>, ������� ������ ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', '������ ������� ³��������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(248 ��������)</b>, ������ ������� ³��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', '���������� ����� ���������', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(248 ��������)</b>, ���������� ����� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', '�������� ����� ���㳿���', types.InputTextMessageContent(
           '�������� ������� ��������������� ����� <b>(248 ��������)</b>, �������� ������� �����',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r19 = types.InlineQueryResultArticle('19.', '��� �������', types.InputTextMessageContent(
           '��������: <b>248</b> \n�������� �������: <b>�.�.�., ����. �������� ���� �������������</b> \n<a href="https://law.knu.ua/ua/library/13-literatura-kafedry-konstytutsiinoho-prava">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/constitutional-law">��������� ��� �������</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)


       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == '������� ����� ����� �� �������' or '�����' or '���' or '�����' or '������� ����')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', '���������� ����� ��������', types.InputTextMessageContent(
                '�.�. ���. ������� ����� ����� �� ������� <b>(344 ��������)</b>, ���������� ����� ��������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', '���������� ����� ��������', types.InputTextMessageContent(
                '�������� ������� ����� ����� �� ������� <b>(344 ��������)</b>, ���������� ����� ��������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', '���� ��������� ���������', types.InputTextMessageContent(
                '�������� ������� ����� ����� �� ������� <b>(344 ��������)</b>, ���� ��������� ���������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', '������� ������ ������������', types.InputTextMessageContent(
           '�������� ������� ����� ����� �� ������� <b>(344 ��������)</b>, ������� ������ ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', '������ ���� ����������', types.InputTextMessageContent(
           '�������� ������� ����� ����� �� ������� <b>(344 ��������)</b>, ������ ���� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', '����� ������ �������������', types.InputTextMessageContent(
           '�������� ������� ����� ����� �� ������� <b>(344 ��������)</b>, ����� ������ �������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', '������������ ������ ����������', types.InputTextMessageContent(
           '�������� ������� ����� ����� �� ������� <b>(344 ��������)</b>, ������������ ������ ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', '������� ������ �������', types.InputTextMessageContent(
           '�������� ������� ����� ����� �� ������� <b>(344 ��������)</b>, ������� ������ �������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', '������ ������ ��������', types.InputTextMessageContent(
           '�������� ������� ����� ����� �� ������� <b>(344 ��������)</b>, ������ ������ ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', '�������� ³���� �������������', types.InputTextMessageContent(
           '�������� ������� ����� ����� �� ������� <b>(344 ��������)</b>, �������� ³���� �������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', '����������� ����� ����������', types.InputTextMessageContent(
           '�������� ������� ����� ����� �� ������� <b>(344 ��������)</b>, ����������� ����� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', '��� �������', types.InputTextMessageContent(
           '��������: <b>344</b> \n�.�. ��������� �������: <b>�.�.�., �.�.�., ����. ̳���������� ���� �������</b> \n<a href="https://law.knu.ua/ua/library/15-literatura-kafedry-istorii-prava-ta-derzhavy">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/history-of-law-and-state">��������� ��� �������</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)

       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == '������� �������������� ��������' or '������� ��������������' or '��������������')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', '����� ����� �������', types.InputTextMessageContent(
                '�. �. ���. ������� �������������� �������� <b>(257 ��������)</b>, ����� ����� �������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', '��������� ������ ���������', types.InputTextMessageContent(
                '�������� ������� �������������� �������� <b>(257 ��������)</b>, ��������� ������ ���������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', '�������� ������� �������������', types.InputTextMessageContent(
           '�������� ������� �������������� �������� <b>(257 ��������)</b>, �������� ������� �������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', '������ ����� ����������', types.InputTextMessageContent(
           '�������� ������� �������������� �������� <b>(257 ��������)</b>, ������ ����� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', '��������� ������ ��������', types.InputTextMessageContent(
           '�������� ������� �������������� �������� <b>(257 ��������)</b>, ��������� ������ ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', '�������� ����� �����������', types.InputTextMessageContent(
           '�������� ������� �������������� �������� <b>(257 ��������)</b>, �������� ����� �����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', '�������� ����� ���������', types.InputTextMessageContent(
           '�������� ������� �������������� �������� <b>(257 ��������)</b>, �������� ����� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', '��������� ������ �����', types.InputTextMessageContent(
           '�������� ������� �������������� �������� <b>(257 ��������)</b>, ��������� ������ �����',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', '���� ��� �������������', types.InputTextMessageContent(
           '�������� ������� �������������� �������� <b>(257 ��������)</b>, ���� ��� �������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', '��������� ���� ��������', types.InputTextMessageContent(
           '�������� ������� �������������� �������� <b>(257 ��������)</b>, ��������� ���� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', '������� ������ ³��������', types.InputTextMessageContent(
           '�������� ������� �������������� �������� <b>(257 ��������)</b>, ������� ������ ³��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', '������ ����� �����', types.InputTextMessageContent(
           '�������� ������� �������������� �������� <b>(257 ��������)</b>, ������ ����� �����',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', '������� ������ ������������', types.InputTextMessageContent(
           '�������� ������� �������������� �������� <b>(257 ��������)</b>, ������� ������ ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', '�������� ����� ��������', types.InputTextMessageContent(
           '�������� ������� �������������� �������� <b>(257 ��������)</b>, �������� ����� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', '������� ����� ǳ��⳿���', types.InputTextMessageContent(
           '�������� ������� �������������� �������� <b>(257 ��������)</b>, ������� ����� ǳ��⳿���',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', '����� ��������� �������������', types.InputTextMessageContent(
           '�������� ������� �������������� �������� <b>(257 ��������)</b>, ����� ��������� �������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', '��� �������', types.InputTextMessageContent(
           '��������: <b>263</b> \n�������� �������: <b>�.�.�., ����. ����� ����� �������</b> \n<a href="https://law.knu.ua/ua/library/40-literatura-kafedry-intelektualnoi-vlasnosti">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/intellectual-property">��������� ��� �������</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)

       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == '������� ��������� ���' or '���������' or '���������' or '������� ���������' or '������� ���������')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', '����������� ������ �����볿���', types.InputTextMessageContent(
                '���. ������� ��������� ��� <b>(257  ��������)</b>, ����������� ������ �����볿���', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', '����� ����� �����볿���', types.InputTextMessageContent(
                '�������� ������� ��������� ��� <b>(257  ��������)</b>, ����� ����� �����볿���', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', '������ ³����� ������������', types.InputTextMessageContent(
           '�������� ������� ��������� ��� <b>(257  ��������)</b>, ������ ³����� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', '����������� ����� �����볿���', types.InputTextMessageContent(
           '�������� ������� ��������� ��� <b>(257  ��������)</b>, ����������� ����� �����볿���',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', '������� ����� �����', types.InputTextMessageContent(
           '�������� ������� ��������� ��� <b>(257  ��������)</b>, ������� ����� �����',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', '����� ˳�� ���������', types.InputTextMessageContent(
           '�������� ������� ��������� ��� <b>(257  ��������)</b>, ����� ˳�� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', '������ ������� �����볿���', types.InputTextMessageContent(
           '�������� ������� ��������� ��� <b>(257  ��������)</b>, ������ ������� �����볿���',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', '������� ���� ��������', types.InputTextMessageContent(
           '�������� ������� ��������� ��� <b>(257  ��������)</b>, ������� ���� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', '������� ����� ��������', types.InputTextMessageContent(
           '�������� ������� ��������� ��� <b>(257  ��������)</b>, ������� ����� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', '�������� �������� ��������', types.InputTextMessageContent(
           '�������� ������� ��������� ��� ����� <b>(257  ��������)</b>, �������� �������� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', '������ ���� ���㳿���', types.InputTextMessageContent(
           '�������� ������� ��������� ��� <b>(257  ��������)</b>, ������ ���� ���㳿���',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', '�������� �������� �����볿���', types.InputTextMessageContent(
           '�������� ������� ��������� ��� <b>(257  ��������)</b>, �������� �������� �����볿���',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', '�������� ����� ������������', types.InputTextMessageContent(
           '�������� ������� ��������� ��� <b>(257  ��������)</b>, �������� ����� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', '�������� ���� �����', types.InputTextMessageContent(
           '�������� ������� ��������� ��� <b>(257  ��������)</b>, �������� ���� �����',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', '������� �������� �����', types.InputTextMessageContent(
           '�������� ������� ��������� ��� <b>(257  ��������)</b>, ������� �������� �����',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', '���������� ����� ���������', types.InputTextMessageContent(
           '�������� ������� ��������� ��� <b>(257  ��������)</b>, ���������� ����� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', '���������� ���� ������������', types.InputTextMessageContent(
           '�������� ������� ��������� ��� <b>(257  ��������)</b>, ���������� ���� ������������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', '��� �������', types.InputTextMessageContent(
           '��������: <b>257</b> \n�������� �������: <b>�.�����.�., ���. ����������� ������ �����볿���</b> \n<a href="https://law.univ.kiev.ua/ua/library/16-literatura-kafedry-inozemnykh-mov">˳�������� �������</a>\n<a href="https://law.univ.kiev.ua/ua/foreign-languages">��������� ��� �������</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)

       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18])
    except Exception as e:
       print(e)


@bot.inline_handler(lambda query: query.query == '������� ���������� �� ��������� �����' or '������� ����������' or '������� ���������' or '����������' or '���������' or '���')
def query_text(inline_query):
    try:
       r = types.InlineQueryResultArticle('1.', '��������� ������ ������������', types.InputTextMessageContent(
                '�.�. ���. ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, ��������� ������ ������������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r2 = types.InlineQueryResultArticle('2.', '���� ������', types.InputTextMessageContent(
                '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, ���� ������', parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
       r3 = types.InlineQueryResultArticle('3.', '�������� ����', types.InputTextMessageContent(
           '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, �������� ����',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r4 = types.InlineQueryResultArticle('4.', '̳���������� ������� �����������', types.InputTextMessageContent(
           '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, ̳���������� ������� �����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r5 = types.InlineQueryResultArticle('5.', '���� ��������� ����������', types.InputTextMessageContent(
           '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, ���� ��������� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r6 = types.InlineQueryResultArticle('6.', '�������� ������ ���������', types.InputTextMessageContent(
           '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, �������� ������ ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r7 = types.InlineQueryResultArticle('7.', '������� ĳ��� ³�������', types.InputTextMessageContent(
           '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, ������� ĳ��� ³�������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r8 = types.InlineQueryResultArticle('8.', ' ������ ����� ����������', types.InputTextMessageContent(
           '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>,  ������ ����� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r9 = types.InlineQueryResultArticle('9.', '�������� ������� �������', types.InputTextMessageContent(
           '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, �������� ������� �������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r10 = types.InlineQueryResultArticle('10.', '��������� ����� ��������', types.InputTextMessageContent(
           '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, ��������� ����� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r11 = types.InlineQueryResultArticle('11.', '����������� ���� ���������', types.InputTextMessageContent(
           '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, ����������� ���� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r12 = types.InlineQueryResultArticle('12.', '���� ����� �������', types.InputTextMessageContent(
           '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, ���� ����� �������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r13 = types.InlineQueryResultArticle('13.', '������� ³���� ����������', types.InputTextMessageContent(
           '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, ������� ³���� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r14 = types.InlineQueryResultArticle('14.', '�������� ������ ��������', types.InputTextMessageContent(
           '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, ������ ����� ����������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r15 = types.InlineQueryResultArticle('15.', '���������� ĳ��� ���������', types.InputTextMessageContent(
           '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, ���������� ĳ��� ���������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r16 = types.InlineQueryResultArticle('16.', '������� ��������� ³����������', types.InputTextMessageContent(
           '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, ������� ��������� ³��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r17 = types.InlineQueryResultArticle('17.', ' �������� ����� ��������', types.InputTextMessageContent(
           '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, �������� ����� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r18 = types.InlineQueryResultArticle('18.', '������� ����� �������', types.InputTextMessageContent(
           '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, ������� ����� �������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r19 = types.InlineQueryResultArticle('19.', '�������� ���������� ��������', types.InputTextMessageContent(
           '�������� ������� ���������� �� ��������� ����� <b>(242 ��������)</b>, �������� ���������� ��������',
           parse_mode='html'), thumb_url=char_icon,
                                           thumb_width=48, thumb_height=48)
       r20 = types.InlineQueryResultArticle('20.', '��� �������', types.InputTextMessageContent(
           '��������: <b>242</b> \n�������� �������: <b>�.�.�., ���. ��������� ������ ������������</b> \n<a href="https://law.univ.kiev.ua/ua/library/18-literatura-kafedry-zemelnoho-ta-ahrarnoho-prava">˳�������� �������</a>\n<a href="https://law.univ.kiev.ua/ua/land-and-agricultural-law">��������� ��� �������</a>',
           parse_mode='html'), thumb_url=char_icon2,
                                           thumb_width=48, thumb_height=48)
       bot.answer_inline_query(inline_query.id, [r,	r2,	r3,	r4,	r5,	r6,	r7,	r8,	r9,	r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20])
    except Exception as e:
       print(e)

@bot.inline_handler(lambda query: query.query == '������� �������������� �����' or '����' or '������� ��������������' or '��������������')
def query_text(inline_query):
        try:
            r = types.InlineQueryResultArticle('1.', '������� �������� ����������', types.InputTextMessageContent(
                '���. ������� �������������� ����� <b>(256 ��������)</b>, ������� �������� ����������',
                parse_mode='html'), thumb_url=char_icon,
                                               thumb_width=48, thumb_height=48)
            r2 = types.InlineQueryResultArticle('2.', '��������� ������ ³������', types.InputTextMessageContent(
                '�������� ������� �������������� ����� <b>(256 ��������)</b>, ��������� ������ ³������',
                parse_mode='html'), thumb_url=char_icon,
                                                thumb_width=48, thumb_height=48)
            r3 = types.InlineQueryResultArticle('3.', 'к������ ³����� ³�������', types.InputTextMessageContent(
                '�������� ������� �������������� ����� <b>(256 ��������)</b>, к������ ³����� ³�������',
                parse_mode='html'), thumb_url=char_icon,
                                                thumb_width=48, thumb_height=48)
            r4 = types.InlineQueryResultArticle('4.', '������ ͳ�� ��������', types.InputTextMessageContent(
                '�������� ������� �������������� ����� <b>(256 ��������)</b>, ������ ͳ�� ��������',
                parse_mode='html'), thumb_url=char_icon,
                                                thumb_width=48, thumb_height=48)
            r5 = types.InlineQueryResultArticle('5.', '������� ������ ³�������', types.InputTextMessageContent(
                '�������� ������� �������������� ����� <b>(256 ��������)</b>, ������� ������ ³�������',
                parse_mode='html'), thumb_url=char_icon,
                                                thumb_width=48, thumb_height=48)
            r6 = types.InlineQueryResultArticle('6.', '��������� ���������� ����������', types.InputTextMessageContent(
                '�������� ������� �������������� ����� <b>(256 ��������)</b>, ��������� ���������� ����������',
                parse_mode='html'), thumb_url=char_icon,
                                                thumb_width=48, thumb_height=48)
            r7 = types.InlineQueryResultArticle('7.', '����� ����� ������������', types.InputTextMessageContent(
                '�������� ������� �������������� ����� <b>(256 ��������)</b>, ����� ����� ������������',
                parse_mode='html'), thumb_url=char_icon,
                                                thumb_width=48, thumb_height=48)
            r8 = types.InlineQueryResultArticle('8.', '³������������ ������� ���������', types.InputTextMessageContent(
                '�������� ������� �������������� ����� <b>(256 ��������)</b>, ³������������ ������� ���������',
                parse_mode='html'), thumb_url=char_icon,
                                                thumb_width=48, thumb_height=48)
            r9 = types.InlineQueryResultArticle('9.', '�������� ����� ³�������', types.InputTextMessageContent(
                '�������� ������� �������������� ����� <b>(256 ��������)</b>, �������� ����� ³�������',
                parse_mode='html'), thumb_url=char_icon,
                                                thumb_width=48, thumb_height=48)
            r10 = types.InlineQueryResultArticle('10.', '����� ����� �������������', types.InputTextMessageContent(
                '�������� ������� �������������� ����� <b>(256 ��������)</b>, ����� ����� �������������',
                parse_mode='html'), thumb_url=char_icon,
                                                 thumb_width=48, thumb_height=48)
            r11 = types.InlineQueryResultArticle('11.', '������ �������� ������������',
                                                 types.InputTextMessageContent(
                                                     '�������� ������� �������������� ����� <b>(256 ��������)</b>, ������ �������� ������������',
                                                     parse_mode='html'), thumb_url=char_icon,
                                                 thumb_width=48, thumb_height=48)
            r12 = types.InlineQueryResultArticle('12.', '������� ����� �����������', types.InputTextMessageContent(
                '�������� ������� �������������� ����� <b>(256 ��������)</b>, ������� ����� �����������',
                parse_mode='html'), thumb_url=char_icon,
                                                 thumb_width=48, thumb_height=48)
            r13 = types.InlineQueryResultArticle('13.', '������� ���������� ���㳿���', types.InputTextMessageContent(
                '�������� ������� �������������� ����� <b>(256 ��������)</b>, ������� ���������� ���㳿���',
                parse_mode='html'), thumb_url=char_icon,
                                                 thumb_width=48, thumb_height=48)
            r14 = types.InlineQueryResultArticle('14.', '�������� ����� ³�������', types.InputTextMessageContent(
                '�������� ������� �������������� ����� <b>(256 ��������)</b>, �������� ����� ³�������',
                parse_mode='html'), thumb_url=char_icon,
                                                 thumb_width=48, thumb_height=48)
            r15 = types.InlineQueryResultArticle('15.', '�������� ������ ���������', types.InputTextMessageContent(
                '�������� ������� �������������� ����� <b>(256 ��������)</b>, �������� ������ ���������',
                parse_mode='html'), thumb_url=char_icon,
                                                 thumb_width=48, thumb_height=48)
            r16 = types.InlineQueryResultArticle('16.', '��������� ����� ��������',
                                                 types.InputTextMessageContent(
                                                     '�������� ������� �������������� ����� <b>(256 ��������)</b>, ��������� ����� ��������',
                                                     parse_mode='html'), thumb_url=char_icon,
                                                 thumb_width=48, thumb_height=48)
            r17 = types.InlineQueryResultArticle('17.', '�������� ������ ���������', types.InputTextMessageContent(
                '�������� ������� �������������� ����� <b>(256 ��������)</b>, �������� ������ ���������',
                parse_mode='html'), thumb_url=char_icon,
                                                 thumb_width=48, thumb_height=48)
            r18 = types.InlineQueryResultArticle('18.', '��� �������', types.InputTextMessageContent(
                '��������: <b>256</b> \n�������� �������: <b>�.�.�., ����. ������� �������� ����������</b> \n<a href="https://law.knu.ua/ua/library/8-literatura-kafedry-hospodarskoho-prava">˳�������� �������</a> \n<a href="https://law.knu.ua/ua/commercial-law">��������� ��� �������</a>',
                parse_mode='html'), thumb_url=char_icon2,
                                                 thumb_width=48, thumb_height=48)
            bot.answer_inline_query(inline_query.id,
                                    [r, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18])
        except Exception as e:
            print(e)

@bot.inline_handler(lambda query: query.query == '������� ����������� �����' or '�����������' or '������� �����������' or '���' or '������')
def query_text(inline_query):
            try:
                r = types.InlineQueryResultArticle('1.', '�������� ���� ��������', types.InputTextMessageContent(
                    '���. ������� ����������� ����� <b>(244 ��������)</b>, �������� ���� ��������',
                    parse_mode='html'), thumb_url=char_icon,
                                                   thumb_width=48, thumb_height=48)
                r2 = types.InlineQueryResultArticle('2.', '����� ������ �������', types.InputTextMessageContent(
                    '�������� ����������� ����� <b>(244 ��������)</b>, ����� ������ �������',
                    parse_mode='html'), thumb_url=char_icon,
                                                    thumb_width=48, thumb_height=48)
                r3 = types.InlineQueryResultArticle('3.', '��������� ������ ���������', types.InputTextMessageContent(
                    '�������� ����������� ����� <b>(244 ��������)</b>, ��������� ������ ���������',
                    parse_mode='html'), thumb_url=char_icon,
                                                    thumb_width=48, thumb_height=48)
                r4 = types.InlineQueryResultArticle('4.', '������ ���� ������������',
                                                    types.InputTextMessageContent(
                                                        '�������� ������� ��������������� ����� <b>(244 ��������)</b>, ������ ���� ������������',
                                                        parse_mode='html'), thumb_url=char_icon,
                                                    thumb_width=48, thumb_height=48)
                r5 = types.InlineQueryResultArticle('5.', '������� ����� ���������', types.InputTextMessageContent(
                    '�������� ����������� ����� <b>(244 ��������)</b>, ������� ����� ���������',
                    parse_mode='html'), thumb_url=char_icon,
                                                    thumb_width=48, thumb_height=48)
                r6 = types.InlineQueryResultArticle('6.', '�������� ��� ��������', types.InputTextMessageContent(
                    '�������� ����������� ����� <b>(244 ��������)</b>, �������� ��� ��������',
                    parse_mode='html'), thumb_url=char_icon,
                                                    thumb_width=48, thumb_height=48)
                r7 = types.InlineQueryResultArticle('7.', '����� ����� ������������', types.InputTextMessageContent(
                    '�������� ����������� ����� <b>(244 ��������)</b>, ����� ����� ������������',
                    parse_mode='html'), thumb_url=char_icon,
                                                    thumb_width=48, thumb_height=48)
                r8 = types.InlineQueryResultArticle('8.', '���� ����� ������������',
                                                    types.InputTextMessageContent(
                                                        '�������� ����������� ����� <b>(244 ��������)</b>, ���� ����� ������������',
                                                        parse_mode='html'), thumb_url=char_icon,
                                                    thumb_width=48, thumb_height=48)
                r9 = types.InlineQueryResultArticle('9.', '��������� ������ �����볿���', types.InputTextMessageContent(
                    '�������� ����������� ����� <b>(244 ��������)</b>, ��������� ������ �����볿���',
                    parse_mode='html'), thumb_url=char_icon,
                                                    thumb_width=48, thumb_height=48)
                r10 = types.InlineQueryResultArticle('10.', '��������� ������ �����볿���', types.InputTextMessageContent(
                    '�������� ������� ����������� ����� <b>(244 ��������)</b>, ��������� ������ �����볿���',
                    parse_mode='html'), thumb_url=char_icon,
                                                     thumb_width=48, thumb_height=48)
                r11 = types.InlineQueryResultArticle('11.', '������ ����� �����볿���',
                                                     types.InputTextMessageContent(
                                                         '�������� ������� ����������� ����� <b>(244 ��������)</b>, ������ ����� �����볿���',
                                                         parse_mode='html'), thumb_url=char_icon,
                                                     thumb_width=48, thumb_height=48)
                r12 = types.InlineQueryResultArticle('12.', '���� ������ �������', types.InputTextMessageContent(
                    '�������� ������� ����������� ����� <b>(244 ��������)</b>, ���� ������ �������',
                    parse_mode='html'), thumb_url=char_icon,
                                                     thumb_width=48, thumb_height=48)
                r13 = types.InlineQueryResultArticle('13.', '��� �������', types.InputTextMessageContent(
                    '��������: <b>244</b> \n�������� �������: <b>�.�.�., ����. �������� ���� ��������</b> \n<a href="https://law.knu.ua/ua/library/17-literatura-kafedry-ekolohichnoho-prava">˳�������� �������</a> \n<a href="https://law.knu.ua/ua/environmental-law">��������� ��� �������</a>',
                    parse_mode='html'), thumb_url=char_icon2,
                                                     thumb_width=48, thumb_height=48)
                bot.answer_inline_query(inline_query.id,
                                        [r, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13])
            except Exception as e:
                print(e)

#bot.send_message(m.chat.id, '���. ������� ��������������� �����, ����. �������� ���� �������������', reply_markup=keyboard)



@bot.message_handler(func=lambda message:message.text=='�������')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['1 ����', '2 ����', '3 ����', '4 ����', '�����']])
    bot.send_message(m.chat.id, '���� �����, ������ ����',
        reply_markup=keyboard)

@bot.message_handler(func=lambda message:message.text=='1 ����')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['I ���� (1�)', 'II ���� (1�)', 'III ���� (1�)', 'IV ���� (1�)', '�����']])
    bot.send_message(m.chat.id, '���� �����, ������ ����',
        reply_markup=keyboard)

@bot.message_handler(func=lambda message:message.text=='2 ����')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['I ���� (2�)', 'II ���� (2�)', 'III ���� (2�)', '�����']])
    bot.send_message(m.chat.id, '���� �����, ������ ����',
        reply_markup=keyboard)

@bot.message_handler(func=lambda message:message.text=='3 ����')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['I ���� (3�)', 'II ���� (3�)', 'III ���� (3�)', '�����']])
    bot.send_message(m.chat.id, '���� �����, ������ ����',
        reply_markup=keyboard)

@bot.message_handler(func=lambda message:message.text=='4 ����')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['I ���� (4�)', 'II ���� (4�)', 'III ���� (4�)', '�����']])
    bot.send_message(m.chat.id, '���� �����, ������ ����',
        reply_markup=keyboard)





#Legal misc
@bot.message_handler(func=lambda message:message.text=='Legal misc')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['LegalWizardBot', 'Legal.random', '�����']])
    bot.send_message(m.chat.id, '�����, ����������� ���������� � ���� �������������.',
        reply_markup=keyboard)


#Club
@bot.message_handler(func=lambda message:message.text=='������')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['ͳ�������� �����', '�������������� �����', '��������� �����', '���������� �����', '��������� �������������', '�����']])
    bot.send_message(m.chat.id, '���� �����, ������ �����',
        reply_markup=keyboard)

#Misc
@bot.message_handler(func=lambda message:message.text=='����������')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['��������� ����������', 'Debate Society', '�����']])
    bot.send_message(m.chat.id, '���� �����, ������ ��������� ��� ��������',
        reply_markup=keyboard)


#Q&A
@bot.message_handler(func=lambda message:message.text=='Q&A')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['������\����� ����', '���� �������', '�����']])
    bot.send_message(m.chat.id, '���� �����, ������ �������',
        reply_markup=keyboard)

#----------------------� � � � � � � =))))))))))))))))))))))
@bot.message_handler(content_types=['sticker'])
def sticker(message):
    bot.send_sticker (message.chat.id, 'CAADAgADCAADHjyUFm82G8zkqvIUAg')

@bot.message_handler(content_types=['voice'])
def sticker(message):
    bot.send_voice (message.chat.id, 'AwADBAADL70AAiIZZAd2IfXkFUsbYgI')


#                �                    �                       �                    �__________________�_________________�________________�
#--------------------------------------------------------------------------------------------

@bot.message_handler(func=lambda message:message.text=='�������')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['�\�\�\�', '�\�', '�\�\�', '�\�', '�����']])
    bot.send_photo(m.chat.id, 'AgADAgADiagxG5c38UlgI0rrVHnod_PWDw4ABNqjUjELwBfeJawAAgI', '���� �����, ������ ����� ����� ����� ��������� ��� �������',
        reply_markup=keyboard)

@bot.message_handler(func=lambda message:message.text=='�\�\�\�')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['�������������', '������������', '���������', '��������&�������', '�����']])
    bot.send_message(m.chat.id, '���� �����, ������ �������',
        reply_markup=keyboard)

@bot.message_handler(func=lambda message:message.text=='�\�')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['��������� ���', '�������������� ��������', '������ �����&�������', '�������������', '����������&����������', '�����']])
    bot.send_message(m.chat.id, '���� �����, ������ �������',
        reply_markup=keyboard)

@bot.message_handler(func=lambda message:message.text=='�\�\�')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['�������, ����������, ���������', '����������', '����� �����&�������', '���������&���', '�����']])
    bot.send_message(m.chat.id, '���� �����, ������ �������',
        reply_markup=keyboard)

@bot.message_handler(func=lambda message:message.text=='�\�')
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Գ�������', '�������', '�����']])
    bot.send_message(m.chat.id, '���� �����, ������ �������',
        reply_markup=keyboard)
#-------------------------------------------------------------------------------------------

#main

#ROZKLAD

@bot.message_handler(content_types=['text'])
def potik(message):
    if message.text == 'I ���� (1�)':
       bot.send_photo(message.chat.id, 'AgADAgADEagxGxkDCUuIt6aNXaH7Bj4ySw0ABIOBwIm7GqVfaNkQAAEC')
    elif message.text == 'II ���� (1�)':
       bot.send_photo(message.chat.id, 'AgADAgADo6gxGyalAUufdoM2wxidYdvlDw4ABCNL8G4wutyhZsoBAAEC')
    elif message.text == 'III ���� (1�)':
       bot.send_photo(message.chat.id, 'AgADAgADpagxGyalAUtoMVQLgTfAUCjTDw4ABEdKq9pyEkUm6sMBAAEC')
    elif message.text == 'IV ���� (1�)':
       bot.send_photo(message.chat.id, 'AgADAgADp6gxGyalAUu3mozNHJK2ceoOSw0ABAwgLHMgBs10QdMQAAEC')

    elif message.text == 'I ���� (2�)':
        bot.send_photo(message.chat.id, 'AgADAgADDqkxGyalCUtw98ZoqvG67U89Sw0ABE1cVkJe4x9IOd0QAAEC')
    elif message.text == 'II ���� (2�)':
        bot.send_photo(message.chat.id, 'AgADAgADEKkxGyalCUs6cgTj3rvRn0bsDw4ABEX9d5yJ0tn2lskBAAEC')
    elif message.text == 'III ���� (2�)':
        bot.send_photo(message.chat.id, 'AgADAgADEakxGyalCUtWTUMsCtYLFR8xSw0ABOZ89VDsigQ_Qt4QAAEC')

    elif message.text == 'I ���� (3�)':
        bot.send_photo(message.chat.id, 'AgADAgADEqkxGyalCUsg2sPu7oiAuxbRDw4ABPAc7LjJp8Do9MoBAAEC')
    elif message.text == 'II ���� (3�)':
        bot.send_photo(message.chat.id, 'AgADAgADE6kxGyalCUu6i9UKuKGDQ7vuDw4ABM1SQz7noKveZc4BAAEC')
    elif message.text == 'III ���� (3�)':
        bot.send_photo(message.chat.id, 'AgADAgADFKkxGyalCUvXLD8DTcU-0o85Sw0ABIrgMEgt1tPE2uUQAAEC')

    elif message.text == 'I ���� (4�)':
        bot.send_photo(message.chat.id, 'AgADAgADF6kxGyalCUt3Yom2hlXTaug8Sw0ABDE-oDGNVXslDekQAAEC')
    elif message.text == 'II ���� (4�)':
        bot.send_photo(message.chat.id, 'AgADAgADGKkxGyalCUtfucVBWZEWAAFi3A8OAATqsRjUwvfEUPHMAQABAg')
    elif message.text == 'III ���� (4�)':
        bot.send_photo(message.chat.id, 'AgADAgADGakxGyalCUtMJBXqC9azFJLVDw4ABHPFO0xHNH5b98kBAAEC')

    #Club
    elif message.text == 'ͳ�������� �����':
       bot.send_message(message.chat.id, '����� �������� ������ � ������������ �������� ���������� ������ �� �������� ��������� ������� ������������ �� ���������� ������� �� ��������� ����������� �� ������ ���������� ����������� ��������� ͳ�������, ��������� �������� ����� ���������� �� ����������� �� ��������� ��������� '
                                         '��� ���������� �������� ��������, ��������� � �������� �������� ͳ�������, ��������� ���������� ����������. http://zdr.knu.ua/ua/')
    elif message.text == '�������������� �����':
       bot.send_message(message.chat.id,'����� �������� ACLC � ��������� �������� ���������� ������ �� �������� ��������� ������� ������������, ���������� ������� �� ���������� �� ���������. http://aclc.knu.ua/index.php')
    elif message.text == '��������� �����':
       bot.send_message(message.chat.id,'http://health.law.knu.ua')
    elif message.text == '��������� �������������':
       bot.send_message(message.chat.id, '���� �������� ������ ������ � ���������� ��������� ��������������� � ���������� ������� ��������� ������������� ������ �� ������������� ������������� ����� (���� acquis communautaire). https://law.knu.ua/ua/center-for-the-study-of-problems-of-adaptation-of-the-ukrainian-laws-to-the-eu-laws')
    elif message.text == '���������� �����':
       bot.send_message(message.chat.id, 'https://www.facebook.com/centrumprawapolskiego/?rc=p')

    #Misc
    elif message.text == '��������� ����������':
       bot.send_message(message.chat.id, '�� ��������� �� �����, ��������� ������� ��� �� ���� �� ����� ������� ���������� �������� ����������, ��� � ������������� ����� ��� � ����������� �����. '
                                         '����� ������ ������� ����� ������� ��� �������� ���� ��������� ����������, ����� �������� �����������, ���������� ���������� �������� �� ����������. ĳ������� ��� ���� �������, � ����� ���������� �� �������� ����� �� ���������� https://alumni.law.knu.ua/')
    elif message.text == 'Debate Society':
       bot.send_message(message.chat.id, '������ - ��������� �������������� ��������, ���� ����������� �������� �������� ���������� ������� �� ������ ���� (�� �������� � ��� �� ѳ���� � ������볿, �� �������� � ������ �� �������������� ����������� � ���). �� �������������� �������, �������� ��� ����������� ��������/����� � ����, �� �� ������� �������� ���� ����������� � �����/����������/��������. https://www.facebook.com/debateclubknu/')

    #M A P
    elif message.text == '����':
       bot.send_photo(message.chat.id, 'AgADAgADI6gxG9HA0UkBzN_OjzvQvDwySw0ABAcvN4qqBQPevagPAAEC', '��������� ������������ ������������� �����! �������� �� ����������, ������ ��������� �������� �� ������ ������� ��, �� ���������� ��������� ���� ����������! http://mapknulaw.org.ua/view/ver1-01/')



    #�������
    # ---------------------------------------------------------------------------
    # ---------------------------------------------------------------------------
    # ---------------------------------------------------------------------------
    elif message.text == '�������������':
       bot.send_message(message.chat.id, '��������: <b>324</b> \n�������� �������: <b>�.�.�., ����. �������� ��������� ����������</b> \n<a href="https://law.knu.ua/ua/library/9-literatura-kafedry-administratyvnoho-prava">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/administrative-law">��������� ��� �������</a>', parse_mode="HTML")

    elif message.text == '������������':
       bot.send_message(message.chat.id, '��������: <b>256</b> \n�������� �������: <b>�.�.�., ����. ������� �������� ����������</b> \n<a href="https://law.knu.ua/ua/library/8-literatura-kafedry-hospodarskoho-prava">˳�������� �������</a> \n<a href="https://law.knu.ua/ua/commercial-law">��������� ��� �������</a>', parse_mode="HTML")

    elif message.text == '���������':
       bot.send_message(message.chat.id, '��������: <b>244</b> \n�������� �������: <b>�.�.�., ����. �������� ���� ��������</b> \n<a href="https://law.knu.ua/ua/library/17-literatura-kafedry-ekolohichnoho-prava">˳�������� �������</a> \n<a href="https://law.knu.ua/ua/environmental-law">��������� ��� �������</a>', parse_mode="HTML")

    elif message.text == '��������&�������':
       bot.send_message(message.chat.id,
                         '��������: <b>242</b> \n�������� �������: <b>�.�.�., ���. ��������� ������ ������������</b> \n<a href="https://law.univ.kiev.ua/ua/library/18-literatura-kafedry-zemelnoho-ta-ahrarnoho-prava">˳�������� �������</a>\n<a href="https://law.univ.kiev.ua/ua/land-and-agricultural-law">��������� ��� �������</a>',
                         parse_mode="HTML")

#-------------------------------------------------------------------------
    elif message.text == '��������� ���':
       bot.send_message(message.chat.id,
                         '��������: <b>257</b> \n�������� �������: <b>�.�����.�., ���. ����������� ������ �����볿���</b> \n<a href="https://law.univ.kiev.ua/ua/library/16-literatura-kafedry-inozemnykh-mov">˳�������� �������</a>\n<a href="https://law.univ.kiev.ua/ua/foreign-languages">��������� ��� �������</a>',
                         parse_mode="HTML")

    elif message.text == '�������������� ��������':
       bot.send_message(message.chat.id,
                         '��������: <b>263</b> \n�������� �������: <b>�.�.�., ����. ����� ����� �������</b> \n<a href="https://law.knu.ua/ua/library/40-literatura-kafedry-intelektualnoi-vlasnosti">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/intellectual-property">��������� ��� �������</a>',
                         parse_mode="HTML")

    elif message.text == '������ �����&�������':
       bot.send_message(message.chat.id,
                         '��������: <b>344</b> \n�.�. ��������� �������: <b>�.�.�., �.�.�., ����. ̳���������� ���� �������</b> \n<a href="https://law.knu.ua/ua/library/15-literatura-kafedry-istorii-prava-ta-derzhavy">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/history-of-law-and-state">��������� ��� �������</a>',
                         parse_mode="HTML")

    elif message.text == '�������������':
       bot.send_message(message.chat.id,
                         '��������: <b>248</b> \n�������� �������: <b>�.�.�., ����. �������� ���� �������������</b> \n<a href="https://law.knu.ua/ua/library/13-literatura-kafedry-konstytutsiinoho-prava">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/constitutional-law">��������� ��� �������</a>',
                         parse_mode="HTML")

    elif message.text == '����������&����������':
       bot.send_message(message.chat.id,
                         '��������: <b>251</b> \n�������� �������: <b>�.�.�., ����. �������� ����� ��������</b> \n<a href="https://law.knu.ua/ua/library/19-literatura-kafedry-kryminalnoho-prava-ta-kryminolohii">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/criminal-law-and-criminology">��������� ��� �������</a>',
                         parse_mode="HTML")

    elif message.text == '�������, ����������, ���������':
       bot.send_message(message.chat.id,
                         '��������: <b>265</b> \n�������� �������: <b>�.�.�., ����. ����� ������� ����������</b> \n<a href="https://law.knu.ua/ua/library/23-literatura-kafedry-notarialnogo-ta-vykonavchogo-procesu-i-advokatury">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/notarial-and-executive-process-and-advocacy">��������� ��� �������</a>',
                         parse_mode="HTML")

    elif message.text == '����������':
       bot.send_message(message.chat.id,
                         '��������: <b>250</b> \n�������� �������: <b>�.�.�., ����. ����������� ������ �����������</b> \n<a href="https://law.knu.ua/ua/library/10-literatura-kafedry-pravosuddia">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/justice">��������� ��� �������</a>',
                         parse_mode="HTML")

    elif message.text == '����� �����&�������':
        bot.send_message(message.chat.id,
                         '��������: <b>260</b> \n�������� �������: <b>�.�.�., ����. ��������� ������� ��������</b> \n<a href="https://law.knu.ua/ua/library/22-literatura-kafedry-teorii-prava-ta-derzhavy">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/theory-of-law-and-state">��������� ��� �������</a>',
                         parse_mode="HTML")

    elif message.text == '���������&���':
        bot.send_message(message.chat.id,
                         '��������: <b>241</b> \n�������� �������: <b>�.�.�., ����. ����� ������ ��������</b> \n<a href="https://law.knu.ua/ua/library/20-literatura-kafedry-trudovogo-prava-ta-prava-socialnogo-zabezpechennja">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/labor-law-and-law-of-social-security">��������� ��� �������</a>',
                         parse_mode="HTML")

    elif message.text == 'Գ�������':
        bot.send_message(message.chat.id,
                         '��������: <b>245</b> \n�������� �������: <b>�.�.�., ����. ������ ���� �����</b> \n<a href="https://law.knu.ua/ua/library/21-literatura-kafedry-finansovogo-prava">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/financial-law">��������� ��� �������</a>',
                         parse_mode="HTML")

    elif message.text == '�������':
        bot.send_message(message.chat.id,
                         '��������: <b>249</b> \n�������� �������: <b>�.�.�., ����. �������� ����� ���������</b> \n<a href="https://law.knu.ua/ua/library/11-literatura-kafedry-tsyvilnoho-prava">˳�������� �������</a>\n<a href="https://law.knu.ua/ua/civil-law">��������� ��� �������</a>',
                         parse_mode="HTML")

bot.delete_webhook()
bot.polling(none_stop=True)