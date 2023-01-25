# -*- coding: windows-1251 -*-
import json

import telebot  # забить
from telebot import types  # забить

token = ''
bot = telebot.TeleBot(token)
bot.delete_webhook()

def handler(event, context):
    body = json.loads(event['body'])
    update = telebot.types.Update.de_json(body)
    bot.process_new_updates([update])

@bot.message_handler(commands=['start'])
def any_msg(message):
    # Здесь все, что отвечает за картинку. Ссылка - это ссылка на картинку, а caption текст, который с ней выходит
    # Если не надо, то убираешь две следующие строки
    photo_url = 'https://www.sunhome.ru/i/wallpapers/73/krasnoe-selo.orig.jpg'
    bot.send_photo(message.chat.id, photo=photo_url, caption='ТУТ БУДЕТ карта-навигатор подразделов')
    # Тут инициализация клавиатуры
    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    # Тут инициалаизаци кнопок text - это то, что на кнопке будет написано callback_data это что будет получать функция,
    # которая кнопку обрабатывает
    sovet_button = types.InlineKeyboardButton(text="Совет дома", callback_data="sovet")
    instructions_button = types.InlineKeyboardButton(text="Инструкции", callback_data="instructions")
    Main_locations_button = types.InlineKeyboardButton(text="Полезные адреса", callback_data="Main_locations")
    Main_phone_button = types.InlineKeyboardButton(text="Важные номера телефонов", callback_data="Main_phone")
    around_button = types.InlineKeyboardButton(text="Что рядом?", callback_data="around")
    # links_button = types.InlineKeyboardButton(text="Полезные ссылки", callback_data="links")
    Que_button = types.InlineKeyboardButton(text="Я Самый ЛУЧШИЙ из соседей", callback_data="Que")

    # Тут добвляешь кнопки в клавиатуру. Опытным путем получено, что сколько добавить столько и будет в строке. Добавишь все он
    # он разместит их по своему сам
    keyboardmain.add(sovet_button, Main_phone_button)
    keyboardmain.add(Main_locations_button)
    keyboardmain.add(instructions_button)
    keyboardmain.add(around_button)  # , links_button)
    keyboardmain.add(Que_button)
    # При первом вызове sent_message, а дальше уже edit_message. В кавычках текст шапки меню, а reply_markup - туда передаешь
    # свою клаву
    bot.send_message(message.chat.id, "МЕНЮ", reply_markup=keyboardmain)


