from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(InlineKeyboardButton('Купить', callback_data='buy_item'))


async def shop_switshots(message: types.Message):
    """
        Функция покажет свитшоты
    """
    await message.answer(text='Вот свитшоты:')
    await message.answer(text='Свитшот "С кричащими Душами", стоимость приобрести эту вещь - 1 душа', reply_markup=buy_item_kb)
    await message.answer(text='Свитшот "С фото Душами из NASA", стоимость приобрести эту вещь - 1 душа', reply_markup=buy_item_kb)