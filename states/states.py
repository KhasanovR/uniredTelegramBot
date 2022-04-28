from aiogram.dispatcher.filters.state import StatesGroup, State


class Application(StatesGroup):
    application_menu = State()


class Card(StatesGroup):
    card_menu = State()


class Payment(StatesGroup):
    payment_menu = State()


class Transaction(StatesGroup):
    transaction_menu = State()


class History(StatesGroup):
    history_menu = State()


class Profile(StatesGroup):
    profile_menu = State()


class Setting(StatesGroup):
    setting_menu = State()