# Тут обработка вызова
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Этот if для кнопки назад.
    if call.data == "mainmenu":
        keyboardmain = types.InlineKeyboardMarkup(row_width=2)
        sovet_button = types.InlineKeyboardButton(text="Совет дома", callback_data="sovet")
        instructions_button = types.InlineKeyboardButton(text="Инструкции", callback_data="instructions")
        Main_locations_button = types.InlineKeyboardButton(text="Полезные адреса", callback_data="Main_locations")
        Main_phone_button = types.InlineKeyboardButton(text="Важные номера телефонов", callback_data="Main_phone")
        around_button = types.InlineKeyboardButton(text="Что рядом?", callback_data="around")
        # links_button = types.InlineKeyboardButton(text="Полезные ссылки", callback_data="links")
        Que_button = types.InlineKeyboardButton(text="Я Самый ЛУЧШИЙ из соседей", callback_data="Que")
        keyboardmain.add(sovet_button, Main_phone_button)
        keyboardmain.add(Main_locations_button)
        keyboardmain.add(instructions_button)
        keyboardmain.add(around_button)  # , links_button)
        keyboardmain.add(Que_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="МЕНЮ",
                              reply_markup=keyboardmain)

    if call.data == "sovet":
        keyboard = types.InlineKeyboardMarkup()
        home_senior_button = types.InlineKeyboardButton(text="Старший по дому", callback_data="home_senior")
        head_porch1_button = types.InlineKeyboardButton(text="Старший по первому подъезду", callback_data="1porch")
        head_porch2_button = types.InlineKeyboardButton(text="Старший по второму подъезду", callback_data="2porch")
        head_porch3_button = types.InlineKeyboardButton(text="Старший по третьему подъезду", callback_data="3porch")
        head_porch4_button = types.InlineKeyboardButton(text="Старший по четвертому подъезду", callback_data="4porch")
        head_porch5_button = types.InlineKeyboardButton(text="Старший по пятому подъезду", callback_data="5porch")
        head_chat_button = types.InlineKeyboardButton(text="Старший по чату", callback_data="head_chat")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(home_senior_button)
        keyboard.add(head_porch1_button)
        keyboard.add(head_porch2_button)
        keyboard.add(head_porch3_button)
        keyboard.add(head_porch4_button)
        keyboard.add(head_porch5_button)
        keyboard.add(head_chat_button)
        keyboard.add(backbutton)
        # Тут обрати внимание, что уже edit message
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Совет дома\n\nБудьте благоразумны: старшие не могут быть всегда онлайн, у них могут быть свои дела.\nПросим уважать личное время и звонить в разумное время)\nА лучше написать, а не звонить)",
                              reply_markup=keyboard)

    elif call.data == "Main_locations":
        keyboard = types.InlineKeyboardMarkup()
        uk_local_button = types.InlineKeyboardButton(text="Местное отделение ООО Наш Дом", callback_data="uk_local")
        uk_main_button = types.InlineKeyboardButton(text="Главный офис ООО Наш Дом", callback_data="uk_main")
        austerliz_button = types.InlineKeyboardButton(text="МУП МосОблЕИРЦ", callback_data="austerliz")
        comp_center_button = types.InlineKeyboardButton(text="МУП Расчетный центр", callback_data="comp_center")
        enrgo_button = types.InlineKeyboardButton(text="МосОблЭнергосбыт", callback_data="energety_pidorasy")
        Administration_button = types.InlineKeyboardButton(text="Администрация", callback_data="Administration")
        Powernet_button = types.InlineKeyboardButton(text="Теплосеть", callback_data="Powernet")
        Watertube_button = types.InlineKeyboardButton(text="Водоканал", callback_data="Watertube")
        MyDocs_button = types.InlineKeyboardButton(text="Офисы Мои Документы", callback_data="MyDocs")
        BTI_button = types.InlineKeyboardButton(text="БТИ", callback_data="BTI")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(uk_local_button)  # austerliz_button, comp_center_button,enrgo_button,backbutton)
        keyboard.add(uk_main_button)
        keyboard.add(austerliz_button)
        keyboard.add(comp_center_button)
        keyboard.add(enrgo_button)
        keyboard.add(Administration_button)
        keyboard.add(Powernet_button)
        keyboard.add(Watertube_button)
        keyboard.add(MyDocs_button)
        keyboard.add(BTI_button)
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Обслуживающие организации", reply_markup=keyboard)

    elif call.data == "Main_phone":
        keyboard = types.InlineKeyboardMarkup()
        ads_button = types.InlineKeyboardButton(text="АДС", callback_data="ads")
        manаger_button = types.InlineKeyboardButton(text="Управляющий", callback_data="manager")
        MVD_button = types.InlineKeyboardButton(text="Полиция", callback_data="MVD")
        Fire_button = types.InlineKeyboardButton(text="МЧС", callback_data="Fire")
        Helth_button = types.InlineKeyboardButton(text="Скорая помощь", callback_data="Helth")
        Snow_button = types.InlineKeyboardButton(text="Уборка снега", callback_data="Snow")
        # carpenter_button = types.InlineKeyboardButton(text="Плотник", callback_data="carpenter")
        # plumber_button = types.InlineKeyboardButton(text="Сантехник", callback_data="plumber")
        # street_cleaner_button = types.InlineKeyboardButton(text="Дворник", callback_data="street_cleaner")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(ads_button)
        keyboard.add(manаger_button)
        keyboard.add(MVD_button)
        keyboard.add(Fire_button)
        keyboard.add(Helth_button)
        keyboard.add(Snow_button)
        # keyboard.add(plumber_button)
        # keyboard.add(street_cleaner_button)
        # keyboard.add(carpenter_button)
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Аварийные телефоны",
                              reply_markup=keyboard)

    elif call.data == "instructions":
        keyboard = types.InlineKeyboardMarkup()
        Adress_button = types.InlineKeyboardButton(text="Адрес дома", callback_data="Adress")
        Plan_button = types.InlineKeyboardButton(text="По каким вопросам куда обращаться?", callback_data="Plan")
        cad_number_button = types.InlineKeyboardButton(
            text="Получение кадастрового номера и оформление в собственность", callback_data="cad_namber")
        reg_button = types.InlineKeyboardButton(text="Подача данных с счетчика", callback_data="reg_counter")
        payment_button = types.InlineKeyboardButton(text="За что платим?", callback_data="payment")
        IT_button = types.InlineKeyboardButton(text="Интернет, ТВ", callback_data="IT")
        heat_button = types.InlineKeyboardButton(text="Вопросы по отоплению", callback_data="heat")
        Silence_button = types.InlineKeyboardButton(text="Закон о тишине", callback_data="Silence")
        HomeLock_button = types.InlineKeyboardButton(text="Вопросы по домофону", callback_data="HomeLock")
        Links_button = types.InlineKeyboardButton(text="Полезные ссылки", callback_data="Links")
        Capital_button = types.InlineKeyboardButton(text="Капитальный ремонт", callback_data="Capital")
        Children_button = types.InlineKeyboardButton(text="Детские учереждения", callback_data="Children")
        Bus_button = types.InlineKeyboardButton(text="Как добраться", callback_data="Bus")
        Hospital_button = types.InlineKeyboardButton(text="Медучереждения", callback_data="Hospital")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(Adress_button)
        keyboard.add(Plan_button)
        keyboard.add(cad_number_button)
        keyboard.add(payment_button)
        keyboard.add(reg_button)
        keyboard.add(IT_button)
        keyboard.add(heat_button)
        keyboard.add(Silence_button)
        keyboard.add(HomeLock_button)
        keyboard.add(Links_button)
        keyboard.add(Capital_button)
        keyboard.add(Children_button)
        keyboard.add(Bus_button)
        keyboard.add(Hospital_button)
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Инструкции",
                              reply_markup=keyboard)

    elif call.data == 'Que':
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Без лишних слов:\n\nhttps://dobrodel.mosreg.ru/",
                              reply_markup=keyboard)
    # Тут пишешь, что хочешь от резрва, по аналогии. Если новую менюшку, то переделываешь одну из верхних,
    # Если вывод текста, то одну из последних
    # elif call.data == 'reserv2:
    # Тут пишешь, что хочешь от резрва, по аналогии. Если новую менюшку, то переделываешь одну из верхних,
    # Если вывод текста, то одну из последних

    elif call.data == 'test1':
        keyboard_61 = types.InlineKeyboardMarkup()
        backbutton_61 = types.InlineKeyboardButton(text="Назад", callback_data="reserv1")
        keyboard_61.add(backbutton_61)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Тестирование успешно",
                              reply_markup=keyboard_61)


    # Совет дома
    elif call.data == 'home_senior':
        keyboard_10 = types.InlineKeyboardMarkup()
        backbutton_10 = types.InlineKeyboardButton(text="Назад", callback_data="sovet")
        keyboard_10.add(backbutton_10)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="ПсевдоМаксим\n\n+79643133461",
                              reply_markup=keyboard_10)
        #   bot.send_message(chat_id=call.message.chat.id, text="Максим")
    elif call.data == '1porch':
        keyboard_11 = types.InlineKeyboardMarkup()
        backbutton_11 = types.InlineKeyboardButton(text="Назад", callback_data="sovet")
        keyboard_11.add(backbutton_11)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Артем\n(@ar_kuz52)\nссылка на чат подъезда"
                              # "https://t.me/+ujecDAndW-djYjgy"
                              ,
                              reply_markup=keyboard_11)
        #  bot.send_message(chat_id=call.message.chat.id, text="Артем")
    elif call.data == '2porch':
        keyboard_12 = types.InlineKeyboardMarkup()
        backbutton_12 = types.InlineKeyboardButton(text="Назад", callback_data="sovet")
        keyboard_12.add(backbutton_12)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Алёна\n\nссылка на чат подъезда\nhttps://t.me/+oz3pqr225HxmYzhi",
                              reply_markup=keyboard_12)
        #  bot.send_message(chat_id=call.message.chat.id, text="Алена")
    elif call.data == '3porch':
        keyboard_13 = types.InlineKeyboardMarkup()
        backbutton_13 = types.InlineKeyboardButton(text="Назад", callback_data="sovet")
        keyboard_13.add(backbutton_13)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Алеся\n(@Lyasya07)",
                              reply_markup=keyboard_13)
        #  bot.send_message(chat_id=call.message.chat.id, text="Алеся")
    elif call.data == '4porch':
        keyboard_14 = types.InlineKeyboardMarkup()
        backbutton_14 = types.InlineKeyboardButton(text="Назад", callback_data="sovet")
        keyboard_14.add(backbutton_14)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Не Максим\n\n+79998098330",
                              reply_markup=keyboard_14)
        #  bot.send_message(chat_id=call.message.chat.id, text="Не Максим")

    elif call.data == '5porch':
        keyboard_15 = types.InlineKeyboardMarkup()
        backbutton_15 = types.InlineKeyboardButton(text="Назад", callback_data="sovet")
        keyboard_15.add(backbutton_15)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Совет дома рекомендует обращаться к Олегу",
                              reply_markup=keyboard_15)
        #  bot.send_message(chat_id=call.message.chat.id, text="Юлия")

    elif call.data == 'head_chat':
        keyboard_16 = types.InlineKeyboardMarkup()
        backbutton_16 = types.InlineKeyboardButton(text="Назад", callback_data="sovet")
        keyboard_16.add(backbutton_16)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="По вопросам добавления в чаты (Вотс и ТГ), банов/разбанов и немножко работы чата) \n\n наша Матерь чатов\nНаталья\n\n+7 926 884 2276",
                              reply_markup=keyboard_16)
        #  bot.send_message(chat_id=call.message.chat.id, text="Наталья")

    # Важные номера телефонов
    elif call.data == 'ads':
        keyboard_21 = types.InlineKeyboardMarkup()
        backbutton_21 = types.InlineKeyboardButton(text="Назад", callback_data="Main_phone")
        keyboard_21.add(backbutton_21)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="84951252726\nКруглосуточно",
                              reply_markup=keyboard_21)
        # bot.send_message(chat_id=call.message.chat.id, text="-1")

    elif call.data == 'manager':
        keyboard_22 = types.InlineKeyboardMarkup()
        backbutton_22 = types.InlineKeyboardButton(text="Назад", callback_data="Main_phone")
        keyboard_22.add(backbutton_22)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Максим\n+7 964 313-34-61\n9:00-17:00",
                              reply_markup=keyboard_22)
        # bot.send_message(chat_id=call.message.chat.id, text="2")

    elif call.data == 'MVD':
        keyboard_23 = types.InlineKeyboardMarkup()
        backbutton_23 = types.InlineKeyboardButton(text="Назад", callback_data="Main_phone")
        keyboard_23.add(backbutton_23)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Участковый Максим Викторович\n89267023941\n\nОбщий номер полиции 102 или 112\n",
                              reply_markup=keyboard_23)
        # bot.send_message(chat_id=call.message.chat.id, text="2")

    elif call.data == 'Fire':
        keyboard_24 = types.InlineKeyboardMarkup()
        backbutton_24 = types.InlineKeyboardButton(text="Назад", callback_data="Main_phone")
        keyboard_24.add(backbutton_24)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Общий номер пожарной охраны и МЧС 101 или 112",
                              reply_markup=keyboard_24)
        # bot.send_message(chat_id=call.message.chat.id, text="2")

    elif call.data == 'Helth':
        keyboard_25 = types.InlineKeyboardMarkup()
        backbutton_25 = types.InlineKeyboardButton(text="Назад", callback_data="Main_phone")
        keyboard_25.add(backbutton_25)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Общий номер пожарной охраны и МЧС 103 или 112",
                              reply_markup=keyboard_25)
        # bot.send_message(chat_id=call.message.chat.id, text="2")

    elif call.data == 'Snow':
        keyboard_26 = types.InlineKeyboardMarkup()
        backbutton_26 = types.InlineKeyboardButton(text="Назад", callback_data="Main_phone")
        keyboard_26.add(backbutton_26)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="89255079933\nТелефон, Telegram, WhatsAp",
                              reply_markup=keyboard_26)
        # bot.send_message(chat_id=call.message.chat.id, text="2")

    elif call.data == 'plumber':
        keyboard_27 = types.InlineKeyboardMarkup()
        backbutton_27 = types.InlineKeyboardButton(text="Назад", callback_data="Main_phone")
        keyboard_27.add(backbutton_27)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="3",
                              reply_markup=keyboard_27)
        # bot.send_message(chat_id=call.message.chat.id, text="3")

    elif call.data == 'street_cleaner':
        keyboard_28 = types.InlineKeyboardMarkup()
        backbutton_28 = types.InlineKeyboardButton(text="Назад", callback_data="Main_phone")
        keyboard_28.add(backbutton_28)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Уткир",
                              reply_markup=keyboard_28)
        # bot.send_message(chat_id=call.message.chat.id, text="4")

    elif call.data == 'carpenter':
        keyboard_29 = types.InlineKeyboardMarkup()
        backbutton_29 = types.InlineKeyboardButton(text="Назад", callback_data="Main_phone")
        keyboard_29.add(backbutton_29)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="5",
                              reply_markup=keyboard_29)
        # bot.send_message(chat_id=call.message.chat.id, text="5")

    # Полезные адреса

    elif call.data == 'uk_local':  # Адрес местного отделения УК
        keyboard_31 = types.InlineKeyboardMarkup()
        backbutton_31 = types.InlineKeyboardButton(text="Назад", callback_data="Main_locations")
        keyboard_31.add(backbutton_31)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Адрес: п. Мебельной фабрики\nУл. Рассветная, д.1\n(рядом с пунктом выдачи WildBerries)\n\nВремя работы: понедельник-пятница 9:00-18:00",
                              reply_markup=keyboard_31)
        # bot.send_message(chat_id=call.message.chat.id, text="Какой-то хрен")

    elif call.data == 'uk_main':  # Адрес и время работы УК - головного офиса
        keyboard_32 = types.InlineKeyboardMarkup()
        backbutton_32 = types.InlineKeyboardButton(text="Назад", callback_data="Main_locations")
        keyboard_32.add(backbutton_32)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Ук?! Работать?! За эту информацию плати деньги)\nНо если ты так хочешь...\n\nЮридический адрес: 141008, РФ, МО, городской округ Мытищи, ул. Колпакова, д. 20\n\nВремя работы: Понедельник - Пятница с 8:00 до 17:00\n\nОбед: с 12:00 до 13:00\n\nВыходные: Суббота и Воскресенье\n\nТелефон: 8(495)125-27-04\n\nEmail: info@nd-msk.ru\n\nУК ООО Наш Дом\nhttps://nd-msk.ru/contact/",
                              reply_markup=keyboard_32)
        # bot.send_message(chat_id=call.message.chat.id, text="Ук?! Работать?! За эту информацию плати деньги)")

    elif call.data == 'austerliz':  # МосОблЕИРЦ
        keyboard_33 = types.InlineKeyboardMarkup()
        backbutton_33 = types.InlineKeyboardButton(text="Назад", callback_data="Main_locations")
        keyboard_33.add(backbutton_33)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Адрес: г. Мытищи, ул. Щербакова, д.2, к.1\n\nРежим работы офиса:пн-чт 9:00-18-00, пт 9-00 - 16:45, сб. 9:00 - 15:00 без перерыва\n\nТелефон: 8(499)444-01-00; 8(496)245-15-99\n\nСайт: https://xn--90aijkdmaud0d.xn--p1ai/\n\nОбратная связь: office@mosobleirc.ru\nДля приема обращений от юридических и физических лиц",
                              reply_markup=keyboard_33)
    # bot.send_message(chat_id=call.message.chat.id, text="Где-то во столько-то")

    elif call.data == 'comp_center':  # МУП РЦ
        keyboard_34 = types.InlineKeyboardMarkup()
        backbutton_34 = types.InlineKeyboardButton(text="Назад", callback_data="Main_locations")
        keyboard_34.add(backbutton_34)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="МУП Расчетный центр\n\nСайт: https://rkcm.ru/\n\nг.Мытищи, ул.Юбилейная, д.40, корп.1\n\nВремя работы: Понедельник - Четверг с 9:30 до 17:30, Пятница с 8:00 до 13:00.\n\nтел.: 8(495)181-18-78\n\nЭлектронная почта: info@rkcm.ru",
                              reply_markup=keyboard_34)
    # bot.send_message(chat_id=call.message.chat.id, text="Ещё реже")
    elif call.data == 'energety_pidorasy':  # МосЭнергоСбыт
        keyboard_35 = types.InlineKeyboardMarkup()
        backbutton_35 = types.InlineKeyboardButton(text="Назад", callback_data="Main_locations")
        keyboard_35.add(backbutton_35)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Услуги за свет предоставляет МОСОБЛЭНЕРГО, Мытищинский филиал производственного отделения Пушкино,\n\nАдрес: Мытищи, ул. Угольная, д.1,\n\nТелефон: +7(495)586-70-07\n\nТелефон Аварийной службы: +7(495)933-54-45\n\nСайт: http://www.mosoblenergo.ru/?yandex-source=desktop-maps\n\nE-mail: Фиг пойми, я запутался в их сайтах и названиях",
                              reply_markup=keyboard_35)
    # bot.send_message(chat_id=call.message.chat.id, text="Чернобыль")

    elif call.data == 'Administration':  # МосЭнергоСбыт
        keyboard_351 = types.InlineKeyboardMarkup()
        backbutton_351 = types.InlineKeyboardButton(text="Назад", callback_data="Main_locations")
        keyboard_351.add(backbutton_351)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Мэр городского округа Мытищи: Юлия Олеговна Купецкая\n\nАдрес администрации: г. Мытищи, Новомытищинский пр-т, д. 36/7\n\nТелефон: 8(495)581-13-83\n\nСайт: http:https://mytyshi.ru/\n\nE-mail: inform@mytyshi.ru\n\n\n",
                              reply_markup=keyboard_351)
    # bot.send_message(chat_id=call.message.chat.id, text="Чернобыль")

    elif call.data == 'Powernet':  # теплосеть
        keyboard_36 = types.InlineKeyboardMarkup()
        backbutton_36 = types.InlineKeyboardButton(text="Назад", callback_data="Main_locations")
        keyboard_36.add(backbutton_36)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="АО «Мытищинская теплосеть\n\n141002, Московская область, г. Мытищи, ул. Колпакова, д.20, офис №17\n\nГрафик работы предприятия:с понедельника по пятницу: с 08.00 до 16.45, обед с 12.00 – 12.45.\n\nТелефон диспетчерской: 8(495)583-55-92, 8(495)583-97-20, 8(495)586-13-21, 8(495)775-55-92 Телефон общего отдела: 8(495)583-07-00\n\nwww.m-teploset.ru",
                              reply_markup=keyboard_36)

    elif call.data == 'Watertube':  # Водоканал
        keyboard_37 = types.InlineKeyboardMarkup()
        backbutton_37 = types.InlineKeyboardButton(text="Назад", callback_data="Main_locations")
        keyboard_37.add(backbutton_37)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Адрес: г. Мытищи, ул. Лётная, д. 20, корп. 3\n\nРежим работы: Понедельник-Пятница: 8:00 – 16:45\n\nБез перерыва на обед\n\nСуббота, Воскресенье: выходной\n\nТелефоны:\nМногоканальный телефон: 8(800)770-78-99\n\nE-mail: ab_otd@mvdk.ru\n\nhttp://www.vodokanalmytischi.ru/",
                              reply_markup=keyboard_37)

    elif call.data == 'MyDocs':  # Мои документы
        keyboard_38 = types.InlineKeyboardMarkup()
        backbutton_38 = types.InlineKeyboardButton(text="Назад", callback_data="Main_locations")
        keyboard_38.add(backbutton_38)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="ТОСП Пирогово г.о. Мытищи, пгт Пироговский, ул. Пионерская д. 4А \nпн-чт 09:00 - 18:00\nпт 09:00 - 16:45\nПерерыв - 13:00 - 13:45\nсб и вс - выходные дни\n\nФилиал Карла Маркса и Филиал в ТЦ «4Daily»\n\nпн-вс 08:00 - 20:00\n\nhttp://mfcmmr.ru.",
                              reply_markup=keyboard_38)

    elif call.data == 'BTI':  # БТИ
        keyboard_39 = types.InlineKeyboardMarkup()
        backbutton_39 = types.InlineKeyboardButton(text="Назад", callback_data="Main_locations")
        keyboard_39.add(backbutton_39)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Адрес г. Мытищи, ул. Станционная, стр. 7\n\nТелефон 8(498)568-88-88 (доб. 2105)\n\nЭлектронная почта: mytischi@mobti.ru\n\nВремя работы:\nПн-Чт:9:00-18:00\nПт:9:00-16:45\nСб:9:00-13.00\n\nhttps://mobti.ru/filialy/mytishchinskiy-filial/",
                              reply_markup=keyboard_39)

    # Инструкции

    elif call.data == 'Adress':  # Полный адрес дома
        keyboard_41 = types.InlineKeyboardMarkup()
        backbutton_41 = types.InlineKeyboardButton(text="Назад", callback_data="instructions")
        keyboard_41.add(backbutton_41)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Московская область,\nгородской округ Мытищи,\nпосёлок Мебельной Фабрики,\nРассветная улица, дом 5\nПочтовый индекс:141033\nКоординаты: 55.969250, 37.734120\nКадастровый номер дома: 50:12:0090234:1214\n\nДом обслуживает отделение почтовой связи № 141033\nКомсомольская улица, 3\nПн-Птн 8:00-20:00\nСб 9:00-18:00",
                              reply_markup=keyboard_41)
        #  bot.send_message(chat_id=call.message.chat.id, text="быстрая")

    elif call.data == 'Plan':  # Полный адрес дома
        keyboard_42 = types.InlineKeyboardMarkup()
        backbutton_42 = types.InlineKeyboardButton(text="Назад", callback_data="instructions")
        keyboard_42.add(backbutton_42)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Данный раздел посвящён вопросам, когда произошла ситуация и пока не понятно, к кому обращаться).\n\nВ первую очередь, необходимо понять, на сколько срочная ситуация. Если крайне срочная (потоп, пожар, насилие), то необходимо позвонить по телефонам, указанным в соответстувующем разделе.\n\nВ случае потопа можно также обратиться в чат или к старшим, но в данном случае можно не получить ответ и потерять время - никто из нас не сидит в сети круглосуточно:).\n\nКроме того, рекомендуется познакомиться с соседями и взять их номера телефонов, так как от таких ситуаций не застрахован никто.\n\nВ остальных ситуациях (а это, как правило, касается неполадок в квартире) необходимо понять, в чьей зоне неполадка: в зона ответственности УК или в зона ответственности жильца. Данные зоны расписаны в договоре, но если коротко, то всё, что за вводными элементами-краном, щитком, ответвлениями труб-принадлежит собственнику, и он несёт за это ответственность. В данном случае необходимо либо самостоятельно устранить проблему, либо обратиться в соотваетствующие службы, например, к специалистам, предоставляемым УК.\n\nСтоит отметить, что квартиры находятся на гарантии 5 лет, поэтому имеет смысл попробовать обратиться к застройщику. Однако, застройщик считает себя банкротом и всячески уходит от ответственности.\n\nВ случае же, если это зона ответственности УК, то необходимо обратиться к ним. Если, как было сказано выше,ситуация не срочная, то обращаться в рабочее время по номеру телефона, оставлять заявку через приложение или лично.\n\nСпокойной Вам жизни без критических ситуаций",
                              #
                              reply_markup=keyboard_42)
        #  bot.send_message(chat_id=call.message.chat.id, text="быстрая")

    elif call.data == 'cad_namber':
        keyboard_43 = types.InlineKeyboardMarkup()
        backbutton_43 = types.InlineKeyboardButton(text="Назад", callback_data="instructions")
        keyboard_43.add(backbutton_43)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Кадастровый номер дома: 50:12:0090234:1214\n\nДля уточнения кадастрового номера Вашей квартиры необходимо позвонить на горячую линию Росреестра 8(800)100-34-34, добавочный 1 как только робот начнет разговор) и спросите оператора. Так как у Росреестра горячая линия не всегда корректно работает со своей базой и/или сайт плохо отображает информацию, Вашу квартиру сразу могут не найти, поэтому наберитесь терпения). Для оформления собственности есть разная информация по документам. Самый полный список приведен ниже. Возможно, потребуется только часть приведенных документов:\n\n•Заявление о регистрации собственности (заполняет оператор в мфц)\n\n•Паспорт\n\n•Снилс\n\n•Дду (у кого с электронной подписью, то копия, желательно с дополнением с печатями. Если нет, то и так возьмут)\n\n•Акт приёма передачи (2 шт)\n\n•Кредит договор (оригинал - просто показать как источник возникновения ипотеки)\n\n•Закладная (для тех, у кого ипотека оформлена до 2018 года, сейчас их не делают)\n\n•Отчёт об оценке (для закладной)\n\n•Госпошлина 2 тыс\n\nОбращаем внимание, что не все МФЦ принимают документы. Ближайший, который назвали - МФЦ по адресу Карла Маркса, 4А. Время работы ПН-ВС 08:00 – 11:00; 11:30 – 16:00; 16:30 – 20:00.\nТак же говорили об МФЦ по адресу улица Мира, с32/2 (ТЦ 4Daily), однако мы пока не проверяли. Время работы ПН-ВС 08:00 – 11:00; 11:30 – 16:00; 16:30 – 20:00.\nМФЦ в Пирогово НЕ ПРИНЕМАЕТ ЗАЯВЛЕНИЯ ДАННОГО РОДА! \n\nХорошие результаты показал сайт https://rosreestor.com/ - на нём не всегда быстро, но находит результаты по квартирам.",
                              reply_markup=keyboard_43)
        #  bot.send_message(chat_id=call.message.chat.id, text="быстрая")

    elif call.data == 'payment':
        keyboard_44 = types.InlineKeyboardMarkup()
        backbutton_44 = types.InlineKeyboardButton(text="Назад", callback_data="instructions")
        keyboard_44.add(backbutton_44)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Содержание платёжных документов (ЕПД)\n\nСейчас нам приходят 3 квитанции:\n\n1.Квитанция от МосОблЕирц включает Капитальный ремонт и мусор\n\n2. Квитанция МУП РЦ: включает все остальные, кроме элетроэнергии, расходы: \n   текущее соджержание жилого фонда\n  подачу холодной воды\n  подачу горячей воды\n   нагрев горячей воды\n   отведение воды\n   общедомовые расходы электроэнергии, воды и отведения воды\n3. Электроэнергия от электросетей ",
                              reply_markup=keyboard_44)
        #  bot.send_message(chat_id=call.message.chat.id, text="утомительная")

    elif call.data == 'reg_counter':
        keyboard_45 = types.InlineKeyboardMarkup()
        backbutton_45 = types.InlineKeyboardButton(text="Назад", callback_data="instructions")
        keyboard_45.add(backbutton_45)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="УТОЧНИТЬ\n\n\nНа данный момент, показания передаются только для воды.\n\nСрок подачи - с 10 по 30 числа месяца\n\n\n\nПоказания электричества снимаются автоматически.\nПоказания по теплу общедомовые и делятся пропорционально площади квартир.\n\nПередать показания можно любым способом: по телефону, через приложение или личным визитом.\n\nДля передачи показаний необходимо:\n\n•подготовить лицевой счет - находится на бумажной квитанции. В случае, если Вы далеко - можно попробовать получить по телефону расчетного центра\n\n•скачать приложение и зарегистрировать в нём лицевой счёт или...\n\n•позвонить по номеру телефона организации или...\n\n•приехать по адресу в приёмные часы.\n\nЕсли необходимо опломбировать счетчик, то необходимо обратиться в УК или к пломбировщику по номеру телефона:\n\n8(916)707-77-81\n\nВалентина",
                              reply_markup=keyboard_45)
        #  bot.send_message(chat_id=call.message.chat.id, text="утомительная")

    elif call.data == 'IT':
        keyboard_46 = types.InlineKeyboardMarkup()
        backbutton_46 = types.InlineKeyboardButton(text="Назад", callback_data="instructions")
        keyboard_46.add(backbutton_46)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Из телекоммункационных сетей, на доме сейчас присутствуют два оператора интернет и центральная сеть телевидения.\n\n\n1.Оптиком\n\n8(495)780-72-62 круглосуточно\n\nСайт: https://www.opticom.net/\n\nПрисутствует IPtv\n\n\n2.Индиком\n\n8(498)500-12-22\n\nСайт: https://indikom.ru/\n\nПрисутствует IPtv\n\n\n3.Кабельное телевидение\n\n",
                              reply_markup=keyboard_46)
        #  bot.send_message(chat_id=call.message.chat.id, text="вообще забудь")

    elif call.data == 'heat':
        keyboard_47 = types.InlineKeyboardMarkup()
        backbutton_47 = types.InlineKeyboardButton(text="Назад", callback_data="instructions")
        keyboard_47.add(backbutton_47)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Отопительный период начинается и заканчивается по распоряжению мера г.о. Мытищи. Не когда *холодно* Не когда *захотелось*. Только по распоряжению. Обычно, такое распоряжение поступает, когда среднесуточная температура на протяжении 5 дней менее 8 градусов.\n\n Первыми тепло получают социально значимые объекты: детские сады, больницы, школы. Затем жилые дома и последними - предприятия.\n\nУ нашего микрорайона своя котельная, которая находится в Афродите-1 у дома 7а (выезд на Совхозную улицу). Дублирующей системы нет и любая авария на котельной приводит понижению температуры в квартире и отсутствию горячей воды\n\n!В летний период производится плановое отключение горячей воды для техобслуживания котельной (не смотря на то, что дом новый, котельная - не особо).\n\nВ многоквартирных домах, оснащенных индивидуальными тепловыми пунктами (ИТП) автоматическое отключение ИТП происходит при повышении температуры наружного воздуха выше +12°С, а автоматическое включение ИТП происходит при понижении температуры наружного воздуха ниже +10°С.Такой температурный график установлен для экономии тепла и сокращения расходов жителей на отопление.\n\n!В нашем доме именно такая система!\n\nЕсли в отопительный сезон у вас холодные батареи, то необходимо, прежде чем оставлять заявку в УК или АДС провести минипроверку:\n\n1.Проверить, горячая ли подающая труба. Если нет, то зайти в чат - возмоможно, кто-то уже сообщил о данной проблеме.\n\n2.Если труба горячая, то проверить, не перкрыт ли вентиль-регулятор (для батарей от застройщика). Попробовать выставить его на максимальное значение или вовсе снять. В течение минуты должно начать поступать тепло.\n\n3.Если тепло так и не пошло, то понажимать на золотник клапана (торчащая тонкая железка)\n\n4. Если действия выше не помогли, то в рабочее время оставлять заявку в УК, в ночное - звонить в АДС",
                              reply_markup=keyboard_47)
        #  bot.send_message(chat_id=call.message.chat.id, text="мир твоему праху")

    elif call.data == 'Silence':
        keyboard_48 = types.InlineKeyboardMarkup()
        backbutton_48 = types.InlineKeyboardButton(text="Назад", callback_data="instructions")
        keyboard_48.add(backbutton_48)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Пред тем, как опубликовать текст закона, не лишним будет напомнить, что стены в доме тонкие. Плачь ребёнка слышится отлично. Перфоратор - ещё лучше. Однако, для многих суббота - единственный днь для ремонта. Поэтому, самое разумное тем, кто хочет делать ремонт сначала предупредить соседей. А остальным, войти в положение - все мы рано или поздно будем делать ремонт. \n\nИ наоборот, если у кого-то ребёнок спит вне пределов установленного законом тихого часа, то всегда можно подойти и попросить. Не быковать, не угрожать, а попросить - многие войдут в положение и можно будет найти компромисс.\n\nКроме того, не стоит злиться из-за 1-2 звуков, в разумное время, например, в праздники.\n\n(не, ну если человек дятел сверлит рано утром или поздно вечером - то он редиска:) )\n\nКроме того, обратите внимание, что в общий чат писать смысла нет - человек с перфоратором чат не читает).\n\nТекст ниже взят из закона Закон Московской области № 16/2014-03 «Об обеспечении тишины и покоя граждан на территории Московской области» с изменениями, внесенными законами Московской области №67/2015-03, №70/2016-03, №159/2016-03, №193/2017-03, №134/2018-03):\n\n1.He допускается использование звуковоспроизводящих устройств и устройств звукоусиления, в том числе установленных на транспортных средствах, в период с 21 часа 00 минут до 08 часов 00 минут, а также с 13 часов 00 минут до 15 часов 00 минут в рабочие дни, с 22 часов 00 минут до 10 часов 00 минут, а также с 13 часов 00 минут до 15 часов 00 минут в выходные дни.\n\n 2. Не допускаются крики, свист, пение, игра на музыкальных инструментах, проведение земляных, строительных, разгрузочно-погрузочных и иных видов работ с применением механических средств и технических устройств, повлекшие нарушение тишины и покоя граждан, в период с 21 часа 00 минут до 08 часов 00 минут в рабочие дни, с 22 часов 00 минут до 10 часов 00 минут в выходные дни.\n\n4. По истечении шести месяцев со дня постановки многоквартирного дома на кадастровый учет не допускается проведение переустройства,перепланировки, ремонтных работ в жилом помещении в этом многоквартирном доме или ремонтных работ в нежилом помещении, не принадлежащем на праве общей долевой собственности собственникам помещений в этом многоквартирном доме, повлекшее нарушение тишины и покоя граждан, в период с 19 часов 00 минут до 09 часов 00 минут, а также с 13 часов 00 минут до 15 часов 00 минут в рабочие дни, с 19 часов 00 минут до 10 часов 00 минут, а также с 13 часов 00 минут до 15 часов 00 минут в субботу, круглосуточно в воскресенье и установленные федеральным mзаконодательством нерабочие праздничные дни.\n\nСсылка: https://mosreg.ru/download/document/1000167",
                              reply_markup=keyboard_48)
        #  bot.send_message(chat_id=call.message.chat.id, text="мир твоему праху")

    elif call.data == 'HomeLock':
        keyboard_49 = types.InlineKeyboardMarkup()
        backbutton_49 = types.InlineKeyboardButton(text="Назад", callback_data="instructions")
        keyboard_49.add(backbutton_49)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Информация по обслуживающей фирме обновляется.\n\nНомер сотрудника, который отвечает за домофоны по нашему дому:\nАлексей\n+7909957-87-60\n\nКоды от домофонов на данный момент спрашивайте у старших\n\nЗапрещено передавать коды третьим лицам",
                              reply_markup=keyboard_49)
        #  bot.send_message(chat_id=call.message.chat.id, text="утомительная")
    elif call.data == 'Links':
        keyboard_410 = types.InlineKeyboardMarkup()
        backbutton_410 = types.InlineKeyboardButton(text="Назад", callback_data="instructions")
        keyboard_410.add(backbutton_410)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Сайт Правительства Московской Области: https://mosreg.ru/\n\nДобродел: https://dobrodel.mosreg.ru/\nТакже есть мобильная версия:\nАнроид: https://play.google.com/store/apps/details?id=ru.mosreg.ekjp&hl=ru&gl=US&pli=1\nАйОС: https://apps.apple.com/ru/app/%D0%B4%D0%BE%D0%B1%D1%80%D0%BE%D0%B4%D0%B5%D0%BB/id1021212577",
                              reply_markup=keyboard_410)
        #  bot.send_message(chat_id=call.message.chat.id, text="утомительная")
    elif call.data == 'Capital':
        keyboard_411 = types.InlineKeyboardMarkup()
        backbutton_411 = types.InlineKeyboardButton(text="Назад", callback_data="instructions")
        keyboard_411.add(backbutton_411)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Согласно постановлению правительства Московской области 1452/45 от 27.12.2021 наш дом внесён в программу капитального ремонта, запланированного не раньше 2044г.\n\nСсылка на документ: https://mgkh.mosreg.ru/download/document/11490501\n\nаш дом тут: строка 21594, страница 369\n\nСсылка на сайт программы капремонта: https://mosreg.ru/seychas-v-rabote/proekty/mkd/mkd-renovation",
                              reply_markup=keyboard_411)
        #  bot.send_message(chat_id=call.message.chat.id, text="утомительная")

    elif call.data == 'Children':
        keyboard_412 = types.InlineKeyboardMarkup()
        backbutton_412 = types.InlineKeyboardButton(text="Назад", callback_data="instructions")
        keyboard_412.add(backbutton_412)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Ближайший детский сад: Заречная улица, 3А\n\nМладшая школа 1-2 класс: улица Советская дом 10\n\nСтаршая школа 3-11 класс: улица Тимирязева дом 7",
                              reply_markup=keyboard_412)
        #  bot.send_message(chat_id=call.message.chat.id, text="утомительная")

    elif call.data == 'Bus':
        keyboard_413 = types.InlineKeyboardMarkup()
        backbutton_413 = types.InlineKeyboardButton(text="Назад", callback_data="instructions")
        keyboard_413.add(backbutton_413)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Ближайшие к дому остановки находятся на Пирогвском перекрёстке и позволяют уехать на два направления на два направления: в сторону м. Медведково по Осташковскому шоссе (остановка Теннисный корт) и в сторону г. Мытищи по Пироговскому шосе (остановка Пироговский перекрёсток).\n\nВ сторону м.Медведково (от нас/к нам) от остановки Теннисный корт:\n581 с 6:39 по 21:09 каждые 20 минут/с 7:20 до 22:10\n166 с 5:21 по 22:31 каждые 15 минут/с 5:50 до 23:20\n314к с 6:30 до 23:00 каждые 10 минут/с 6:20 до 00:30 каждые 20 минут\n509 с 6:23 по 20:33/с7:10 по 21:20\nОт остановки Пироговский перекрёсток\n502 с 5:55 до 22:15 каждые 15 минут/с 06:10 до 22:10 каждые 15 минут\n\nОт остановки Пироговский перекрёсток до ж/д станции Мытищи:\n22 с 5:31 до 21:26 каждые 10 минут/с 5:30 до 21:30 каждые 10 минут\n23 9:00, 11:55, 16:15, 17:50, 20:00, 21:49/ с 5:15 до 21:35 каждые 45-120 минут\n26 9:00, 11:55, 16:15, 17:50, 20:00, 21:49/с 5:35 до 23:10 каждые 15-35 минут\n31 9:09, 12:59, 16:59, 20:34/6:15, 9:55, 13:55, 17:45\n314 с 6:55 до 01:05 каждые 20 минут/с 5:20 до 23:25 каждые 20 минут",
                              reply_markup=keyboard_413)
        #  bot.send_message(chat_id=call.message.chat.id, text="утомительная")

    elif call.data == 'Hospital':
        keyboard_414 = types.InlineKeyboardMarkup()
        backbutton_414 = types.InlineKeyboardButton(text="Назад", callback_data="instructions")
        keyboard_414.add(backbutton_414)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Территориально мы относимся к больнице Пирогово\nАдрес: Советская улица, 2\n\nРядом присутствует кабинет с врачом общей практики\nАдрес: Заречная улица, 5",
                              reply_markup=keyboard_414)
        #  bot.send_message(chat_id=call.message.chat.id, text="утомительная")

    elif call.data == 'around':
        keyboard_414 = types.InlineKeyboardMarkup()
        backbutton_414 = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_414.add(backbutton_414)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Магазины продовольствия\nПятерочка: Рассветная 1а\nВерный: Рассветная 1\nКрасноеБелое: Рассветная 1\nСвежее мясо: Рассветная 1\nМагазин круглосуточный: Рассветная 1\nПивстанция: Рассветная 1\n\nБыт\nТысяча мелочей, мастерская ключей: Рассветная 1\nРемонт одежды: Рассветная 3 с торца со стороны д.1\n\nПункты выдачи заказов\nWilberries: Рассветная 1, Заречная 5\nOzon: Заречная 5\n\nБанкоматы\nСоветская 1А, магазин Пятёрочка\nСовхозная 20г, магазин Перекресток",
                              reply_markup=keyboard_414)
        #  bot.send_message(chat_id=call.message.chat.id, text="утомительная")


bot.polling(none_stop=True)

"""
В общем правила простые. Хочешь что то добавить во вторую или третью клаву, то копируешь из части, где обработчик
Если хочешь менять первую, то копируешь только из того, что есть в первой. Иначе с этими chat_id  т.д. можно сойти с ума
Кнопке назад наужно передавать ссылку на ту клаву, куда хочешь, чтобы она перешла
Ну вот вроде бы и все"""

#  Copyright (c) ChernV (@otter18), 2021.
