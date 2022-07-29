#!venv/bin/python
import logging
import aiogram
import asyncio
import aiohttp
import json
from tokenbot import tokenbot
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# Объект бота
bot = Bot(token=tokenbot, parse_mode=types.ParseMode.HTML)
#bot = Bot(token=' ', parse_mode=types.ParseMode.HTML)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

#inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
#inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

#@dp.message_handler(commands='test')
#async def process_command_1(message: types.Message):
#    await message.answer("Первая инлайн кнопка", reply_markup = inline_kb1)

#@dp.callback_query_handler(lambda c: c.data == 'button1')
#async def process_callback_button1(callback_query: types.CallbackQuery):
#    await bot.answer_callback_query(callback_query.id)
#    json_callback_query = json.loads(f'{callback_query}')
#    dict_callback_query = json_callback_query["message"]
#    #chat_callback_query = dict_callback_query["chat"]
#    #await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')
#    await bot.send_message(chat_callback_query["id"], f'Тест выполнен')




#ВЫШЕ КОД КОТОРЫЙ ТЕСТИРУЮ
button_help = InlineKeyboardButton('Помощь', callback_data='help')
button_mail = InlineKeyboardButton('Почта', callback_data='mail')
button_contact = InlineKeyboardButton('Контакты', callback_data='contact')
button_server = InlineKeyboardButton('Ссылки на сервера', callback_data='server')
button_helpmob = InlineKeyboardButton('Скачать приложения', callback_data='helpmob')
button_join = InlineKeyboardButton('ID CHAT', callback_data='join')
button_myid = InlineKeyboardButton('ID USER', callback_data='myid')
button_task = InlineKeyboardButton('ТЕХ.ПОДДЕРЖКА', callback_data='task')
group_button_start = InlineKeyboardMarkup().row(button_help, button_mail).row(button_contact, button_server).row(button_helpmob, button_task).row(button_join, button_myid)

@dp.callback_query_handler(lambda c: c.data == 'test')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    json_callback_query = json.loads(f'{callback_query}')
    dict_callback_query = json_callback_query["message"]
    chat_callback_query = dict_callback_query["chat"]
    await bot.send_message(chat_callback_query["id"], f"Пустой запрос")

@dp.callback_query_handler(lambda c: c.data == 'task')
async def process_callback_button1(callback_query: types.CallbackQuery):
    #await bot.answer_callback_query(callback_query.id)
    json_callback_query = json.loads(f'{callback_query}')
    dict_callback_query = json_callback_query["message"]
    chat_callback_query = dict_callback_query["chat"]
    await bot.answer_callback_query(callback_query.id, text=f'Для обращения в техническую службу, напишите:\n/task Описание сути проблемы/вопроса\nАвтоматические будет создана заявка в CRM технической службе\nПосле получения/решения с вами свяжуться', show_alert=True)
    #await bot.answer_callback_query(chat_callback_query["id"], text = 'Для обращения в техническую службу, напишите:\n /task Описание сути проблемы/вопроса\n', show_alert=True)

@dp.callback_query_handler(lambda c: c.data == 'myid')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    json_callback_query = json.loads(f'{callback_query}')
    dict_callback_query = json_callback_query["message"]
    chat_callback_query = dict_callback_query["chat"]
    id_chat = chat_callback_query["id"]
    await bot.send_message(chat_callback_query["id"], f"Ваш id chat: {id_chat}; Ваш id: {callback_query.from_user.id}\n"
    "Главное меню /start\n")

@dp.callback_query_handler(lambda c: c.data == 'join')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    json_callback_query = json.loads(f'{callback_query}')
    dict_callback_query = json_callback_query["message"]
    chat_callback_query = dict_callback_query["chat"]
    id_chat = chat_callback_query["id"]
    await bot.send_message(chat_callback_query["id"], f"Ваш id chat: {id_chat}; Ваш id: {callback_query.from_user.id}\n"
    "Главное меню /start\n")

