from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from os import getenv
import logging
from my_addons.admin import start_command
from my_addons.help_command import help
from my_addons.myinfo_command import myinfo
from my_addons.pictures_command import picture
from my_addons.shop import shop_start
from my_addons.shop_souvenier import shop_souvenier
from my_addons.shop_adress import shop_adress
from my_addons.shop_magnets import shop_magnets
from my_addons.shop_switshots import shop_switshots
from my_addons.buy_item import buy_item
from my_addons.echo_command import chsv_uper
from my_addons.fms import (
    Form,
    handler,
    name,
    adress_get,
    get_age,
    age_check,
    day,
    process_done
)

from DB.data_base_bot import (
    init,
    create_table,
    make_full_products
)
from my_addons.echo_command import chsv_uper


async def startup(_):
    init()
    create_table()



load_dotenv()

bot= Bot(getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


dp.register_message_handler(start_command, commands=['start'])
dp.register_message_handler(help, commands=['help'])
dp.register_message_handler(myinfo, commands=['myinfo'])
dp.register_message_handler(picture, commands=['picture'])
dp.register_callback_query_handler(shop_start, text='shop_start')
dp.register_callback_query_handler(shop_adress, text='shop_adress')
dp.register_callback_query_handler(shop_souvenier, Text(equals='Сувениры с Душами'))
dp.register_callback_query_handler(shop_switshots, Text(equals='Свитшоты с Душами'))
dp.register_callback_query_handler(shop_magnets, Text(equals='Магниты с Душами'))
dp.register_callback_query_handler(buy_item, text='buy_item')
dp.register_message_handler(name, Text(equals='Нет'), state=Form.done)
dp.register_message_handler(handler, state='*', commands='cancel')
dp.register_message_handler(handler, Text(equals='cancel', ignore_case=True), state='*')
dp.register_message_handler(adress_get, state=Form.name)
dp.register_message_handler(get_age, state=Form.adress)
dp.register_message_handler(age_check, state=Form.age)
dp.register_message_handler(day, state=Form.day)
dp.register_message_handler(process_done, Text(equals='Да'), state=Form.done)
dp.register_message_handler(chsv_uper)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)




