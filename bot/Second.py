# -*- coding: windows-1251 -*-
import json

import telebot  # ������
from telebot import types  # ������

token = ''
bot = telebot.TeleBot(token)
bot.delete_webhook()

def handler(event, context):
    body = json.loads(event['body'])
    update = telebot.types.Update.de_json(body)
    bot.process_new_updates([update])

@bot.message_handler(commands=['start'])
def any_msg(message):
    # ����� ���, ��� �������� �� ��������. ������ - ��� ������ �� ��������, � caption �����, ������� � ��� �������
    # ���� �� ����, �� �������� ��� ��������� ������
    photo_url = 'https://www.sunhome.ru/i/wallpapers/73/krasnoe-selo.orig.jpg'
    bot.send_photo(message.chat.id, photo=photo_url, caption='��� ����� �����-��������� �����������')
    # ��� ������������� ����������
    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    # ��� ������������� ������ text - ��� ��, ��� �� ������ ����� �������� callback_data ��� ��� ����� �������� �������,
    # ������� ������ ������������
    sovet_button = types.InlineKeyboardButton(text="����� ����", callback_data="sovet")
    instructions_button = types.InlineKeyboardButton(text="����������", callback_data="instructions")
    Main_locations_button = types.InlineKeyboardButton(text="�������� ������", callback_data="Main_locations")
    Main_phone_button = types.InlineKeyboardButton(text="������ ������ ���������", callback_data="Main_phone")
    around_button = types.InlineKeyboardButton(text="��� �����?", callback_data="around")
    # links_button = types.InlineKeyboardButton(text="�������� ������", callback_data="links")
    Que_button = types.InlineKeyboardButton(text="� ����� ������ �� �������", callback_data="Que")

    # ��� ��������� ������ � ����������. ������� ����� ��������, ��� ������� �������� ������� � ����� � ������. �������� ��� ��
    # �� ��������� �� �� ������ ���
    keyboardmain.add(sovet_button, Main_phone_button)
    keyboardmain.add(Main_locations_button)
    keyboardmain.add(instructions_button)
    keyboardmain.add(around_button)  # , links_button)
    keyboardmain.add(Que_button)
    # ��� ������ ������ sent_message, � ������ ��� edit_message. � �������� ����� ����� ����, � reply_markup - ���� ���������
    # ���� �����
    bot.send_message(message.chat.id, "����", reply_markup=keyboardmain)


