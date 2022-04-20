from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_cancel_uz = [
    KeyboardButton(text="⬅️Orqaga"),
    KeyboardButton(text="🏠 Asosiy sahifa")
]

keyboard_cancel_ru = [
    KeyboardButton(text="⬅ Назад"),
    KeyboardButton(text="🏠 На главную")
]

basic_cancel_button_uz = ReplyKeyboardMarkup(
    keyboard=[keyboard_cancel_uz]
)
basic_cancel_button_ru = ReplyKeyboardMarkup(
    keyboard=[keyboard_cancel_ru]
)
