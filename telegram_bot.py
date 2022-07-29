#!venv/bin/python
import logging
from aiogram import Bot, Dispatcher, executor, types
from tokenbot import tokenbot

# Объект бота
bot = Bot(token=tokenbot, parse_mode=types.ParseMode.HTML)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="inline_url")
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="GitHub", url="https://github.com"),
        types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Кнопки-ссылки", reply_markup=keyboard)


@dp.message_handler(commands='text')
async def cmd_text(message: types.Message):
    await message.answer(f"Вы прислали:{message.text}\n")

@dp.message_handler(commands='num')
async def cmd_text(message: types.Message):
    argument = message.get_args()
    await message.answer(f"Вы прислали число:{argument}\n")

@dp.message_handler(commands='myid')
async def cmd_myid(message: types.Message):
    await message.answer(f"Ваш id:{message.from_user.id}\n")

@dp.message_handler(commands='help')
async def cmd_help(message: types.Message):
    await message.answer(f"Список доспутных команд:\n /Help - справка\n")

@dp.message_handler(content_types=types.ContentType.TEXT)
async def cmd_text(message: types.Message):
    text = message.text
    if text and not  text.startswith('/'):
        await message.answer(f"Вы мне прислали:{message.text}\nУ меня нет таких команд\n")
    else:
        await message.answer(f"В списке нет таких команд\n")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
