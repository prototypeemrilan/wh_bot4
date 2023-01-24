from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(InlineKeyboardButton('Приобрести', callback_data='buy_item'))


async def shop_souvenier(message: types.Message):
    """
        Функция покажет сувениры и стоимости
    """
    await message.answer(text='Вот сувениры с душами:')
    await message.answer(text='Статуэтка Души Алдияра, стоимость не дорогая - 1 душа', reply_markup=buy_item_kb)
    await message.answer(text='Балванчик в форме Души человека, стоимость не дорогая - 1 душа', reply_markup=buy_item_kb)
    await message.answer(text='Плакат с Душами известных людей, стоимость не дорогая - 1 душа', reply_markup=buy_item_kb)