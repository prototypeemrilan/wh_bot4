from aiogram import types

async def chsv_uper(message: types.Message):
    """
          Функция отправит сообщение пользователя заглавными буквами если в его сообщении 3 или более слов
      """
    if len(message.text.split()) >= 3:
        await message.reply(text=message.text.upper())
    else:
        await message.answer(text='Нам нечем разговаривать')