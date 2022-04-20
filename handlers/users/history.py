from aiogram.types import Message
from keyboards.default import history_uz_button, history_ru_button
from aiogram.dispatcher.filters import Text
from loader import dp
from states import History
from data.config import LANG_STORAGE


@dp.message_handler(Text(equals=["📜 To'lovlar Tarixi", "📜 История платежей"]))
async def show_history_menu(message: Message):
    user_id = message.from_user.id
    await History.history_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=history_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=history_uz_button)

# TODO
