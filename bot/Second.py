import base64
import json

import telebot  # забить
from telebot import types  # забить

token = '5712181802:AAFB94I_Kgs9TmCMSWQmcpmHVU8jkc-uQR4'
bot = telebot.TeleBot(token)
bot.delete_webhook()

with open('test.json') as file:
    jsonString = json.load(file)
    full_data = json.loads(json.dumps(jsonString))


def handler(event):
    body = json.loads(event['body'])
    update = telebot.types.Update.de_json(body)
    bot.process_new_updates([update])
    bot.stop_polling()


def go_back_to_the_menu():
    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    for key, value in full_data.items():
        try:
            keyboardmain.add(types.InlineKeyboardButton(text=value['description'], callback_data=str(key)))
        except Exception as e:
            print(e)
    return keyboardmain


@bot.message_handler(commands=['start'])
def any_msg(message):
    photo_url = 'https://www.sunhome.ru/i/wallpapers/73/krasnoe-selo.orig.jpg'
    bot.send_photo(message.chat.id, photo=photo_url, caption='ТУТ БУДЕТ карта-навигатор подразделов')
    bot.send_message(message.chat.id, "МЕНЮ", reply_markup=go_back_to_the_menu())


# Тут обработка вызова
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Этот if для кнопки назад.
    if call.data == "main_menu":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="МЕНЮ",
                              reply_markup=go_back_to_the_menu())

    else:
        if call.data in full_data:
            keyboard = types.InlineKeyboardMarkup()
            buttons_arr = full_data[call.data]['buttons']
            for button, value in buttons_arr.items():
                keyboard.add(types.InlineKeyboardButton(text=value['name'], callback_data=str(button)))
            keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="main_menu"))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=str(full_data[call.data]['description']).upper() + "\n\n" + full_data[call.data][
                                      'edit_message'],
                                  reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, text="ПсевдоМаксим\n\n+79643133461")


#
# # Совет дома
# elif call.data == 'home_senior':
# keyboard_10 = types.InlineKeyboardMarkup()
# backbutton_10 = types.InlineKeyboardButton(text="Назад", callback_data="sovet")
# keyboard_10.add(backbutton_10)
# bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                       text="ПсевдоМаксим\n\n+79643133461",
#                       reply_markup=keyboard_10)
# #   bot.send_message(chat_id=call.message.chat.id, text="Максим")
# elif call.data == '1porch':
# keyboard_11 = types.InlineKeyboardMarkup()
# backbutton_11 = types.InlineKeyboardButton(text="Назад", callback_data="sovet")
# keyboard_11.add(backbutton_11)
# bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                       text="Артем\n(@ar_kuz52)\nссылка на чат подъезда"
#                       # "https://t.me/+ujecDAndW-djYjgy"
#                       ,
#                       reply_markup=keyboard_11)
# #  bot.send_message(chat_id=call.message.chat.id, text="Артем")
# elif call.data == '2porch':
# keyboard_12 = types.InlineKeyboardMarkup()
# backbutton_12 = types.InlineKeyboardButton(text="Назад", callback_data="sovet")
# keyboard_12.add(backbutton_12)
# bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                       text="Алёна\n\nссылка на чат подъезда\nhttps://t.me/+oz3pqr225HxmYzhi",
#                       reply_markup=keyboard_12)
# #  bot.send_message(chat_id=call.message.chat.id, text="Алена")
# elif call.data == '3porch':
# keyboard_13 = types.InlineKeyboardMarkup()
# backbutton_13 = types.InlineKeyboardButton(text="Назад", callback_data="sovet")
# keyboard_13.add(backbutton_13)
# bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                       text="Алеся\n(@Lyasya07)",
#                       reply_markup=keyboard_13)
# #  bot.send_message(chat_id=call.message.chat.id, text="Алеся")
# elif call.data == '4porch':
# keyboard_14 = types.InlineKeyboardMarkup()
# backbutton_14 = types.InlineKeyboardButton(text="Назад", callback_data="sovet")
# keyboard_14.add(backbutton_14)
# bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                       text="Не Максим\n\n+79998098330",
#                       reply_markup=keyboard_14)
# #  bot.send_message(chat_id=call.message.chat.id, text="Не Максим")
#
# elif call.data == '5porch':
# keyboard_15 = types.InlineKeyboardMarkup()
# backbutton_15 = types.InlineKeyboardButton(text="Назад", callback_data="sovet")
# keyboard_15.add(backbutton_15)
# bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                       text="Совет дома рекомендует обращаться к Олегу",
#                       reply_markup=keyboard_15)
#
# elif call.data == 'head_chat':
# keyboard_16 = types.InlineKeyboardMarkup()
# backbutton_16 = types.InlineKeyboardButton(text="Назад", callback_data="sovet")
# keyboard_16.add(backbutton_16)
# bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                       text="По вопросам добавления в чаты (Вотс и ТГ), банов/разбанов и немножко работы чата) \n\n наша Матерь чатов\nНаталья\n\n+7 926 884 2276",
#                       reply_markup=keyboard_16)

if str(bot.get_webhook_info().url).strip() == "":
    bot.delete_webhook()
    bot.polling()

"""
В общем правила простые. Хочешь что то добавить во вторую или третью клаву, то копируешь из части, где обработчик
Если хочешь менять первую, то копируешь только из того, что есть в первой. Иначе с этими chat_id  т.д. можно сойти с ума
Кнопке назад наужно передавать ссылку на ту клаву, куда хочешь, чтобы она перешла
Ну вот вроде бы и все"""

#  Copyright (c) ChernV (@otter18), 2021.
# 628955904
