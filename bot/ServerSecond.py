import base64
import json

import telebot  # забить
from telebot import types  # забить

token = 'ТОКЕН БОТА'
bot = telebot.TeleBot(token)

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
    main_locations_button = types.InlineKeyboardButton(text="Полезные адреса", callback_data="Main_locations")
    main_phone_button = types.InlineKeyboardButton(text="Важные номера телефонов", callback_data="Main_phone")
    around_button = types.InlineKeyboardButton(text="Что рядом?", callback_data="around")
    # links_button = types.InlineKeyboardButton(text="Полезные ссылки", callback_data="links")
    que_button = types.InlineKeyboardButton(text="Я Самый ЛУЧШИЙ из соседей", callback_data="Que")
    under_the_egg = types.InlineKeyboardButton(text="Под ЯИЧКО!!", callback_data="egg")

    # Тут добвляешь кнопки в клавиатуру. Опытным путем получено, что сколько добавить столько и будет в строке. Добавишь все он
    # он разместит их по своему сам
    keyboardmain.add(sovet_button, main_phone_button)
    keyboardmain.add(main_locations_button)
    keyboardmain.add(instructions_button)
    keyboardmain.add(around_button)  # , links_button)
    keyboardmain.add(que_button)
    keyboardmain.add(under_the_egg)
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
        underTheEgg = types.InlineKeyboardButton(text="Под ЯИЧКО!!", callback_data="egg")
        keyboardmain.add(sovet_button, Main_phone_button)
        keyboardmain.add(Main_locations_button)
        keyboardmain.add(instructions_button)
        keyboardmain.add(around_button)  # , links_button)
        keyboardmain.add(Que_button)
        keyboardmain.add(underTheEgg)
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
    if call.data == 'egg':
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="От ЯИЧКА", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Сейчас мы все вычистим, под яичко!",
                              reply_markup=keyboard
                              )
        bot.send_audio(chat_id=call.message.chat.id,
                       caption="Под Яичко будет день светлей",
                       audio=base64.b64decode(
                           "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")
                       )


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

"""
В общем правила простые. Хочешь что то добавить во вторую или третью клаву, то копируешь из части, где обработчик
Если хочешь менять первую, то копируешь только из того, что есть в первой. Иначе с этими chat_id  т.д. можно сойти с ума
Кнопке назад наужно передавать ссылку на ту клаву, куда хочешь, чтобы она перешла
Ну вот вроде бы и все"""

#  Copyright (c) ChernV (@otter18), 2021.
