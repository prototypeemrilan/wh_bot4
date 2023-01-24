from aiogram import types


async def buy_item(cb: types.CallbackQuery):
    """
        Ответ на нажатие кнопку купить
    """
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text='У вас нет души.',
    )