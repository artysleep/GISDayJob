from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, BaseFilter
from aiogram.types import Message, ContentType
from os import getenv
from pprint import pprint
from datetime import datetime, timezone
import pytz
import json
import requests
import time

msk_tz = pytz.timezone('Europe/Moscow')
load_dotenv()
bot: Bot = Bot(getenv('TOKEN'))
dp: Dispatcher = Dispatcher()

# Список с ID участников группы бота. !!!Замените на ваш!!!
group_ids: list[int] = [] #238821137


# Собственный фильтр, проверяющий юзера на админа
class IsGroupMember(BaseFilter):
    def __init__(self, group_ids: list[int]) -> None:
        # В качестве параметра фильтр принимает список с целыми числами 
        self.group_ids = group_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in group_ids

# @dp.message(Command(commands=["daily_report"]))
# async def process_start_command(message: Message):
#     await 

@dp.message(Command(commands=["daily_report"]),IsGroupMember(group_ids))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Вы админ')
    #pprint (IsAdmin(group_ids))


@dp.message()
async def answer_if__update(message: Message):
    await message.answer(text='Вы админ')
    #pprint (IsAdmin(group_ids))


@dp.message()
async def send_echo(message: Message):
    try:
        pprint(json.loads(message.model_dump_json()))
        pprint(f'{message.from_user.id} {message.from_user.first_name} {message.from_user.last_name} {message.date.astimezone(msk_tz)}')
        #pprint(message.from_user.first_name)
        #await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Что-то пошло не так :C')

if __name__ == "__main__":
    dp.run_polling(bot)

