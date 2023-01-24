from aiogram import Bot, types
from random import choice
from os import listdir


async def picture(message: types.Message):
    """
         выберет картинку из папки и отправит её пользователю наугад
    """
    photo = open('images/' + choice(listdir('images')), 'rb')
    await message.answer_photo(photo)
    await message.delete()