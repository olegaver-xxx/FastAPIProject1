import asyncio
import os
from aiogram import Bot, Dispatcher, types

from bot.my_requests import make_post_request, get_user_if_exist


BOT_TOKEN = "8431808507:AAFy-cJ6eWAZ6NB4-6u8PuTHnVUGB_jbrUs"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


@dp.message()
async def send_user_data(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=message.text,
    )
    user_id = int(message.from_user.id)
    username = message.from_user.username
    a = await get_user_if_exist(user_id)
    print(a, "<<<<<<<<<<")
    if a:
        print(f"{username} already exists")
    else:
        await make_post_request(username, user_id)


if __name__ == "__main__":
    asyncio.run(main())
