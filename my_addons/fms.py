from aiogram.bot import bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


class Form(StatesGroup):
    name = State()
    age = State()
    day = State()
    done = State()


async def handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply(
        'Отмена',
        reply_markup=types.ReplyKeyboardRemove())


async def start(message: types.Message):
    """
         для старта FMS
    """
    await Form.name.set()
    await message.reply("Введите ваше имя:")


async def name(message: types.Message, state: FSMContext):
    """
        Обработчик первой функции и задаем второй вопрос
    """
    async with state.proxy() as data:
        data['name'] = message.text
        print(data)

    await Form.next()
    await message.reply("Введите ваш возраст:")


async def adress_get(message: types.Message, state: FSMContext):
    """
    Обрабатываем имя, узнаем адресс
    """
    async with state.proxy() as data:
        data['name'] = message.text
        print(data)
    await Form.next()
    await message.reply("Введите ваш адресс:")


async def get_age(message: types.Message, state: FSMContext):
    """
        Обработчик второй функции и задаем третий вопрос
    """
    if not message.text.isdigit():
        await message.reply("Слушай человечина или как вас там, я думаю возраст пишется с помощью чисел ;)")



async def age_check(message: types.Message, state: FSMContext):
    """
    Обрабатывваем возраст, задаем следующий вопрос
    """
    if not message.text.isdigit():
        await message.reply("Введите возвраст числами")
    elif int(message.text) <= 18:
        await message.reply("Подождите пока вам будет совершенолетия :)")
        await state.finish()
        await message.answer(
            'Будем ждать вас.',
            reply_markup=types.ReplyKeyboardRemove())
    else:
        async with state.proxy() as data:
            data['age']=int(message.text)

        week_days_kb = ReplyKeyboardMarkup(resize_keyboard=True)
        week_days_kb.add(
            KeyboardButton("Вторник"),
            KeyboardButton("Среда"),
            KeyboardButton("Четверг"),
            KeyboardButton("Пятница"),
            KeyboardButton("Суббота"),
            KeyboardButton("Воскресение"),
        )
        await Form.next()
        await message.reply(
            "Выберите день недели для получения посылки в ближайшую неделю",
            reply_markup=week_days_kb
        )


async def day(message: types.Message, state: FSMContext):
    """
        Обработчик третьей функции
    """
    async with state.proxy() as data:
        data['day'] = message.text

    yes_no_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    yes_no_kb.add(
        KeyboardButton("Да"),
        KeyboardButton("Нет")
    )

    await Form.next()
    await message.reply(f"""Подтвердите ваши данные:
    Имя: {data['name']}
    Возраст: {data['age']}
    День получения ответа: {data['day']}
    Все верно?
    """, reply_markup=yes_no_kb)


async def process_done(message: types.Message, state: FSMContext):
    """
    Финишная премая
    """
    async with state.proxy() as data:
        make_full_order(data)
    await state.finish()
    await message.reply(
        "Благодарю вас за это.",
        reply_markup=ReplyKeyboardRemove()
    )