# ��� ��������� ������
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # ���� if ��� ������ �����.
    if call.data == "mainmenu":
        keyboardmain = types.InlineKeyboardMarkup(row_width=2)
        sovet_button = types.InlineKeyboardButton(text="����� ����", callback_data="sovet")
        instructions_button = types.InlineKeyboardButton(text="����������", callback_data="instructions")
        Main_locations_button = types.InlineKeyboardButton(text="�������� ������", callback_data="Main_locations")
        Main_phone_button = types.InlineKeyboardButton(text="������ ������ ���������", callback_data="Main_phone")
        around_button = types.InlineKeyboardButton(text="��� �����?", callback_data="around")
        # links_button = types.InlineKeyboardButton(text="�������� ������", callback_data="links")
        Que_button = types.InlineKeyboardButton(text="� ����� ������ �� �������", callback_data="Que")
        keyboardmain.add(sovet_button, Main_phone_button)
        keyboardmain.add(Main_locations_button)
        keyboardmain.add(instructions_button)
        keyboardmain.add(around_button)  # , links_button)
        keyboardmain.add(Que_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="����",
                              reply_markup=keyboardmain)

    if call.data == "sovet":
        keyboard = types.InlineKeyboardMarkup()
        home_senior_button = types.InlineKeyboardButton(text="������� �� ����", callback_data="home_senior")
        head_porch1_button = types.InlineKeyboardButton(text="������� �� ������� ��������", callback_data="1porch")
        head_porch2_button = types.InlineKeyboardButton(text="������� �� ������� ��������", callback_data="2porch")
        head_porch3_button = types.InlineKeyboardButton(text="������� �� �������� ��������", callback_data="3porch")
        head_porch4_button = types.InlineKeyboardButton(text="������� �� ���������� ��������", callback_data="4porch")
        head_porch5_button = types.InlineKeyboardButton(text="������� �� ������ ��������", callback_data="5porch")
        head_chat_button = types.InlineKeyboardButton(text="������� �� ����", callback_data="head_chat")
        backbutton = types.InlineKeyboardButton(text="�����", callback_data="mainmenu")
        keyboard.add(home_senior_button)
        keyboard.add(head_porch1_button)
        keyboard.add(head_porch2_button)
        keyboard.add(head_porch3_button)
        keyboard.add(head_porch4_button)
        keyboard.add(head_porch5_button)
        keyboard.add(head_chat_button)
        keyboard.add(backbutton)
        # ��� ������ ��������, ��� ��� edit message
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="����� ����\n\n������ ������������: ������� �� ����� ���� ������ ������, � ��� ����� ���� ���� ����.\n������ ������� ������ ����� � ������� � �������� �����)\n� ����� ��������, � �� �������)",
                              reply_markup=keyboard)

    elif call.data == "Main_locations":
        keyboard = types.InlineKeyboardMarkup()
        uk_local_button = types.InlineKeyboardButton(text="������� ��������� ��� ��� ���", callback_data="uk_local")
        uk_main_button = types.InlineKeyboardButton(text="������� ���� ��� ��� ���", callback_data="uk_main")
        austerliz_button = types.InlineKeyboardButton(text="��� ����������", callback_data="austerliz")
        comp_center_button = types.InlineKeyboardButton(text="��� ��������� �����", callback_data="comp_center")
        enrgo_button = types.InlineKeyboardButton(text="����������������", callback_data="energety_pidorasy")
        Administration_button = types.InlineKeyboardButton(text="�������������", callback_data="Administration")
        Powernet_button = types.InlineKeyboardButton(text="���������", callback_data="Powernet")
        Watertube_button = types.InlineKeyboardButton(text="���������", callback_data="Watertube")
        MyDocs_button = types.InlineKeyboardButton(text="����� ��� ���������", callback_data="MyDocs")
        BTI_button = types.InlineKeyboardButton(text="���", callback_data="BTI")
        backbutton = types.InlineKeyboardButton(text="�����", callback_data="mainmenu")
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
                              text="������������� �����������", reply_markup=keyboard)

    elif call.data == "Main_phone":
        keyboard = types.InlineKeyboardMarkup()
        ads_button = types.InlineKeyboardButton(text="���", callback_data="ads")
        man�ger_button = types.InlineKeyboardButton(text="�����������", callback_data="manager")
        MVD_button = types.InlineKeyboardButton(text="�������", callback_data="MVD")
        Fire_button = types.InlineKeyboardButton(text="���", callback_data="Fire")
        Helth_button = types.InlineKeyboardButton(text="������ ������", callback_data="Helth")
        Snow_button = types.InlineKeyboardButton(text="������ �����", callback_data="Snow")
        # carpenter_button = types.InlineKeyboardButton(text="�������", callback_data="carpenter")
        # plumber_button = types.InlineKeyboardButton(text="���������", callback_data="plumber")
        # street_cleaner_button = types.InlineKeyboardButton(text="�������", callback_data="street_cleaner")
        backbutton = types.InlineKeyboardButton(text="�����", callback_data="mainmenu")
        keyboard.add(ads_button)
        keyboard.add(man�ger_button)
        keyboard.add(MVD_button)
        keyboard.add(Fire_button)
        keyboard.add(Helth_button)
        keyboard.add(Snow_button)
        # keyboard.add(plumber_button)
        # keyboard.add(street_cleaner_button)
        # keyboard.add(carpenter_button)
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="��������� ��������",
                              reply_markup=keyboard)

    elif call.data == "instructions":
        keyboard = types.InlineKeyboardMarkup()
        Adress_button = types.InlineKeyboardButton(text="����� ����", callback_data="Adress")
        Plan_button = types.InlineKeyboardButton(text="�� ����� �������� ���� ����������?", callback_data="Plan")
        cad_number_button = types.InlineKeyboardButton(
            text="��������� ������������ ������ � ���������� � �������������", callback_data="cad_namber")
        reg_button = types.InlineKeyboardButton(text="������ ������ � ��������", callback_data="reg_counter")
        payment_button = types.InlineKeyboardButton(text="�� ��� ������?", callback_data="payment")
        IT_button = types.InlineKeyboardButton(text="��������, ��", callback_data="IT")
        heat_button = types.InlineKeyboardButton(text="������� �� ���������", callback_data="heat")
        Silence_button = types.InlineKeyboardButton(text="����� � ������", callback_data="Silence")
        HomeLock_button = types.InlineKeyboardButton(text="������� �� ��������", callback_data="HomeLock")
        Links_button = types.InlineKeyboardButton(text="�������� ������", callback_data="Links")
        Capital_button = types.InlineKeyboardButton(text="����������� ������", callback_data="Capital")
        Children_button = types.InlineKeyboardButton(text="������� �����������", callback_data="Children")
        Bus_button = types.InlineKeyboardButton(text="��� ���������", callback_data="Bus")
        Hospital_button = types.InlineKeyboardButton(text="��������������", callback_data="Hospital")
        backbutton = types.InlineKeyboardButton(text="�����", callback_data="mainmenu")
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
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="����������",
                              reply_markup=keyboard)

    elif call.data == 'Que':
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="�����", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="��� ������ ����:\n\nhttps://dobrodel.mosreg.ru/",
                              reply_markup=keyboard)
    # ��� ������, ��� ������ �� ������, �� ��������. ���� ����� �������, �� ������������� ���� �� �������,
    # ���� ����� ������, �� ���� �� ���������
    # elif call.data == 'reserv2:
    # ��� ������, ��� ������ �� ������, �� ��������. ���� ����� �������, �� ������������� ���� �� �������,
    # ���� ����� ������, �� ���� �� ���������

    elif call.data == 'test1':
        keyboard_61 = types.InlineKeyboardMarkup()
        backbutton_61 = types.InlineKeyboardButton(text="�����", callback_data="reserv1")
        keyboard_61.add(backbutton_61)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="������������ �������",
                              reply_markup=keyboard_61)


    # ����� ����
    elif call.data == 'home_senior':
        keyboard_10 = types.InlineKeyboardMarkup()
        backbutton_10 = types.InlineKeyboardButton(text="�����", callback_data="sovet")
        keyboard_10.add(backbutton_10)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="������������\n\n+79643133461",
                              reply_markup=keyboard_10)
        #   bot.send_message(chat_id=call.message.chat.id, text="������")
    elif call.data == '1porch':
        keyboard_11 = types.InlineKeyboardMarkup()
        backbutton_11 = types.InlineKeyboardButton(text="�����", callback_data="sovet")
        keyboard_11.add(backbutton_11)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="�����\n(@ar_kuz52)\n������ �� ��� ��������"
                              # "https://t.me/+ujecDAndW-djYjgy"
                              ,
                              reply_markup=keyboard_11)
        #  bot.send_message(chat_id=call.message.chat.id, text="�����")
    elif call.data == '2porch':
        keyboard_12 = types.InlineKeyboardMarkup()
        backbutton_12 = types.InlineKeyboardButton(text="�����", callback_data="sovet")
        keyboard_12.add(backbutton_12)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="����\n\n������ �� ��� ��������\nhttps://t.me/+oz3pqr225HxmYzhi",
                              reply_markup=keyboard_12)
        #  bot.send_message(chat_id=call.message.chat.id, text="�����")
    elif call.data == '3porch':
        keyboard_13 = types.InlineKeyboardMarkup()
        backbutton_13 = types.InlineKeyboardButton(text="�����", callback_data="sovet")
        keyboard_13.add(backbutton_13)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="�����\n(@Lyasya07)",
                              reply_markup=keyboard_13)
        #  bot.send_message(chat_id=call.message.chat.id, text="�����")
    elif call.data == '4porch':
        keyboard_14 = types.InlineKeyboardMarkup()
        backbutton_14 = types.InlineKeyboardButton(text="�����", callback_data="sovet")
        keyboard_14.add(backbutton_14)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="�� ������\n\n+79998098330",
                              reply_markup=keyboard_14)
        #  bot.send_message(chat_id=call.message.chat.id, text="�� ������")

    elif call.data == '5porch':
        keyboard_15 = types.InlineKeyboardMarkup()
        backbutton_15 = types.InlineKeyboardButton(text="�����", callback_data="sovet")
        keyboard_15.add(backbutton_15)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="����� ���� ����������� ���������� � �����",
                              reply_markup=keyboard_15)
        #  bot.send_message(chat_id=call.message.chat.id, text="����")

    elif call.data == 'head_chat':
        keyboard_16 = types.InlineKeyboardMarkup()
        backbutton_16 = types.InlineKeyboardButton(text="�����", callback_data="sovet")
        keyboard_16.add(backbutton_16)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="�� �������� ���������� � ���� (���� � ��), �����/�������� � �������� ������ ����) \n\n ���� ������ �����\n�������\n\n+7 926 884 2276",
                              reply_markup=keyboard_16)
        #  bot.send_message(chat_id=call.message.chat.id, text="�������")

    # ������ ������ ���������
    elif call.data == 'ads':
        keyboard_21 = types.InlineKeyboardMarkup()
        backbutton_21 = types.InlineKeyboardButton(text="�����", callback_data="Main_phone")
        keyboard_21.add(backbutton_21)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="84951252726\n�������������",
                              reply_markup=keyboard_21)
        # bot.send_message(chat_id=call.message.chat.id, text="-1")

    elif call.data == 'manager':
        keyboard_22 = types.InlineKeyboardMarkup()
        backbutton_22 = types.InlineKeyboardButton(text="�����", callback_data="Main_phone")
        keyboard_22.add(backbutton_22)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="������\n+7 964 313-34-61\n9:00-17:00",
                              reply_markup=keyboard_22)
        # bot.send_message(chat_id=call.message.chat.id, text="2")

    elif call.data == 'MVD':
        keyboard_23 = types.InlineKeyboardMarkup()
        backbutton_23 = types.InlineKeyboardButton(text="�����", callback_data="Main_phone")
        keyboard_23.add(backbutton_23)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="���������� ������ ����������\n89267023941\n\n����� ����� ������� 102 ��� 112\n",
                              reply_markup=keyboard_23)
        # bot.send_message(chat_id=call.message.chat.id, text="2")

    elif call.data == 'Fire':
        keyboard_24 = types.InlineKeyboardMarkup()
        backbutton_24 = types.InlineKeyboardButton(text="�����", callback_data="Main_phone")
        keyboard_24.add(backbutton_24)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="����� ����� �������� ������ � ��� 101 ��� 112",
                              reply_markup=keyboard_24)
        # bot.send_message(chat_id=call.message.chat.id, text="2")

    elif call.data == 'Helth':
        keyboard_25 = types.InlineKeyboardMarkup()
        backbutton_25 = types.InlineKeyboardButton(text="�����", callback_data="Main_phone")
        keyboard_25.add(backbutton_25)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="����� ����� �������� ������ � ��� 103 ��� 112",
                              reply_markup=keyboard_25)
        # bot.send_message(chat_id=call.message.chat.id, text="2")

    elif call.data == 'Snow':
        keyboard_26 = types.InlineKeyboardMarkup()
        backbutton_26 = types.InlineKeyboardButton(text="�����", callback_data="Main_phone")
        keyboard_26.add(backbutton_26)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="89255079933\n�������, Telegram, WhatsAp",
                              reply_markup=keyboard_26)
        # bot.send_message(chat_id=call.message.chat.id, text="2")

    elif call.data == 'plumber':
        keyboard_27 = types.InlineKeyboardMarkup()
        backbutton_27 = types.InlineKeyboardButton(text="�����", callback_data="Main_phone")
        keyboard_27.add(backbutton_27)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="3",
                              reply_markup=keyboard_27)
        # bot.send_message(chat_id=call.message.chat.id, text="3")

    elif call.data == 'street_cleaner':
        keyboard_28 = types.InlineKeyboardMarkup()
        backbutton_28 = types.InlineKeyboardButton(text="�����", callback_data="Main_phone")
        keyboard_28.add(backbutton_28)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="�����",
                              reply_markup=keyboard_28)
        # bot.send_message(chat_id=call.message.chat.id, text="4")

    elif call.data == 'carpenter':
        keyboard_29 = types.InlineKeyboardMarkup()
        backbutton_29 = types.InlineKeyboardButton(text="�����", callback_data="Main_phone")
        keyboard_29.add(backbutton_29)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="5",
                              reply_markup=keyboard_29)
        # bot.send_message(chat_id=call.message.chat.id, text="5")

    # �������� ������

    elif call.data == 'uk_local':  # ����� �������� ��������� ��
        keyboard_31 = types.InlineKeyboardMarkup()
        backbutton_31 = types.InlineKeyboardButton(text="�����", callback_data="Main_locations")
        keyboard_31.add(backbutton_31)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="�����: �. ��������� �������\n��. ����������, �.1\n(����� � ������� ������ WildBerries)\n\n����� ������: �����������-������� 9:00-18:00",
                              reply_markup=keyboard_31)
        # bot.send_message(chat_id=call.message.chat.id, text="�����-�� ����")

    elif call.data == 'uk_main':  # ����� � ����� ������ �� - ��������� �����
        keyboard_32 = types.InlineKeyboardMarkup()
        backbutton_32 = types.InlineKeyboardButton(text="�����", callback_data="Main_locations")
        keyboard_32.add(backbutton_32)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="��?! ��������?! �� ��� ���������� ����� ������)\n�� ���� �� ��� ������...\n\n����������� �����: 141008, ��, ��, ��������� ����� ������, ��. ���������, �. 20\n\n����� ������: ����������� - ������� � 8:00 �� 17:00\n\n����: � 12:00 �� 13:00\n\n��������: ������� � �����������\n\n�������: 8(495)125-27-04\n\nEmail: info@nd-msk.ru\n\n�� ��� ��� ���\nhttps://nd-msk.ru/contact/",
                              reply_markup=keyboard_32)
        # bot.send_message(chat_id=call.message.chat.id, text="��?! ��������?! �� ��� ���������� ����� ������)")

    elif call.data == 'austerliz':  # ����������
        keyboard_33 = types.InlineKeyboardMarkup()
        backbutton_33 = types.InlineKeyboardButton(text="�����", callback_data="Main_locations")
        keyboard_33.add(backbutton_33)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="�����: �. ������, ��. ���������, �.2, �.1\n\n����� ������ �����:��-�� 9:00-18-00, �� 9-00 - 16:45, ��. 9:00 - 15:00 ��� ��������\n\n�������: 8(499)444-01-00; 8(496)245-15-99\n\n����: https://xn--90aijkdmaud0d.xn--p1ai/\n\n�������� �����: office@mosobleirc.ru\n��� ������ ��������� �� ����������� � ���������� ���",
                              reply_markup=keyboard_33)
    # bot.send_message(chat_id=call.message.chat.id, text="���-�� �� �������-��")

    elif call.data == 'comp_center':  # ��� ��
        keyboard_34 = types.InlineKeyboardMarkup()
        backbutton_34 = types.InlineKeyboardButton(text="�����", callback_data="Main_locations")
        keyboard_34.add(backbutton_34)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="��� ��������� �����\n\n����: https://rkcm.ru/\n\n�.������, ��.���������, �.40, ����.1\n\n����� ������: ����������� - ������� � 9:30 �� 17:30, ������� � 8:00 �� 13:00.\n\n���.: 8(495)181-18-78\n\n����������� �����: info@rkcm.ru",
                              reply_markup=keyboard_34)
    # bot.send_message(chat_id=call.message.chat.id, text="��� ����")
    elif call.data == 'energety_pidorasy':  # �������������
        keyboard_35 = types.InlineKeyboardMarkup()
        backbutton_35 = types.InlineKeyboardButton(text="�����", callback_data="Main_locations")
        keyboard_35.add(backbutton_35)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="������ �� ���� ������������� ������������, ����������� ������ ����������������� ��������� �������,\n\n�����: ������, ��. ��������, �.1,\n\n�������: +7(495)586-70-07\n\n������� ��������� ������: +7(495)933-54-45\n\n����: http://www.mosoblenergo.ru/?yandex-source=desktop-maps\n\nE-mail: ��� �����, � ��������� � �� ������ � ���������",
                              reply_markup=keyboard_35)
    # bot.send_message(chat_id=call.message.chat.id, text="���������")

    elif call.data == 'Administration':  # �������������
        keyboard_351 = types.InlineKeyboardMarkup()
        backbutton_351 = types.InlineKeyboardButton(text="�����", callback_data="Main_locations")
        keyboard_351.add(backbutton_351)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="��� ���������� ������ ������: ���� �������� ��������\n\n����� �������������: �. ������, ��������������� ��-�, �. 36/7\n\n�������: 8(495)581-13-83\n\n����: http:https://mytyshi.ru/\n\nE-mail: inform@mytyshi.ru\n\n\n",
                              reply_markup=keyboard_351)
    # bot.send_message(chat_id=call.message.chat.id, text="���������")

    elif call.data == 'Powernet':  # ���������
        keyboard_36 = types.InlineKeyboardMarkup()
        backbutton_36 = types.InlineKeyboardButton(text="�����", callback_data="Main_locations")
        keyboard_36.add(backbutton_36)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="�� ������������ ���������\n\n141002, ���������� �������, �. ������, ��. ���������, �.20, ���� �17\n\n������ ������ �����������:� ������������ �� �������: � 08.00 �� 16.45, ���� � 12.00 � 12.45.\n\n������� �������������: 8(495)583-55-92, 8(495)583-97-20, 8(495)586-13-21, 8(495)775-55-92 ������� ������ ������: 8(495)583-07-00\n\nwww.m-teploset.ru",
                              reply_markup=keyboard_36)

    elif call.data == 'Watertube':  # ���������
        keyboard_37 = types.InlineKeyboardMarkup()
        backbutton_37 = types.InlineKeyboardButton(text="�����", callback_data="Main_locations")
        keyboard_37.add(backbutton_37)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="�����: �. ������, ��. ˸����, �. 20, ����. 3\n\n����� ������: �����������-�������: 8:00 � 16:45\n\n��� �������� �� ����\n\n�������, �����������: ��������\n\n��������:\n�������������� �������: 8(800)770-78-99\n\nE-mail: ab_otd@mvdk.ru\n\nhttp://www.vodokanalmytischi.ru/",
                              reply_markup=keyboard_37)

    elif call.data == 'MyDocs':  # ��� ���������
        keyboard_38 = types.InlineKeyboardMarkup()
        backbutton_38 = types.InlineKeyboardButton(text="�����", callback_data="Main_locations")
        keyboard_38.add(backbutton_38)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="���� �������� �.�. ������, ��� �����������, ��. ���������� �. 4� \n��-�� 09:00 - 18:00\n�� 09:00 - 16:45\n������� - 13:00 - 13:45\n�� � �� - �������� ���\n\n������ ����� ������ � ������ � �� �4Daily�\n\n��-�� 08:00 - 20:00\n\nhttp://mfcmmr.ru.",
                              reply_markup=keyboard_38)

    elif call.data == 'BTI':  # ���
        keyboard_39 = types.InlineKeyboardMarkup()
        backbutton_39 = types.InlineKeyboardButton(text="�����", callback_data="Main_locations")
        keyboard_39.add(backbutton_39)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="����� �. ������, ��. �����������, ���. 7\n\n������� 8(498)568-88-88 (���. 2105)\n\n����������� �����: mytischi@mobti.ru\n\n����� ������:\n��-��:9:00-18:00\n��:9:00-16:45\n��:9:00-13.00\n\nhttps://mobti.ru/filialy/mytishchinskiy-filial/",
                              reply_markup=keyboard_39)

    # ����������

    elif call.data == 'Adress':  # ������ ����� ����
        keyboard_41 = types.InlineKeyboardMarkup()
        backbutton_41 = types.InlineKeyboardButton(text="�����", callback_data="instructions")
        keyboard_41.add(backbutton_41)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="���������� �������,\n��������� ����� ������,\n������ ��������� �������,\n���������� �����, ��� 5\n�������� ������:141033\n����������: 55.969250, 37.734120\n����������� ����� ����: 50:12:0090234:1214\n\n��� ����������� ��������� �������� ����� � 141033\n������������� �����, 3\n��-��� 8:00-20:00\n�� 9:00-18:00",
                              reply_markup=keyboard_41)
        #  bot.send_message(chat_id=call.message.chat.id, text="�������")

    elif call.data == 'Plan':  # ������ ����� ����
        keyboard_42 = types.InlineKeyboardMarkup()
        backbutton_42 = types.InlineKeyboardButton(text="�����", callback_data="instructions")
        keyboard_42.add(backbutton_42)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="������ ������ �������� ��������, ����� ��������� �������� � ���� �� �������, � ���� ����������).\n\n� ������ �������, ���������� ������, �� ������� ������� ��������. ���� ������ ������� (�����, �����, �������), �� ���������� ��������� �� ���������, ��������� � ���������������� �������.\n\n� ������ ������ ����� ����� ���������� � ��� ��� � �������, �� � ������ ������ ����� �� �������� ����� � �������� ����� - ����� �� ��� �� ����� � ���� �������������:).\n\n����� ����, ������������� ������������� � �������� � ����� �� ������ ���������, ��� ��� �� ����� �������� �� ����������� �����.\n\n� ��������� ��������� (� ���, ��� �������, �������� ��������� � ��������) ���������� ������, � ���� ���� ���������: � ���� ��������������� �� ��� � ���� ��������������� ������. ������ ���� ��������� � ��������, �� ���� �������, �� ��, ��� �� �������� ����������-������, ������, ������������� ����-����������� ������������, � �� ���� �� ��� ���������������. � ������ ������ ���������� ���� �������������� ��������� ��������, ���� ���������� � ���������������� ������, ��������, � ������������, ��������������� ��.\n\n����� ��������, ��� �������� ��������� �� �������� 5 ���, ������� ����� ����� ����������� ���������� � �����������. ������, ���������� ������� ���� ��������� � �������� ������ �� ���������������.\n\n� ������ ��, ���� ��� ���� ��������������� ��, �� ���������� ���������� � ���. ����, ��� ���� ������� ����,�������� �� �������, �� ���������� � ������� ����� �� ������ ��������, ��������� ������ ����� ���������� ��� �����.\n\n��������� ��� ����� ��� ����������� ��������",
                              #
                              reply_markup=keyboard_42)
        #  bot.send_message(chat_id=call.message.chat.id, text="�������")

    elif call.data == 'cad_namber':
        keyboard_43 = types.InlineKeyboardMarkup()
        backbutton_43 = types.InlineKeyboardButton(text="�����", callback_data="instructions")
        keyboard_43.add(backbutton_43)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="����������� ����� ����: 50:12:0090234:1214\n\n��� ��������� ������������ ������ ����� �������� ���������� ��������� �� ������� ����� ���������� 8(800)100-34-34, ���������� 1 ��� ������ ����� ������ ��������) � �������� ���������. ��� ��� � ���������� ������� ����� �� ������ ��������� �������� �� ����� ����� �/��� ���� ����� ���������� ����������, ���� �������� ����� ����� �� �����, ������� ���������� ��������). ��� ���������� ������������� ���� ������ ���������� �� ����������. ����� ������ ������ �������� ����. ��������, ����������� ������ ����� ����������� ����������:\n\n���������� � ����������� ������������� (��������� �������� � ���)\n\n��������\n\n������\n\n���� (� ���� � ����������� ��������, �� �����, ���������� � ����������� � ��������. ���� ���, �� � ��� �������)\n\n���� ����� �������� (2 ��)\n\n������� ������� (�������� - ������ �������� ��� �������� ������������� �������)\n\n���������� (��� ���, � ���� ������� ��������� �� 2018 ����, ������ �� �� ������)\n\n������ �� ������ (��� ���������)\n\n����������� 2 ���\n\n�������� ��������, ��� �� ��� ��� ��������� ���������. ���������, ������� ������� - ��� �� ������ ����� ������, 4�. ����� ������ ��-�� 08:00 � 11:00; 11:30 � 16:00; 16:30 � 20:00.\n��� �� �������� �� ��� �� ������ ����� ����, �32/2 (�� 4Daily), ������ �� ���� �� ���������. ����� ������ ��-�� 08:00 � 11:00; 11:30 � 16:00; 16:30 � 20:00.\n��� � �������� �� ��������� ��������� ������� ����! \n\n������� ���������� ������� ���� https://rosreestor.com/ - �� �� �� ������ ������, �� ������� ���������� �� ���������.",
                              reply_markup=keyboard_43)
        #  bot.send_message(chat_id=call.message.chat.id, text="�������")

    elif call.data == 'payment':
        keyboard_44 = types.InlineKeyboardMarkup()
        backbutton_44 = types.InlineKeyboardButton(text="�����", callback_data="instructions")
        keyboard_44.add(backbutton_44)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="���������� �������� ���������� (���)\n\n������ ��� �������� 3 ���������:\n\n1.��������� �� ���������� �������� ����������� ������ � �����\n\n2. ��������� ��� ��: �������� ��� ���������, ����� �������������, �������: \n   ������� ����������� ������ �����\n  ������ �������� ����\n  ������ ������� ����\n   ������ ������� ����\n   ��������� ����\n   ����������� ������� ��������������, ���� � ��������� ����\n3. �������������� �� ������������ ",
                              reply_markup=keyboard_44)
        #  bot.send_message(chat_id=call.message.chat.id, text="������������")

    elif call.data == 'reg_counter':
        keyboard_45 = types.InlineKeyboardMarkup()
        backbutton_45 = types.InlineKeyboardButton(text="�����", callback_data="instructions")
        keyboard_45.add(backbutton_45)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="��������\n\n\n�� ������ ������, ��������� ���������� ������ ��� ����.\n\n���� ������ - � 10 �� 30 ����� ������\n\n\n\n��������� ������������� ��������� �������������.\n��������� �� ����� ����������� � ������� ��������������� ������� �������.\n\n�������� ��������� ����� ����� ��������: �� ��������, ����� ���������� ��� ������ �������.\n\n��� �������� ��������� ����������:\n\n������������ ������� ���� - ��������� �� �������� ���������. � ������, ���� �� ������ - ����� ����������� �������� �� �������� ���������� ������\n\n�������� ���������� � ���������������� � �� ������� ���� ���...\n\n���������� �� ������ �������� ����������� ���...\n\n��������� �� ������ � ������� ����.\n\n���� ���������� ������������� �������, �� ���������� ���������� � �� ��� � ������������� �� ������ ��������:\n\n8(916)707-77-81\n\n���������",
                              reply_markup=keyboard_45)
        #  bot.send_message(chat_id=call.message.chat.id, text="������������")

    elif call.data == 'IT':
        keyboard_46 = types.InlineKeyboardMarkup()
        backbutton_46 = types.InlineKeyboardButton(text="�����", callback_data="instructions")
        keyboard_46.add(backbutton_46)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="�� ������������������� �����, �� ���� ������ ������������ ��� ��������� �������� � ����������� ���� �����������.\n\n\n1.�������\n\n8(495)780-72-62 �������������\n\n����: https://www.opticom.net/\n\n������������ IPtv\n\n\n2.�������\n\n8(498)500-12-22\n\n����: https://indikom.ru/\n\n������������ IPtv\n\n\n3.��������� �����������\n\n",
                              reply_markup=keyboard_46)
        #  bot.send_message(chat_id=call.message.chat.id, text="������ ������")

    elif call.data == 'heat':
        keyboard_47 = types.InlineKeyboardMarkup()
        backbutton_47 = types.InlineKeyboardButton(text="�����", callback_data="instructions")
        keyboard_47.add(backbutton_47)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="������������ ������ ���������� � ������������� �� ������������ ���� �.�. ������. �� ����� *�������* �� ����� *����������*. ������ �� ������������. ������, ����� ������������ ���������, ����� �������������� ����������� �� ���������� 5 ���� ����� 8 ��������.\n\n ������� ����� �������� ��������� �������� �������: ������� ����, ��������, �����. ����� ����� ���� � ���������� - �����������.\n\n� ������ ����������� ���� ���������, ������� ��������� � ��������-1 � ���� 7� (����� �� ��������� �����). ����������� ������� ��� � ����� ������ �� ��������� �������� ��������� ����������� � �������� � ���������� ������� ����\n\n!� ������ ������ ������������ �������� ���������� ������� ���� ��� ��������������� ��������� (�� ������ �� ��, ��� ��� �����, ��������� - �� �����).\n\n� ��������������� �����, ���������� ��������������� ��������� �������� (���) �������������� ���������� ��� ���������� ��� ��������� ����������� ��������� ������� ���� +12��, � �������������� ��������� ��� ���������� ��� ��������� ����������� ��������� ������� ���� +10��.����� ������������� ������ ���������� ��� �������� ����� � ���������� �������� ������� �� ���������.\n\n!� ����� ���� ������ ����� �������!\n\n���� � ������������ ����� � ��� �������� �������, �� ����������, ������ ��� ��������� ������ � �� ��� ��� �������� ������������:\n\n1.���������, ������� �� �������� �����. ���� ���, �� ����� � ��� - ����������, ���-�� ��� ������� � ������ ��������.\n\n2.���� ����� �������, �� ���������, �� ������� �� �������-��������� (��� ������� �� �����������). ����������� ��������� ��� �� ������������ �������� ��� ����� �����. � ������� ������ ������ ������ ��������� �����.\n\n3.���� ����� ��� � �� �����, �� ���������� �� �������� ������� (�������� ������ �������)\n\n4. ���� �������� ���� �� �������, �� � ������� ����� ��������� ������ � ��, � ������ - ������� � ���",
                              reply_markup=keyboard_47)
        #  bot.send_message(chat_id=call.message.chat.id, text="��� ������ �����")

    elif call.data == 'Silence':
        keyboard_48 = types.InlineKeyboardMarkup()
        backbutton_48 = types.InlineKeyboardButton(text="�����", callback_data="instructions")
        keyboard_48.add(backbutton_48)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="���� ���, ��� ������������ ����� ������, �� ������ ����� ���������, ��� ����� � ���� ������. ����� ������ �������� �������. ���������� - ��� �����. ������, ��� ������ ������� - ������������ ��� ��� �������. �������, ����� �������� ���, ��� ����� ������ ������ ������� ������������ �������. � ���������, ����� � ��������� - ��� �� ���� ��� ������ ����� ������ ������. \n\n� ��������, ���� � ����-�� ������ ���� ��� �������� �������������� ������� ������ ����, �� ������ ����� ������� � ���������. �� ��������, �� ��������, � ��������� - ������ ������ � ��������� � ����� ����� ����� ����������.\n\n����� ����, �� ����� ������� ��-�� 1-2 ������, � �������� �����, ��������, � ���������.\n\n(��, �� ���� ������� ����� ������� ���� ����� ��� ������ ������� - �� �� �������:) )\n\n����� ����, �������� ��������, ��� � ����� ��� ������ ������ ��� - ������� � ������������ ��� �� ������).\n\n����� ���� ���� �� ������ ����� ���������� ������� � 16/2014-03 ��� ����������� ������ � ����� ������� �� ���������� ���������� ������� � �����������, ���������� �������� ���������� ������� �67/2015-03, �70/2016-03, �159/2016-03, �193/2017-03, �134/2018-03):\n\n1.He ����������� ������������� �������������������� ��������� � ��������� �������������, � ��� ����� ������������� �� ������������ ���������, � ������ � 21 ���� 00 ����� �� 08 ����� 00 �����, � ����� � 13 ����� 00 ����� �� 15 ����� 00 ����� � ������� ���, � 22 ����� 00 ����� �� 10 ����� 00 �����, � ����� � 13 ����� 00 ����� �� 15 ����� 00 ����� � �������� ���.\n\n 2. �� ����������� �����, �����, �����, ���� �� ����������� ������������, ���������� ��������, ������������, �����������-����������� � ���� ����� ����� � ����������� ������������ ������� � ����������� ���������, ��������� ��������� ������ � ����� �������, � ������ � 21 ���� 00 ����� �� 08 ����� 00 ����� � ������� ���, � 22 ����� 00 ����� �� 10 ����� 00 ����� � �������� ���.\n\n4. �� ��������� ����� ������� �� ��� ���������� ���������������� ���� �� ����������� ���� �� ����������� ���������� ��������������,��������������, ��������� ����� � ����� ��������� � ���� ��������������� ���� ��� ��������� ����� � ������� ���������, �� ������������� �� ����� ����� ������� ������������� ������������� ��������� � ���� ��������������� ����, ��������� ��������� ������ � ����� �������, � ������ � 19 ����� 00 ����� �� 09 ����� 00 �����, � ����� � 13 ����� 00 ����� �� 15 ����� 00 ����� � ������� ���, � 19 ����� 00 ����� �� 10 ����� 00 �����, � ����� � 13 ����� 00 ����� �� 15 ����� 00 ����� � �������, ������������� � ����������� � ������������� ����������� m����������������� ��������� ����������� ���.\n\n������: https://mosreg.ru/download/document/1000167",
                              reply_markup=keyboard_48)
        #  bot.send_message(chat_id=call.message.chat.id, text="��� ������ �����")

    elif call.data == 'HomeLock':
        keyboard_49 = types.InlineKeyboardMarkup()
        backbutton_49 = types.InlineKeyboardButton(text="�����", callback_data="instructions")
        keyboard_49.add(backbutton_49)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="���������� �� ������������� ����� �����������.\n\n����� ����������, ������� �������� �� �������� �� ������ ����:\n�������\n+7909957-87-60\n\n���� �� ��������� �� ������ ������ ����������� � �������\n\n��������� ���������� ���� ������� �����",
                              reply_markup=keyboard_49)
        #  bot.send_message(chat_id=call.message.chat.id, text="������������")
    elif call.data == 'Links':
        keyboard_410 = types.InlineKeyboardMarkup()
        backbutton_410 = types.InlineKeyboardButton(text="�����", callback_data="instructions")
        keyboard_410.add(backbutton_410)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="���� ������������� ���������� �������: https://mosreg.ru/\n\n��������: https://dobrodel.mosreg.ru/\n����� ���� ��������� ������:\n������: https://play.google.com/store/apps/details?id=ru.mosreg.ekjp&hl=ru&gl=US&pli=1\n����: https://apps.apple.com/ru/app/%D0%B4%D0%BE%D0%B1%D1%80%D0%BE%D0%B4%D0%B5%D0%BB/id1021212577",
                              reply_markup=keyboard_410)
        #  bot.send_message(chat_id=call.message.chat.id, text="������������")
    elif call.data == 'Capital':
        keyboard_411 = types.InlineKeyboardMarkup()
        backbutton_411 = types.InlineKeyboardButton(text="�����", callback_data="instructions")
        keyboard_411.add(backbutton_411)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="�������� ������������� ������������� ���������� ������� 1452/45 �� 27.12.2021 ��� ��� ����� � ��������� ������������ �������, ���������������� �� ������ 2044�.\n\n������ �� ��������: https://mgkh.mosreg.ru/download/document/11490501\n\n�� ��� ���: ������ 21594, �������� 369\n\n������ �� ���� ��������� ����������: https://mosreg.ru/seychas-v-rabote/proekty/mkd/mkd-renovation",
                              reply_markup=keyboard_411)
        #  bot.send_message(chat_id=call.message.chat.id, text="������������")

    elif call.data == 'Children':
        keyboard_412 = types.InlineKeyboardMarkup()
        backbutton_412 = types.InlineKeyboardButton(text="�����", callback_data="instructions")
        keyboard_412.add(backbutton_412)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="��������� ������� ���: �������� �����, 3�\n\n������� ����� 1-2 �����: ����� ��������� ��� 10\n\n������� ����� 3-11 �����: ����� ���������� ��� 7",
                              reply_markup=keyboard_412)
        #  bot.send_message(chat_id=call.message.chat.id, text="������������")

    elif call.data == 'Bus':
        keyboard_413 = types.InlineKeyboardMarkup()
        backbutton_413 = types.InlineKeyboardButton(text="�����", callback_data="instructions")
        keyboard_413.add(backbutton_413)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="��������� � ���� ��������� ��������� �� ���������� ���������� � ��������� ������ �� ��� ����������� �� ��� �����������: � ������� �. ���������� �� ������������� ����� (��������� ��������� ����) � � ������� �. ������ �� ������������ ���� (��������� ����������� ����������).\n\n� ������� �.���������� (�� ���/� ���) �� ��������� ��������� ����:\n581 � 6:39 �� 21:09 ������ 20 �����/� 7:20 �� 22:10\n166 � 5:21 �� 22:31 ������ 15 �����/� 5:50 �� 23:20\n314� � 6:30 �� 23:00 ������ 10 �����/� 6:20 �� 00:30 ������ 20 �����\n509 � 6:23 �� 20:33/�7:10 �� 21:20\n�� ��������� ����������� ����������\n502 � 5:55 �� 22:15 ������ 15 �����/� 06:10 �� 22:10 ������ 15 �����\n\n�� ��������� ����������� ���������� �� �/� ������� ������:\n22 � 5:31 �� 21:26 ������ 10 �����/� 5:30 �� 21:30 ������ 10 �����\n23 9:00, 11:55, 16:15, 17:50, 20:00, 21:49/ � 5:15 �� 21:35 ������ 45-120 �����\n26 9:00, 11:55, 16:15, 17:50, 20:00, 21:49/� 5:35 �� 23:10 ������ 15-35 �����\n31 9:09, 12:59, 16:59, 20:34/6:15, 9:55, 13:55, 17:45\n314 � 6:55 �� 01:05 ������ 20 �����/� 5:20 �� 23:25 ������ 20 �����",
                              reply_markup=keyboard_413)
        #  bot.send_message(chat_id=call.message.chat.id, text="������������")

    elif call.data == 'Hospital':
        keyboard_414 = types.InlineKeyboardMarkup()
        backbutton_414 = types.InlineKeyboardButton(text="�����", callback_data="instructions")
        keyboard_414.add(backbutton_414)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="�������������� �� ��������� � �������� ��������\n�����: ��������� �����, 2\n\n����� ������������ ������� � ������ ����� ��������\n�����: �������� �����, 5",
                              reply_markup=keyboard_414)
        #  bot.send_message(chat_id=call.message.chat.id, text="������������")

    elif call.data == 'around':
        keyboard_414 = types.InlineKeyboardMarkup()
        backbutton_414 = types.InlineKeyboardButton(text="�����", callback_data="mainmenu")
        keyboard_414.add(backbutton_414)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="�������� ��������������\n���������: ���������� 1�\n������: ���������� 1\n������������: ���������� 1\n������ ����: ���������� 1\n������� ��������������: ���������� 1\n����������: ���������� 1\n\n���\n������ �������, ���������� ������: ���������� 1\n������ ������: ���������� 3 � ����� �� ������� �.1\n\n������ ������ �������\nWilberries: ���������� 1, �������� 5\nOzon: �������� 5\n\n���������\n��������� 1�, ������� ��������\n��������� 20�, ������� �����������",
                              reply_markup=keyboard_414)
        #  bot.send_message(chat_id=call.message.chat.id, text="������������")


bot.polling(none_stop=True)

"""
� ����� ������� �������. ������ ��� �� �������� �� ������ ��� ������ �����, �� ��������� �� �����, ��� ����������
���� ������ ������ ������, �� ��������� ������ �� ����, ��� ���� � ������. ����� � ����� chat_id  �.�. ����� ����� � ���
������ ����� ������ ���������� ������ �� �� �����, ���� ������, ����� ��� �������
�� ��� ����� �� � ���"""

#  Copyright (c) ChernV (@otter18), 2021.
