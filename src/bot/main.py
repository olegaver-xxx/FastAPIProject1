import asyncio
import os
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from bot.my_requests import make_post_request, get_user_if_exist

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
print(BOT_TOKEN, "<<<<<<<<<<<<<")
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
