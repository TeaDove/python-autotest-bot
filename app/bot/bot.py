from aiogram import Bot, Dispatcher, executor, types, utils
import aiogram

from ..core.settings import Settings
from .utils import res_dict
from ..excel.excel import Students
from ..tests.downloader import download
from ..tests.start_tests import start_tests

bot = Bot(token=Settings().telegram_api_key)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send(message: types.Message):
    await message.reply(res_dict['start'], parse_mode='html')


@dp.message_handler(commands='help')
async def send(message: types.Message):
    await message.reply(res_dict['start'], parse_mode='html')


@dp.message_handler(commands='check_homework')
async def send(message: types.Message):
    await message.reply(res_dict['check_homework'], parse_mode='html')
    students = Students()
    username = "@" + message.from_user.username.lower()
    hm_to_do = students.get_undone_homework(username)
    if hm_to_do is None:
        await message.reply('Вы не зарегестрированы в системе. \nЧтобы зарегестрироваться, пройдите в канал:\n'
                            'https://t.me/itam_python_course', parse_mode='html')
        return
    await message.reply("Вам необходимо сделать домашку: \n<i>{}</i>".format('\n'.join(hm_to_do)), parse_mode='html')
    download('https://github.com/{}/itam_python_courses'.format(students[username][1]))
    output = start_tests()
    await message.reply(str(output['summary']))

def bot_start():
    executor.start_polling(dp, skip_updates=True)