@dp.callback_query_handler(lambda c: c.data == 'helpmob')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    json_callback_query = json.loads(f'{callback_query}')
    dict_callback_query = json_callback_query["message"]
    chat_callback_query = dict_callback_query["chat"]
    await bot.send_message(chat_callback_query["id"], f"Скачать мобильные приложения для GSH24:\n"
    "ANDROID - https://play.google.com/store/apps/details?id=com.gpsserver.gpsservermobile\n"
    "IOS - https://apps.apple.com/us/app/gps-server-mobile-tracking/id1174827849?ls=1\n"
    "Как правильно авторизоваться на сервере GSH24\n"
    "https://youtu.be/TjchCJcyp6k\n"
    "Скачать мобильные приложения для WIALON:\n"
    "ANDROID - https://play.google.com/store/apps/details?id=com.gurtam.wialon_client&hl=ru\n"
    "IOS - https://apps.apple.com/ru/app/wialon/id960699792\n"
    "Скачать мобильное приложение для АВТОФОН:\n"
    "ANDROID - https://play.google.com/store/apps/details?id=ru.autofon\n"
    "IOS - https://apps.apple.com/ru/app/avtofon-ksa/id971258255\n"
    "Скачать мобильное приложение для CAR-ONLINE:"
    "ANDROID - https://play.google.com/store/apps/details?id=ru.caronline.app"
    "IOS - https://apps.apple.com/ru/app/car-online/id1162687937"
    "Для справки введите команду /help\n")

@dp.callback_query_handler(lambda c: c.data == 'server')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    json_callback_query = json.loads(f'{callback_query}')
    dict_callback_query = json_callback_query["message"]
    chat_callback_query = dict_callback_query["chat"]
    await bot.send_message(chat_callback_query["id"], f"WIALON - https://hosting.wialon.com\n"
    "Справка по работе с сервером WIALON:\n"
    "https://help.wialon.com/help/wialon-hosting/ru/user-guide\n"
    "GSH24 (РЕД) - https://gsh24.net/id28\n"
    "Спрака по работе с сервером GSH24:\n"
    "https://docs.gps-server.net\n"
    "АВТОФОН - https://control.autofon.ru\n"
    "Спрака по работе с сервером АВТОФОН:\n"
    "http://www.autofon.ru/documentation\n"
    "CAR-ONLINE - https://group.car-online.pro/login\n"
    "Для справки введите команду /help\n")

@dp.callback_query_handler(lambda c: c.data == 'contact')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    json_callback_query = json.loads(f'{callback_query}')
    dict_callback_query = json_callback_query["message"]
    chat_callback_query = dict_callback_query["chat"]
    await bot.send_message(chat_callback_query["id"], f"+8-800-550-79-21 Бесплатный номер по России 24/7\n"
    "+7-937-075-82-54 Диспетчерская старший смены 24/7\n"
    "+7-937-203-54-28 Руководитель диспетчерской службы с 8:00 до 16:00 по Московскому времени\n"
    "@VPKd1 - Старший смены 24/7\n"
    "@EvgeniaVPK - Отдел продаж с 8:00 до 16:00 по Московскому времени\n"
    "Для справки введите команду /help\n")

@dp.callback_query_handler(lambda c: c.data == 'mail')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    json_callback_query = json.loads(f'{callback_query}')
    dict_callback_query = json_callback_query["message"]
    chat_callback_query = dict_callback_query["chat"]
    await bot.send_message(chat_callback_query["id"], f"info@vpk-potok.ru Директор, бухгалтерия, диспетчерская служба\n"
    "bux@vpk-potok.ru Бухгалтер\n"
    "tex@vpk-potok.ru Техническая служба\n"
    "Для справки введите команду /help\n")

@dp.callback_query_handler(lambda c: c.data == 'help')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    json_callback_query = json.loads(f'{callback_query}')
    dict_callback_query = json_callback_query["message"]
    chat_callback_query = dict_callback_query["chat"]
    await bot.send_message(chat_callback_query["id"], f"Список доступных команд:\n"
    "/help - Получить справку по командам\n"
    "/start - Общая информация\n"
    "/mail - Почтовые адреса компании\n"
    "/contact - Телефон для связи\n"
    "/join - Получить ID чата\n"
    "/myid - Получить свой ID\n"
    "/server - Ссылки на сервера\n"
    "/helpmob - Ссылки для скачивания мобильных приложений\n"
    "Для обращения по общим вопросам, напишите:\n"
    "/проблема Описание сути проблемы/вопроса\n"
    "Для обращения в диспетчерскую службу, напишите:\n"
    "/задача Описание сути проблемы/вопроса\n"
    "Для обращения в техническую службу, напишите:\n"
    "/task Описание сути проблемы/вопроса\n")

