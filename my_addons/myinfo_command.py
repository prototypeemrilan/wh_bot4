from aiogram import types
from my_addons.constants import INFO_TEXT


async def myinfo(message: types.Message):
    """
         представляет информацию о пользователе
    """
    await message.answer(text=INFO_TEXT.format(
        id = message.from_user.id,
        first_name = message.from_user.first_name,
        username = message.from_user.username
    ))
    await message.delete()
