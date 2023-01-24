from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(InlineKeyboardButton('Купить', callback_data='buy_item'))


async def shop_magnets(message: types.Message):
    """
        Функция покажет магниты и сколько стоят
    """
    await message.answer(text='Все магниты :')
    await message.answer(text='Магнит Матери Джостары, стоимость - 1 душа', reply_markup=buy_item_kb)
    await message.answer(text='Магнит  Дио, стоимость - 1 душа', reply_markup=buy_item_kb)
    await message.answer(text='Магнит Спид вагона, стоимость - 1 душа', reply_markup=buy_item_kb)