#!venv/bin/python
import logging
import aiogram
import json
from tokenbot import tokenbot
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# Объект бота
bot = Bot(token=tokenbot, parse_mode=types.ParseMode.HTML)
# Диспетчер для бота
#i.x.c.o.n@yandex.ru
#+7-909-364-80-05
#Дмитрий
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
button_server = InlineKeyboardButton('Ссылки на сервер', callback_data='server')
button_helpmob = InlineKeyboardButton('Скачать приложения', callback_data='helpmob')
button_join = InlineKeyboardButton('ID CHAT', callback_data='join')
group_button_start = InlineKeyboardMarkup().row(button_help, button_mail).row(button_contact, button_server).row(button_helpmob ,button_join)

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
    await bot.send_message(chat_callback_query["id"], f"Скачать мобильные приложения для WIALON:\n"
    "ANDROID - https://play.google.com/store/apps/details?id=com.gurtam.wialon_client&hl=ru\n"
    "IOS - https://apps.apple.com/ru/app/wialon/id960699792\n")

@dp.callback_query_handler(lambda c: c.data == 'server')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    json_callback_query = json.loads(f'{callback_query}')
    dict_callback_query = json_callback_query["message"]
    chat_callback_query = dict_callback_query["chat"]
    await bot.send_message(chat_callback_query["id"], f"WIALON - https://hosting.wialon.com\n"
    "Справка по работе с сервером WIALON:\n"
    "https://help.wialon.com/help/wialon-hosting/ru/user-guide\n"
    "Для справки введите команду /help\n")

@dp.callback_query_handler(lambda c: c.data == 'contact')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    json_callback_query = json.loads(f'{callback_query}')
    dict_callback_query = json_callback_query["message"]
    chat_callback_query = dict_callback_query["chat"]
    await bot.send_message(chat_callback_query["id"], f"Офис в Тольятти\n"
    "+8-800-700-54-56\n"
    "+7(8482)-68-66-08\n"
    "sales@wialon-service.ru\n"
    "ООО «Виалон-сервис РУС» ИНН 6321369390 КПП 632101001\n"
    "445037, Россия, Самарская обл., г. Тольятти, ул. Юбилейная, дом 29, офис 52\n"
    "Офис в Москве\n"
    "+7-495-410-20-22\n"
    "moscow@wialon-service.ru\n"
    "105187, Россия, г. Москва, Окружной проезд, дом 18, офис 106\n"
    "Для справки введите команду /help\n")

@dp.callback_query_handler(lambda c: c.data == 'mail')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    json_callback_query = json.loads(f'{callback_query}')
    dict_callback_query = json_callback_query["message"]
    chat_callback_query = dict_callback_query["chat"]
    await bot.send_message(chat_callback_query["id"], f"sales@wialon-service.ru\n"
    "moscow@wialon-service.ru\n"
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
    "/server - Ссылки на сервера\n"
    "/helpmob - Ссылки для скачивания мобильных приложений\n")

@dp.message_handler(commands='start')
async def process_start_command(message: types.Message):
    await message.answer(f"Добрый день.\n"
    "Вас приветсвует телеграм бот технической поддержки.\n"
    "Вы можете связаться с нами по круглосуточному бесплатному номеру +8-800-700-54-56\n", reply_markup=group_button_start)

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
    await message.answer(f"sales@wialon-service.ru\n"
    "moscow@wialon-service.ru\n"
    "Для справки введите команду /help\n")

@dp.message_handler(commands='contact')
async def cmd_myid(message: types.Message):
    await message.answer(f"Офис в Тольятти\n"
    "+8-800-700-54-56\n"
    "+7(8482)-68-66-08\n"
    "sales@wialon-service.ru\n"
    "ООО «Виалон-сервис РУС» ИНН 6321369390 КПП 632101001\n"
    "445037, Россия, Самарская обл., г. Тольятти, ул. Юбилейная, дом 29, офис 52\n"
    "Офис в Москве\n"
    "+7-495-410-20-22\n"
    "moscow@wialon-service.ru\n"
    "105187, Россия, г. Москва, Окружной проезд, дом 18, офис 106\n"
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
    "Для справки введите команду /help\n")

@dp.message_handler(commands='helpmob')
async def cmd_myid(message: types.Message):
    await message.answer(f"Скачать мобильные приложения для WIALON:\n"
    "ANDROID - https://play.google.com/store/apps/details?id=com.gurtam.wialon_client&hl=ru\n"
    "IOS - https://apps.apple.com/ru/app/wialon/id960699792\n\n\n"
    "Для справки введите команду /help\n")

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