@dp.message_handler(commands='start')
async def process_start_command(message: types.Message):
    await message.answer(f"Добрый день.\n"
    "Вас приветсвует телеграм бот технической поддержки.\n"
    "Вы можете связаться с нами по круглосуточному бесплатному номеру +8-800-550-79-21\n"
    "Ответ по сотрудничеству, оплате счетов, покупке оборудования и другим вопросам на почту info@vpk-potok.ru\n"
    "Ответ по работе оборудования, технической помощи, можно получить по почте tex@vpk-potok.ru\n", reply_markup=group_button_start)

@dp.message_handler(commands='join')
async def cmd_myid(message: types.Message):
    await message.answer(f"Ваш id chat: {message.chat.id}\nВаш id: {message.from_user.id}\n"
    "Для справки введите команду /help\n")

@dp.message_handler(commands='myid')
async def cmd_myid(message: types.Message):
    await message.answer(f"Ваш id chat: {message.chat.id}\nВаш id: {message.from_user.id}\n"
    "Для справки введите команду /help\n")

@dp.message_handler(commands='mail')
async def cmd_myid(message: types.Message):
    await message.answer(f"info@vpk-potok.ru Директор, бухгалтерия, диспетчерская служба\n"
    "bux@vpk-potok.ru Бухгалтер\n"
    "tex@vpk-potok.ru Техническая служба\n"
    "Для справки введите команду /help\n")

@dp.message_handler(commands='contact')
async def cmd_myid(message: types.Message):
    await message.answer(f"+8-800-550-79-21 Бесплатный номер по России 24/7\n"
    "+7-937-075-82-54 Диспетчерская старший смены 24/7\n"
    "+7-937-203-54-28 Руководитель диспетчерской службы с 8:00 до 16:00 по Московскому времени, пн-пт, сб-вс-выходной\n"
    "@VPKd1 - Старший смены 24/7\n"
    "@EvgeniaVPK - Отдел продаж с 8:00 до 16:00 по Московскому времени, пн-пт, сб-вс-выходной\n"
    "Для справки введите команду /help\n")

@dp.message_handler(commands='help')
async def cmd_myid(message: types.Message):
    await message.answer(f"Список доступных команд:\n"
    "/help - Получить справку по командам\n"
    "/start - Общая информация\n"
    "/mail - Почтовые адреса компании\n"
    "/contact - Телефон для связи\n"
    "/join - Получить ID чата\n"
    "/myid - Получить свой ID\n"
    "/server - Ссылки на сервера\n"
    "/helpmob - Ссылки для скачивания мобильных приложений\n"
    "Для обращения по общим вопросам, напишите:\n"
    "/проблема Описание сути проблемы/вопроса\n"
    "Для обращения в диспетчерскую службу, напишите:\n"
    "/задача Описание сути проблемы/вопроса\n"
    "Для обращения в техническую службу, напишите:\n"
    "/task Описание сути проблемы/вопроса\n")

@dp.message_handler(commands='server')
async def cmd_myid(message: types.Message):
    await message.answer(f"WIALON - https://hosting.wialon.com\n"
    "Справка по работе с сервером WIALON:\n"
    "https://help.wialon.com/help/wialon-hosting/ru/user-guide\n"
    "GSH24 (РЕД) - https://gsh24.net/id28\n"
    "Спрака по работе с сервером GSH24:\n"
    "https://docs.gps-server.net\n"
    "АВТОФОН - https://control.autofon.ru\n"
    "Спрака по работе с сервером АВТОФОН:\n"
    "http://www.autofon.ru/documentation\n"
    "CAR-ONLINE - https://group.car-online.pro/login\n"
    "Для справки введите команду /help\n")

