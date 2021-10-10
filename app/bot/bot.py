from aiogram import Bot, Dispatcher, executor, types, utils
import aiogram

from ..core.settings import Settings
from .utils import res_dict
from ..excel.excel import Students
from ..tests.downloader import download
from ..tests.start_tests import gen_summary

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
    output = gen_summary()
    to_return_chapter = []
    for key, value in output['chapters'].items():
        to_return_chapter.append("<b>{}</b>, пройдено тестов <b>{}</b> из <b>{}</b>".format(key, value[0], value[1]))

    to_return_tasks = []
    for key, value in output['tasks'].items():
        to_return_chapter.append("Задание <b>{}</b>, пройдено тестов <b>{}</b> из <b>{}</b>".format(key, value[0], value[1]))
    to_return = '\n'.join(to_return_chapter) + '\n\n' + '\n'.join(to_return_tasks)
    await message.reply(to_return, parse_mode='html')


@dp.message_handler(commands='check_all_homework')
async def send(message: types.Message):
    if message.from_user.id in Settings().admin_ids:

        students = Students()
        for username, student in students.items():
            download('https://github.com/{}/itam_python_courses'.format(student[1]))
            output = gen_summary()
            to_return_chapter = []
            for key, value in output['chapters'].items():
                to_return_chapter.append("<b>{}</b>, пройдено тестов <b>{}</b> из <b>{}</b>".format(key, value[0], value[1]))

            to_return_tasks = []
            for key, value in output['tasks'].items():
                to_return_chapter.append("Задание <b>{}</b>, пройдено тестов <b>{}</b> из <b>{}</b>".format(key, value[0], value[1]))
            to_return = "Студент: " + username + '\n\n' + '\n'.join(to_return_chapter) + '\n\n' + '\n'.join(to_return_tasks)
            await message.answer(to_return, parse_mode='html')

def bot_start():
    executor.start_polling(dp, skip_updates=True)
