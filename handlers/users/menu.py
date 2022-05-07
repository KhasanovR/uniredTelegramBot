from aiogram.types import Message
from aiogram import types
from keyboards.default import menu_uz_button, menu_ru_button
from loader import dp
import database
from data.config import LANG_STORAGE
from states import Home

db = database.DBCommands()


@dp.message_handler(state=Home.home_menu)
async def show_menu(message: Message):
    user_id = types.User.get_current().id
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=menu_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Xizmat turini tanlang:", reply_markup=menu_uz_button)