@dp.message_handler(commands='helpmob')
async def cmd_myid(message: types.Message):
    await message.answer(f"Скачать мобильные приложения для GSH24:\n"
    "ANDROID - https://play.google.com/store/apps/details?id=com.gpsserver.gpsservermobile\n"
    "IOS - https://apps.apple.com/us/app/gps-server-mobile-tracking/id1174827849?ls=1\n"
    "Как правильно авторизоваться на сервере GSH24\n"
    "https://youtu.be/TjchCJcyp6k\n\n\n"
    "Скачать мобильные приложения для WIALON:\n"
    "ANDROID - https://play.google.com/store/apps/details?id=com.gurtam.wialon_client&hl=ru\n"
    "IOS - https://apps.apple.com/ru/app/wialon/id960699792\n\n\n"
    "Скачать мобильное приложение для АВТОФОН:\n"
    "ANDROID - https://play.google.com/store/apps/details?id=ru.autofon\n"
    "IOS - https://apps.apple.com/ru/app/avtofon-ksa/id971258255\n"
    "Скачать мобильное приложение для CAR-ONLINE:"
    "ANDROID - https://play.google.com/store/apps/details?id=ru.caronline.app"
    "IOS - https://apps.apple.com/ru/app/car-online/id1162687937"
    "Для справки введите команду /help\n")

@dp.message_handler(commands='task') #API интеграция с контрольной панелью
async def cmd_myid(message: types.Message):
    #requests.get('https://service-gps-potok.ru/api/send/message/0/4/Тестовое')
    argument = message.get_args()
    chat_username = message.chat.username
    if chat_username is not None:
        URL = f"https://service-gps-potok.ru/api/send/message/0/4/Task:{argument} User:@{message.chat.username} - {message.chat.first_name} {message.chat.last_name}"
    else:
        URL = f"https://service-gps-potok.ru/api/send/message/0/4/Task:{argument} Chat:{message.chat.title}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL):
            pass
    await message.answer(f"Ваше обращение принято, в ближайшее время с вами свяжется сотрудник технической службы\n"
    "Для справки введите команду /help\n")

@dp.message_handler(commands='задача') #API интеграция с контрольной панелью
async def cmd_myid(message: types.Message):
    #requests.get('https://service-gps-potok.ru/api/send/message/0/4/Тестовое')
    argument = message.get_args()
    chat_username = message.chat.username
    if chat_username is not None:
        URL = f"https://service-gps-potok.ru/api/send/message/0/4/Задача на выполение:{argument} User:@{message.chat.username} - {message.chat.first_name} {message.chat.last_name}"
    else:
        URL = f"https://service-gps-potok.ru/api/send/message/0/4/Задача на выполение:{argument} Chat:{message.chat.title}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL):
            pass
    await message.answer(f"Ваше обращение принято, в ближайшее время с вами свяжется сотрудник технической службы\n"
    "Для справки введите команду /help\n")

@dp.message_handler(commands='проблема') #API интеграция с контрольной панелью
async def cmd_myid(message: types.Message):
    #requests.get('https://service-gps-potok.ru/api/send/message/0/4/Тестовое')
    argument = message.get_args()
    chat_username = message.chat.username
    if chat_username is not None:
        URL = f"https://service-gps-potok.ru/api/send/message/0/4/Проблема:{argument} User:@{message.chat.username} - {message.chat.first_name} {message.chat.last_name}"
    else:
        URL = f"https://service-gps-potok.ru/api/send/message/0/4/Проблема:{argument} Chat:{message.chat.title}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL):
            pass
    await message.answer(f"Принято\n")

@dp.message_handler(commands='отчет') #API интеграция с контрольной панелью
async def cmd_myid(message: types.Message):
    #requests.get('https://service-gps-potok.ru/api/send/message/0/4/Тестовое')
    argument = message.get_args()
    chat_username = message.chat.username
    if chat_username is not None:
        URL = f"https://service-gps-potok.ru/api/send/message/0/4/Отчет о проделанной работе: {argument} User:@{message.chat.username} - {message.chat.first_name} {message.chat.last_name}"
    else:
        URL = f"https://service-gps-potok.ru/api/send/message/0/4/Отчет о проделанной работе: {argument} Chat:{message.chat.title}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL):
            pass
    await message.answer(f"Принято\n")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
