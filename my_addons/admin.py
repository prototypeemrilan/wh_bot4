from aiogram import types
from my_addons.constants import WELCOME_USER
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_kb = InlineKeyboardMarkup(resize_keyboard=True)
start_kb.add(
    InlineKeyboardButton('Магазинчик "Всё у дяди ДЖО ДЖО"', callback_data='shop_start'),
    InlineKeyboardButton('Адрес магазина"', callback_data='shop_adress')
)


async def start_command(message: types.Message):
    """
        Бот приветсвует пользователя по имени профиля
    """
    await message.answer(
        text=WELCOME_USER.format(first_name = message.from_user.first_name),
        reply_markup=start_kb
    )
    await message.delete()