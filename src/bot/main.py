import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
import keyboards as kb
from bot.my_requests import get_user_if_exist, make_post_request
from app.core.config import settings

load_dotenv()
bot = Bot(token=settings.bot_token)
dp = Dispatcher()

dp.include_router(kb.router)


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

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
