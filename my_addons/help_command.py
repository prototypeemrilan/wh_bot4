from aiogram import types
from my_addons.constants import HELP_TEXT


async def help(message: types.Message):
    """
         Показывает пользователю команды
    """
    await message.answer(text=HELP_TEXT)
    await message.delete()