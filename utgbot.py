# Python Modules

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from selenium.webdriver.common.by import By

from video_decrypt.Browser import Browser

# For telegram api
from aiogram import Bot, Dispatcher, executor, types

DEBUG = True

API_TOKEN = '5504023015:AAH4_HxkH42vmCIV-9uiRALpqmNitiD-3Do'
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

COMMANDS = ['записать видео']

# States
class States(StatesGroup):
    ADMIN = State()
    MAIN = State()
    TO_RECORD = State()
    RECORD = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
#     username = message.chat.username
#     id = str(message.chat.id)
#     print(username, id, 'is started')
#     whitelisted = Whitelist.check(id)
#     if whitelisted:
#         await States.MAIN.set()
#         markup = get_markups('main_main', Admin.is_admin(id))
#         await message.reply("Привет", reply_markup=markup)
#     elif username:
#         wl = Whitelist.set_tg_id(id, username=username)
#         if wl:
#             await States.MAIN.set()
#             markup = get_markups('main_main')
#             await message.reply("Привет", reply_markup=markup)
#     else:
#         await States.WL_SECRET_KEY.set()
    await message.reply("Привет")

@dp.message_handler(state=States.MAIN)
async def main_handler(message: types.Message):
    msg = message.text.lower()
    if 'записать видео' in msg:
        await States.TO_RECORD.set()
        await message.answer("Отправьте мне ссылку на видео")


@dp.message_handler(state=States.TO_RECORD)
async def to_record(message: types.Message):
    msg = message.text
    if '' in msg:
        browser = Browser()
        driver = browser.driver

        browser.open()
        driver.maximize_window()
        browser.open_site(msg)

        driver.find_element(By.XPATH, '')

@dp.message_handler()
async def read_url(message: types.Message):
    ms = message.text.lower()
    if ms in COMMANDS:
        await States.MAIN.set()
        await main_handler(message)
    await message.reply("Привет")

if __name__ == '__main__':
    executor.start_polling(dp)


