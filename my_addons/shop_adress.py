from aiogram import types


async def shop_adress(cb: types.CallbackQuery):
    """
        Ответ на нажатие кнопки адресса
    """
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text='Мы находим-cя в Спит вагоне, в конце вагоне мы сидим играем карты на души',
    )