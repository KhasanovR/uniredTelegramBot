from aiogram.types import Message
from aiogram import types
from keyboards.default import menu_uz_button, menu_ru_button
from aiogram.dispatcher.filters import Text
from loader import dp
import database

db = database.DBCommands()
from data.config import LANG_STORAGE


@dp.message_handler(Text(equals=["🇷🇺 Русский", "🇺🇿 O'zbek"]))
async def show_menu(message: Message):
    user_id = types.User.get_current().id
    if message.text == "🇷🇺 Русский":
        LANG_STORAGE[user_id] = 'ru'
        await db.set_language('ru')
        await message.answer("👇 Выберите действие:", reply_markup=menu_ru_button)
    elif message.text == "🇺🇿 O'zbek":
        LANG_STORAGE[user_id] = 'uz'
        await message.answer("👇 Xizmat turini tanlang:", reply_markup=menu_uz_button)

