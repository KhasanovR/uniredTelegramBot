from aiogram import types
from loader import dp


async def my_filter(message: types.Message):
    print(message.from_user.last_name, message.from_user.username, message.from_user.id)
    if message.from_user.id == 482156670:
        return {'foo': 'foo', 'bar': 42}


@dp.message_handler(lambda message: message.text == 'foo')
@dp.message_handler(types.ChatType.is_group_or_super_group, my_filter)
async def bot_echo(message: types.Message):
    await message.answer('Zaviduy molchaaa ononii😝😝😝')


