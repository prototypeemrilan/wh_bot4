from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

shop_kb = ReplyKeyboardMarkup(resize_keyboard=True)
shop_kb.add(
    KeyboardButton('Сувениры с Дущами'),
    KeyboardButton('Свитшоты с Душами'),
    KeyboardButton('Магниты с Душами')
)


async def shop_start(cb: types.CallbackQuery):
    """
        Ответ на нажатие кнопки магазин
    """
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text='Что тебя интересует из Душ?',
        reply_markup=shop_kb
    )