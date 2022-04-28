from aiogram.types import Message
from keyboards.default import cards_uz_button, cards_ru_button, menu_uz_button, menu_ru_button
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from loader import dp
from states import Card
from data.config import LANG_STORAGE


@dp.message_handler(Text(equals=["💳 Kartalarim", "💳 Карты"]))
async def show_cards_manu(message: Message):
    user_id = message.from_user.id
    await Card.card_menu.set()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=cards_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=cards_uz_button)


@dp.message_handler(Text(equals=["➕ Karta qo'shish", "➕ Добавить карту"]),
                    state=Card.card_menu)
async def add_card(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["➖ Kartani o'chirish", "➖ Удалить карту"]),
                    state=Card.card_menu)
async def remove_card(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # TODO


@dp.message_handler(Text(equals=["⬅️Orqaga", "⬅ Назад"]), state=Card.card_menu)
async def back(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await state.reset_state()
    if LANG_STORAGE[user_id] == 'ru':
        await message.answer("👇 Выберите действие:", reply_markup=menu_ru_button)
    elif LANG_STORAGE[user_id] == 'uz':
        await message.answer("👇 Quyidagilardan birini tanlang", reply_markup=menu_uz_button)
