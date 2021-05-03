import telebot
from informirovanie import clicked
bot = telebot.TeleBot('1785994865:AAEEfMmp51g_JjVS2w10Rr0_OVf1GjALwXw')
from telebot import types
name = ''
surname = ''
age = 0
tema = ""
dol = ""
zvan = ""
UFIO = ""
Ndol = ""
group = ""
NZvan = ""
NFio = ""
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    def start(message):
        if message.text == '/info':
            bot.send_message(message.from_user.id, "Какая должность у подписавшего?")
            bot.register_next_step_handler(message, get_dol)
        else:
            bot.send_message(message.from_user.id, 'Напиши /info')
    def get_dol(message):
        global dol
        dol = message.text
        bot.send_message(message.from_user.id, 'Какое звание у подписавшего?')
        bot.register_next_step_handler(message, get_zvan)
    def get_zvan(message):
        global zvan
        zvan = message.text
        bot.send_message(message.from_user.id, 'Его Фамилия И.О.')
        bot.register_next_step_handler(message, get_UFIO)
    def get_UFIO(message):
        global UFIO
        UFIO = message.text
        bot.send_message(message.from_user.id, 'Какая у Вас должность?')
        bot.register_next_step_handler(message, get_Ndol)
    def get_Ndol(message):
        global Ndol
        Ndol = message.text
        bot.send_message(message.from_user.id, 'Номер группы:')
        bot.register_next_step_handler(message, get_group)
    def get_group(message):
        global group
        group = message.text
        bot.send_message(message.from_user.id, 'Ваше звание?')
        bot.register_next_step_handler(message, get_NZvan)
    def get_NZvan(message):
        global NZvan
        NZvan = message.text
        bot.send_message(message.from_user.id, 'Ваша Фамилия И.О.')
        bot.register_next_step_handler(message, get_NFio)
    def get_NFio(message):
        global NFio
        NFio = message.text
        keyboard = types.InlineKeyboardMarkup()
        key_oven = types.InlineKeyboardButton(text='Новости Орла и Орловской области', callback_data='1')
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Военно-политическая обстановка в мире', callback_data='2')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Новости культуры и спорта', callback_data='3')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(
            text='Актуальные вопросы военной службы, новинки российской военной техники и вооружения',
            callback_data='4')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Социально-экономическая жизнь общества', callback_data='5')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Новости информационных технологий', callback_data='6')
        keyboard.add(key_deva)
        bot.send_message(message.from_user.id, text='Выбери тему для информирования', reply_markup=keyboard)
    start(message)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global tema
    if call.data == "1":
        bot.send_message(call.message.chat.id, '1')
        tema = "Новости Орла и Орловской области"
    if call.data == "2":
        bot.send_message(call.message.chat.id, '2')
        tema = 'Военно-политическая обстановка в мире'
    if call.data == "3":
        bot.send_message(call.message.chat.id, '3')
        tema = 'Новости культуры и спорта'
    if call.data == "4":
        bot.send_message(call.message.chat.id, '4')
        tema = 'Актуальные вопросы военной службы, новинки российской военной техники и вооружения'
    if call.data == "5":
        bot.send_message(call.message.chat.id, '5')
        tema = 'Социально-экономическая жизнь общества'
    if call.data == "6":
        bot.send_message(call.message.chat.id, '6')
        tema = 'Новости информационных технологий'
    clicked( tema, dol, zvan, UFIO, Ndol, group, NZvan, NFio)
    doc = open("информирование.docx", 'rb')
    bot.send_message(call.message.chat.id, '6')
    bot.send_document(call.message.chat.id, doc)

bot.polling(none_stop=True, interval=0)