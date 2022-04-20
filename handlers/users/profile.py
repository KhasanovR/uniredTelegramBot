from aiogram.types import Message
from keyboards.default import profile_uz_button, profile_ru_button
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from loader import dp
from states import Profile
from data.config import LANG_STORAGE


@dp.message_handler(Text(equals=["🟦 Profil", "🟦 Профиль"]))
async def show_profile_menu(message: Message):
    user_id = message.from_user.id
    await Profile.profile_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=profile_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=profile_uz_button)


@dp.message_handler(Text(equals=["Ism familiyani o'zgartirish", "Изменить имя фамилию"]),
                    state=Profile.profile_menu)
async def change_name(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO

