#from dotenv import load_dotenv

import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from pprint import pprint

# Функция конфигурирования и запуска бота
async def main() -> None:

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())



#для времени
#print(datetime.datetime.now().astimezone(TimeZone.msk))



# # Собственный фильтр, проверяющий юзера на админа
# class IsGroupMember(BaseFilter):
#     def __init__(self, group_ids: list[int]) -> None:
#         # В качестве параметра фильтр принимает список с целыми числами 
#         self.group_ids = group_ids

#     async def __call__(self, message: Message) -> bool:
#         return message.from_user.id in group_ids

# # @dp.message(Command(commands=["daily_report"]))
# # async def process_start_command(message: Message):
# #     await 

# @dp.message(Command(commands=["daily_report"]),IsGroupMember(group_ids))
# async def answer_if_admins_update(message: Message):
#     await message.answer(text='Вы админ')
#     #pprint (IsAdmin(group_ids))

# @dp.message()
# async def send_echo(message: Message):
#     try:
#         pprint(json.loads(message.model_dump_json()))
#         pprint(f'{message.from_user.id} {message.from_user.first_name} {message.from_user.last_name} {message.date.astimezone(msk_tz)}')
#         #pprint(message.from_user.first_name)
#         #await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.reply(text='Что-то пошло не так :C')

# if __name__ == "__main__":
#     dp.run_polling(bot)
